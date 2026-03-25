#!/usr/bin/env python3
"""
Post FIR Risk content to LinkedIn (feed post + link comment).

Strategy: Algorithm-friendly posting —
  1. Native text + image (no outbound link in post body)
  2. Drop firrisk.ai link as first comment (avoids algorithm penalty)

Reads OAuth tokens from macOS Keychain.
Extracts the LINKEDIN POST section from a newsletter/INTEL markdown file.

Setup (one-time):
    python3 post_to_linkedin.py --setup

Usage:
    python3 post_to_linkedin.py newsletters/2026-03-13-slug.md --dry-run
    python3 post_to_linkedin.py newsletters/2026-03-13-slug.md
    python3 post_to_linkedin.py newsletters/2026-03-13-slug.md --no-comment
    python3 post_to_linkedin.py intel/2026-03-11-slug.md
"""

import argparse
import http.server
import json
import os
import re
import subprocess
import threading
import time
import urllib.parse
import webbrowser
from datetime import datetime, timedelta

import requests


# --- Keychain helpers ---

KEYCHAIN_ACCOUNT = "stikman28"
KEYCHAIN_KEYS = {
    "client_id": "LINKEDIN_CLIENT_ID",
    "client_secret": "LINKEDIN_CLIENT_SECRET",
    "access_token": "LINKEDIN_ACCESS_TOKEN",
    "person_id": "LINKEDIN_PERSON_ID",
}

LI_API = "https://api.linkedin.com/rest"
LI_VERSION = "202503"


def get_keychain_secret(service: str) -> str:
    """Retrieve a secret from macOS Keychain."""
    result = subprocess.run(
        ["security", "find-generic-password", "-a", KEYCHAIN_ACCOUNT, "-s", service, "-w"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Key '{service}' not in Keychain. Run --setup first.")
    return result.stdout.strip()


def set_keychain_secret(service: str, value: str):
    """Store a secret in macOS Keychain (update if exists)."""
    # Delete existing if present
    subprocess.run(
        ["security", "delete-generic-password", "-a", KEYCHAIN_ACCOUNT, "-s", service],
        capture_output=True
    )
    subprocess.run(
        ["security", "add-generic-password", "-a", KEYCHAIN_ACCOUNT, "-s", service, "-w", value],
        check=True, capture_output=True
    )


def li_headers(access_token: str) -> dict:
    """Standard LinkedIn API headers."""
    return {
        "Authorization": f"Bearer {access_token}",
        "Linkedin-Version": LI_VERSION,
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    }


# --- OAuth Setup ---

def setup_oauth():
    """Interactive OAuth 2.0 setup flow."""
    print("=" * 50)
    print("LinkedIn OAuth Setup")
    print("=" * 50)
    print()
    print("1. Go to https://www.linkedin.com/developers/apps")
    print("2. Create an app (or use existing)")
    print("3. Under 'Products', request 'Share on LinkedIn'")
    print("4. Under 'Auth', add redirect URL: http://localhost:8585/callback")
    print("5. Copy your Client ID and Client Secret")
    print()

    client_id = input("Client ID: ").strip()
    client_secret = input("Client Secret: ").strip()

    if not client_id or not client_secret:
        print("Error: Both Client ID and Client Secret required.")
        return

    # Store credentials
    set_keychain_secret(KEYCHAIN_KEYS["client_id"], client_id)
    set_keychain_secret(KEYCHAIN_KEYS["client_secret"], client_secret)
    print("Credentials saved to Keychain.")

    # OAuth consent flow
    redirect_uri = "http://localhost:8585/callback"
    scopes = "openid profile w_member_social"
    auth_url = (
        f"https://www.linkedin.com/oauth/v2/authorization?"
        f"response_type=code&client_id={client_id}"
        f"&redirect_uri={urllib.parse.quote(redirect_uri)}"
        f"&scope={urllib.parse.quote(scopes)}"
    )

    # Start local server to catch the redirect
    auth_code = [None]

    class CallbackHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            if "code" in params:
                auth_code[0] = params["code"][0]
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(b"<h2>LinkedIn authorized! You can close this tab.</h2>")
            else:
                self.send_response(400)
                self.end_headers()
                error = params.get("error_description", ["Unknown error"])[0]
                self.wfile.write(f"Error: {error}".encode())

        def log_message(self, format, *args):
            pass  # Suppress server logs

    server = http.server.HTTPServer(("localhost", 8585), CallbackHandler)
    server_thread = threading.Thread(target=server.handle_request)
    server_thread.start()

    print(f"\nOpening browser for LinkedIn authorization...")
    webbrowser.open(auth_url)
    print("Waiting for authorization...")

    server_thread.join(timeout=120)
    server.server_close()

    if not auth_code[0]:
        print("Error: No authorization code received. Try again.")
        return

    # Exchange code for access token
    print("Exchanging code for access token...")
    resp = requests.post("https://www.linkedin.com/oauth/v2/accessToken", data={
        "grant_type": "authorization_code",
        "code": auth_code[0],
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
    })

    if resp.status_code != 200:
        print(f"Token exchange failed: {resp.status_code} {resp.text}")
        return

    token_data = resp.json()
    access_token = token_data["access_token"]
    expires_in = token_data.get("expires_in", 0)

    set_keychain_secret(KEYCHAIN_KEYS["access_token"], access_token)
    print(f"Access token saved. Expires in {expires_in // 86400} days.")

    # Get person ID via userinfo
    print("Fetching LinkedIn profile...")
    profile_resp = requests.get(
        "https://api.linkedin.com/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    if profile_resp.status_code == 200:
        person_id = profile_resp.json()["sub"]
        name = profile_resp.json().get("name", "")
        set_keychain_secret(KEYCHAIN_KEYS["person_id"], person_id)
        print(f"Linked as: {name} (ID: {person_id})")
    else:
        print(f"Warning: Couldn't fetch profile ({profile_resp.status_code}). "
              f"Set LINKEDIN_PERSON_ID manually in Keychain.")

    print("\nSetup complete! You can now post to LinkedIn.")


# --- Content extraction ---

def extract_linkedin_post(filepath: str) -> str:
    """Extract the LINKEDIN POST section from a markdown file."""
    with open(filepath) as f:
        content = f.read()

    # Try both ## and # header levels
    match = re.search(
        r"#+ LINKEDIN POST\s*\n+```\n?(.*?)```",
        content, re.DOTALL
    )
    if match:
        return match.group(1).strip()

    # Fallback: no code fence
    match = re.search(
        r"#+ LINKEDIN POST\s*\n(.*?)(?=\n---|\n#+ (?:X POST|SOURCE DATA)|\Z)",
        content, re.DOTALL
    )
    if match:
        return match.group(1).strip()

    raise ValueError(f"No LINKEDIN POST section found in {filepath}")


def extract_image_path(filepath: str) -> str:
    """Extract the content image path from the markdown file."""
    content_dir = os.path.dirname(filepath)
    with open(filepath) as f:
        content = f.read()

    match = re.search(r"!\[.*?\]\((images/.+?\.png)\)", content)
    if not match:
        return None

    image_path = os.path.join(content_dir, match.group(1))
    if not os.path.exists(image_path):
        print(f"Image referenced but not found: {image_path}")
        return None
    return image_path


def detect_content_ref(filepath: str) -> str:
    """Detect E## or INTEL-# from the file content."""
    with open(filepath) as f:
        content = f.read()

    # Check INTEL first — INTEL files reference E## in Learn More section
    m = re.search(r"\bINTEL-(\d+)\b", content)
    if m:
        return f"INTEL-{m.group(1)}"

    m = re.search(r"\bE(\d{2,3})\b", content)
    if m:
        return f"E{m.group(1)}"

    return os.path.basename(filepath).replace(".md", "")


def build_firrisk_url(filepath: str, content_ref: str) -> str:
    """Build the firrisk.ai URL for this content."""
    slug = os.path.basename(filepath).replace(".md", "")
    # Remove date prefix (YYYY-MM-DD-)
    parts = slug.split("-", 3)
    if len(parts) > 3:
        slug_clean = parts[3]
    else:
        slug_clean = slug

    if content_ref.startswith("E"):
        return f"https://firrisk.ai/tuesday/{content_ref.lower()}-{slug_clean}/"
    elif content_ref.startswith("INTEL"):
        return f"https://firrisk.ai/intel/{content_ref.lower().replace('-', '-')}-{slug_clean}/"
    return f"https://firrisk.ai/"


# --- LinkedIn API ---

def upload_image(image_path: str, access_token: str, person_id: str) -> str:
    """Upload image to LinkedIn. Returns image URN."""
    print(f"Uploading image: {image_path}")
    headers = li_headers(access_token)

    # Step 1: Initialize upload
    init_resp = requests.post(
        f"{LI_API}/images?action=initializeUpload",
        headers=headers,
        json={
            "initializeUploadRequest": {
                "owner": f"urn:li:person:{person_id}"
            }
        }
    )

    if init_resp.status_code != 200:
        raise RuntimeError(f"Image init failed {init_resp.status_code}: {init_resp.text}")

    upload_data = init_resp.json()["value"]
    upload_url = upload_data["uploadUrl"]
    image_urn = upload_data["image"]

    # Step 2: Upload binary
    with open(image_path, "rb") as f:
        img_data = f.read()

    put_resp = requests.put(
        upload_url,
        data=img_data,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/octet-stream",
        }
    )

    if put_resp.status_code not in (200, 201):
        raise RuntimeError(f"Image upload failed {put_resp.status_code}: {put_resp.text}")

    print(f"Image uploaded: {image_urn}")
    return image_urn


def create_post(text: str, access_token: str, person_id: str, image_urn: str = None) -> str:
    """Create a LinkedIn feed post. Returns post URN."""
    headers = li_headers(access_token)

    payload = {
        "author": f"urn:li:person:{person_id}",
        "commentary": text,
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": []
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }

    if image_urn:
        payload["content"] = {
            "media": {
                "id": image_urn
            }
        }

    resp = requests.post(f"{LI_API}/posts", headers=headers, json=payload)

    if resp.status_code in (200, 201):
        # Post URN is in the x-restli-id header
        post_urn = resp.headers.get("x-restli-id", "")
        if not post_urn:
            # Try response body
            data = resp.json() if resp.text else {}
            post_urn = data.get("id", "unknown")
        print(f"Post created: {post_urn}")
        return post_urn
    else:
        raise RuntimeError(f"Post failed {resp.status_code}: {resp.text}")


def add_comment(post_urn: str, text: str, access_token: str, person_id: str):
    """Add a comment to a post (for dropping the firrisk.ai link)."""
    headers = li_headers(access_token)

    # URL-encode the URN for the path
    encoded_urn = urllib.parse.quote(post_urn, safe="")

    resp = requests.post(
        f"{LI_API}/socialActions/{encoded_urn}/comments",
        headers=headers,
        json={
            "actor": f"urn:li:person:{person_id}",
            "message": {
                "text": text
            }
        }
    )

    if resp.status_code in (200, 201):
        print("Link comment added.")
    else:
        print(f"Warning: Comment failed {resp.status_code}: {resp.text}")
        print("Post succeeded — add the link comment manually.")


def update_db(content_ref: str):
    """Mark content as posted on LinkedIn in our tracking DB."""
    import sqlite3
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "x_platform.db")
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        conn.execute(
            "UPDATE content_status SET linkedin_posted=1 WHERE content_ref=?",
            (content_ref,)
        )
        conn.commit()
        conn.close()
        print(f"DB updated: {content_ref} linkedin_posted=1")


def do_linkedin_post(li_text, image_path, content_ref, firrisk_url, no_comment=False):
    """Execute the LinkedIn post (image upload + post + comment)."""
    access_token = get_keychain_secret(KEYCHAIN_KEYS["access_token"])
    person_id = get_keychain_secret(KEYCHAIN_KEYS["person_id"])

    image_urn = None
    if image_path:
        image_urn = upload_image(image_path, access_token, person_id)

    print("Posting to LinkedIn...")
    post_urn = create_post(li_text, access_token, person_id, image_urn)

    if not no_comment:
        time.sleep(2)
        comment_text = f"Full {content_ref} analysis: {firrisk_url}"
        add_comment(post_urn, comment_text, access_token, person_id)

    update_db(content_ref)
    print(f"Done! Check your LinkedIn feed.")
    return post_urn


# --- Main ---

def main():
    parser = argparse.ArgumentParser(
        description="Post FIR Risk content to LinkedIn (algorithm-friendly: native post + link comment)"
    )
    parser.add_argument("file", nargs="?", help="Path to newsletter/INTEL markdown file")
    parser.add_argument("--setup", action="store_true", help="Run OAuth setup flow")
    parser.add_argument("--dry-run", action="store_true", help="Preview post without publishing")
    parser.add_argument("--no-image", action="store_true", help="Post without image")
    parser.add_argument("--no-comment", action="store_true", help="Skip the link comment")
    parser.add_argument("--schedule", type=int, metavar="MINUTES",
                        help="Schedule post to go out in N minutes")
    args = parser.parse_args()

    if args.setup:
        setup_oauth()
        return

    if not args.file:
        parser.error("File path required (or use --setup)")

    # Extract content
    print(f"Reading: {args.file}")
    li_text = extract_linkedin_post(args.file)
    image_path = extract_image_path(args.file) if not args.no_image else None
    content_ref = detect_content_ref(args.file)
    firrisk_url = build_firrisk_url(args.file, content_ref)

    print(f"Content: {content_ref}")
    print(f"Post length: {len(li_text)} characters")
    if image_path:
        print(f"Image: {image_path}")
    print(f"Link comment: {firrisk_url}")

    if args.dry_run:
        print(f"\n{'=' * 50}")
        print("DRY RUN — LinkedIn Post Preview")
        print(f"{'=' * 50}\n")
        if image_path:
            print(f"[IMAGE: {image_path}]\n")
        print(li_text)
        print(f"\n{'=' * 50}")
        print(f"COMMENT: Full {content_ref} analysis: {firrisk_url}")
        print(f"{'=' * 50}")
        print(f"\n{len(li_text)} characters | Content ref: {content_ref}")
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

    do_linkedin_post(li_text, image_path, content_ref, firrisk_url, args.no_comment)


if __name__ == "__main__":
    main()
