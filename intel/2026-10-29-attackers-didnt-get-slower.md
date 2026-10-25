# FIR Risk INTEL-43 — Attackers Didn't Get Slower. We Did.

**Type:** `TREND`
**Date:** October 29, 2026
**Platform Source:** FIR Risk E94 — MDDR 2026: A Shift in the Physics of Cyber Risk (Microsoft Digital Defense Report 2026)

---

## The INTEL

**Intruders are going unnoticed for longer, and it isn't because they're working more slowly. Comparing two years of its incident response engagements, Microsoft found "a statistically significant increase in dwell time," while "the overall length of threat actor activity remained broadly stable." Microsoft's reading: "organizations took longer to identify malicious activity following compromise."**

Dwell time is the gap between an intruder's first activity and its detection. If attackers were simply staying longer, both measures would rise together. Instead the attack lasted about as long, and the discovery came later. Microsoft adds that the increase was consistent "across multiple sectors," which points to "a broader operational trend" rather than a few bad cases. The sharpest rise was in industrials and manufacturing.

Microsoft shows the change in charts rather than putting a single number on it. Mandiant does give a number, from a different set of investigations: in M-Trends 2026, global median dwell time rose to 14 days from 11, the first increase since it began tracking in 2010. Two incident response teams, two datasets, same direction.

---

## Why It Matters

Most security budgets are weighted toward keeping attackers out. This year's data says the slippage is on the other side: noticing them once they're in. Every extra day undetected is another day to find data, move through systems and stage ransomware.

Microsoft lists dwell time among the six things leadership should see, alongside identity exposure, patch latency, agent permissions, critical dependencies and recovery readiness. Few board packs include it today.

---

## What To Do — One Key Action

**Add dwell time and time to contain to the leadership view each quarter, with the trend, and ask management what it would take to shorten them.**

---

## MITRE ATT&CK

- **TA0005 — Defense Evasion:** The techniques attackers use to stay unnoticed after they get in; dwell time measures how well they work against you.

---

## Learn More

- [Microsoft Digital Defense Report 2026: Decoding emergence (Microsoft, PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Digital-Defense-Report.pdf) — Primary source, "The threat landscape in 2026"
- [FIR Risk Tuesday E94 — MDDR 2026: A Shift in the Physics of Cyber Risk](/tuesday/e94-shift-in-the-physics-of-cyber-risk/) — Full analysis of the report
- [FIR Risk Tuesday E85 — M-Trends 2026](/tuesday/e85-responders-report/) — Mandiant's dwell-time data

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Attackers didn't get slower. We got slower at noticing them.

Microsoft's 2026 Digital Defense Report compared two years of its incident response cases. Dwell time (first intruder activity to detection) rose significantly. The length of the attacks stayed broadly the same.

Microsoft's conclusion: "organizations took longer to identify malicious activity following compromise." And the rise showed up across multiple sectors, so it's a trend, not a few bad cases.

Mandiant sees the same thing in different data: median dwell time rose to 14 days from 11, its first increase since 2010.

Most budgets go to keeping attackers out. This year's slippage is in finding them once they're in.

One action: put dwell time and time to contain on the leadership dashboard every quarter, with the trend, and ask what it would take to shorten them.

#CyberSecurity #CyberResilience #IncidentResponse #CISO #BoardGovernance #RiskManagement
```

## X POST

Attackers didn't get slower. We got slower at noticing them.

Microsoft compared two years of incident response cases: dwell time rose significantly while the length of the attacks stayed broadly the same. "Organizations took longer to identify malicious activity following compromise."

Mandiant agrees: median dwell time rose to 14 days from 11, the first increase since 2010.

One action: put dwell time and time to contain on the leadership dashboard, with the trend.

Full INTEL → FIR Risk INTEL-43

#CyberSecurity #CyberResilience

---

## SOURCE DATA

**Editorial Frame:**
INTEL-43 expands E94 §2. The insight is the pairing: dwell time up, activity length flat, so the change is on the defender's side. One action: make dwell time a leadership metric (Microsoft priority #1 lists it).

**Primary Source:**
- Microsoft Digital Defense Report 2026, "Decoding emergence" (reporting period July 2025 – June 2026; YoY vs July 2024 – June 2025). Verified against the PDF on Oct 25, 2026.

**Fact-Check Notes:**
- p35 CONFIRMED: definitions: dwell time = "period between the earliest evidence of threat actor activity and its detection"; length of activity = "period between the earliest and latest observed activity."
- p35 CONFIRMED verbatim: "Comparing year over year DART engagement data shows a statistically significant increase in dwell time, while the overall length of threat actor activity remained broadly stable. This suggests organizations took longer to identify malicious activity following compromise, with the consistency of the increase across multiple sectors indicating a broader operational trend."
- p35 CONFIRMED: "most pronounced increase in dwell time was observed in industrials and manufacturing sector."
- p35: box plots only; NO median stated. Do not attribute a number to Microsoft.
- p7 CONFIRMED: priority #1 "Report identity exposure, patch latency, agent permissions, critical dependencies, dwell time, and recovery readiness."
- E85 (verified edition): M-Trends 2026 global median dwell time 14 days, up from 11, first increase since tracking began in 2010.

**FIR Risk Editorial Position:**
- "Few board packs include it today" is FIR's observation, not a Microsoft statistic.
- Board direction (what leadership sees), not an operational mandate.
