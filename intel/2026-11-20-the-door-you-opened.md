# FIR Risk INTEL-60 — The Door You Opened on Purpose

**Type:** `TECHNIQUE`
**Date:** November 20, 2026
**Platform Source:** FIR SIGNALS 2026, Signal 01 "The window is gone. Expose less." (Mandiant M-Trends 2026, MITRE ATT&CK mapping in the SIGNALS appendix)

---

## The INTEL

**When leaders hear "exposure," they think of unpatched software. But in Mandiant's 2025 investigations, attackers used remote-access services almost as often as they exploited flaws: VPNs, remote desktop and similar ways in that companies open on purpose.**

From the SIGNALS 2026 appendix for security teams, using Mandiant's M-Trends 2026 technique data:

- **T1190 — Exploit Public-Facing Application:** seen in **27.7%** of investigations.
- **T1133 — External Remote Services:** seen in **23.8%**. Both made Mandiant's top 10 techniques of the year.

Mandiant's case notes show how it works. One ransomware group got in "through the use of either stolen or brute-forced virtual private network (VPN) credentials." Another, using the ransomware Mandiant saw most often in 2025, got in by exploiting "known vulnerabilities in network edge devices," the same kind of equipment that runs VPNs.

---

## Why It Matters

Remote access is exposure you chose. Every VPN, remote desktop gateway and remote support tool was opened for a business reason, and most were never closed when the reason ended. A patch fixes a flaw. It does nothing about a door that works exactly as designed for anyone holding a stolen password.

**Our read:** this is the half of Signal 01 that leaders can act on fastest, because it needs decisions, not patches. Close what isn't needed. Put strong sign-in on what remains. Know who uses each one.

---

## What To Do — One Key Action

**Ask for a list of every way someone can reach the company's systems remotely, including the API keys for its AI services, with a business owner for each. Close the ones nobody owns, and require phishing-resistant multi-factor authentication on the rest.**

---

## MITRE ATT&CK

- **T1133 — External Remote Services:** 23.8% of Mandiant's 2025 investigations
- **T1190 — Exploit Public-Facing Application:** 27.7%, including flaws in the edge devices that run remote access
- **T1078 — Valid Accounts:** stolen or guessed VPN credentials turn a remote-access service into a way in
- MITRE mitigations listed in SIGNALS: M1035 Limit Access to Resource Over Network · M1042 Disable or Remove Feature or Program · M1030 Network Segmentation · M1032 Multi-factor Authentication

**MITRE ATLAS** (attacks on AI systems, v5.6)

- **AML.T0012 — Valid Accounts:** in ATLAS, the credentials include "API keys that provide access to various AI resources and services": an AI service key is a remote-access credential too
- **AML.T0040 — AI Model Inference API Access:** access to an AI model through its API, the AI version of a remote-access service. ATLAS mitigations: AML.M0019 Control Access to AI Models and Data in Production · AML.M0024 AI Telemetry Logging

---

## Learn More

- [FIR SIGNALS 2026](/reports/signals-2026/) — Signal 01, plus the MITRE ATT&CK appendix in the PDF
- [Mandiant M-Trends 2026](https://cloud.google.com/security/resources/m-trends) — Primary source
- [FIR Risk INTEL-59 — Six Years at the Top](/intel/intel-59-six-years-at-the-top/) — Why exposure is a signal this year

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
The door you opened on purpose.

When leaders hear "exposure," they think of unpatched software. Mandiant's 2025 investigations say look again:
→ Exploiting public-facing applications: seen in 27.7% of investigations
→ Remote-access services like VPNs and remote desktop: 23.8%

Both made Mandiant's top 10 techniques of the year. One ransomware group got in with stolen or brute-forced VPN passwords. Another, using the ransomware Mandiant saw most often in 2025, came in through known flaws in network edge devices.

Remote access is exposure you chose. Every VPN and remote support tool was opened for a reason, and most were never closed when the reason ended. A patch does nothing about a door that works exactly as designed for anyone with a stolen password.

The action: list every way someone can reach your systems remotely, including the API keys for your AI services, with a business owner for each. Close the ones nobody owns. Put phishing-resistant MFA on the rest.

FIR Risk INTEL-60 · SIGNALS 2026, Signal 01

#CyberRisk #RemoteAccess #MFA #MITREATTACK #CISO #RiskManagement
```

## X POST

Exposure isn't just unpatched software.

Mandiant 2025: exploited public-facing apps in 27.7% of investigations. Remote-access services like VPNs: 23.8%.

Remote access is a door you opened on purpose. List every one, close what nobody owns, and put phishing-resistant MFA on the rest.

Full INTEL → FIR Risk INTEL-60

#CyberRisk #MITREATTACK

---

## SOURCE DATA

**Editorial Frame:**
SIGNALS INTEL series, Signal 01, INTEL 2 of 3. Unique insight from the SIGNALS MITRE appendix: T1133 (remote services) nearly as common as T1190, so "expose less" means remote access as much as patching. Actor names minimized (executive framing); ransomware family not named in the post.

**Fact-Check Notes (verified Nov 16, 2026 against SIGNALS source texts; page = printed page):**
- M-Trends 2026 p41, "Top 10 Most Frequently Seen MITRE ATT&CK Techniques": #5 T1190 Exploit Public-Facing Application 27.7%; #10 T1133 External Remote Services 23.8%. Same figures in the appendix tables (pp.85–101), which the SIGNALS appendix cites.
- M-Trends 2026 p37 (UNC6276): "gain initial network access through the use of either stolen or brute-forced virtual private network (VPN) credentials."
- M-Trends 2026 p37–38 (REDBIKE, aka Akira): "the most commonly observed ransomware variant" in 2025 Mandiant investigations; cluster UNC6361 "compromises target environments through the exploitation of known vulnerabilities in network edge devices."
- Mitigations: SIGNALS PDF appendix p16, Signal 01 (M1035, M1042, M1030, M1016) and Signal 02 (M1032).

**MITRE ATLAS (v5.6.0, atlas-data dist/ATLAS.yaml, checked Nov 16, 2026):** AML.T0012 Valid Accounts (Initial Access, Privilege Escalation; ATT&CK T1078), description quoted: credentials "may take the form of usernames and passwords of individual user accounts or API keys that provide access to various AI resources and services." AML.T0040 AI Model Inference API Access (tactic AI Model Access); mitigations AML.M0019, AML.M0024. FIR mapping.

**FIR Risk Editorial Position:** "exposure you chose", the owner list and phishing-resistant MFA action are FIR's read. MITRE T1078 added by FIR (stolen VPN credentials).
