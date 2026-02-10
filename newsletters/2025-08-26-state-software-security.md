# FIR Risk Tuesday E68 - State of Software Security 2025

**Publish Date:** August 26, 2025
**Source:** [Veracode — 2025 State of Software Security](https://www.veracode.com/resources/analyst-reports)
**Analysis:** FIR Risk Advisory

---

## NEWSLETTER DRAFT

# FIR Risk E68 - Your Code Is Aging Faster Than You're Fixing It

![FIR Risk E68 - State of Software Security](images/E68-state-software-security.png)

By FIR Risk Advisory | Cybersecurity Fraud Intelligence

## Weekly Risk Intelligence Brief

**Source:** [Veracode — 2025 State of Software Security: A New View of Maturity](https://www.veracode.com/resources/analyst-reports) (15th annual edition)

### The 30-Second Brief

Veracode's 15th annual report delivers a data-driven reality check on application security. 80% of applications contain security flaws. Median remediation time has ballooned to 252 days — up from 171. And 74% of organizations carry security debt (flaws unresolved for over a year).

But here's the actionable insight: only about 8% of flaws are both severe AND easily exploitable. That's your fastest risk-reduction target. Focus there first.

---

## The Numbers That Matter

### The Flaw Landscape

- **80%** of applications contain security flaws
- **56%** have high or critical severity issues
- **~8%** are both severe and easily exploitable — the intersection that actually drives breach probability

That last number is the one your team should obsess over. Not all flaws are created equal. The 8% that combine severity with exploitability are where attackers live.

> **INTEL [VULNERABILITY]:** 80% of apps have flaws, but only ~8% combine high severity with exploitability. Prioritize remediation at this intersection — it's the fastest path to material risk reduction. Everything else is noise until this is handled.

---

### The Remediation Crisis

Median flaw remediation now takes **252 days** — up from 171. That's not progress. That's regression.

- **28%** of flaws persist unresolved beyond two years
- **9%** persist beyond five years
- Teams with structured developer training achieve **7.5-month improvements** in median remediation time

The detection-remediation gap is widening. Organizations are finding more flaws (181% increase in detected high-severity flaws since 2020) but fixing them slower.

> **INTEL [TREND]:** Remediation velocity is declining even as detection improves. Organizations should establish fix-speed and capacity targets — not just discovery metrics. If you're measuring how many flaws you find but not how fast you fix them, you're tracking the wrong thing.

---

### Security Debt Is Compounding

- **74%** of organizations carry security debt (flaws unresolved >1 year)
- **50%** carry critical security debt concentrated in legacy and larger applications
- Debt compounds — the longer flaws persist, the harder and more expensive they become to fix

> **INTEL [SECTOR ALERT]:** Half of all organizations carry critical security debt in their largest, most important applications. These are the crown jewels — and they're accumulating unpatched vulnerabilities. Audit your legacy portfolio and establish retirement or refactoring strategies.

---

### The Open-Source Problem

This is where the risk concentrates:

- Only **11%** of overall security debt exists in third-party code
- But **70% of critical debt** resides there
- Third-party flaw remediation averages **12 months** versus 8 months for internal code

You control your own code. You don't control your dependencies.

> **INTEL [GLOBAL RECOMMENDATION]:** 70% of critical security debt lives in open-source dependencies — code you didn't write and can't directly fix. Implement Software Bill of Materials (SBOM) tracking, monitor transitive dependencies, and establish vendor remediation SLAs. The supply chain is your critical path.

---

## Board Dashboard KPIs

Veracode's maturity framework gives you concrete targets to track:

| Metric | Target | Stretch Goal |
|--------|--------|-------------|
| Fix Speed (median half-life) | ≤90 days overall | 5 weeks for high-risk |
| Fix Capacity | >10% of open flaws/month | Per application |
| Flaw Prevalence | <43% of apps with unresolved flaws | ≤20% high-severity |
| Debt Prevalence | <17% of apps carrying debt | Zero critical debt in crown jewels |
| Open-Source Critical Debt | <15% of total | Half-life ≤12 months |

---

## Five Questions for Your Next Board Meeting

1. Are remediation efforts targeting exploitability AND severity simultaneously — or just closing tickets?
2. What is the organizational trend in fix half-life by product line?
3. What percentage of critical debt originates from open-source dependencies?
4. Which legacy applications are accumulating debt, and what's the retirement strategy?
5. Does the organization employ hands-on developer training to accelerate remediation?

---

## The Bottom Line

Modern application security maturity isn't about finding flaws. It's about fixing them — fast, in the right order, with measurable velocity.

Leaders maintain remediation capacity exceeding 10% monthly, contain debt to less than 17% of applications, restrict open-source critical debt below 15%, and concentrate resources on the small subset of flaws that actually drive breach probability.

Your code is aging faster than you're fixing it. The math doesn't lie.

---

Stay tuned for more in future FIR Risk Newsletters!

Find all editions on [FIR Risk Tuesday](https://firriskadvisory.com/tuesday/) | [GitHub](https://github.com/stikman28/fir-risk-intelligence)

---

## LINKEDIN POST

```
FIR Risk Tuesday E68 is out.

Veracode's 15th annual State of Software Security report.
The remediation crisis is real:

→ 80% of apps contain security flaws
→ Median fix time: 252 days (up from 171)
→ 74% of orgs carry security debt (flaws unresolved >1 year)
→ Only 8% of flaws are both severe AND exploitable — that's your target
→ 70% of critical debt lives in open-source dependencies

Your code is aging faster than you're fixing it.

Full analysis + board KPIs: [link]

#AppSec #SoftwareSecurity #CISO #SecurityDebt #OpenSource
```

---

## NOTES

- Source: Veracode — 2025 State of Software Security (15th annual edition)
- Content pulled from LinkedIn newsletter via WebFetch for fir-risk-intelligence archive
- Original published August 26, 2025
- Reformatted to match 2026 newsletter template with INTEL callouts added
- Hero image downloaded from LinkedIn CDN
- Strong board-level framing with KPI table and executive questions
