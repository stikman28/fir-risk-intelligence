# FIR Risk INTEL-63 — Who's Really at the Table?

**Type:** `TREND`
**Date:** November 26, 2026
**Platform Source:** FIR SIGNALS 2026, Signal 02 "Inside, they look like you." (CrowdStrike 2026 Global Threat Report, Red Canary 2026 Threat Detection Report, Microsoft Digital Defense Report 2026)

---

## The INTEL

**Happy Thanksgiving. Today, everyone who walks through the door is welcome, because everyone at the table looks like family. Attackers count on the same trust at work. In 2025, 82% of what CrowdStrike detected involved no malware at all: just someone who looked like they belonged.**

CrowdStrike's malware-free share of detections, from its 2026 report:

- **2020: 51% · 2021: 62% · 2022: 71% · 2023: 75% · 2024: 79% · 2025: 82%.** Up every year for six years.
- **How they get a seat.** Attackers "operated through valid credentials, trusted identity flows, approved SaaS integrations, and inherited software supply chains… blending into normal activity." Defenders "are often forced to identify malicious intent within otherwise legitimate actions."
- **Others see the same shift.** At Red Canary, identity threats overtook endpoint threats in 2025, at 53% of detection volume (from 20%). Red Canary measures what it detects, so better visibility explains part of the jump. The direction matches CrowdStrike's.

---

## Why It Matters

Most security tools were built to spot the stranger: the malicious file, the unknown program. When the intruder signs in with a real account and uses the company's own tools, there is no stranger to spot. What is left to notice is behavior: the cousin who never helps in the kitchen suddenly carrying out the silverware. At work, that's a user who never touches the finance share copying all of it, or an admin signing in from a new device at 3 a.m.

**Something to be thankful for:** the front door is holding. Microsoft reports password attacks fell 26% this year, "strong evidence that security measures such as MFA and passkeys are forcing attackers to pivot." That pivot is why they now try to look like family instead.

**Our read:** the question for leaders is no longer "do we have good malware protection?" Most companies do. It is the SIGNALS board question: "If an attacker were logged in as one of our employees today, would we know?"

---

## What To Do — One Key Action

**Know your guest list. Pick your 25 most powerful accounts: admins, service accounts and AI agents with broad access. For each, ask the security team what "normal" looks like and which unusual action would raise an alert today. Where nobody can answer, that account is where an attacker would sit at the table unnoticed.**

---

## MITRE ATT&CK

- **T1078 — Valid Accounts:** 17.0% of Mandiant's 2025 investigations. ATT&CK v20 places it under a new tactic, Stealth: "appearing as normal behavior"
- MITRE mitigations listed in SIGNALS: M1026 Privileged Account Management · M1036 Account Use Policies · M1032 Multi-factor Authentication

**MITRE ATLAS** (attacks on AI systems, v5.6)

- **AML.T0012 — Valid Accounts:** in ATLAS, stolen credentials include "API keys that provide access to various AI resources and services"
- **AML.T0053 — AI Agent Tool Invocation:** an attacker with access to an AI agent can "invoke tools the agent has access to," including tools "not directly accessible by users." To your logs, that activity looks like the agent doing its job. ATLAS mitigations: AML.M0024 AI Telemetry Logging (including "identity of the agent") · AML.M0027 Single-User AI Agent Permissions Configuration

---

## Learn More

- [FIR SIGNALS 2026](/reports/signals-2026/) — Signal 02, plus the MITRE ATT&CK appendix in the PDF
- [CrowdStrike 2026 Global Threat Report](https://www.crowdstrike.com/global-threat-report/) — Primary source
- [Red Canary 2026 Threat Detection Report](https://redcanary.com/threat-detection-report/) — Primary source
- [FIR Risk INTEL-44 — The Basics Are Working](/intel/intel-44-the-basics-are-working/) — Why attackers pivoted away from passwords
- [FIR Risk INTEL-23 — The Permission Problem](/intel/intel-23-the-permission-problem/) — Escalation without exploits

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Who's really at the table?

Happy Thanksgiving. Today everyone who walks in is welcome, because everyone looks like family.

Attackers count on the same trust at work. The share of CrowdStrike detections with no malware at all:
→ 2020: 51%
→ 2022: 71%
→ 2024: 79%
→ 2025: 82%

They sign in with real accounts and use your own tools, "blending into normal activity." There's no stranger to spot. Only behavior that's out of character.

Something to be thankful for: the front door is holding. Microsoft says password attacks fell 26% this year, as MFA and passkeys force attackers to pivot. That's why they now try to look like family.

The action: know your guest list. Pick your 25 most powerful accounts, including admins, service accounts and AI agents. For each, ask what "normal" looks like and what unusual action would raise an alert today. Where nobody can answer, that's where an attacker sits at the table unnoticed.

Grateful for everyone who reads and shares FIR Risk. Enjoy the day.

FIR Risk INTEL-63 · SIGNALS 2026, Signal 02

#Thanksgiving #CyberRisk #IdentitySecurity #ThreatDetection #CISO #RiskManagement
```

## X POST

Happy Thanksgiving. Everyone at the table looks like family. That's the trick attackers use too.

82% of CrowdStrike's 2025 detections had no malware, up from 51% in 2020. They sign in and blend in.

Know your guest list: for your 25 most powerful accounts, AI agents included, what's normal?

Full INTEL → FIR Risk INTEL-63

#Thanksgiving #CyberRisk

---

## SOURCE DATA

**Editorial Frame:**
SIGNALS INTEL series, Signal 02, INTEL 2 of 3. Thanksgiving-themed (Bruce 11/19: "Thanksgiving post needs to be themed for thanksgiving"); posts Thu 11/26. Theme: guests who look like family / know your guest list, plus a gratitude note (the basics are working). "Why it's a signal": persistence, six years of growth in the malware-free share (SIGNALS showed 2022–2025; CrowdStrike 2026 Figure 4 goes back to 2020). Distinct from INTEL-11 (Red Canary 850%, used here only as corroboration with caveat), INTEL-23 (83% escalation without exploit), INTEL-44 (password attacks −26%, reused here as the thankful note only) and INTEL-51.

**Fact-Check Notes (verified Nov 16, 2026 against SIGNALS source texts; page = printed page):**
- CrowdStrike 2026 GTR p11, Figure 4 ("Percentage of malware-free detections since 2020"): 2020 51%, 2021 62%, 2022 71%, 2023 75%, 2024 79%, 2025 82%. Earlier editions agree: cs2024 p11 (71% 2022, 75% 2023); cs2025 p9 (79% 2024).
- CrowdStrike 2026 GTR p2: "Adversaries operated through valid credentials, trusted identity flows, approved SaaS integrations, and inherited software supply chains. Notably, 82% of detections were malware-free. Intrusions moved through authorized pathways and trusted systems, blending into normal activity."
- CrowdStrike 2026 GTR p10: "Defenders are often forced to identify malicious intent within otherwise legitimate actions."
- Red Canary 2026 TDR p4: "Identity threats accounted for 53 percent of overall detection volume in 2025, up from 20 percent in 2024." p22: identity detections "overtake endpoint detections by a significant margin." Caveat (claims register): detection volume reflects visibility, so it is used as corroboration with the caveat stated.
- MDDR 2026 p64: password attacks down "26% year-over-year. This provides strong evidence that security measures such as MFA and passkeys are forcing attackers to pivot to other approaches to achieve access to high-value targets." (Same quote as INTEL-44; SIGNALS claims register ✅.)
- M-Trends 2026 p86/p89: T1078 Valid Accounts 17.0%. SIGNALS appendix p16: "ATT&CK v20 names this tactic Stealth: 'appearing as normal behavior.'" Board question from SIGNALS p6.

**MITRE ATLAS (v5.6.0, atlas-data dist/ATLAS.yaml, checked Nov 16, 2026):** AML.T0012 Valid Accounts, quoted ("API keys that provide access to various AI resources and services"). AML.T0053 AI Agent Tool Invocation, quoted: "use their access to an AI agent to invoke tools the agent has access to"; "AI agents may be configured to have access to tools that are not directly accessible by users." AML.M0024 AI Telemetry Logging, quoted ("identity of the agent"). AML.M0027 Single-User AI Agent Permissions Configuration. FIR mapping; no AI-specific figures claimed.

**FIR Risk Editorial Position:** the Thanksgiving framing, the behavior examples (silverware, finance share, 3 a.m. sign-in) and the 25-account "guest list" action are FIR's read. The examples are illustrative, not from a source.
