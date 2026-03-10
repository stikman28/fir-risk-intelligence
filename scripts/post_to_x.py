#!/usr/bin/env python3
"""
Post FIR Risk newsletters to X (@stikman28).

Reads OAuth keys from macOS Keychain (fir-risk-publisher app).
Extracts the X POST section from a newsletter markdown file,
uploads the newsletter image, and posts as a long-form post with image.

Usage:
    python3 post_to_x.py newsletters/2026-03-03-unit42-incident-response-debrief.md
    python3 post_to_x.py newsletters/2026-03-03-unit42-incident-response-debrief.md --dry-run
"""

import argparse
import os
import re
import subprocess

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


def extract_image_path(filepath: str) -> str:
    """Extract the newsletter image path from the markdown file."""
    newsletter_dir = os.path.dirname(filepath)
    with open(filepath, "r") as f:
        content = f.read()

    match = re.search(r"!\[.*?\]\((images/.+?\.png)\)", content)
    if not match:
        raise ValueError(f"No image reference found in {filepath}")

    return os.path.join(newsletter_dir, match.group(1))


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
    args = parser.parse_args()

    print(f"Reading: {args.file}")
    x_post_text = extract_x_post(args.file)
    image_path = extract_image_path(args.file) if not args.no_image else None

    print(f"Post length: {len(x_post_text)} characters")
    if image_path:
        print(f"Image: {image_path}")

    if args.dry_run:
        print(f"\n{'='*50}")
        print("DRY RUN — Post preview")
        print(f"{'='*50}\n")
        if image_path:
            print(f"[IMAGE: {image_path}]\n")
        print(x_post_text)
        print(f"\n{'='*50}")
        print(f"{len(x_post_text)} characters")
    else:
        auth = get_auth()
        media_id = None
        if image_path:
            media_id = upload_image(image_path, auth)
        print("Posting to X...")
        data = post_to_x(x_post_text, auth, media_id)
        tweet_id = data["id"]
        print(f"Posted! https://x.com/stikman28/status/{tweet_id}")


if __name__ == "__main__":
    main()
