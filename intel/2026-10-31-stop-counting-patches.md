# FIR Risk INTEL-45 — Stop Counting Patches

**Type:** `TREND`
**Date:** October 31, 2026
**Platform Source:** FIR Risk E94 — MDDR 2026: A Shift in the Physics of Cyber Risk (Microsoft Digital Defense Report 2026)

---

## The INTEL

**Microsoft's 2026 Digital Defense Report tells leaders to change the scoreboard: "reporting metrics should shift from number of patches deployed to exposure reduced, detection coverage increased, and time-to-mitigate compressed."**

The reason is the clock. Microsoft says the median time from a flaw being discovered in the wild to a working exploit "has now collapsed to well below 24 hours," while enterprise remediation of critical external vulnerabilities "can take 30–60 days." Attackers often don't wait for disclosure at all: pre-disclosure windows of 30 days or more "are now routine." Against that, a count of patches deployed says little about whether the systems attackers actually target are still open.

Microsoft frames the shift as moving "from tool-centric vulnerability management to threat exposure management": knowing what you have exposed, ranking it by real risk and closing the gaps that matter first. Its first priority for organizations is to govern cyber risk at leadership level and report "identity exposure, patch latency, agent permissions, critical dependencies, dwell time, and recovery readiness."

---

## Why It Matters

What gets reported gets managed. A patch count can rise every month while one forgotten, internet-facing VPN stays exposed, and that VPN is where the attack comes from. Exposure reduced, detection coverage and time to mitigate measure the thing the board actually cares about: how open the organization is, and how fast it closes.

The board's job isn't to set patch deadlines. It's to ask for the measures that show whether the defense is keeping pace, and to fund what moves them.

---

## What To Do — One Key Action

**Ask management to replace patch counts in board reporting with three trend lines: exposure reduced (internet-facing and identity systems first), detection coverage, and time to mitigate.**

---

## MITRE ATT&CK

- **T1190 — Exploit Public-Facing Application:** The exposure these metrics are meant to track; Microsoft's incident response data shows it rising from 15% to 24% of initial access.

---

## Learn More

- [Microsoft Digital Defense Report 2026: Decoding emergence (Microsoft, PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Digital-Defense-Report.pdf) — Primary source, "Top 10 takeaways" and "Ten security priorities"
- [FIR Risk Tuesday E94 — MDDR 2026: A Shift in the Physics of Cyber Risk](/tuesday/e94-shift-in-the-physics-of-cyber-risk/) — Full analysis of the report
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — The flaws attackers are actively using

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Your patch count is going up. Is your exposure going down?

Microsoft's 2026 Digital Defense Report says it's time to change the scoreboard: "reporting metrics should shift from number of patches deployed to exposure reduced, detection coverage increased, and time-to-mitigate compressed."

The reason is the clock. Microsoft puts the median time from discovery to weaponization at "well below 24 hours." Enterprise remediation of critical external flaws "can take 30–60 days."

A patch count can rise every month while one forgotten, internet-facing VPN stays open, and that's where the attack comes from.

Boards don't set patch deadlines. They decide what gets measured and funded.

One action: ask management to replace patch counts in board reporting with three trend lines: exposure reduced, detection coverage, and time to mitigate.

#CyberSecurity #BoardGovernance #CyberRisk #VulnerabilityManagement #CISO #RiskManagement
```

## X POST

Your patch count is going up. Is your exposure going down?

Microsoft's 2026 Digital Defense Report: "reporting metrics should shift from number of patches deployed to exposure reduced, detection coverage increased, and time-to-mitigate compressed."

Why: weaponization now takes "well below 24 hours," while enterprise remediation "can take 30–60 days."

One action: replace patch counts in board reporting with exposure reduced, detection coverage and time to mitigate.

Full INTEL → FIR Risk INTEL-45

#CyberSecurity #BoardGovernance

---

## SOURCE DATA

**Editorial Frame:**
INTEL-45 turns E94's "Change what gets reported" action into a standalone board piece. Follows the board message rule: the board sets what is measured and funded, not patch speed. No 72-hour figure (technical guidance, kept out of board framing).

**Primary Source:**
- Microsoft Digital Defense Report 2026, "Decoding emergence" (reporting period July 2025 – June 2026). Verified against the PDF on Oct 25, 2026.

**Fact-Check Notes:**
- p8 CONFIRMED verbatim (takeaway 8): "Defenders must shift from tool-centric vulnerability management to threat exposure management… This means reporting metrics should shift from number of patches deployed to exposure reduced, detection coverage increased, and time-to-mitigate compressed."
- p7 CONFIRMED: priority #1 "Govern cyber risk at leadership level. Report identity exposure, patch latency, agent permissions, critical dependencies, dwell time, and recovery readiness."
- p14 CONFIRMED (E94 fact-check 10/15): "The median time from vulnerability discovery in the wild to weaponization has now collapsed to well below 24 hours."
- p48 CONFIRMED (E94 fact-check 10/15): enterprise remediation for critical external vulnerabilities "can take 30–60 days" (no citation in the report); "pre-disclosure windows of 30 days or more are now routine."
- p33 CONFIRMED (E94 fact-check 10/15): exploit public-facing application 15% → 24% of initial access, Microsoft Threat Intelligence IR findings.

**FIR Risk Editorial Position:**
- "One forgotten VPN" is an illustration, not a Microsoft statistic (the report's examples include SonicWall VPN and Cisco FMC exploitation, p48).
- Board direction on metrics and funding only, per the board message rule.
