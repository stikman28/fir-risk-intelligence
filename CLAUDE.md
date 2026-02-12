# FIR Risk Intelligence — Content Workflow

> **This repo**: Source content for INTEL posts, newsletters, methodology
> **Website repo**: `/Users/stikman/Projects/ai-assistant/fir-risk-website` (Hugo site)
> **Live site**: https://fir-risk-website.pages.dev (Cloudflare Pages, auto-deploy from main)

---

## Content Types

| Type | Naming | Frequency | Location |
|------|--------|-----------|----------|
| **FIR Risk INTEL** | `YYYY-MM-DD-slug.md` | 2-3x/week | `/intel/` |
| **FIR Risk Tuesday** | `YYYY-MM-DD-slug.md` | Weekly | `/newsletters/` |

**INTEL Types:** `THREAT ALERT` · `VULNERABILITY` · `SECTOR ALERT` · `TECHNIQUE` · `REGULATORY` · `TREND` · `FILING INTEL`

---

## Current Status

| Content | Latest | Date |
|---------|--------|------|
| **INTEL** | INTEL-3 (LLM Infrastructure Targeting) | 2026-02-11 |
| **Tuesday** | E78 (Three Flags, One Target) | 2026-02-10 |

---

## INTEL Publishing Workflow

### 1. Select Topic from Latest Newsletter

Review the most recent FIR Risk Tuesday edition for INTEL callout blocks (marked with `> **INTEL [TYPE]:**`). Pick the angle that would be most compelling for busy executives — prioritize:
- Forward-looking trends over well-covered threats
- Specific numbers that grab attention (e.g., "91,000 sessions")
- Topics where FIR Risk Platform Agent can add depth

### 2. Research with FIR Risk Platform Agent

Ask 3-4 targeted follow-up questions to derive deeper intelligence:
- **Question 1**: Expand on the core INTEL — threat actor details, MITRE ATT&CK mappings, source research
- **Question 2**: Specific vulnerabilities, CVEs, technologies at risk
- **Question 3**: Attack chain analysis — what happens next after the initial finding
- **Question 4**: Defensive controls and actionable recommendations

Paste Agent responses back to Claude for drafting.

### 3. Fact-Check Sources

- Verify stats and claims with Agent before publishing
- If source is unclear, either find authoritative source or remove the claim
- Lead with principles over unverified numbers
- Note any Agent hallucinations in the NOTES section (correct against primary sources)

### 4. Draft INTEL

Use template in `/intel/TEMPLATE.md`. Keep it tight — executives scan in 60 seconds.

- **The INTEL** — 1-2 short paragraphs with the core insight. Specific numbers, CVEs, technique IDs.
- **Why It Matters** — 1 paragraph. Business impact. Who should care.
- **What To Do** — One primary action + 2 supporting recommendations. Not a laundry list.
- **MITRE ATT&CK** — 3-4 relevant techniques max (table format)
- **Learn More** — Source links + link to this repo
- **LINKEDIN POST** — Ready-to-publish (150-250 words, no tables, hook + insight + CTA)
- **SOURCE DATA** — Platform queries used and KB sources

### 5. Create Image

- Save to `/intel/images/intel-N-slug.png`

### 6. Publish to Both Repos

**This repo (fir-risk-intelligence) — full version:**
```bash
git add intel/YYYY-MM-DD-slug.md intel/images/intel-N-slug.png
git commit -m "content: Add INTEL-N — Title"
git push
```

**Website repo (fir-risk-website) — Hugo version:**

The website version differs from the intelligence repo version:
- **Has** Hugo front matter (title, description, date, type, intel_type, image, thumbnail, tags)
- **Has** content sections (The INTEL, Why It Matters, What To Do, MITRE ATT&CK, Learn More)
- **Does NOT have** LinkedIn post section or Source Data section
- **Does NOT have** inline `<img>` tag — Hinode renders the hero image from front matter `thumbnail` field

```bash
cd /Users/stikman/Projects/ai-assistant/fir-risk-website

# 1. Copy image to BOTH paths (Hinode dual-path requirement)
cp intel-N-slug.png static/images/intel/
cp intel-N-slug.png assets/images/intel/

# 2. Create Hugo post: content/intel/intel-N-slug.md
# 3. Commit and push (Cloudflare Pages auto-deploys from main)
git add content/intel/intel-N-slug.md static/images/intel/ assets/images/intel/
git commit -m "content: Add INTEL-N — Title"
git push
```

---

## Hugo Front Matter (Website)

```yaml
---
title: "INTEL-N: Title Here"
description: "One-line summary for SEO"
date: YYYY-MM-DD
type: "intel"
intel_type: "TREND"  # or THREAT ALERT, VULNERABILITY, etc.
image: "/images/intel/intel-N-slug.png"
thumbnail: "/images/intel/intel-N-slug.png"
tags: ["Tag1", "Tag2"]
---
```

**Important:**
- Both `image` and `thumbnail` fields are required — `thumbnail` drives the listing card on `/intel/` and og:image for social shares
- Do NOT include an `<img>` tag in the body — Hinode renders the image from front matter (adding `<img>` creates a duplicate)
- Images must exist in BOTH `static/images/intel/` and `assets/images/intel/` (Hinode dual-path requirement)

---

## Key URLs

| Resource | URL |
|----------|-----|
| **Live INTEL** | https://fir-risk-website.pages.dev/intel/ |
| **This repo** | https://github.com/stikman28/fir-risk-intelligence |
| **Website repo** | https://github.com/stikman28/fir-risk-website |
| **Cloudflare Pages** | Auto-deploys from main branch |

---

## LinkedIn Posting

After publishing, copy the LINKEDIN POST section from the intelligence repo and post to LinkedIn. Add relevant hashtags:

Common tags: `#CyberSecurity` `#ThreatIntelligence` `#CISO` `#RiskManagement` `#NIST` `#AI`

---

## Lessons Learned

- **Newsletter as INTEL source**: The weekly Tuesday edition is the best pipeline for INTEL topics — each edition contains 3-5 INTEL callout blocks ready to be expanded
- **Agent questions pattern**: 4 targeted questions (expand core INTEL, vulnerabilities, attack chain, defensive controls) consistently produce enough material for a tight INTEL post
- **Keep it short**: Executives scan in 60 seconds. One primary takeaway, not five. INTEL-3 was tightened from ~600 words to ~300 after review.
- **Images signal trust**: The `/intel/` listing page needs thumbnail images for all posts — posts without thumbnails look incomplete
- **No inline `<img>` with Hinode**: Front matter `thumbnail` handles both the listing card and the hero image on the post page. Adding `<img>` in the body creates a duplicate.
