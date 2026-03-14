"""SQLite persistence for X platform tool."""

import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "x_platform.db")


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db():
    conn = get_conn()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS posts (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            tweet_id        TEXT    NOT NULL UNIQUE,
            posted_at       TEXT    NOT NULL,
            post_type       TEXT    NOT NULL DEFAULT 'organic',
            content_ref     TEXT,
            source_file     TEXT,
            text_preview    TEXT,
            full_text       TEXT,
            has_image       INTEGER NOT NULL DEFAULT 0,
            is_reply        INTEGER NOT NULL DEFAULT 0,
            reply_to_tweet_id TEXT,
            reply_to_username TEXT,
            is_quote        INTEGER NOT NULL DEFAULT 0,
            quote_of_tweet_id TEXT,
            likes           INTEGER NOT NULL DEFAULT 0,
            retweets        INTEGER NOT NULL DEFAULT 0,
            replies         INTEGER NOT NULL DEFAULT 0,
            quotes          INTEGER NOT NULL DEFAULT 0,
            bookmarks       INTEGER NOT NULL DEFAULT 0,
            impressions     INTEGER NOT NULL DEFAULT 0,
            metrics_updated_at TEXT,
            created_at      TEXT    DEFAULT (datetime('now')),
            updated_at      TEXT    DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS content_status (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            content_type    TEXT    NOT NULL,
            content_ref     TEXT    NOT NULL,
            source_file     TEXT    NOT NULL,
            title           TEXT,
            publish_date    TEXT,
            has_x_post      INTEGER NOT NULL DEFAULT 0,
            x_posted        INTEGER NOT NULL DEFAULT 0,
            x_format        TEXT,
            tweet_id        TEXT,
            has_linkedin     INTEGER NOT NULL DEFAULT 0,
            linkedin_posted  INTEGER NOT NULL DEFAULT 0,
            website_live     INTEGER NOT NULL DEFAULT 0,
            created_at      TEXT    DEFAULT (datetime('now')),
            UNIQUE(content_type, content_ref)
        );

        CREATE TABLE IF NOT EXISTS influencers (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            username        TEXT    NOT NULL UNIQUE,
            user_id         TEXT,
            display_name    TEXT,
            category        TEXT    NOT NULL DEFAULT 'cybersecurity',
            priority        TEXT    NOT NULL DEFAULT 'medium',
            active          INTEGER NOT NULL DEFAULT 1,
            notes           TEXT,
            created_at      TEXT    DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS feed_posts (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            tweet_id        TEXT    NOT NULL UNIQUE,
            author_username TEXT    NOT NULL,
            author_user_id  TEXT,
            posted_at       TEXT    NOT NULL,
            text_preview    TEXT,
            full_text       TEXT,
            likes           INTEGER NOT NULL DEFAULT 0,
            retweets        INTEGER NOT NULL DEFAULT 0,
            replies         INTEGER NOT NULL DEFAULT 0,
            quotes          INTEGER NOT NULL DEFAULT 0,
            is_retweet      INTEGER NOT NULL DEFAULT 0,
            is_reply        INTEGER NOT NULL DEFAULT 0,
            is_quote        INTEGER NOT NULL DEFAULT 0,
            flagged         INTEGER NOT NULL DEFAULT 0,
            flag_reason     TEXT,
            engaged         INTEGER NOT NULL DEFAULT 0,
            engage_tweet_id TEXT,
            fetched_at      TEXT    DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS fetch_log (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            fetch_type      TEXT    NOT NULL,
            target          TEXT,
            posts_fetched   INTEGER NOT NULL DEFAULT 0,
            credits_used    REAL    NOT NULL DEFAULT 0,
            fetched_at      TEXT    DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS scheduled_posts (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            platform        TEXT    NOT NULL,
            content_ref     TEXT,
            source_file     TEXT,
            post_text       TEXT,
            image_path      TEXT,
            scheduled_for   TEXT    NOT NULL,
            status          TEXT    NOT NULL DEFAULT 'pending',
            pid             INTEGER,
            result          TEXT,
            created_at      TEXT    DEFAULT (datetime('now'))
        );

        CREATE INDEX IF NOT EXISTS idx_posts_tweet_id ON posts(tweet_id);
        CREATE INDEX IF NOT EXISTS idx_posts_post_type ON posts(post_type);
        CREATE INDEX IF NOT EXISTS idx_posts_posted_at ON posts(posted_at);
        CREATE INDEX IF NOT EXISTS idx_feed_posts_author ON feed_posts(author_username);
        CREATE INDEX IF NOT EXISTS idx_feed_posts_posted_at ON feed_posts(posted_at);
        CREATE INDEX IF NOT EXISTS idx_scheduled_status ON scheduled_posts(status);
    """)
    conn.commit()
    conn.close()


def upsert_post(conn, tweet_id, posted_at, full_text, metrics, post_type="organic",
                content_ref=None, source_file=None,
                is_reply=0, reply_to_tweet_id=None, reply_to_username=None,
                is_quote=0, quote_of_tweet_id=None):
    preview = full_text[:280] if full_text else None
    conn.execute("""
        INSERT INTO posts (tweet_id, posted_at, post_type, content_ref, source_file,
                           text_preview, full_text,
                           is_reply, reply_to_tweet_id, reply_to_username,
                           is_quote, quote_of_tweet_id,
                           likes, retweets, replies, quotes,
                           bookmarks, impressions, metrics_updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
        ON CONFLICT(tweet_id) DO UPDATE SET
            likes=excluded.likes, retweets=excluded.retweets, replies=excluded.replies,
            quotes=excluded.quotes, bookmarks=excluded.bookmarks, impressions=excluded.impressions,
            metrics_updated_at=datetime('now'), updated_at=datetime('now')
    """, (tweet_id, posted_at, post_type, content_ref, source_file, preview, full_text,
          is_reply, reply_to_tweet_id, reply_to_username,
          is_quote, quote_of_tweet_id,
          metrics.get("like_count", 0), metrics.get("retweet_count", 0),
          metrics.get("reply_count", 0), metrics.get("quote_count", 0),
          metrics.get("bookmark_count", 0), metrics.get("impression_count", 0)))


def upsert_content_status(conn, content_type, content_ref, source_file,
                          title=None, publish_date=None, has_x_post=0, has_linkedin=0):
    conn.execute("""
        INSERT INTO content_status (content_type, content_ref, source_file, title,
                                    publish_date, has_x_post, has_linkedin)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(content_type, content_ref) DO UPDATE SET
            source_file=excluded.source_file, title=excluded.title,
            publish_date=excluded.publish_date, has_x_post=excluded.has_x_post,
            has_linkedin=excluded.has_linkedin
    """, (content_type, content_ref, source_file, title, publish_date, has_x_post, has_linkedin))


def upsert_feed_post(conn, tweet_id, author_username, author_user_id, posted_at, full_text, metrics,
                      is_retweet=0, is_reply=0, is_quote=0):
    preview = full_text[:280] if full_text else None
    conn.execute("""
        INSERT INTO feed_posts (tweet_id, author_username, author_user_id, posted_at,
                                text_preview, full_text, likes, retweets, replies, quotes,
                                is_retweet, is_reply, is_quote)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(tweet_id) DO UPDATE SET
            likes=excluded.likes, retweets=excluded.retweets,
            replies=excluded.replies, quotes=excluded.quotes
    """, (tweet_id, author_username, author_user_id, posted_at, preview, full_text,
          metrics.get("like_count", 0), metrics.get("retweet_count", 0),
          metrics.get("reply_count", 0), metrics.get("quote_count", 0),
          is_retweet, is_reply, is_quote))


def log_fetch(conn, fetch_type, target, posts_fetched, credits_used):
    conn.execute("""
        INSERT INTO fetch_log (fetch_type, target, posts_fetched, credits_used)
        VALUES (?, ?, ?, ?)
    """, (fetch_type, target, posts_fetched, credits_used))
