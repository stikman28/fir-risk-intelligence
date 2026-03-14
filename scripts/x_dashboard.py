"""FIR Risk Intelligence Dashboard — Content, Social, and Engagement."""

import streamlit as st
import sqlite3
import os
import re
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "x_platform.db")
REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")


def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def read_content_file(source_file):
    """Read a newsletter or INTEL markdown file."""
    fpath = os.path.join(REPO_ROOT, source_file)
    if os.path.exists(fpath):
        with open(fpath) as f:
            return f.read()
    return None


def extract_section(content, section_name):
    """Extract a named ## section from markdown."""
    pattern = rf"## {re.escape(section_name)}\s*\n(.*?)(?=\n## |\n---|\Z)"
    m = re.search(pattern, content, re.DOTALL)
    return m.group(1).strip() if m else None


WEBSITE_ROOT = "/Users/stikman/Projects/ai-assistant/fir-risk-website"


def find_image(source_file):
    """Find the image for a content file. Checks intelligence repo first, then website."""
    content = read_content_file(source_file)
    if not content:
        return None
    m = re.search(r"!\[.*?\]\((images/.+?\.png)\)", content)
    if m:
        # 1. Check intelligence repo (newsletters/images/ or intel/images/)
        content_dir = os.path.dirname(source_file)
        img_path = os.path.join(REPO_ROOT, content_dir, m.group(1))
        if os.path.exists(img_path):
            return img_path

    # 2. Try website repo static/images/ as fallback
    # Extract image filename from content ref
    m2 = re.search(r"!\[.*?\]\((?:images/)?(.+?\.png)\)", content)
    if m2:
        fname = m2.group(1)
        for prefix in ["static/images", "assets/images", "static/images/intel", "assets/images/intel"]:
            web_path = os.path.join(WEBSITE_ROOT, prefix, fname)
            if os.path.exists(web_path):
                return web_path
    return None


# --- Page Config ---
st.set_page_config(
    page_title="FIR Risk Intelligence",
    page_icon="https://firrisk.ai/favicon.ico",
    layout="wide",
)

st.markdown("""
<style>
    .block-container { padding-top: 3.5rem; }
    div[data-testid="stMetric"] { background: #1a1a2e; border-radius: 8px; padding: 12px 16px; }
    a { color: #1DA1F2; }
    .posted { color: #10b981; font-weight: bold; }
    .pending { color: #f59e0b; }
    .na { color: #6b7280; }
    .header-sub { color: #9ca3af; margin-top: -1rem; }
</style>
""", unsafe_allow_html=True)

# Check DB
if not os.path.exists(DB_PATH):
    st.error("Database not found. Run `x_platform.py init` first.")
    st.stop()

conn = get_conn()

# --- Header ---
st.title("FIR Risk Intelligence")
st.markdown(
    '<p class="header-sub">Content publishing + social engagement &nbsp;|&nbsp; '
    '<a href="https://firrisk.ai" target="_blank">firrisk.ai</a> &nbsp;|&nbsp; '
    '<a href="https://x.com/stikman28" target="_blank">@stikman28</a></p>',
    unsafe_allow_html=True
)

# --- Tabs ---
tab_overview, tab_content, tab_social = st.tabs(["Overview", "Content", "Social"])


# ============================================================
# TAB 1: OVERVIEW
# ============================================================
with tab_overview:

    # Hero — latest content with image
    latest = conn.execute("""
        SELECT content_ref, title, source_file, content_type
        FROM content_status
        ORDER BY content_ref DESC LIMIT 1
    """).fetchone()

    if latest:
        hero_img = find_image(latest["source_file"])
        if hero_img:
            col_img, col_info = st.columns([1, 2])
            with col_img:
                st.image(hero_img, width="stretch")
            with col_info:
                st.markdown(f"### Latest: {latest['content_ref']}")
                st.markdown(f"**{latest['title'] or ''}**")
                # Link to firrisk.ai
                ref = latest["content_ref"]
                if ref.startswith("E"):
                    slug = os.path.basename(latest["source_file"]).replace(".md", "")
                    # Remove date prefix for website slug
                    slug_parts = slug.split("-", 3)
                    if len(slug_parts) > 3:
                        web_slug = slug_parts[3]
                    else:
                        web_slug = slug
                    st.markdown(f"[View on firrisk.ai](https://firrisk.ai/tuesday/{ref.lower()}-{web_slug}/)")
                elif ref.startswith("INTEL"):
                    st.markdown(f"[View on firrisk.ai](https://firrisk.ai/intel/)")
            st.divider()

    # Content KPIs
    content_stats = conn.execute("""
        SELECT
            COUNT(*) as total,
            SUM(CASE WHEN content_type='newsletter' THEN 1 ELSE 0 END) as newsletters,
            SUM(CASE WHEN content_type='intel' THEN 1 ELSE 0 END) as intels,
            SUM(has_x_post) as with_x,
            SUM(x_posted) as x_published,
            SUM(has_linkedin) as with_li,
            SUM(linkedin_posted) as li_published
        FROM content_status
    """).fetchone()

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Newsletters", content_stats["newsletters"])
    c2.metric("INTELs", content_stats["intels"])
    c3.metric("X Published", f"{content_stats['x_published'] or 0}/{content_stats['with_x'] or 0}")
    c4.metric("LI Published", f"{content_stats['li_published'] or 0}/{content_stats['with_li'] or 0}")
    c5.metric("Total Content", content_stats["total"])

    # Scheduled posts
    sched_pending = conn.execute(
        "SELECT COUNT(*) as cnt FROM scheduled_posts WHERE status='pending'"
    ).fetchone()
    c6.metric("Scheduled", sched_pending["cnt"] or 0)

    st.divider()

    # X engagement KPIs
    x_stats = conn.execute("""
        SELECT COUNT(*) as posts,
               SUM(likes) as likes,
               SUM(retweets) as retweets,
               SUM(impressions) as impressions
        FROM posts
    """).fetchone()

    feed_stats = conn.execute("SELECT COUNT(*) as total FROM feed_posts").fetchone()
    inf_stats = conn.execute("SELECT COUNT(*) as total FROM influencers WHERE active=1").fetchone()
    cost_stats = conn.execute("SELECT SUM(credits_used) as total FROM fetch_log").fetchone()

    st.subheader("X Engagement")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Posts", x_stats["posts"])
    c2.metric("Total Likes", x_stats["likes"] or 0)
    c3.metric("Impressions", f"{(x_stats['impressions'] or 0):,}")
    c4.metric("Influencers", inf_stats["total"])
    c5.metric("Feed Posts", feed_stats["total"])
    c6.metric("API Spent", f"\\${(cost_stats['total'] or 0):.2f}")

    st.divider()

    # What's next — priorities summary
    st.subheader("What's Next")

    pending_x = conn.execute(
        "SELECT content_ref, title FROM content_status WHERE has_x_post=1 AND x_posted=0"
    ).fetchall()
    pending_li = conn.execute(
        "SELECT content_ref, title FROM content_status WHERE has_linkedin=1 AND linkedin_posted=0"
    ).fetchall()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**X — Pending**")
        if pending_x:
            for p in pending_x:
                st.markdown(f"- {p['content_ref']}: {(p['title'] or '')[:45]}")
        else:
            st.success("All caught up")

    with col2:
        st.markdown("**LinkedIn — Pending**")
        if pending_li:
            for p in pending_li[:10]:
                st.markdown(f"- {p['content_ref']}: {(p['title'] or '')[:45]}")
            if len(pending_li) > 10:
                st.caption(f"...and {len(pending_li) - 10} more")
        else:
            st.success("All caught up")

    # Algorithm playbook
    st.divider()
    algo_col1, algo_col2 = st.columns(2)
    with algo_col1:
        st.markdown("**LinkedIn Algorithm**")
        st.markdown("""
- Native text + image — **never** link in post body
- Drop firrisk.ai URL as **first comment**
- Comments >> Reactions (1 comment = 10-15 likes)
- **Reply to every comment** within 1 hour
- First 60-90 min = make or break window
- 3-5 posts/week, not just on publish day
- 6-9 hashtags per post
- Short hook posts > long newsletters in feed
- Carousels / document posts get 2-3x reach
""")

    with algo_col2:
        st.markdown("**X Algorithm**")
        st.markdown("""
- Long-form posts OK (X Premium, 25K chars)
- Image leads the post — always attach
- 2 hashtags max (#cybersecurity + 1 more)
- Replies to influencers = visibility boost
- Quote-tweets with your take > plain retweets
- Conversational story tone, no bullet points
- Post when related topics are trending
- Engagement within first hour matters most
- Thread replies to your own post = algorithm signal
""")

    # Weekly Content Plan
    st.subheader("Weekly Content Plan")
    st.caption("Maximize reach: repurpose every piece across platforms throughout the week")

    plan_data = [
        ["**Monday**", "INTEL hook post (short)", "INTEL hook post (short)", "Tee up the week's topic"],
        ["**Tuesday**", "Newsletter full post (long-form/Article)", "Newsletter full post (native)", "Publish day — full value everywhere"],
        ["**Tuesday +1hr**", "Newsletter hook post (short)", "Newsletter hook post (short)", "Second touchpoint, different angle"],
        ["**Wednesday**", "Reply to 2 influencer posts", "Reply to 2 influencer posts", "Engage — connect your content to theirs"],
        ["**Thursday**", "Quote-tweet with your take", "Key stat post with image", "Stay visible between editions"],
        ["**Friday**", "INTEL full post or hook", "INTEL full post (native)", "End-of-week intelligence drop"],
        ["**Weekend**", "Browse feed, flag for Monday", "—", "Low effort, prep for next week"],
    ]

    st.markdown("""
| Day | X | LinkedIn | Strategy |
|-----|---|----------|----------|""")
    for row in plan_data:
        st.markdown(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")

    st.markdown("""
**Post types:**
- **Hook post** — 3-5 lines, one shocking stat or insight, image attached, drives awareness
- **Full post** — Complete analysis (X Article or long-form on X, native on LinkedIn)
- **Reply** — Substantive reply to influencer, reference your research
- **Quote-tweet** — Add your analysis on top of someone else's post

**Weekly target:** 8-10 posts across both platforms (4-5 each)
""")

    st.divider()

    # Top engagement opportunities
    top_engage = conn.execute("""
        SELECT author_username, full_text, likes, retweets, tweet_id,
               (likes + retweets*3 + replies*2) AS score
        FROM feed_posts
        WHERE posted_at >= datetime('now', '-3 days')
          AND is_retweet=0 AND likes >= 50
        ORDER BY score DESC LIMIT 3
    """).fetchall()

    if top_engage:
        st.markdown("**Top Engagement Opportunities (last 3 days)**")
        for e in top_engage:
            preview = (e["full_text"] or "")[:100].replace("\n", " ")
            url = f"https://x.com/{e['author_username']}/status/{e['tweet_id']}"
            st.markdown(f"- **@{e['author_username']}** (♥{e['likes']} ↻{e['retweets']}): {preview} [Open]({url})")


# ============================================================
# TAB 2: CONTENT
# ============================================================
with tab_content:

    col1, col2 = st.columns([1, 3])
    with col1:
        content_type = st.radio("Type", ["All", "Newsletters", "INTEL"], key="ct_type")
    with col2:
        search = st.text_input("Search titles", key="ct_search")

    where_parts = []
    params = []
    if content_type == "Newsletters":
        where_parts.append("content_type='newsletter'")
    elif content_type == "INTEL":
        where_parts.append("content_type='intel'")
    if search:
        where_parts.append("title LIKE ?")
        params.append(f"%{search}%")

    where = f"WHERE {' AND '.join(where_parts)}" if where_parts else ""

    all_content = conn.execute(f"""
        SELECT content_type, content_ref, source_file, title, publish_date,
               has_x_post, x_posted, has_linkedin, linkedin_posted, website_live, tweet_id
        FROM content_status {where}
        ORDER BY content_ref DESC
    """, params).fetchall()

    st.caption(f"{len(all_content)} items")

    for c in all_content:
        # Channel status badges
        x_badge = "X:Posted" if c["x_posted"] else ("X:Ready" if c["has_x_post"] else "")
        li_badge = "LI:Posted" if c["linkedin_posted"] else ("LI:Ready" if c["has_linkedin"] else "")
        web_badge = "Web:Live" if c["website_live"] else ""

        badges = []
        if c["x_posted"]:
            badges.append('<span style="color:#10b981">X ✓</span>')
        elif c["has_x_post"]:
            badges.append('<span style="color:#f59e0b">X ⏳</span>')
        if c["linkedin_posted"]:
            badges.append('<span style="color:#10b981">LI ✓</span>')
        elif c["has_linkedin"]:
            badges.append('<span style="color:#f59e0b">LI ⏳</span>')
        if c["website_live"]:
            badges.append('<span style="color:#10b981">Web ✓</span>')

        badge_str = "  ".join(badges) if badges else '<span style="color:#6b7280">No social</span>'
        title = (c["title"] or c["content_ref"])[:60]
        date_str = c["publish_date"] or ""

        with st.expander(f"**{c['content_ref']}** — {title}"):
            # Image + metadata row
            img_path = find_image(c["source_file"])
            if img_path:
                img_col, meta_col = st.columns([1, 3])
                with img_col:
                    st.image(img_path, width="stretch")
                with meta_col:
                    st.markdown(f"**Date:** {date_str}  |  **Type:** {c['content_type']}  |  {badge_str}",
                                unsafe_allow_html=True)
            else:
                st.markdown(f"**Date:** {date_str}  |  **Type:** {c['content_type']}  |  {badge_str}",
                            unsafe_allow_html=True)

            # Read the actual content
            content = read_content_file(c["source_file"])
            if content:
                # Show sections as sub-tabs
                sub_tabs = ["Newsletter/INTEL"]
                sections = {}

                li_section = extract_section(content, "LINKEDIN POST")
                if li_section:
                    sub_tabs.append("LinkedIn Post")
                    sections["LinkedIn Post"] = li_section

                x_section = extract_section(content, "X POST")
                if x_section:
                    sub_tabs.append("X Post")
                    sections["X Post"] = x_section

                src_section = extract_section(content, "SOURCE DATA")
                if src_section:
                    sub_tabs.append("Source Data")
                    sections["Source Data"] = src_section

                if len(sub_tabs) > 1:
                    inner_tabs = st.tabs(sub_tabs)
                    with inner_tabs[0]:
                        # Main content — strip LinkedIn/X/Source sections
                        main = content
                        for sec_name in ["LINKEDIN POST", "X POST", "SOURCE DATA"]:
                            main = re.sub(
                                rf"\n## {sec_name}.*?(?=\n## |\Z)", "", main, flags=re.DOTALL
                            )
                        # Also strip trailing ---
                        main = re.sub(r"\n---\s*$", "", main)
                        st.markdown(main)

                    for i, sec_name in enumerate(sub_tabs[1:], 1):
                        with inner_tabs[i]:
                            sec_content = sections[sec_name]
                            # LinkedIn might be in a code block
                            sec_content = re.sub(r"^```\n?|```$", "", sec_content.strip())
                            st.text_area(
                                f"Copy {sec_name}",
                                sec_content,
                                height=300,
                                key=f"ta_{c['content_ref']}_{sec_name}"
                            )
                            st.caption(f"{len(sec_content)} characters")
                else:
                    st.markdown(content)


# ============================================================
# TAB 3: SOCIAL
# ============================================================
with tab_social:

    social_section = st.radio(
        "Section",
        ["My Posts", "Scheduler", "Priorities", "Influencer Feed", "Trending", "Cost"],
        horizontal=True, key="social_section"
    )

    days_filter = st.slider("Days", 1, 30, 7, key="social_days")

    # --- MY POSTS ---
    if social_section == "My Posts":
        platform_filter = st.radio("Platform", ["All", "X", "LinkedIn"], horizontal=True, key="mp_plat")

        # X stats
        post_stats = conn.execute("""
            SELECT COUNT(*) as total,
                   SUM(likes) as likes, SUM(retweets) as retweets,
                   SUM(impressions) as impressions,
                   SUM(CASE WHEN is_reply=1 THEN 1 ELSE 0 END) as replies_out,
                   SUM(CASE WHEN is_quote=1 THEN 1 ELSE 0 END) as quotes_out
            FROM posts WHERE posted_at >= datetime('now', ?)
        """, (f"-{days_filter} days",)).fetchone()

        # LinkedIn stats
        li_stats = conn.execute("""
            SELECT COUNT(*) as total, SUM(linkedin_posted) as posted
            FROM content_status WHERE has_linkedin=1
        """).fetchone()

        if platform_filter in ("All", "X"):
            st.subheader("X Posts")
            c1, c2, c3, c4, c5 = st.columns(5)
            c1.metric("X Posts", post_stats["total"])
            c2.metric("Likes", post_stats["likes"] or 0)
            c3.metric("Retweets", post_stats["retweets"] or 0)
            c4.metric("Impressions", f"{(post_stats['impressions'] or 0):,}")
            c5.metric("Replies Out", post_stats["replies_out"] or 0)

            sort_by = st.selectbox("Sort", ["Date", "Likes", "Impressions", "Retweets"], key="p_sort")
            sort_map = {"Date": "posted_at DESC", "Likes": "likes DESC",
                        "Impressions": "impressions DESC", "Retweets": "retweets DESC"}

            posts = conn.execute(f"""
                SELECT tweet_id, posted_at, post_type, content_ref, full_text,
                       is_reply, reply_to_username, is_quote,
                       likes, retweets, replies, quotes, bookmarks, impressions
                FROM posts WHERE posted_at >= datetime('now', ?)
                ORDER BY {sort_map[sort_by]}
            """, (f"-{days_filter} days",)).fetchall()

            for p in posts:
                label = p["content_ref"] or p["post_type"]
                if p["is_reply"] and p["reply_to_username"]:
                    label += f" → @{p['reply_to_username']}"
                imp = f"👁 {p['impressions']:,}" if p["impressions"] else ""

                with st.expander(f"**{label}** — {p['posted_at'][:10]}  |  ♥ {p['likes']}  ↻ {p['retweets']}  {imp}"):
                    st.write(p["full_text"] or "")
                    tid = p["tweet_id"]
                    if not tid.startswith("article-"):
                        st.caption(f"[Open on X](https://x.com/stikman28/status/{tid})")
                    else:
                        st.caption("Published as X Article")
                    st.caption(f"💬 {p['replies']}  🔁 {p['quotes']}  🔖 {p['bookmarks']}")

        if platform_filter in ("All", "LinkedIn"):
            st.subheader("LinkedIn")
            c1, c2, c3 = st.columns(3)
            c1.metric("LI Content Ready", li_stats["total"] or 0)
            c2.metric("LI Posted", li_stats["posted"] or 0)
            pending_li = (li_stats["total"] or 0) - (li_stats["posted"] or 0)
            c3.metric("LI Pending", pending_li)

            li_content = conn.execute("""
                SELECT content_ref, title, source_file, linkedin_posted, has_linkedin
                FROM content_status WHERE has_linkedin=1
                ORDER BY content_ref DESC
            """).fetchall()

            for lc in li_content:
                status = "Posted" if lc["linkedin_posted"] else "Pending"
                badge = '<span style="color:#10b981">Posted</span>' if lc["linkedin_posted"] else '<span style="color:#f59e0b">Pending</span>'
                with st.expander(f"**{lc['content_ref']}** — {lc['title'] or ''} | {status}"):
                    st.markdown(badge, unsafe_allow_html=True)
                    content = read_content_file(lc["source_file"])
                    if content:
                        li_section = extract_section(content, "LINKEDIN POST")
                        if not li_section:
                            # Try # LINKEDIN POST (h1)
                            m = re.search(r"# LINKEDIN POST\s*\n+```\n?(.*?)```", content, re.DOTALL)
                            if m:
                                li_section = m.group(1).strip()
                        if li_section:
                            li_section = re.sub(r"^```\n?|```$", "", li_section.strip())
                            st.text_area("Copy for LinkedIn", li_section, height=200,
                                         key=f"li_{lc['content_ref']}")
                            st.caption(f"{len(li_section)} characters")

    # --- SCHEDULER ---
    elif social_section == "Scheduler":
        st.subheader("Post Scheduler")

        # Show scheduled posts
        scheduled = conn.execute("""
            SELECT id, platform, content_ref, post_text, scheduled_for, status, pid
            FROM scheduled_posts ORDER BY scheduled_for DESC LIMIT 20
        """).fetchall()

        # Active/pending
        pending_sched = [s for s in scheduled if s["status"] == "pending"]
        completed_sched = [s for s in scheduled if s["status"] == "completed"]

        if pending_sched:
            st.markdown(f"**Upcoming** ({len(pending_sched)})")
            for s in pending_sched:
                platform_icon = "X" if s["platform"] == "x" else "LI"
                ref = s["content_ref"] or (s["post_text"] or "")[:40]
                st.markdown(
                    f"- **[{platform_icon}]** {ref} — "
                    f"Scheduled: {s['scheduled_for']} | PID: {s['pid'] or 'N/A'}"
                )
        else:
            st.info("No scheduled posts.")

        if completed_sched:
            with st.expander(f"Completed ({len(completed_sched)})"):
                for s in completed_sched:
                    platform_icon = "X" if s["platform"] == "x" else "LI"
                    ref = s["content_ref"] or (s["post_text"] or "")[:40]
                    st.markdown(f"- **[{platform_icon}]** {ref} — {s['scheduled_for']}")

        st.divider()

        # Schedule new post
        st.markdown("**Schedule a Post**")
        col1, col2 = st.columns(2)
        with col1:
            sched_platform = st.selectbox("Platform", ["linkedin", "x"], key="sched_plat")
        with col2:
            sched_delay = st.number_input("Delay (minutes)", min_value=1, value=60, step=15, key="sched_delay")

        # Content source
        sched_source = st.radio("Source", ["From content file", "Ad-hoc text"], horizontal=True, key="sched_src")

        if sched_source == "From content file":
            all_files = conn.execute(
                "SELECT content_ref, source_file, title FROM content_status ORDER BY content_ref DESC"
            ).fetchall()
            file_options = {f"{c['content_ref']} — {c['title'] or ''}": c["source_file"] for c in all_files}
            selected = st.selectbox("Content", list(file_options.keys()), key="sched_file")
            sched_file = file_options.get(selected, "")
            sched_text = None
        else:
            sched_file = None
            sched_text = st.text_area("Post text", height=200, key="sched_text")

        if st.button("Schedule Post", key="sched_btn"):
            from datetime import datetime, timedelta
            import subprocess as sp

            target_time = datetime.now() + timedelta(minutes=sched_delay)
            content_ref = selected.split(" — ")[0] if sched_source == "From content file" else None

            # Save to DB
            conn.execute("""
                INSERT INTO scheduled_posts (platform, content_ref, source_file, post_text,
                                             scheduled_for, status, created_at)
                VALUES (?, ?, ?, ?, ?, 'pending', datetime('now'))
            """, (sched_platform, content_ref, sched_file, sched_text,
                  target_time.strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()

            # Launch background process
            scripts_dir = os.path.dirname(os.path.abspath(__file__))
            python = os.path.join(os.path.dirname(scripts_dir), "..", "AIQToolkit", ".venv", "bin", "python3")
            if not os.path.exists(python):
                python = "python3"

            if sched_file:
                if sched_platform == "linkedin":
                    cmd = f"sleep {sched_delay * 60} && {python} {scripts_dir}/post_to_linkedin.py {sched_file} --no-comment"
                else:
                    cmd = f"sleep {sched_delay * 60} && {python} {scripts_dir}/post_to_x.py {sched_file}"

                result = sp.Popen(cmd, shell=True, cwd=os.path.join(scripts_dir, ".."),
                                  stdout=open(f"/tmp/sched_{sched_platform}_{sched_delay}.log", "w"),
                                  stderr=sp.STDOUT)
                # Update PID
                conn.execute("UPDATE scheduled_posts SET pid=? WHERE id=(SELECT MAX(id) FROM scheduled_posts)",
                             (result.pid,))
                conn.commit()

            st.success(f"Scheduled! {sched_platform.upper()} post at {target_time:%I:%M %p} ({sched_delay} min)")
            st.rerun()

    # --- PRIORITIES ---
    elif social_section == "Priorities":
        st.subheader("Daily Priorities")
        st.caption("Where to spend your 20 minutes on X today")

        # 1. Pending
        pending = conn.execute(
            "SELECT content_ref, title FROM content_status WHERE has_x_post=1 AND x_posted=0"
        ).fetchall()
        if pending:
            st.markdown(f"**1. Publish** ({len(pending)} ready)")
            for p in pending:
                st.markdown(f"- **{p['content_ref']}**: {p['title'] or ''}")
        else:
            st.success("All X content published")

        # 2. Engage
        st.markdown("**2. Engage** — Top posts to reply to")
        engage = conn.execute("""
            SELECT tweet_id, author_username, full_text, likes, retweets,
                   (likes + retweets*3 + replies*2) AS score
            FROM feed_posts
            WHERE posted_at >= datetime('now', '-3 days')
              AND is_retweet=0 AND flagged=0 AND engaged=0 AND likes >= 20
            ORDER BY score DESC LIMIT 5
        """).fetchall()

        if engage:
            for e in engage:
                preview = (e["full_text"] or "")[:100].replace("\n", " ")
                url = f"https://x.com/{e['author_username']}/status/{e['tweet_id']}"
                col1, col2 = st.columns([5, 1])
                with col1:
                    st.markdown(f"**@{e['author_username']}** — {preview}")
                    st.caption(f"[Open on X]({url})")
                with col2:
                    st.metric("Score", e["score"], label_visibility="collapsed")
        else:
            st.info("No engagement opportunities. Run `feed` to refresh.")

        # 3. Flagged
        flagged = conn.execute("""
            SELECT tweet_id, author_username, flag_reason, full_text
            FROM feed_posts WHERE flagged=1 AND engaged=0 LIMIT 5
        """).fetchall()
        if flagged:
            st.markdown(f"**3. Flagged** ({len(flagged)} awaiting)")
            for f in flagged:
                preview = (f["full_text"] or "")[:80].replace("\n", " ")
                reason = f" — *{f['flag_reason']}*" if f["flag_reason"] else ""
                url = f"https://x.com/{f['author_username']}/status/{f['tweet_id']}"
                st.markdown(f"- **@{f['author_username']}**{reason}: {preview} [Open]({url})")

        # 4. Time split
        st.markdown("**Suggested Time Split (20 min)**")
        st.markdown("""
- **3 min** — Publish pending content
- **7 min** — Reply to 2 trending posts with substance
- **5 min** — Quote-tweet one post with your take
- **5 min** — Browse feed for new opportunities
""")

    # --- INFLUENCER FEED ---
    elif social_section == "Influencer Feed":
        st.subheader("Influencer Feed")

        col1, col2 = st.columns(2)
        categories = conn.execute(
            "SELECT DISTINCT category FROM influencers WHERE active=1"
        ).fetchall()
        with col1:
            cat = st.selectbox("Category", ["All"] + [c["category"] for c in categories], key="f_cat")
        with col2:
            influencers = conn.execute(
                "SELECT username FROM influencers WHERE active=1 ORDER BY username"
            ).fetchall()
            inf = st.selectbox("Account", ["All"] + [f"@{i['username']}" for i in influencers], key="f_inf")

        where_parts = ["posted_at >= datetime('now', ?)", "is_retweet=0"]
        params = [f"-{days_filter} days"]

        if cat != "All":
            where_parts.append("author_username IN (SELECT username FROM influencers WHERE category=?)")
            params.append(cat)
        if inf != "All":
            where_parts.append("author_username=?")
            params.append(inf.lstrip("@"))

        feed = conn.execute(f"""
            SELECT tweet_id, author_username, posted_at, full_text,
                   likes, retweets, replies, flagged, engaged
            FROM feed_posts
            WHERE {' AND '.join(where_parts)}
            ORDER BY posted_at DESC LIMIT 50
        """, params).fetchall()

        st.caption(f"{len(feed)} posts")

        for fp in feed:
            status = ""
            if fp["engaged"]:
                status = " ✅"
            elif fp["flagged"]:
                status = " 🚩"

            with st.expander(
                f"**@{fp['author_username']}**{status} — {fp['posted_at'][:10]}  |  "
                f"♥ {fp['likes']}  ↻ {fp['retweets']}  💬 {fp['replies']}"
            ):
                st.write(fp["full_text"] or "")
                st.caption(f"[Open on X](https://x.com/{fp['author_username']}/status/{fp['tweet_id']})")

    # --- TRENDING ---
    elif social_section == "Trending":
        st.subheader("Trending Posts")

        col1, col2 = st.columns(2)
        min_likes = col1.number_input("Min likes", value=20, step=10, key="t_likes")
        min_rts = col2.number_input("Min retweets", value=5, step=5, key="t_rts")

        trending = conn.execute("""
            SELECT tweet_id, author_username, posted_at, full_text,
                   likes, retweets, replies, quotes,
                   (likes + retweets*3 + replies*2 + quotes*5) AS score
            FROM feed_posts
            WHERE posted_at >= datetime('now', ?)
              AND (likes >= ? OR retweets >= ?) AND is_retweet=0
            ORDER BY score DESC LIMIT 30
        """, (f"-{days_filter} days", min_likes, min_rts)).fetchall()

        if not trending:
            st.info("No trending posts. Try lowering thresholds or run `feed`.")
        else:
            for t in trending:
                url = f"https://x.com/{t['author_username']}/status/{t['tweet_id']}"
                with st.expander(
                    f"Score **{t['score']}** — @{t['author_username']} ({t['posted_at'][:10]})  |  "
                    f"♥ {t['likes']}  ↻ {t['retweets']}  💬 {t['replies']}"
                ):
                    st.write(t["full_text"] or "")
                    st.caption(f"[Open on X]({url})")
                    st.caption(
                        f"♥{t['likes']} + ↻{t['retweets']}×3 + "
                        f"💬{t['replies']}×2 + 🔁{t['quotes']}×5 = {t['score']}"
                    )

    # --- COST ---
    elif social_section == "Cost":
        st.subheader("X API Credit Usage")

        costs = conn.execute("""
            SELECT fetch_type, COUNT(*) as calls,
                   SUM(posts_fetched) as posts, SUM(credits_used) as cost
            FROM fetch_log
            WHERE fetched_at >= datetime('now', ?)
            GROUP BY fetch_type ORDER BY cost DESC
        """, (f"-{days_filter} days",)).fetchall()

        total = conn.execute("""
            SELECT SUM(credits_used) as total FROM fetch_log
            WHERE fetched_at >= datetime('now', ?)
        """, (f"-{days_filter} days",)).fetchone()

        if costs:
            total_cost = total["total"] or 0
            c1, c2, c3 = st.columns(3)
            c1.metric("Spent", f"\\${total_cost:.2f}")
            c2.metric("Remaining (est.)", f"\\${25.0 - total_cost:.2f}")
            c3.metric("API Calls", sum(c["calls"] for c in costs))

            st.divider()
            for c in costs:
                st.markdown(
                    f"**{c['fetch_type']}** — {c['calls']} calls, "
                    f"{c['posts']} posts, \\${c['cost']:.2f}"
                )

            if total_cost > 0:
                daily = total_cost / max(days_filter, 1)
                st.caption(f"Daily avg: \\${daily:.3f} | Monthly projection: \\${daily * 30:.2f}")
        else:
            st.info("No API usage yet.")


conn.close()
