# FIR Risk Intelligence — Content Workflow

> **This repo**: Source content for INTEL posts, newsletters, methodology
> **Website repo**: `/Users/stikman/Projects/ai-assistant/fir-risk-website` (Hugo site)
> **Live site**: https://firriskadvisory.com

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
| **INTEL** | INTEL-2 (Human-in-the-Loop AI Security) | 2026-02-04 |
| **Tuesday** | E77 | 2026-02-03 |

---

## INTEL Publishing Workflow

### 1. Research in FIR Risk Platform
- Use AGENT to explore insights from KB (MITRE, NIST, CISA, etc.)
- Ask follow-up questions to develop the angle

### 2. Fact-Check Sources
- Verify stats and claims with AGENT before publishing
- If source is unclear, either find authoritative source or remove the claim
- Lead with principles over unverified numbers

### 3. Draft INTEL
Use template in `/intel/TEMPLATE.md`. Key sections:
- **The INTEL** — Core insight with specifics
- **Why It Matters** — Business impact
- **What To Do** — 1-2 actionable recommendations (keep it tight)
- **MITRE ATT&CK** — Relevant techniques (if applicable)
- **LINKEDIN POST** — Ready-to-publish version
- **SOURCE DATA** — Platform query and KB sources

### 4. Create Image
- Save to `/intel/images/intel-N-slug.png`
- Also copy to website: `fir-risk-website/static/images/intel/`

### 5. Publish to Both Repos

**This repo (fir-risk-intelligence):**
```bash
# Full version with LinkedIn post + source data
git add intel/YYYY-MM-DD-slug.md intel/images/intel-N-slug.png
git commit -m "Add INTEL-N: Title"
git push
```

**Website repo (fir-risk-website):**
```bash
cd /Users/stikman/Projects/ai-assistant/fir-risk-website

# Hugo version (no LinkedIn/source sections, has front matter)
# File: content/intel/intel-N-slug.md
# Image: static/images/intel/intel-N-slug.png

# Update index
# Edit: content/intel/_index.md (add new INTEL to list)

git add content/intel/intel-N-slug.md content/intel/_index.md static/images/intel/
git commit -m "Add INTEL-N: Title"
git push
# Cloudflare Pages auto-deploys
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
tags: ["Tag1", "Tag2"]
---
```

---

## Key URLs

| Resource | URL |
|----------|-----|
| **Live INTEL** | https://firriskadvisory.com/intel/ |
| **This repo** | https://github.com/stikman28/fir-risk-intelligence |
| **Website repo** | https://github.com/stikman28/fir-risk-website |
| **Cloudflare Pages** | Check dashboard for deploy status |

---

## LinkedIn Posting

After publishing, copy the LINKEDIN POST section from the intelligence repo and post to LinkedIn. Add relevant hashtags:

Common tags: `#CyberSecurity` `#ThreatIntelligence` `#CISO` `#RiskManagement` `#NIST` `#AI`
