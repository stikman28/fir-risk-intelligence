# FIR Risk INTEL-62 — The Call Is the Lure. The Remote Tool Is the Door.

**Type:** `TECHNIQUE`
**Date:** November 24, 2026
**Platform Source:** FIR SIGNALS 2026, Signal 02 "Inside, they look like you." (Microsoft Digital Defense Report 2026, CrowdStrike 2026 Global Threat Report)

---

## The INTEL

**SIGNALS 2026 reported a 502% rise in malicious voice calls over Microsoft Teams. Behind the number is a simple pattern: the call builds trust, and a remote-control tool, often one already on the computer, hands the attacker the keyboard.**

What Microsoft and CrowdStrike saw in 2025–2026:

- **The callers look like colleagues now.** Fake "Help Desk" and "IT Support" names used to dominate. Now "a majority now use personal-looking usernames that either match or appear to match legitimate employee naming conventions" (Microsoft).
- **Warnings don't stop it.** "Despite red flags such as Teams' 'External' banners and call warnings, skilled attackers successfully persuade victims to comply, usually on workdays during business hours." 93% of attackers kept a target on the line for 20 seconds or longer at least once, the point where a script can begin (Microsoft).
- **Then the remote tool.** The attacker "convinces the victim to grant access through a remote monitoring and management (RMM) tool" and completes reconnaissance "in two minutes or less" (Microsoft). In one CrowdStrike case, an employee granted access through Quick Assist, the remote help tool built into Windows, and the attacker tried to move data out within four minutes.

---

## Why It Matters

Security teams can't hear a phone call. Microsoft notes that "the voice channel itself carries no link to intercept." Training helps, but this year's data shows trained people, with warning banners in front of them, still comply.

**Our read:** the call is the part you can't fully control. The remote-control tool is the part you can. If an employee can't hand over their keyboard to a stranger, a convincing call ends as a conversation, not an intrusion.

---

## What To Do — One Key Action

**Limit remote-control and remote-assistance tools, including the ones built into the operating system, to IT staff only, and confirm it with a test on an ordinary employee's laptop. This is Microsoft's own recommendation: "Limit remote assistance tools to IT-only groups."**

---

## MITRE ATT&CK

- **T1566.004 — Phishing: Spearphishing Voice:** 6.1% of Mandiant's 2025 investigations (SIGNALS appendix)
- **T1684.001 — Impersonation** (T1656 in M-Trends): the caller poses as a colleague or IT support
- **T1219 — Remote Access Tools:** the victim installs or opens a remote-control tool for the attacker
- MITRE mitigations listed in SIGNALS: M1017 User Training · M1036 Account Use Policies

**MITRE ATLAS** (attacks on AI systems, v5.6)

- **AML.T0052.001 — Deepfake-Assisted Phishing:** ATLAS notes that cloned voices "are used in vishing (voice phishing) attacks over telephone or VoIP." The Microsoft figures above don't say how many calls used AI voices; this is how AI can make the same call more convincing.
- **AML.T0073 — Impersonation:** posing as "a known sender such as an executive, colleague, or third-party vendor." ATLAS mitigation: AML.M0018 User Training ("how to identify deepfakes and phishing attempts")

---

## Learn More

- [FIR SIGNALS 2026](/reports/signals-2026/) — Signal 02, plus the MITRE ATT&CK appendix in the PDF
- [Microsoft Digital Defense Report 2026](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2026) — Primary source
- [CrowdStrike 2026 Global Threat Report](https://www.crowdstrike.com/global-threat-report/) — Primary source
- [FIR Risk INTEL-8 — The Breach Starts With a Phone Call](/intel/intel-8-voice-phishing-surge/) — When attackers call your help desk

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
The call is the lure. The remote tool is the door.

Malicious voice calls over Microsoft Teams rose 502% in a year. What's behind the number:
→ Callers now use names that look like your colleagues, not "IT Support"
→ "External" banners and call warnings don't stop skilled attackers, Microsoft says
→ The goal is a remote-control tool. Once granted, reconnaissance takes "two minutes or less"
→ In one CrowdStrike case, an employee opened Quick Assist, built into Windows, and the attacker tried to move data out within four minutes

Security teams can't hear a phone call. But they can decide who is allowed to hand over a keyboard.

The action: limit remote-control and remote-assistance tools, including the built-in ones, to IT staff only. Then test it on an ordinary employee's laptop. A convincing call then ends as a conversation, not an intrusion.

FIR Risk INTEL-62 · SIGNALS 2026, Signal 02

#CyberRisk #Vishing #SocialEngineering #MITREATTACK #CISO #RiskManagement
```

## X POST

Malicious Teams voice calls: +502% in a year.

The call builds trust. A remote-control tool, often one already on the PC, hands over the keyboard. Recon takes two minutes.

Limit remote-assistance tools to IT staff, built-in ones included.

Full INTEL → FIR Risk INTEL-62

#CyberRisk #Vishing

---

## SOURCE DATA

**Editorial Frame:**
SIGNALS INTEL series, Signal 02, INTEL 1 of 3. Unique insight: what sits behind the SIGNALS "+502%" stat (Microsoft's case detail), and that the controllable step is the remote-control tool, not the call. Distinct from INTEL-8 (attackers calling the help desk; M-Trends voice #2) and INTEL-18 (ClickFix). Actor names kept out of the post; CHATTY SPIDER's target sector (law firms) not used.

**Fact-Check Notes (verified Nov 16, 2026 against SIGNALS source texts; page = printed page):**
- MDDR 2026 p46: "Vishing over cross-tenant calls … in Microsoft Teams in particular has become a more prominent access vector. The weekly confirmed malicious volume has risen 502% from this time last year. Over 90% of attackers that use Teams have incorporated voice calling into some of their attacks. Despite red flags such as Teams' 'External' banners and call warnings, skilled attackers successfully persuade victims to comply, usually on workdays during business hours." "Across the attacks we studied, 93% of attackers succeeded at least once in keeping a target on the line for 20 seconds or longer—the point at which an attacker has captured attention and can begin a social engineering script." "…the voice channel itself carries no link to intercept."
- MDDR 2026 p47: "While 'Help Desk' and 'IT Support' variants used to account for most malicious display names, a majority now use personal-looking usernames that either match or appear to match legitimate employee naming conventions." "The attacker convinces the victim to grant access through a remote monitoring and management (RMM) tool, achieving interactive control of the endpoint. Attackers complete reconnaissance in two minutes or less and then download malicious payloads." Recommendation: "RMM tools. Limit remote assistance tools to IT-only groups through endpoint management policy."
- CrowdStrike 2026 GTR p11: CHATTY SPIDER persuaded an employee "to grant workstation access via Microsoft Quick Assist. Within four minutes, CHATTY SPIDER attempted to exfiltrate data using WinSCP." (First attempt blocked by firewall; detected before exfiltration completed. Post says "tried to," which matches.)
- M-Trends 2026 p86 (appendix): T1566.004 Spearphishing Voice 6.1%. SIGNALS appendix p16 lists it with T1684.001 and mitigations M1032, M1036, M1026, M1017.

**MITRE ATLAS (v5.6.0, atlas-data dist/ATLAS.yaml, checked Nov 16, 2026):** AML.T0052.001 Deepfake-Assisted Phishing, quoted: voice deepfakes "are used in vishing [1] (voice phishing) attacks over telephone or VoIP." AML.T0073 Impersonation, quoted: "a known sender such as an executive, colleague, or third-party vendor." AML.M0018 User Training, quoted. FIR mapping; no AI-specific figures claimed (Microsoft does not say what share of Teams vishing used AI voices).

**FIR Risk Editorial Position:** "the call is the part you can't control; the remote tool is the part you can" and the test-on-a-laptop step are FIR's read. MITRE T1219 added by FIR (not in SIGNALS appendix).
