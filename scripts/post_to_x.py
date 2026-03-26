#!/usr/bin/env python3
"""
Post FIR Risk newsletters to X (@stikman28).

Reads OAuth keys from macOS Keychain (fir-risk-publisher app).
Extracts the X POST section from a newsletter markdown file,
uploads the newsletter image, and posts as a long-form post with image.

Modes:
    Full post:  python3 post_to_x.py newsletters/2026-03-24-m-trends-2026.md
    Hook + link: python3 post_to_x.py newsletters/2026-03-24-m-trends-2026.md --hook
    Dry run:    python3 post_to_x.py newsletters/2026-03-24-m-trends-2026.md --hook --dry-run

Hook mode posts a short teaser (from ## X HOOK section, or auto-extracted from
Bottom Line) as a native text post, then replies with the firrisk.ai link.
Use for Tuesday editions published as X Articles — hook drives attention,
reply provides the website link without algorithm penalty.
"""

import argparse
import os
import re
import subprocess
import time
from datetime import datetime, timedelta

import requests
from requests_oauthlib import OAuth1


def get_keychain_secret(service: str, account: str = "stikman28") -> str:
    """Retrieve a secret from macOS Keychain."""
    result = subprocess.run(
        ["security", "find-generic-password", "-a", account, "-s", service, "-w"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to retrieve '{service}' from Keychain: {result.stderr.strip()}")
    return result.stdout.strip()


def get_auth() -> OAuth1:
    """Create OAuth1 auth using Keychain credentials (fir-risk-publisher app)."""
    return OAuth1(
        get_keychain_secret("X_PUBLISH_CONSUMER_KEY"),
        get_keychain_secret("X_PUBLISH_CONSUMER_SECRET"),
        get_keychain_secret("X_PUBLISH_ACCESS_TOKEN"),
        get_keychain_secret("X_PUBLISH_ACCESS_TOKEN_SECRET"),
    )


def extract_x_post(filepath: str) -> str:
    """Extract the X POST section from a newsletter markdown file."""
    with open(filepath, "r") as f:
        content = f.read()

    match = re.search(r"## X POST\s*\n(.*?)(?=\n---|\n## SOURCE DATA|\Z)", content, re.DOTALL)
    if not match:
        raise ValueError(f"No X POST section found in {filepath}")

    return match.group(1).strip()


def extract_x_hook(filepath: str) -> str:
    """Extract the X HOOK section from a newsletter markdown file.
    Falls back to auto-generating from Bottom Line if no X HOOK section exists."""
    with open(filepath, "r") as f:
        content = f.read()

    # Try explicit X HOOK section first
    match = re.search(r"## X HOOK\s*\n(.*?)(?=\n---|\n## |\Z)", content, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Auto-generate from Bottom Line — take first 2 paragraphs
    match = re.search(r"## Bottom Line\s*\n(.*?)(?=\n---|\n## )", content, re.DOTALL)
    if match:
        paragraphs = [p.strip() for p in match.group(1).strip().split("\n\n") if p.strip()]
        # Take first 2 substantive paragraphs, strip markdown bold
        hook_parts = []
        for p in paragraphs[:2]:
            clean = re.sub(r"\*\*(.*?)\*\*", r"\1", p)  # strip bold markdown
            clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", clean)  # strip links
            hook_parts.append(clean)
        return "\n\n".join(hook_parts)

    raise ValueError(f"No X HOOK or Bottom Line section found in {filepath}")


def extract_slug(filepath: str) -> str:
    """Extract the URL slug from the newsletter/INTEL filename.
    Checks the website repo for the matching Hugo page."""
    with open(filepath, "r") as f:
        content = f.read(3000)

    # Check INTEL first (INTEL files reference E## in body)
    intel_match = re.search(r"# FIR Risk INTEL-(\d+)", content)
    if intel_match:
        intel_num = intel_match.group(1)
        intel_dir = "/Users/stikman/Projects/ai-assistant/fir-risk-website/content/intel"
        if os.path.isdir(intel_dir):
            for fname in os.listdir(intel_dir):
                if fname.startswith(f"intel-{intel_num}-") and fname.endswith(".md"):
                    return fname.replace(".md", "")

    # Then check newsletter E##
    edition_match = re.search(r"# FIR Risk (?:Tuesday )?(E\d+)", content)
    if edition_match:
        edition = edition_match.group(1).lower()
        website_dir = "/Users/stikman/Projects/ai-assistant/fir-risk-website/content/tuesday"
        if os.path.isdir(website_dir):
            for fname in os.listdir(website_dir):
                if fname.startswith(edition + "-") and fname.endswith(".md"):
                    return fname.replace(".md", "")

    # Fallback: use source filename
    basename = os.path.splitext(os.path.basename(filepath))[0]
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", basename)
    return slug


def build_reply_url(filepath: str) -> str:
    """Build the firrisk.ai URL for the reply post."""
    slug = extract_slug(filepath)

    # Determine if Tuesday or INTEL — check slug, filepath, and filename
    is_intel = (slug.startswith("intel-")
                or "/intel/" in filepath
                or filepath.startswith("intel/"))
    if is_intel:
        return f"https://firrisk.ai/intel/{slug}/"
    else:
        return f"https://firrisk.ai/tuesday/{slug}/"


def post_reply(text: str, reply_to_id: str, auth: OAuth1) -> dict:
    """Post a reply to an existing tweet. Returns response data."""
    payload = {
        "text": text,
        "reply": {"in_reply_to_tweet_id": reply_to_id}
    }

    response = requests.post(
        "https://api.x.com/2/tweets",
        json=payload,
        auth=auth,
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 201:
        return response.json()["data"]
    else:
        raise RuntimeError(f"X API error {response.status_code}: {response.text}")


def extract_image_path(filepath: str) -> str:
    """Extract the newsletter image path from the markdown file."""
    newsletter_dir = os.path.dirname(filepath)
    with open(filepath, "r") as f:
        content = f.read()

    match = re.search(r"!\[.*?\]\((images/.+?\.png)\)", content)
    if not match:
        return None

    image_path = os.path.join(newsletter_dir, match.group(1))
    if not os.path.exists(image_path):
        print(f"Image referenced but not found: {image_path}")
        return None
    return image_path


def upload_image(image_path: str, auth: OAuth1) -> str:
    """Upload an image to X via v1.1 media upload endpoint. Returns media_id."""
    print(f"Uploading image: {image_path}")

    with open(image_path, "rb") as f:
        response = requests.post(
            "https://upload.x.com/1.1/media/upload.json",
            files={"media": f},
            auth=auth,
        )

    if response.status_code == 200:
        media_id = response.json()["media_id_string"]
        print(f"Image uploaded: media_id={media_id}")
        return media_id
    else:
        raise RuntimeError(f"Image upload failed {response.status_code}: {response.text}")


def post_to_x(text: str, auth: OAuth1, media_id: str = None) -> dict:
    """Post text (with optional image) to X via API v2. Returns response data."""
    payload = {"text": text}
    if media_id:
        payload["media"] = {"media_ids": [media_id]}

    response = requests.post(
        "https://api.x.com/2/tweets",
        json=payload,
        auth=auth,
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 201:
        return response.json()["data"]
    else:
        raise RuntimeError(f"X API error {response.status_code}: {response.text}")


def main():
    parser = argparse.ArgumentParser(description="Post FIR Risk newsletter to X (@stikman28)")
    parser.add_argument("file", help="Path to newsletter markdown file")
    parser.add_argument("--dry-run", action="store_true", help="Preview post without publishing")
    parser.add_argument("--no-image", action="store_true", help="Post without image")
    parser.add_argument("--hook", action="store_true",
                        help="Post a short hook + reply with firrisk.ai link (for X Article promotion)")
    parser.add_argument("--no-reply", action="store_true",
                        help="Skip the auto-reply with firrisk.ai link")
    parser.add_argument("--schedule", type=int, metavar="MINUTES",
                        help="Schedule post to go out in N minutes")
    args = parser.parse_args()

    print(f"Reading: {args.file}")

    if args.hook:
        # ── Hook mode: short teaser + reply with link ──
        hook_text = extract_x_hook(args.file)
        reply_url = build_reply_url(args.file)
        reply_text = f"Full edition → {reply_url}"

        print(f"Hook length: {len(hook_text)} characters")
        print(f"Reply URL: {reply_url}")

        if args.dry_run:
            print(f"\n{'='*50}")
            print("DRY RUN — Hook + Reply preview")
            print(f"{'='*50}\n")
            print("[POST 1 — Hook]")
            print(hook_text)
            print(f"\n[POST 2 — Reply]")
            print(reply_text)
            print(f"\n{'='*50}")
            print(f"Hook: {len(hook_text)} chars | Reply: {len(reply_text)} chars")
            if args.schedule:
                target = datetime.now() + timedelta(minutes=args.schedule)
                print(f"\nWould be scheduled for: {target:%I:%M %p}")
            return

        if args.schedule:
            target = datetime.now() + timedelta(minutes=args.schedule)
            print(f"\nScheduled for {target:%I:%M %p} ({args.schedule} min)")
            print("Leave this running. Ctrl+C to cancel.\n")
            time.sleep(args.schedule * 60)
            print(f"[{datetime.now():%H:%M:%S}] Executing scheduled post...")

        auth = get_auth()

        print("Posting hook...")
        hook_data = post_to_x(hook_text, auth)
        hook_id = hook_data["id"]
        print(f"Hook posted! https://x.com/stikman28/status/{hook_id}")

        print("Posting reply with link...")
        reply_data = post_reply(reply_text, hook_id, auth)
        reply_id = reply_data["id"]
        print(f"Reply posted! https://x.com/stikman28/status/{reply_id}")

    else:
        # ── Full post mode (original behavior) ──
        x_post_text = extract_x_post(args.file)
        image_path = extract_image_path(args.file) if not args.no_image else None

        print(f"Post length: {len(x_post_text)} characters")
        if image_path:
            print(f"Image: {image_path}")

        if args.dry_run:
            reply_url = build_reply_url(args.file)
            print(f"\n{'='*50}")
            print("DRY RUN — Post preview")
            print(f"{'='*50}\n")
            if image_path:
                print(f"[IMAGE: {image_path}]\n")
            print(x_post_text)
            if not args.no_reply:
                print(f"\n[REPLY] Full analysis: {reply_url}")
            print(f"\n{'='*50}")
            print(f"{len(x_post_text)} characters")
            if args.schedule:
                target = datetime.now() + timedelta(minutes=args.schedule)
                print(f"\nWould be scheduled for: {target:%I:%M %p}")
            return

        if args.schedule:
            target = datetime.now() + timedelta(minutes=args.schedule)
            print(f"\nScheduled for {target:%I:%M %p} ({args.schedule} min)")
            print("Leave this running. Ctrl+C to cancel.\n")
            time.sleep(args.schedule * 60)
            print(f"[{datetime.now():%H:%M:%S}] Executing scheduled post...")

        auth = get_auth()
        media_id = None
        if image_path:
            media_id = upload_image(image_path, auth)
        print("Posting to X...")
        data = post_to_x(x_post_text, auth, media_id)
        tweet_id = data["id"]
        print(f"Posted! https://x.com/stikman28/status/{tweet_id}")

        # Auto-reply with firrisk.ai link
        if not args.no_reply:
            reply_url = build_reply_url(args.file)
            reply_text = f"Full analysis: {reply_url}"
            try:
                reply_data = post_reply(reply_text, tweet_id, auth)
                print(f"Reply posted! https://x.com/stikman28/status/{reply_data['id']}")
            except Exception as e:
                print(f"Reply failed (post succeeded): {e}")


if __name__ == "__main__":
    main()
