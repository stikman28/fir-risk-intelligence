# FIR Risk INTEL-59 — Six Years at the Top

**Type:** `TREND`
**Date:** November 18, 2026
**Platform Source:** FIR SIGNALS 2026, Signal 01 "The window is gone. Expose less." (Mandiant M-Trends 2026; Verizon DBIR 2026; IBM X-Force Threat Intelligence Index 2026; Microsoft Digital Defense Report 2026)

---

## The INTEL

**Exploiting a flaw in something you expose to the internet has been the most common way into a company in Mandiant's investigations for six years running. This year, the other major datasets caught up. That is what makes it a signal, not a headline.**

What the sources say:

- **Mandiant (incident response):** "For the sixth year running, exploits represented the most frequently observed initial infection vector." 32% of investigations where the way in could be identified.
- **Verizon DBIR (breach data):** exploitation is now the #1 way in for the first time, at 31% of breaches, up from 20%. Credential abuse, the previous leader, fell to 13%.
- **IBM X-Force:** incidents caused by exploiting public-facing applications rose 44%, to 40% of cases.
- **Microsoft:** in its incident response work, exploiting public-facing applications rose from 15% to 24% of initial access.

Four different datasets, collected four different ways, pointing the same direction.

---

## Why It Matters

Vendor reports are full of spikes. A spike is a reason to look, not a reason to change strategy. SIGNALS kept a finding only if independent sources agree, it has lasted more than a year, and it changes a board decision. This one passes all three: the incident responders have seen it for six years, the breach data now agrees, and the decision it drives is clear.

**Our read:** treat exposure as a standing risk, not this year's emergency. Attackers keep coming through the front door because it keeps working. The question for leaders is no longer whether to act, but whether the number of doors is going down.

---

## What To Do — One Key Action

**Ask for one number every quarter: how many systems and services the company exposes to the internet, including its AI applications, and whether that count is going down. A shrinking footprint is the measure that matches six years of evidence.**

---

## MITRE ATT&CK

- **T1190 — Exploit Public-Facing Application:** seen in 27.7% of Mandiant's 2025 investigations
- **T1133 — External Remote Services:** seen in 23.8%, the other half of what you expose

**MITRE ATLAS** (attacks on AI systems, v5.6)

- **AML.T0049 — Exploit Public-Facing Application:** ATLAS applies the same technique to internet-facing AI applications, so they belong in the exposure count

---

## Learn More

- [FIR SIGNALS 2026](/reports/signals-2026/) — Signal 01, with every figure checked at the source
- [Mandiant M-Trends 2026](https://cloud.google.com/security/resources/m-trends) — Primary source
- [FIR Risk INTEL-45 — Stop Counting Patches](/intel/intel-45-stop-counting-patches/) — Why exposure beats patch counts as a board metric

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Six years at the top.

For the sixth year running, exploiting a flaw in something exposed to the internet was the most common way into a company in Mandiant's investigations: 32% where the way in could be identified.

This year, the other datasets caught up:
→ Verizon DBIR: exploitation is the #1 way in for the first time, 31% of breaches, up from 20%
→ IBM X-Force: exploitation of public-facing applications up 44%, to 40% of cases
→ Microsoft: up from 15% to 24% of initial access in its incident response work

Four datasets, collected four different ways, pointing the same direction. That's why it made SIGNALS 2026. A spike is a reason to look. Six years of agreement is a reason to act.

The action: ask for one number every quarter. How many systems and services do we expose to the internet, including our AI applications, and is that count going down?

FIR Risk INTEL-59 · SIGNALS 2026, Signal 01

#CyberRisk #VulnerabilityManagement #ExposureManagement #BoardGovernance #CISO #RiskManagement
```

## X POST

Six years at the top: exploits have been the #1 way in for six straight years of Mandiant investigations (32%).

This year Verizon agrees for the first time: 31% of breaches, up from 20%.

A spike is a reason to look. Six years of agreement is a reason to act. Count what you expose, and make it shrink.

Full INTEL → FIR Risk INTEL-59

#CyberRisk #ExposureManagement

---

## SOURCE DATA

**Editorial Frame:**
SIGNALS 2026 INTEL series (Bruce 11/16): 3 INTELs per signal, unique insight into each signal and why it is a signal this year; every other day from Wed 11/18. INTEL-59 = Signal 01, "why it's a signal": persistence (six years, Mandiant) + agreement (Verizon first time #1, IBM, Microsoft). Distinct from INTEL-22 (DBIR 31% + 29% pre-disclosure), INTEL-30 (VulnCheck pre-disclosure), INTEL-32 (three sellers agree on speed), INTEL-45 (MDDR patch-count metric).

**Fact-Check Notes (verified Nov 16, 2026 against SIGNALS source texts; page = printed page):**
- M-Trends 2026 p11: "For the sixth year running, exploits represented the most frequently observed initial infection vector in 2025 Mandiant incident response investigations. Exploits comprised 32% of investigations in which an initial infection vector could be identified." (SIGNALS claims ledger said "four years" from M-Trends 2025 p10 history; the 2026 report's own wording is six. Use six.)
- M-Trends 2026 p41: T1190 27.7%, T1133 23.8% (top 10 techniques, share of investigations).
- Verizon DBIR 2026 p10: exploitation "the most common initial access vector for breaches… risen to 31%… while credential abuse—the previous leader—is down to 13%." 20% prior year (p15; SIGNALS figure list).
- IBM X-Force 2026 p4, p7: "44% increase in incidents caused by the exploitation of public-facing applications… accounted for 40% of cases, whereas use of valid credentials made up only 32%."
- Microsoft MDDR 2026 p33: IR initial access, exploit public-facing application 15% → 24%.

**MITRE ATLAS (v5.6.0, atlas-data dist/ATLAS.yaml, checked Nov 16, 2026):** AML.T0049 Exploit Public-Facing Application, tactic Initial Access, ATT&CK reference T1190. FIR mapping; SIGNALS appendix maps ATLAS to Signal 05b only.

**FIR Risk Editorial Position:** "standing risk, not this year's emergency" and the quarterly exposure count are FIR's read; matches the SIGNALS Signal 01 board question. MITRE mapping from the SIGNALS appendix.
