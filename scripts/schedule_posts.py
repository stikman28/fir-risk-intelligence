#!/usr/bin/env python3
"""
FIR Risk Social Scheduler — Queue posts across LinkedIn and X.

Schedule multiple posts with delays between them. Posts execute sequentially,
each waiting its specified delay from the previous post.

Usage:
    # Schedule from a YAML/JSON queue file:
    python3 schedule_posts.py queue.json

    # Quick schedule: LinkedIn now + X in 60 min from same file:
    python3 schedule_posts.py --linkedin newsletters/2026-03-13-slug.md --x newsletters/2026-03-13-slug.md --x-delay 60

    # Ad-hoc text post to LinkedIn in 30 min:
    python3 schedule_posts.py --linkedin-text "Your hook post here" --linkedin-image path/to/image.png --delay 30

    # Dry run — show what would post and when:
    python3 schedule_posts.py queue.json --dry-run

Queue file format (JSON):
[
    {"platform": "linkedin", "file": "newsletters/2026-03-13-slug.md", "delay_min": 0},
    {"platform": "x", "file": "newsletters/2026-03-13-slug.md", "delay_min": 60},
    {"platform": "linkedin", "text": "Hook post text...", "image": "path/to/img.png", "delay_min": 120}
]
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable


def run_post(platform, file=None, text=None, image=None, no_comment=False, dry_run=False):
    """Execute a single post via the platform-specific script."""
    if platform == "linkedin":
        if file:
            cmd = [PYTHON, os.path.join(SCRIPTS_DIR, "post_to_linkedin.py"), file]
            if no_comment:
                cmd.append("--no-comment")
        elif text:
            # Ad-hoc text post — use the LinkedIn API directly
            cmd = [PYTHON, "-c", _adhoc_linkedin_script(text, image)]
        else:
            print("  ERROR: LinkedIn post needs --file or --text")
            return False

    elif platform == "x":
        if file:
            cmd = [PYTHON, os.path.join(SCRIPTS_DIR, "post_to_x.py"), file]
        else:
            print("  ERROR: X posts require a markdown file")
            return False
    else:
        print(f"  ERROR: Unknown platform '{platform}'")
        return False

    if dry_run:
        cmd.append("--dry-run")

    print(f"  Running: {' '.join(cmd[-3:])}")
    result = subprocess.run(cmd, cwd=os.path.join(SCRIPTS_DIR, ".."))
    return result.returncode == 0


def _adhoc_linkedin_script(text, image_path=None):
    """Generate inline Python for ad-hoc LinkedIn text post."""
    escaped_text = text.replace("'", "\\'").replace("\n", "\\n")
    img_line = ""
    if image_path:
        img_line = f"""
# Upload image
init = requests.post(f'{{LI_API}}/images?action=initializeUpload', headers=headers, json={{'initializeUploadRequest': {{'owner': f'urn:li:person:{{person_id}}'}}}})
if init.status_code == 200:
    upload_url = init.json()['value']['uploadUrl']
    image_urn = init.json()['value']['image']
    with open('{image_path}', 'rb') as f:
        requests.put(upload_url, data=f.read(), headers={{'Authorization': f'Bearer {{access_token}}', 'Content-Type': 'application/octet-stream'}})
    payload['content'] = {{'media': {{'id': image_urn}}}}
    print(f'Image uploaded: {{image_urn}}')
"""
    return f"""
import subprocess, requests
def get_key(s):
    return subprocess.run(['security','find-generic-password','-a','stikman28','-s',s,'-w'], capture_output=True, text=True).stdout.strip()
access_token = get_key('LINKEDIN_ACCESS_TOKEN')
person_id = get_key('LINKEDIN_PERSON_ID')
LI_API = 'https://api.linkedin.com/rest'
headers = {{'Authorization': f'Bearer {{access_token}}', 'Linkedin-Version': '202503', 'X-Restli-Protocol-Version': '2.0.0', 'Content-Type': 'application/json'}}
payload = {{'author': f'urn:li:person:{{person_id}}', 'commentary': '{escaped_text}', 'visibility': 'PUBLIC', 'distribution': {{'feedDistribution': 'MAIN_FEED', 'targetEntities': [], 'thirdPartyDistributionChannels': []}}, 'lifecycleState': 'PUBLISHED', 'isReshareDisabledByAuthor': False}}
{img_line}
resp = requests.post(f'{{LI_API}}/posts', headers=headers, json=payload)
if resp.status_code in (200, 201):
    print(f'Posted! URN: {{resp.headers.get("x-restli-id", "unknown")}}')
else:
    print(f'Failed: {{resp.status_code}} {{resp.text}}')
"""


def run_queue(queue, dry_run=False):
    """Execute a queue of scheduled posts."""
    print(f"\n{'=' * 60}")
    print(f"FIR Risk Social Scheduler — {len(queue)} posts queued")
    print(f"{'=' * 60}\n")

    now = datetime.now()
    cumulative_delay = 0

    for i, item in enumerate(queue, 1):
        delay = item.get("delay_min", 0)
        platform = item["platform"]
        post_time = now + timedelta(minutes=cumulative_delay + delay)

        print(f"[{i}/{len(queue)}] {platform.upper()} — ", end="")
        if item.get("file"):
            print(f"{os.path.basename(item['file'])}", end="")
        elif item.get("text"):
            print(f"\"{item['text'][:50]}...\"", end="")
        print(f" — {'NOW' if delay == 0 and cumulative_delay == 0 else f'{post_time:%I:%M %p}'}")

        cumulative_delay += delay

    if dry_run:
        print(f"\n(Dry run — no posts will be sent)\n")

    print(f"\nStarting at {datetime.now():%I:%M:%S %p}...\n")

    cumulative_delay = 0
    for i, item in enumerate(queue, 1):
        delay = item.get("delay_min", 0)
        platform = item["platform"]

        if delay > 0:
            target = datetime.now() + timedelta(minutes=delay)
            print(f"\n  Waiting {delay} min (until {target:%I:%M %p})...")
            if not dry_run:
                time.sleep(delay * 60)

        print(f"\n[{datetime.now():%H:%M:%S}] Posting {i}/{len(queue)}: {platform.upper()}")
        success = run_post(
            platform=platform,
            file=item.get("file"),
            text=item.get("text"),
            image=item.get("image"),
            no_comment=item.get("no_comment", False),
            dry_run=dry_run,
        )

        status = "OK" if success else "FAILED"
        print(f"  [{status}]")

    print(f"\n{'=' * 60}")
    print(f"Queue complete! {datetime.now():%I:%M:%S %p}")
    print(f"{'=' * 60}")


def main():
    parser = argparse.ArgumentParser(
        description="FIR Risk Social Scheduler — queue posts across LinkedIn and X"
    )
    parser.add_argument("queue_file", nargs="?", help="JSON queue file")
    parser.add_argument("--dry-run", action="store_true", help="Preview schedule without posting")

    # Quick scheduling shortcuts
    parser.add_argument("--linkedin", metavar="FILE", help="LinkedIn post from markdown file")
    parser.add_argument("--linkedin-text", metavar="TEXT", help="Ad-hoc LinkedIn text post")
    parser.add_argument("--linkedin-image", metavar="IMG", help="Image for ad-hoc LinkedIn post")
    parser.add_argument("--linkedin-delay", type=int, default=0, metavar="MIN",
                        help="Delay LinkedIn post by N minutes (default: 0)")
    parser.add_argument("--x", metavar="FILE", help="X post from markdown file")
    parser.add_argument("--x-delay", type=int, default=0, metavar="MIN",
                        help="Delay X post by N minutes (default: 0)")
    parser.add_argument("--no-comment", action="store_true",
                        help="Skip LinkedIn link comment")

    args = parser.parse_args()

    # Build queue
    queue = []

    if args.queue_file:
        with open(args.queue_file) as f:
            queue = json.load(f)
    else:
        if args.linkedin:
            queue.append({
                "platform": "linkedin",
                "file": args.linkedin,
                "delay_min": args.linkedin_delay,
                "no_comment": args.no_comment,
            })
        if args.linkedin_text:
            queue.append({
                "platform": "linkedin",
                "text": args.linkedin_text,
                "image": args.linkedin_image,
                "delay_min": args.linkedin_delay if not args.linkedin else 0,
            })
        if args.x:
            queue.append({
                "platform": "x",
                "file": args.x,
                "delay_min": args.x_delay,
            })

    if not queue:
        parser.error("Provide a queue file or use --linkedin/--x flags")

    run_queue(queue, args.dry_run)


if __name__ == "__main__":
    main()
