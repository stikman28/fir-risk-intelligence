# GitHub Actions Social Poster — Setup

One-time setup to move social posting off the local Mac. After this, posts fire from GitHub every 15 min regardless of whether the Mac is on.

## What runs

`.github/workflows/social-poster.yml` runs every 15 minutes. It:

1. Reads every `scripts/*-queue.json` file.
2. For each item where `at` has passed and `posted_at` is not set, posts it to the target platform.
3. Writes `posted_at` and `post_id` back into the queue file.
4. Commits the queue file update with message `ops: social-poster state update [skip ci]`.

Items more than 36 hours past their scheduled time are skipped (defense against stale queues re-firing).

## Secrets to add

Go to: **Settings → Secrets and variables → Actions → New repository secret**.

Add all six of these. Values come from your local macOS Keychain (account `stikman28`):

| Secret name | Retrieve locally with |
|---|---|
| `X_PUBLISH_CONSUMER_KEY` | `security find-generic-password -a stikman28 -s X_PUBLISH_CONSUMER_KEY -w` |
| `X_PUBLISH_CONSUMER_SECRET` | `security find-generic-password -a stikman28 -s X_PUBLISH_CONSUMER_SECRET -w` |
| `X_PUBLISH_ACCESS_TOKEN` | `security find-generic-password -a stikman28 -s X_PUBLISH_ACCESS_TOKEN -w` |
| `X_PUBLISH_ACCESS_TOKEN_SECRET` | `security find-generic-password -a stikman28 -s X_PUBLISH_ACCESS_TOKEN_SECRET -w` |
| `LINKEDIN_ACCESS_TOKEN` | `security find-generic-password -a stikman28 -s LINKEDIN_ACCESS_TOKEN -w` |
| `LINKEDIN_PERSON_ID` | `security find-generic-password -a stikman28 -s LINKEDIN_PERSON_ID -w` |

`LINKEDIN_CLIENT_ID` / `LINKEDIN_CLIENT_SECRET` are not needed at posting time (only for token refresh).

## LinkedIn token rotation

LinkedIn access tokens expire ~59 days after issuance. When they do:

1. Locally: `$XPYTHON scripts/post_to_linkedin.py --setup` to mint a new one (writes to Keychain).
2. Copy the new token into the `LINKEDIN_ACCESS_TOKEN` GitHub secret.

## Queue file format

```json
[
    {
        "platform": "linkedin",
        "file": "intel/2026-04-23-slug.md",
        "at": "2026-04-23 07:00"
    },
    {
        "platform": "x",
        "file": "intel/2026-04-23-slug.md",
        "at": "2026-04-23 07:05"
    }
]
```

- `at` is **America/New_York** time (naive string, no timezone suffix).
- After a successful post, the runner adds `posted_at` (UTC ISO-8601) and `post_id`.
- On failure, it writes `error` with a timestamp — item will retry on the next run.

## Testing

### Local dry-run
```bash
$XPYTHON scripts/run_queue.py --dry-run
```

### Trigger the workflow manually
**Actions → Social Poster → Run workflow → dry_run: true** — verifies the workflow environment and secrets without posting.

## Monitoring

- **GitHub**: Actions tab shows every 15-min run, green or red.
- **Queue files**: `posted_at` / `post_id` fields show what's shipped; `error` fields show what's failing.
- **Platforms**: check `@stikman28` on X and the LinkedIn feed.

## Rollback

If something goes wrong, disable the workflow: **Actions → Social Poster → ⋯ → Disable workflow**. Revert to running `scripts/post_to_x.py` / `scripts/post_to_linkedin.py` manually.
