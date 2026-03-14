#!/usr/bin/env python3
"""
X Platform Tool — Post tracker + influencer feed monitor for @stikman28.

Usage:
    python3 x_platform.py sync              # Fetch own recent posts
    python3 x_platform.py metrics           # Refresh engagement metrics
    python3 x_platform.py scan              # Scan local content files
    python3 x_platform.py status            # Show posting status
    python3 x_platform.py history           # Show post history
    python3 x_platform.py link TWEET_ID REF # Link tweet to content (e.g., E82)
    python3 x_platform.py activity          # Show all activity (posts + replies + quotes)
    python3 x_platform.py priorities        # Daily action plan for limited X time
    python3 x_platform.py feed              # Fetch influencer feeds
    python3 x_platform.py trending          # Show trending posts
    python3 x_platform.py influencers       # List/add/remove influencers
    python3 x_platform.py engage            # Show engagement queue
    python3 x_platform.py resolve           # Resolve influencer user IDs
    python3 x_platform.py cost              # Show API credit usage
    python3 x_platform.py init              # Initialize DB + seed influencers
"""

import argparse
import sys

from x_db import init_db, get_conn


def cmd_init(args):
    from x_config import INFLUENCER_SEED
    init_db()
    conn = get_conn()
    seeded = 0
    for inf in INFLUENCER_SEED:
        conn.execute("""
            INSERT OR IGNORE INTO influencers (username, category, priority, notes)
            VALUES (?, ?, ?, ?)
        """, (inf["username"], inf["category"], inf["priority"], inf.get("notes")))
        seeded += 1
    conn.commit()
    conn.close()
    print(f"Database initialized. Seeded {seeded} influencer accounts.")
    print("Next: run 'x_platform.py resolve' to look up their X user IDs.")


def cmd_sync(args):
    from x_tracker import sync_timeline
    init_db()
    sync_timeline(limit=args.limit)


def cmd_metrics(args):
    from x_tracker import refresh_metrics
    init_db()
    refresh_metrics(days=args.days)


def cmd_scan(args):
    from x_tracker import scan_content
    init_db()
    scan_content()


def cmd_status(args):
    from x_tracker import show_status
    show_status(content_type=args.type)


def cmd_history(args):
    from x_tracker import show_history
    show_history(limit=args.limit, post_type=args.type, sort=args.sort)


def cmd_link(args):
    from x_tracker import link_tweet
    link_tweet(args.tweet_id, args.ref)


def cmd_article(args):
    from x_tracker import mark_article
    mark_article(args.ref, url=args.url)


def cmd_activity(args):
    from x_tracker import show_activity
    show_activity(days=args.days)


def cmd_priorities(args):
    from x_tracker import show_priorities
    show_priorities(days=args.days, max_items=args.limit)


def cmd_feed(args):
    from x_feed import fetch_feed
    init_db()
    fetch_feed(category=args.category, limit=args.limit)


def cmd_trending(args):
    from x_feed import show_trending
    show_trending(days=args.days, min_likes=args.min_likes, min_retweets=args.min_retweets)


def cmd_influencers(args):
    from x_feed import manage_influencers
    if args.add:
        manage_influencers("add", args.add, category=args.category,
                           priority=args.priority, notes=args.notes)
    elif args.remove:
        manage_influencers("remove", args.remove)
    else:
        manage_influencers("list")


def cmd_resolve(args):
    from x_feed import resolve_user_ids
    resolve_user_ids()


def cmd_engage(args):
    from x_feed import flag_post, mark_engaged, show_engage_queue
    if args.flag:
        flag_post(args.flag, reason=args.reason)
    elif args.done:
        mark_engaged(args.done)
    else:
        show_engage_queue()


def cmd_cost(args):
    conn = get_conn()
    rows = conn.execute("""
        SELECT fetch_type,
               COUNT(*) as calls,
               SUM(posts_fetched) as total_posts,
               SUM(credits_used) as total_cost
        FROM fetch_log
        WHERE fetched_at >= datetime('now', ?)
        GROUP BY fetch_type
        ORDER BY total_cost DESC
    """, (f"-{args.days} days",)).fetchall()

    total = conn.execute("""
        SELECT SUM(credits_used) as total FROM fetch_log
        WHERE fetched_at >= datetime('now', ?)
    """, (f"-{args.days} days",)).fetchone()
    conn.close()

    if not rows:
        print(f"No API usage in last {args.days} days.")
        return

    print(f"\nAPI credit usage (last {args.days} days):\n")
    print(f"{'Type':<20} {'Calls':>6} {'Posts':>8} {'Cost':>8}")
    print("-" * 45)
    for r in rows:
        print(f"{r['fetch_type']:<20} {r['calls']:>6} {r['total_posts']:>8} ${r['total_cost']:>7.2f}")
    print("-" * 45)
    print(f"{'TOTAL':<20} {'':>6} {'':>8} ${total['total'] or 0:>7.2f}")


def main():
    parser = argparse.ArgumentParser(
        description="X Platform Tool — Post tracker + influencer monitor (@stikman28)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", help="Command to run")

    # init
    sub.add_parser("init", help="Initialize DB and seed influencer list")

    # sync
    p = sub.add_parser("sync", help="Fetch recent posts from @stikman28")
    p.add_argument("--limit", type=int, default=20, help="Number of posts (default: 20)")

    # metrics
    p = sub.add_parser("metrics", help="Refresh engagement metrics")
    p.add_argument("--days", type=int, default=7, help="Refresh posts from last N days (default: 7)")

    # scan
    sub.add_parser("scan", help="Scan local content files for X POST sections")

    # status
    p = sub.add_parser("status", help="Show content posting status")
    p.add_argument("--type", default="all", choices=["all", "newsletter", "intel"])

    # history
    p = sub.add_parser("history", help="Show post history with metrics")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--type", default="all", choices=["all", "newsletter", "intel", "organic", "reply", "quote"])
    p.add_argument("--sort", default="date", choices=["date", "likes", "impressions", "retweets"])

    # link
    p = sub.add_parser("link", help="Link a tweet to content (e.g., E82, INTEL-5)")
    p.add_argument("tweet_id", help="X tweet ID")
    p.add_argument("ref", help="Content reference (e.g., E82, INTEL-5)")

    # article
    p = sub.add_parser("article", help="Mark content as posted via X Article (manual UI)")
    p.add_argument("ref", help="Content reference (e.g., E83, INTEL-5)")
    p.add_argument("--url", help="X Article URL if known")

    # activity
    p = sub.add_parser("activity", help="Show all activity (posts + replies + quotes)")
    p.add_argument("--days", type=int, default=7)

    # priorities
    p = sub.add_parser("priorities", help="Daily action plan — where to spend your X time")
    p.add_argument("--days", type=int, default=3, help="Look back days for trending (default: 3)")
    p.add_argument("--limit", type=int, default=5, help="Items per section (default: 5)")

    # feed
    p = sub.add_parser("feed", help="Fetch influencer feeds")
    p.add_argument("--category", help="Filter by category")
    p.add_argument("--limit", type=int, default=10, help="Posts per account (default: 10)")

    # trending
    p = sub.add_parser("trending", help="Show trending influencer posts")
    p.add_argument("--days", type=int, default=3)
    p.add_argument("--min-likes", type=int, default=50)
    p.add_argument("--min-retweets", type=int, default=20)

    # influencers
    p = sub.add_parser("influencers", help="List/add/remove influencer accounts")
    p.add_argument("--add", help="Add username")
    p.add_argument("--remove", help="Remove username")
    p.add_argument("--category", default="cybersecurity")
    p.add_argument("--priority", default="medium", choices=["high", "medium", "low"])
    p.add_argument("--notes", help="Notes about this account")

    # resolve
    sub.add_parser("resolve", help="Resolve influencer X user IDs")

    # engage
    p = sub.add_parser("engage", help="Engagement queue — flag/track posts")
    p.add_argument("--flag", help="Flag a tweet ID for engagement")
    p.add_argument("--reason", help="Reason for flagging")
    p.add_argument("--done", help="Mark tweet ID as engaged")

    # cost
    p = sub.add_parser("cost", help="Show API credit usage")
    p.add_argument("--days", type=int, default=30)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "init": cmd_init, "sync": cmd_sync, "metrics": cmd_metrics,
        "scan": cmd_scan, "status": cmd_status, "history": cmd_history,
        "link": cmd_link, "article": cmd_article,
        "activity": cmd_activity, "priorities": cmd_priorities,
        "feed": cmd_feed, "trending": cmd_trending,
        "influencers": cmd_influencers, "resolve": cmd_resolve,
        "engage": cmd_engage, "cost": cmd_cost,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
