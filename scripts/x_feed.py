"""Influencer feed monitor — fetch, trending, engagement tracking."""

import time

import requests

from x_auth import get_auth
from x_db import get_conn, upsert_feed_post, log_fetch

COST_PER_READ = 0.01
COST_PER_LOOKUP = 0.01


def resolve_user_ids():
    """Resolve X user IDs for influencers that don't have one yet."""
    conn = get_conn()
    rows = conn.execute(
        "SELECT username FROM influencers WHERE user_id IS NULL AND active=1"
    ).fetchall()

    if not rows:
        print("All influencer user IDs already resolved.")
        conn.close()
        return

    auth = get_auth()
    resolved = 0

    # Batch lookup: up to 100 usernames per request
    usernames = [r["username"] for r in rows]
    for i in range(0, len(usernames), 100):
        batch = usernames[i:i+100]
        resp = requests.get(
            "https://api.x.com/2/users/by",
            params={"usernames": ",".join(batch), "user.fields": "name"},
            auth=auth,
        )
        if resp.status_code != 200:
            print(f"API error {resp.status_code}: {resp.text}")
            continue

        for user in resp.json().get("data", []):
            conn.execute(
                "UPDATE influencers SET user_id=?, display_name=? WHERE username=?",
                (user["id"], user.get("name"), user["username"])
            )
            resolved += 1

        # Log errors (suspended/not found accounts)
        for err in resp.json().get("errors", []):
            print(f"  Could not resolve @{err.get('value', '?')}: {err.get('detail', 'unknown')}")

        log_fetch(conn, "user_lookup", "batch", len(batch), len(batch) * COST_PER_LOOKUP)

    conn.commit()
    conn.close()
    print(f"Resolved {resolved}/{len(usernames)} user IDs")


def fetch_feed(category=None, limit=10):
    """Fetch recent posts from monitored influencer accounts."""
    conn = get_conn()

    where = "WHERE active=1 AND user_id IS NOT NULL"
    params = []
    if category:
        where += " AND category=?"
        params.append(category)

    influencers = conn.execute(
        f"SELECT username, user_id, display_name, category FROM influencers {where} ORDER BY priority, username",
        params
    ).fetchall()

    if not influencers:
        print("No influencers with resolved user IDs. Run 'x_platform.py init' then 'x_platform.py resolve'.")
        conn.close()
        return

    auth = get_auth()
    total_fetched = 0

    for inf in influencers:
        resp = requests.get(
            f"https://api.x.com/2/users/{inf['user_id']}/tweets",
            params={
                "max_results": min(limit, 100),
                "tweet.fields": "created_at,public_metrics,text,referenced_tweets",
                "exclude": "retweets",
            },
            auth=auth,
        )

        if resp.status_code == 429:
            print(f"  Rate limited — pausing 60s...")
            time.sleep(60)
            continue
        if resp.status_code != 200:
            print(f"  @{inf['username']}: API error {resp.status_code}")
            continue

        tweets = resp.json().get("data", [])
        for tw in tweets:
            metrics = tw.get("public_metrics", {})
            refs = tw.get("referenced_tweets", [])
            is_reply = 1 if any(r["type"] == "replied_to" for r in refs) else 0
            is_quote = 1 if any(r["type"] == "quoted" for r in refs) else 0

            upsert_feed_post(conn, tw["id"], inf["username"], inf["user_id"],
                             tw["created_at"], tw.get("text", ""), metrics,
                             is_reply=is_reply, is_quote=is_quote)

        total_fetched += len(tweets)
        log_fetch(conn, "influencer", inf["username"], len(tweets), len(tweets) * COST_PER_READ)
        name = inf["display_name"] or inf["username"]
        print(f"  @{inf['username']:<25} ({name}) — {len(tweets)} posts")

        # Brief pause between accounts to be rate-limit friendly
        time.sleep(1)

    conn.commit()
    conn.close()
    print(f"\nFetched {total_fetched} posts from {len(influencers)} accounts")


def show_trending(days=3, min_likes=50, min_retweets=20):
    """Show high-engagement posts from influencer feeds."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT tweet_id, author_username, posted_at, full_text,
               likes, retweets, replies, quotes,
               (likes + retweets*3 + replies*2 + quotes*5) AS score
        FROM feed_posts
        WHERE posted_at >= datetime('now', ?)
          AND (likes >= ? OR retweets >= ?)
          AND is_retweet = 0
        ORDER BY score DESC
        LIMIT 30
    """, (f"-{days} days", min_likes, min_retweets)).fetchall()
    conn.close()

    if not rows:
        print(f"No trending posts in last {days} days above thresholds "
              f"(likes≥{min_likes}, retweets≥{min_retweets}). Try lowering thresholds.")
        return

    print(f"\nTrending posts (last {days} days, score = ♥ + ↻×3 + 💬×2 + 🔁×5):\n")
    print(f"{'Score':>6} {'♥':>5} {'↻':>5} {'💬':>5}  {'Account':<25} {'Date':<12} Preview")
    print("-" * 110)
    for r in rows:
        preview = (r["full_text"] or "")[:55].replace("\n", " ")
        print(f"{r['score']:>6} {r['likes']:>5} {r['retweets']:>5} {r['replies']:>5}  "
              f"@{r['author_username']:<24} {r['posted_at'][:10]:<12} {preview}")
        print(f"       https://x.com/{r['author_username']}/status/{r['tweet_id']}")


def manage_influencers(action, username=None, category="cybersecurity", priority="medium", notes=None):
    """Add, remove, or list influencer accounts."""
    conn = get_conn()

    if action == "list":
        rows = conn.execute(
            "SELECT username, display_name, category, priority, active, user_id FROM influencers ORDER BY category, priority, username"
        ).fetchall()
        conn.close()

        if not rows:
            print("No influencers configured. Run 'x_platform.py init' to seed.")
            return

        print(f"\n{'Username':<25} {'Name':<25} {'Category':<16} {'Pri':<7} {'ID?'}")
        print("-" * 85)
        for r in rows:
            status = "Yes" if r["user_id"] else "—"
            active = "" if r["active"] else " [inactive]"
            name = (r["display_name"] or "—")[:24]
            print(f"@{r['username']:<24} {name:<25} {r['category']:<16} {r['priority']:<7} {status}{active}")
        return

    if action == "add" and username:
        username = username.lstrip("@")
        conn.execute("""
            INSERT INTO influencers (username, category, priority, notes)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(username) DO UPDATE SET category=excluded.category,
                priority=excluded.priority, notes=excluded.notes, active=1
        """, (username, category, priority, notes))
        conn.commit()
        conn.close()
        print(f"Added @{username} ({category}, {priority})")
        return

    if action == "remove" and username:
        username = username.lstrip("@")
        conn.execute("UPDATE influencers SET active=0 WHERE username=?", (username,))
        conn.commit()
        conn.close()
        print(f"Deactivated @{username}")
        return


def flag_post(tweet_id, reason=None):
    """Flag a feed post for engagement."""
    conn = get_conn()
    conn.execute("UPDATE feed_posts SET flagged=1, flag_reason=? WHERE tweet_id=?", (reason, tweet_id))
    conn.commit()
    conn.close()
    print(f"Flagged {tweet_id} for engagement" + (f": {reason}" if reason else ""))


def mark_engaged(tweet_id, our_tweet_id=None):
    """Mark a feed post as engaged (replied/quoted)."""
    conn = get_conn()
    conn.execute("UPDATE feed_posts SET engaged=1, engage_tweet_id=? WHERE tweet_id=?",
                 (our_tweet_id, tweet_id))
    conn.commit()
    conn.close()
    print(f"Marked {tweet_id} as engaged")


def show_engage_queue():
    """Show posts flagged for engagement."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT tweet_id, author_username, posted_at, full_text, likes, retweets,
               flag_reason, engaged
        FROM feed_posts
        WHERE flagged=1
        ORDER BY engaged ASC, posted_at DESC
    """).fetchall()
    conn.close()

    if not rows:
        print("No posts flagged for engagement.")
        return

    print(f"\nEngagement queue:\n")
    for r in rows:
        status = "DONE" if r["engaged"] else "TODO"
        preview = (r["full_text"] or "")[:70].replace("\n", " ")
        print(f"  [{status}] @{r['author_username']} ({r['posted_at'][:10]}) "
              f"♥{r['likes']} ↻{r['retweets']}")
        print(f"         {preview}")
        if r["flag_reason"]:
            print(f"         Reason: {r['flag_reason']}")
        print(f"         https://x.com/{r['author_username']}/status/{r['tweet_id']}")
        print()
