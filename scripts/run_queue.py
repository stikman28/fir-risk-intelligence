#!/usr/bin/env python3
"""
FIR Risk queue runner — posts due items from queue JSON files.

Designed to be invoked every 15 min by GitHub Actions (or local cron/launchd).
Scans scripts/*-queue.json for items whose 'at' time has passed and 'posted_at'
is not yet set, posts them, and writes the result back to the queue file.

Queue item format:
    {
        "platform": "linkedin" | "x",
        "file": "intel/2026-04-22-slug.md",
        "at": "2026-04-22 07:00",       # America/New_York (naive = assumed ET)
        "posted_at": "...",              # ISO-8601 UTC, set after success
        "post_id": "...",                # platform post id, set after success
        "error": "..."                   # set if posting failed (can retry)
    }

Usage:
    python3 run_queue.py                     # post everything due
    python3 run_queue.py --dry-run           # show what would post
    python3 run_queue.py --queue FILE.json   # limit to one queue file
"""

import argparse
import glob
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)
TZ_LOCAL = ZoneInfo("America/New_York")

STALE_CUTOFF_HOURS = 36

POST_ID_PATTERNS = {
    "x": re.compile(r"status/(\d+)"),
    "linkedin": re.compile(r"urn:li:share:(\d+)"),
}


def parse_at(at_str: str) -> datetime:
    """Parse a queue 'at' timestamp as America/New_York local time."""
    dt = datetime.strptime(at_str.strip(), "%Y-%m-%d %H:%M")
    return dt.replace(tzinfo=TZ_LOCAL)


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def find_queue_files() -> list[str]:
    return sorted(glob.glob(os.path.join(SCRIPTS_DIR, "*-queue.json")))


def post_item(platform: str, file_path: str, dry_run: bool) -> tuple[bool, str, str]:
    """Invoke the relevant post script. Returns (success, post_id, raw_output)."""
    script = {
        "x": os.path.join(SCRIPTS_DIR, "post_to_x.py"),
        "linkedin": os.path.join(SCRIPTS_DIR, "post_to_linkedin.py"),
    }.get(platform)
    if not script:
        return False, "", f"Unknown platform: {platform}"

    abs_file = os.path.join(REPO_ROOT, file_path)
    cmd = [sys.executable, script, abs_file]
    if dry_run:
        cmd.append("--dry-run")

    result = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT)
    output = result.stdout + "\n" + result.stderr

    if result.returncode != 0:
        return False, "", output

    if dry_run:
        return True, "DRY_RUN", output

    match = POST_ID_PATTERNS[platform].search(result.stdout)
    post_id = match.group(1) if match else ""
    return True, post_id, output


def run(queue_path: str, dry_run: bool) -> int:
    """Process one queue file. Returns count of items posted."""
    with open(queue_path) as f:
        items = json.load(f)

    changed = False
    posted_count = 0
    now = now_utc()

    for item in items:
        if item.get("posted_at"):
            continue
        try:
            due_at = parse_at(item["at"]).astimezone(timezone.utc)
        except Exception as e:
            print(f"  SKIP (bad at): {item.get('at')} — {e}")
            continue
        if due_at > now:
            continue
        if (now - due_at).total_seconds() > STALE_CUTOFF_HOURS * 3600:
            print(f"  SKIP (stale >{STALE_CUTOFF_HOURS}h overdue): {item['platform']} :: {item['file']}")
            continue

        platform = item["platform"]
        file_rel = item["file"]
        print(f"→ Posting {platform} :: {file_rel} (due {item['at']} ET)")

        success, post_id, output = post_item(platform, file_rel, dry_run)
        last_line = output.strip().splitlines()[-1] if output.strip() else ""

        if success:
            if dry_run:
                print(f"  DRY-RUN OK: {last_line}")
            else:
                item["posted_at"] = now_utc().isoformat(timespec="seconds")
                item["post_id"] = post_id
                item.pop("error", None)
                changed = True
                posted_count += 1
                print(f"  OK post_id={post_id}")
        else:
            item["error"] = f"{now_utc().isoformat(timespec='seconds')}: {last_line[:300]}"
            changed = True
            print(f"  FAIL: {last_line}")
            print(output)

    if changed and not dry_run:
        with open(queue_path, "w") as f:
            json.dump(items, f, indent=4)
            f.write("\n")

    return posted_count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Preview without posting")
    ap.add_argument("--queue", help="Single queue file to process (default: all scripts/*-queue.json)")
    args = ap.parse_args()

    queue_files = [args.queue] if args.queue else find_queue_files()
    if not queue_files:
        print("No queue files found.")
        return 0

    total = 0
    for qf in queue_files:
        print(f"\n=== {os.path.basename(qf)} ===")
        total += run(qf, args.dry_run)

    print(f"\nDone. Posted {total} item(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
