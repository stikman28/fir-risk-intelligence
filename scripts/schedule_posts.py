#!/usr/bin/env python3
"""
FIR Risk Social Scheduler — Queue posts across LinkedIn and X.

Uses wall-clock time (not sleep) so posts fire correctly even if the
Mac sleeps. Checks the DB before posting to prevent duplicates if a
post was already sent manually.

Usage:
    # Schedule for a specific time (today or tomorrow):
    python3 schedule_posts.py --linkedin file.md --x file.md --at 07:00

    # Schedule with delay from now:
    python3 schedule_posts.py --linkedin file.md --x file.md --x-delay 5

    # Post immediately:
    python3 schedule_posts.py --linkedin file.md --x file.md

    # From a JSON queue file with absolute times:
    python3 schedule_posts.py queue.json

    # Dry run:
    python3 schedule_posts.py --linkedin file.md --at 07:00 --dry-run

Queue file format (JSON):
[
    {"platform": "linkedin", "file": "intel/2026-03-26-slug.md", "at": "2026-03-27 07:00"},
    {"platform": "x", "file": "intel/2026-03-26-slug.md", "at": "2026-03-27 07:05"}
]
"""

import argparse
import json
import os
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timedelta

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable
DB_PATH = os.path.join(SCRIPTS_DIR, "..", "data", "x_platform.db")


def is_already_posted(platform, content_ref):
    """Check if this content was already posted to this platform."""
    if not os.path.exists(DB_PATH):
        return False
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        if platform == "x":
            row = conn.execute(
                "SELECT x_posted FROM content_status WHERE content_ref = ?",
                (content_ref,)
            ).fetchone()
            conn.close()
            return row and row["x_posted"] == 1
        elif platform == "linkedin":
            row = conn.execute(
                "SELECT linkedin_posted FROM content_status WHERE content_ref = ?",
                (content_ref,)
            ).fetchone()
            conn.close()
            return row and row["linkedin_posted"] == 1
    except Exception:
        pass
    return False


def detect_content_ref(filepath):
    """Detect INTEL-# or E## from file content."""
    try:
        with open(filepath) as f:
            content = f.read(2000)
        import re
        m = re.search(r"\bINTEL-(\d+)\b", content)
        if m:
            return f"INTEL-{m.group(1)}"
        m = re.search(r"\bE(\d{2,3})\b", content)
        if m:
            return f"E{m.group(1)}"
    except Exception:
        pass
    return os.path.basename(filepath).replace(".md", "")


def update_scheduled_status(platform, content_ref, status, result=None):
    """Update scheduled_posts table with outcome."""
    if not os.path.exists(DB_PATH):
        return
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("""
            UPDATE scheduled_posts SET status = ?, result = ?
            WHERE platform = ? AND content_ref = ? AND status = 'pending'
        """, (status, result, platform, content_ref))
        conn.commit()
        conn.close()
    except Exception:
        pass


def run_post(platform, file=None, text=None, image=None, no_comment=False, dry_run=False):
    """Execute a single post via the platform-specific script."""
    if platform == "linkedin":
        if file:
            cmd = [PYTHON, os.path.join(SCRIPTS_DIR, "post_to_linkedin.py"), file]
            if no_comment:
                cmd.append("--no-comment")
        elif text:
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

    max_retries = 5
    retry_delay = 30  # seconds between retries
    for attempt in range(1, max_retries + 1):
        print(f"  Running: {' '.join(cmd[-3:])}" + (f" (attempt {attempt}/{max_retries})" if attempt > 1 else ""))
        result = subprocess.run(cmd, cwd=os.path.join(SCRIPTS_DIR, ".."), capture_output=True, text=True)
        if result.returncode == 0:
            if result.stdout:
                print(result.stdout.rstrip())
            return True
        # Check if it's a network error worth retrying
        stderr = result.stderr or ""
        stdout = result.stdout or ""
        output = stderr + stdout
        is_network_error = any(kw in output for kw in [
            "ConnectionError", "NameResolutionError", "nodename nor servname",
            "Network is unreachable", "Temporary failure in name resolution",
            "Max retries exceeded", "ConnectionRefusedError", "TimeoutError",
        ])
        if is_network_error and attempt < max_retries:
            print(f"  Network error — retrying in {retry_delay}s...")
            time.sleep(retry_delay)
            continue
        else:
            # Non-network error or final attempt — print output and fail
            if result.stdout:
                print(result.stdout.rstrip())
            if result.stderr:
                print(result.stderr.rstrip())
            if is_network_error:
                print(f"  FAILED after {max_retries} retries — network still unavailable")
            return False
    return False


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


def wait_until(target_time, check_interval=30):
    """
    Wait until target_time using wall-clock checks.
    Survives Mac sleep — checks actual time every interval.
    Returns True if time reached, False if interrupted.
    """
    while datetime.now() < target_time:
        remaining = (target_time - datetime.now()).total_seconds()
        # Sleep for min of check_interval or remaining time
        sleep_time = min(check_interval, max(remaining, 1))
        time.sleep(sleep_time)
    return True


def run_queue(queue, dry_run=False):
    """Execute a queue of scheduled posts with wall-clock timing."""
    print(f"\n{'=' * 60}")
    print(f"FIR Risk Social Scheduler — {len(queue)} posts queued")
    print(f"{'=' * 60}\n")

    # Show schedule
    for i, item in enumerate(queue, 1):
        platform = item["platform"]
        target = item.get("_target_time", datetime.now())
        label = os.path.basename(item['file']) if item.get('file') else (item.get('text', '')[:40] + '...')
        is_now = target <= datetime.now()
        print(f"[{i}/{len(queue)}] {platform.upper():>2} — {label} — {'NOW' if is_now else f'{target:%I:%M %p}'}")

    if dry_run:
        print(f"\n(Dry run — no posts will be sent)\n")

    print(f"\nStarting at {datetime.now():%I:%M:%S %p}...\n")

    for i, item in enumerate(queue, 1):
        platform = item["platform"]
        target = item.get("_target_time", datetime.now())
        content_ref = item.get("_content_ref", "")

        # Check if already posted (manual post or previous run)
        if content_ref and is_already_posted(platform, content_ref):
            print(f"\n[{datetime.now():%H:%M:%S}] Skipping {i}/{len(queue)}: {platform.upper()} {content_ref} — already posted")
            update_scheduled_status(platform, content_ref, "skipped", "Already posted")
            continue

        # Wait for target time (wall-clock, survives sleep)
        if target > datetime.now():
            remaining = (target - datetime.now()).total_seconds() / 60
            print(f"\n  Waiting until {target:%I:%M %p} ({remaining:.0f} min)...")
            if not dry_run:
                wait_until(target)

                # Re-check after waking — might have been posted manually
                if content_ref and is_already_posted(platform, content_ref):
                    print(f"  Skipping — {content_ref} was posted manually while waiting")
                    update_scheduled_status(platform, content_ref, "skipped", "Posted manually")
                    continue

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
        if content_ref:
            update_scheduled_status(platform, content_ref,
                                    "completed" if success else "failed",
                                    f"Posted at {datetime.now():%Y-%m-%d %H:%M}")

    print(f"\n{'=' * 60}")
    print(f"Queue complete! {datetime.now():%I:%M:%S %p}")
    print(f"{'=' * 60}")


def parse_at_time(at_str):
    """Parse --at time string into a datetime. If time has passed today, schedule for tomorrow."""
    try:
        target = datetime.strptime(at_str, "%H:%M").replace(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
        )
        if target <= datetime.now():
            target += timedelta(days=1)
        return target
    except ValueError:
        # Try full datetime format
        try:
            return datetime.strptime(at_str, "%Y-%m-%d %H:%M")
        except ValueError:
            raise argparse.ArgumentTypeError(f"Invalid time format: {at_str}. Use HH:MM or YYYY-MM-DD HH:MM")


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
    parser.add_argument("--x", metavar="FILE", help="X post from markdown file")
    parser.add_argument("--x-delay", type=int, default=5, metavar="MIN",
                        help="Delay X post after LinkedIn (default: 5 min)")
    parser.add_argument("--at", metavar="TIME",
                        help="Schedule for specific time: HH:MM (today/tomorrow) or YYYY-MM-DD HH:MM")
    parser.add_argument("--no-comment", action="store_true",
                        help="Skip LinkedIn link comment")

    args = parser.parse_args()

    # Build queue
    queue = []

    if args.queue_file:
        with open(args.queue_file) as f:
            raw_queue = json.load(f)
        for item in raw_queue:
            if item.get("at"):
                item["_target_time"] = datetime.strptime(item["at"], "%Y-%m-%d %H:%M")
            else:
                item["_target_time"] = datetime.now()
            if item.get("file"):
                item["_content_ref"] = detect_content_ref(item["file"])
            queue.append(item)
    else:
        base_time = parse_at_time(args.at) if args.at else datetime.now()

        if args.linkedin:
            content_ref = detect_content_ref(args.linkedin)
            queue.append({
                "platform": "linkedin",
                "file": args.linkedin,
                "no_comment": args.no_comment,
                "_target_time": base_time,
                "_content_ref": content_ref,
            })
        if args.linkedin_text:
            queue.append({
                "platform": "linkedin",
                "text": args.linkedin_text,
                "image": args.linkedin_image,
                "_target_time": base_time,
                "_content_ref": "",
            })
        if args.x:
            content_ref = detect_content_ref(args.x)
            x_time = base_time + timedelta(minutes=args.x_delay) if args.at else datetime.now()
            queue.append({
                "platform": "x",
                "file": args.x,
                "_target_time": x_time,
                "_content_ref": content_ref,
            })

    if not queue:
        parser.error("Provide a queue file or use --linkedin/--x flags")

    # Sort by target time
    queue.sort(key=lambda x: x.get("_target_time", datetime.now()))

    run_queue(queue, args.dry_run)


if __name__ == "__main__":
    main()
