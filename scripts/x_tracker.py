"""Post tracker — sync own timeline, scan content, refresh metrics."""

import os
import re

import requests

from x_auth import get_auth, get_user_id
from x_db import get_conn, upsert_post, upsert_content_status, log_fetch

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")
COST_PER_READ = 0.01


def detect_post_type(text):
    """Auto-detect post type from text content."""
    if not text:
        return "organic", None
    # Newsletter: look for E## pattern
    m = re.search(r"\bE(\d{2,3})\b", text)
    if m and ("FIR Risk" in text or "Tuesday" in text):
        return "newsletter", f"E{m.group(1)}"
    # INTEL: look for INTEL-# pattern
    m = re.search(r"\bINTEL[- ]?(\d+)\b", text, re.IGNORECASE)
    if m:
        return "intel", f"INTEL-{m.group(1)}"
    return "organic", None


def sync_timeline(limit=20, include_replies=True):
    """Fetch recent posts from @stikman28 and store in DB."""
    auth = get_auth()
    user_id = get_user_id(auth)

    params = {
        "max_results": min(limit, 100),
        "tweet.fields": "created_at,public_metrics,text,referenced_tweets,in_reply_to_user_id",
        "expansions": "referenced_tweets.id,referenced_tweets.id.author_id",
        "user.fields": "username",
        "exclude": "retweets",
    }
    if not include_replies:
        params["exclude"] = "retweets,replies"

    all_tweets = []
    includes_users = {}
    next_token = None

    while len(all_tweets) < limit:
        if next_token:
            params["pagination_token"] = next_token

        resp = requests.get(
            f"https://api.x.com/2/users/{user_id}/tweets",
            params=params, auth=auth,
        )
        if resp.status_code != 200:
            print(f"API error {resp.status_code}: {resp.text}")
            break

        data = resp.json()
        tweets = data.get("data", [])
        if not tweets:
            break

        # Build user ID → username lookup from includes
        for user in data.get("includes", {}).get("users", []):
            includes_users[user["id"]] = user.get("username", "")

        all_tweets.extend(tweets)
        next_token = data.get("meta", {}).get("next_token")
        if not next_token:
            break

    conn = get_conn()
    reply_count = 0
    quote_count = 0

    for tw in all_tweets[:limit]:
        post_type, content_ref = detect_post_type(tw.get("text", ""))
        metrics = tw.get("public_metrics", {})

        # Parse referenced tweets for reply/quote info
        refs = tw.get("referenced_tweets", [])
        is_reply = 0
        reply_to_tweet_id = None
        reply_to_username = None
        is_quote = 0
        quote_of_tweet_id = None

        for ref in refs:
            if ref["type"] == "replied_to":
                is_reply = 1
                reply_to_tweet_id = ref["id"]
                reply_to_user_id = tw.get("in_reply_to_user_id")
                if reply_to_user_id:
                    reply_to_username = includes_users.get(reply_to_user_id)
                if post_type == "organic":
                    post_type = "reply"
                reply_count += 1
            elif ref["type"] == "quoted":
                is_quote = 1
                quote_of_tweet_id = ref["id"]
                if post_type == "organic":
                    post_type = "quote"
                quote_count += 1

        upsert_post(conn, tw["id"], tw["created_at"], tw.get("text", ""),
                     metrics, post_type, content_ref,
                     is_reply=is_reply, reply_to_tweet_id=reply_to_tweet_id,
                     reply_to_username=reply_to_username,
                     is_quote=is_quote, quote_of_tweet_id=quote_of_tweet_id)

    log_fetch(conn, "own_timeline", "self", len(all_tweets), len(all_tweets) * COST_PER_READ)
    conn.commit()
    conn.close()

    print(f"Synced {len(all_tweets)} posts from @stikman28 "
          f"({reply_count} replies, {quote_count} quotes)")
    for tw in all_tweets[:limit]:
        post_type, content_ref = detect_post_type(tw.get("text", ""))
        metrics = tw.get("public_metrics", {})
        refs = tw.get("referenced_tweets", [])
        is_reply = any(r["type"] == "replied_to" for r in refs)
        is_qt = any(r["type"] == "quoted" for r in refs)
        if is_reply:
            label = "reply"
        elif is_qt:
            label = "quote"
        else:
            label = content_ref or post_type
        preview = tw.get("text", "")[:80].replace("\n", " ")
        print(f"  [{label:>12}] {tw['created_at'][:10]}  "
              f"♥{metrics.get('like_count',0)} ↻{metrics.get('retweet_count',0)} "
              f"💬{metrics.get('reply_count',0)}  {preview}...")


def refresh_metrics(days=7):
    """Refresh engagement metrics for recent posts."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT tweet_id FROM posts
        WHERE posted_at >= datetime('now', ?)
        ORDER BY posted_at DESC
    """, (f"-{days} days",)).fetchall()

    if not rows:
        print(f"No posts found in last {days} days.")
        conn.close()
        return

    tweet_ids = [r["tweet_id"] for r in rows]
    auth = get_auth()

    # API supports up to 100 IDs per request
    for i in range(0, len(tweet_ids), 100):
        batch = tweet_ids[i:i+100]
        resp = requests.get(
            "https://api.x.com/2/tweets",
            params={"ids": ",".join(batch), "tweet.fields": "public_metrics,created_at"},
            auth=auth,
        )
        if resp.status_code != 200:
            print(f"API error {resp.status_code}: {resp.text}")
            continue

        for tw in resp.json().get("data", []):
            metrics = tw.get("public_metrics", {})
            conn.execute("""
                UPDATE posts SET likes=?, retweets=?, replies=?, quotes=?,
                    bookmarks=?, impressions=?, metrics_updated_at=datetime('now'),
                    updated_at=datetime('now')
                WHERE tweet_id=?
            """, (metrics.get("like_count", 0), metrics.get("retweet_count", 0),
                  metrics.get("reply_count", 0), metrics.get("quote_count", 0),
                  metrics.get("bookmark_count", 0), metrics.get("impression_count", 0),
                  tw["id"]))

    log_fetch(conn, "metrics_refresh", "self", len(tweet_ids), len(tweet_ids) * COST_PER_READ)
    conn.commit()
    conn.close()
    print(f"Refreshed metrics for {len(tweet_ids)} posts")


def scan_content():
    """Scan newsletters/ and intel/ directories, update content_status."""
    conn = get_conn()
    count = 0

    # Scan newsletters
    nl_dir = os.path.join(REPO_ROOT, "newsletters")
    if os.path.isdir(nl_dir):
        for fname in sorted(os.listdir(nl_dir)):
            if not fname.endswith(".md") or fname in ("README.md", "TEMPLATE.md"):
                continue
            fpath = os.path.join(nl_dir, fname)
            with open(fpath) as f:
                content = f.read()
            # Extract edition from first line
            m = re.search(r"E(\d{2,3})", content[:200])
            if not m:
                continue
            ref = f"E{m.group(1)}"
            # Extract title
            title_match = re.match(r"#\s*(.+)", content)
            title = title_match.group(1).strip() if title_match else fname
            # Check for X POST and LINKEDIN POST sections
            has_x = 1 if re.search(r"## X POST", content) else 0
            has_li = 1 if re.search(r"## LINKEDIN POST", content) else 0
            # Extract date
            date_match = re.search(r"\*\*(?:Original Publish )?Date:\*\*\s*(.+)", content)
            pub_date = date_match.group(1).strip() if date_match else None

            upsert_content_status(conn, "newsletter", ref, f"newsletters/{fname}",
                                  title, pub_date, has_x, has_li)
            count += 1

    # Scan intel
    intel_dir = os.path.join(REPO_ROOT, "intel")
    if os.path.isdir(intel_dir):
        for fname in sorted(os.listdir(intel_dir)):
            if not fname.endswith(".md") or fname in ("README.md", "TEMPLATE.md"):
                continue
            fpath = os.path.join(intel_dir, fname)
            with open(fpath) as f:
                content = f.read()
            m = re.search(r"INTEL[- ]?(\d+)", content[:200])
            if not m:
                continue
            ref = f"INTEL-{m.group(1)}"
            title_match = re.match(r"#\s*(.+)", content)
            title = title_match.group(1).strip() if title_match else fname
            has_x = 1 if re.search(r"## X POST", content) else 0
            has_li = 1 if re.search(r"## LINKEDIN POST", content) else 0
            date_match = re.search(r"\*\*Date:\*\*\s*(.+)", content)
            pub_date = date_match.group(1).strip() if date_match else None

            upsert_content_status(conn, "intel", ref, f"intel/{fname}",
                                  title, pub_date, has_x, has_li)
            count += 1

    conn.commit()
    conn.close()
    print(f"Scanned {count} content files")


def show_status(content_type="all"):
    """Show posting status for all content."""
    conn = get_conn()
    where = ""
    params = ()
    if content_type != "all":
        where = "WHERE content_type = ?"
        params = (content_type,)

    rows = conn.execute(f"""
        SELECT content_type, content_ref, title, has_x_post, x_posted, tweet_id,
               has_linkedin, linkedin_posted, website_live
        FROM content_status {where}
        ORDER BY content_type, content_ref
    """, params).fetchall()
    conn.close()

    if not rows:
        print("No content found. Run 'scan' first.")
        return

    print(f"\n{'Type':<12} {'Ref':<10} {'X Post?':<8} {'Posted?':<8} {'Title'}")
    print("-" * 90)
    for r in rows:
        has_x = "Yes" if r["has_x_post"] else "—"
        posted = "Posted" if r["x_posted"] else "Pending" if r["has_x_post"] else "—"
        title = (r["title"] or "")[:50]
        print(f"{r['content_type']:<12} {r['content_ref']:<10} {has_x:<8} {posted:<8} {title}")


def show_history(limit=20, post_type="all", sort="date"):
    """Show post history with engagement metrics."""
    conn = get_conn()
    where = ""
    params = []
    if post_type != "all":
        where = "WHERE post_type = ?"
        params.append(post_type)

    sort_col = {
        "date": "posted_at DESC",
        "likes": "likes DESC",
        "impressions": "impressions DESC",
        "retweets": "retweets DESC",
    }.get(sort, "posted_at DESC")

    rows = conn.execute(f"""
        SELECT tweet_id, posted_at, post_type, content_ref,
               likes, retweets, replies, quotes, bookmarks, impressions, text_preview
        FROM posts {where}
        ORDER BY {sort_col}
        LIMIT ?
    """, params + [limit]).fetchall()
    conn.close()

    if not rows:
        print("No posts found. Run 'sync' first.")
        return

    print(f"\n{'Date':<12} {'Type':<12} {'♥':>5} {'↻':>5} {'💬':>5} {'👁':>8}  Preview")
    print("-" * 95)
    for r in rows:
        label = r["content_ref"] or r["post_type"]
        preview = (r["text_preview"] or "")[:60].replace("\n", " ")
        imp = f"{r['impressions']:,}" if r["impressions"] else "—"
        print(f"{r['posted_at'][:10]:<12} {label:<12} {r['likes']:>5} {r['retweets']:>5} "
              f"{r['replies']:>5} {imp:>8}  {preview}")


def show_activity(days=7):
    """Show all activity — original posts, replies, quotes — with context."""
    conn = get_conn()
    rows = conn.execute("""
        SELECT tweet_id, posted_at, post_type, content_ref, full_text,
               is_reply, reply_to_tweet_id, reply_to_username,
               is_quote, quote_of_tweet_id,
               likes, retweets, replies, impressions
        FROM posts
        WHERE posted_at >= datetime('now', ?)
        ORDER BY posted_at DESC
    """, (f"-{days} days",)).fetchall()
    conn.close()

    if not rows:
        print(f"No activity in last {days} days. Run 'sync' first.")
        return

    # Count by type
    type_counts = {}
    for r in rows:
        t = r["post_type"]
        type_counts[t] = type_counts.get(t, 0) + 1

    total = len(rows)
    print(f"\nActivity summary (last {days} days): {total} total")
    for t, c in sorted(type_counts.items()):
        print(f"  {t}: {c}")

    print(f"\n{'Date':<12} {'Type':<10} {'To':<20} {'♥':>4} {'↻':>4} {'💬':>4} {'👁':>7}  Preview")
    print("-" * 105)
    for r in rows:
        preview = (r["full_text"] or "")[:50].replace("\n", " ")
        to_user = ""
        if r["is_reply"] and r["reply_to_username"]:
            to_user = f"@{r['reply_to_username']}"
        elif r["is_quote"]:
            to_user = "[quote]"
        imp = f"{r['impressions']:,}" if r["impressions"] else "—"
        print(f"{r['posted_at'][:10]:<12} {r['post_type']:<10} {to_user:<20} "
              f"{r['likes']:>4} {r['retweets']:>4} {r['replies']:>4} {imp:>7}  {preview}")
        if r["is_reply"] and r["reply_to_tweet_id"]:
            print(f"{'':>12} ↳ replying to https://x.com/{r['reply_to_username'] or 'i'}/status/{r['reply_to_tweet_id']}")

    # Engagement rate
    originals = [r for r in rows if not r["is_reply"] and not r["is_quote"]]
    replies_out = [r for r in rows if r["is_reply"]]
    quotes_out = [r for r in rows if r["is_quote"]]
    print(f"\n  Originals: {len(originals)}  |  Replies: {len(replies_out)}  |  Quotes: {len(quotes_out)}")
    if originals:
        avg_likes = sum(r["likes"] for r in originals) / len(originals)
        avg_imp = sum(r["impressions"] for r in originals) / len(originals)
        print(f"  Avg engagement on originals: ♥{avg_likes:.1f}  👁{avg_imp:.0f}")


def show_priorities(days=3, max_items=5):
    """Show prioritized actions for limited X time (~20 min)."""
    conn = get_conn()

    print("\n" + "=" * 60)
    print("  X PRIORITIES — Where to spend your time today")
    print("=" * 60)

    # 1. Check for pending content to post
    pending = conn.execute("""
        SELECT content_ref, title FROM content_status
        WHERE has_x_post = 1 AND x_posted = 0
        ORDER BY content_ref
    """).fetchall()
    if pending:
        print(f"\n1. PUBLISH ({len(pending)} ready to post)")
        for p in pending:
            title = (p["title"] or "")[:55]
            print(f"   → {p['content_ref']}: {title}")

    # 2. High-engagement influencer posts to reply to
    trending = conn.execute("""
        SELECT tweet_id, author_username, posted_at, full_text,
               likes, retweets, replies,
               (likes + retweets*3 + replies*2) AS score
        FROM feed_posts
        WHERE posted_at >= datetime('now', ?)
          AND is_retweet = 0
          AND flagged = 0
          AND engaged = 0
          AND likes >= 20
        ORDER BY score DESC
        LIMIT ?
    """, (f"-{days} days", max_items)).fetchall()

    if trending:
        print(f"\n2. ENGAGE — Top posts to reply to (last {days} days)")
        for t in trending:
            preview = (t["full_text"] or "")[:55].replace("\n", " ")
            print(f"   → @{t['author_username']} (♥{t['likes']} ↻{t['retweets']}): {preview}")
            print(f"     https://x.com/{t['author_username']}/status/{t['tweet_id']}")

    # 3. Flagged posts not yet engaged
    flagged = conn.execute("""
        SELECT tweet_id, author_username, flag_reason, full_text
        FROM feed_posts
        WHERE flagged = 1 AND engaged = 0
        ORDER BY posted_at DESC
        LIMIT ?
    """, (max_items,)).fetchall()

    if flagged:
        print(f"\n3. FLAGGED — Posts you marked for engagement")
        for f_row in flagged:
            preview = (f_row["full_text"] or "")[:55].replace("\n", " ")
            reason = f" ({f_row['flag_reason']})" if f_row["flag_reason"] else ""
            print(f"   → @{f_row['author_username']}{reason}: {preview}")
            print(f"     https://x.com/{f_row['author_username']}/status/{f_row['tweet_id']}")

    # 4. Metrics check — posts that might need a boost
    own_recent = conn.execute("""
        SELECT tweet_id, posted_at, content_ref, post_type, likes, impressions, full_text
        FROM posts
        WHERE posted_at >= datetime('now', '-7 days')
          AND is_reply = 0
        ORDER BY posted_at DESC
        LIMIT 5
    """).fetchall()

    if own_recent:
        print(f"\n4. YOUR RECENT POSTS — Consider boosting low performers")
        for r in own_recent:
            label = r["content_ref"] or r["post_type"]
            preview = (r["full_text"] or "")[:50].replace("\n", " ")
            imp = f"👁{r['impressions']:,}" if r["impressions"] else "👁—"
            print(f"   {label:<10} ♥{r['likes']} {imp}  {preview}")

    # 5. Time allocation suggestion
    print(f"\n5. SUGGESTED TIME SPLIT (20 min)")
    if pending:
        print("   • 3 min — Publish pending content")
    print("   • 5 min — Reply to 1-2 trending posts with substance")
    if flagged:
        print("   • 5 min — Engage with flagged posts")
    print("   • 5 min — Quote-tweet one post with your take")
    print("   • 2 min — Check metrics on recent posts")
    print()

    conn.close()


def mark_article(content_ref, url=None):
    """Mark content as published via X Article (manual UI post)."""
    conn = get_conn()
    from datetime import datetime, timezone

    now = datetime.now(timezone.utc).isoformat()
    post_type = "intel" if content_ref.startswith("INTEL") else "newsletter"

    # Look up content_status for title
    row = conn.execute(
        "SELECT title, source_file FROM content_status WHERE content_ref=?",
        (content_ref,)
    ).fetchone()
    title = row["title"] if row else content_ref
    source_file = row["source_file"] if row else None

    # Create a post record with article- prefix as pseudo tweet ID
    pseudo_id = f"article-{content_ref.lower()}-{now[:10]}"
    text = f"[X Article] {title}"
    if url:
        text += f"\n{url}"

    upsert_post(conn, pseudo_id, now, text, {}, post_type, content_ref, source_file)

    # Also set the format on the post
    conn.execute(
        "UPDATE posts SET post_type=? WHERE tweet_id=?",
        (f"{post_type}_article", pseudo_id)
    )

    # Mark content as posted
    conn.execute(
        "UPDATE content_status SET x_posted=1, tweet_id=? WHERE content_ref=?",
        (pseudo_id, content_ref)
    )

    conn.commit()
    conn.close()
    print(f"Marked {content_ref} as X Article (published manually)")
    if url:
        print(f"  URL: {url}")
    print(f"  Run 'metrics' later — metrics will need manual update or 'sync' to pick up the real tweet.")


def link_tweet(tweet_id, content_ref):
    """Link a tweet to a content reference (e.g., E82, INTEL-5)."""
    conn = get_conn()

    # Update post record
    conn.execute("""
        UPDATE posts SET content_ref=?, post_type=?,
            updated_at=datetime('now')
        WHERE tweet_id=?
    """, (content_ref,
          "intel" if content_ref.startswith("INTEL") else "newsletter",
          tweet_id))

    # Update content_status
    conn.execute("""
        UPDATE content_status SET x_posted=1, tweet_id=?
        WHERE content_ref=?
    """, (tweet_id, content_ref))

    conn.commit()
    conn.close()
    print(f"Linked tweet {tweet_id} → {content_ref}")
