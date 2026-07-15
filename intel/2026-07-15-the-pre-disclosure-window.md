# FIR Risk INTEL-30 — The Pre-Disclosure Window

**Type:** `VULNERABILITY`
**Date:** July 15, 2026
**Platform Source:** FIR Risk E91 — The Window Closed (Rapid7 + VulnCheck + Zscaler)

---

## The INTEL

**Nearly three in ten actively-exploited vulnerabilities in 2025 were being weaponized on or before the day they were disclosed. For those, "patch faster" was never an option — exploitation arrived before the fix existed. Stop planning your vulnerability program around a reaction window that, for the vulnerabilities that matter most, no longer exists.**

VulnCheck's 2026 Exploit Intelligence Report puts a hard number on the fear defenders couldn't previously quantify: **28.96% of the vulnerabilities added to CISA's Known Exploited Vulnerabilities (KEV) catalog in 2025 were exploited on or before the day their CVE was published** — up from 23.6% the year before. The 2026 Verizon DBIR, working from a completely separate dataset, put the same figure at **29%**. Two independent sources, the same fraction — which is exactly the kind of agreement worth trusting.

The case study is Microsoft SharePoint's "ToolShell." Microsoft patched two flaws on July 8, 2025. **Eleven days later** it disclosed those patches were *incomplete* — and that attackers were already exploiting the bypass, a critical unauthenticated remote-code-execution flaw, *before the complete fix existed.* Within days, three China-nexus actors were named; one deployed Warlock ransomware. By year-end that single flaw had drawn ten distinct threat actors and multiple ransomware families. VulnCheck ranked it the **#2 most-exploited vulnerability of 2025**.

---

## Why It Matters

Every vulnerability-management program is built on an unstated assumption: that there is a window between disclosure and exploitation, and the job is to patch inside it. The 2025 data breaks that assumption for the vulnerabilities most likely to hurt you. When roughly three in ten actively-exploited flaws are hit on or before disclosure day — and when a vendor's own "complete" patch can itself be bypassed and exploited within eleven days — patch speed alone is a losing race for internet-facing systems.

This does not mean patching stops mattering. It means the *strategy* has to widen. If you cannot reliably patch before exploitation, the leverage moves to reducing what an attacker can reach in the first place: taking edge and internet-facing systems off open exposure where they don't need it, segmenting so a single exploited box isn't a path to everything, and prioritizing the KEV list not as a to-do queue but as evidence of where the pre-disclosure risk actually lands. VulnCheck's own framing is that the KEV catalog is a starting point, not the whole map — attackers also revisit old, unpatched flaws (884 CVEs picked up first-time exploitation evidence in 2025, more than 160 of them dating from 2024).

The organizations that handle this well stop asking "how fast can we patch?" and start asking "what is exposed, to whom, and does it need to be?"

---

## What To Do — One Key Action

**Treat the patch window as zero for anything internet-facing. Shift the program's center of gravity from patch speed to exposure reduction — decommission or firewall edge systems that don't need open exposure, segment aggressively, and use the CISA KEV catalog as a prioritization signal for where pre-disclosure risk concentrates, not as a checklist you can always beat the clock on.**

This is a CISO-and-infrastructure move, and it is a reframe more than a tooling purchase. Keep patching — but stop betting the program on winning a race the 2025 data says you lose nearly a third of the time. The single highest-leverage change is to make internet-facing exposure a deliberate, minimized, reviewed decision rather than a default. When a flaw is exploited before it's disclosed, the only defense you controlled in advance was whether the vulnerable surface was reachable at all.

---

## MITRE ATT&CK

- **T1190 — Exploit Public-Facing Application:** The initial-access vector in the ToolShell chain and the broader pre-disclosure-exploitation pattern. The control posture is exposure reduction and segmentation — minimizing what is reachable — since patch timing cannot be relied on when exploitation precedes disclosure.
- **T1195 — Supply Chain Compromise:** An incomplete vendor patch that is itself bypassed shifts risk into the software-supply-chain relationship; the control is treating vendor patch cadence as a risk input, not a guarantee.

---

## Learn More

- [FIR Risk Tuesday E91 — The Window Closed](/tuesday/e91-the-window-closed/) — The full three-report synthesis
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — The catalog at the center of the finding
- [VulnCheck 2026 Exploit Intelligence Report](https://vulncheck.com/) — Primary source

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Nearly 3 in 10 actively-exploited vulnerabilities in 2025 were weaponized on or before the day they were disclosed.

For those, "patch faster" was never an option. The exploit arrived before the fix existed.

That's VulnCheck's 2026 finding — 28.96% of 2025 CISA KEV entries exploited on or before their CVE publication date, up from 23.6%. The Verizon DBIR, from an entirely separate dataset, put it at 29%. Two independent sources, the same fraction.

The case study: Microsoft SharePoint "ToolShell." Patched July 8. Eleven days later, Microsoft disclosed the patch was incomplete — and attackers were already exploiting the bypass before a complete fix existed. It became the #2 most-exploited vulnerability of the year.

The uncomfortable implication for every vulnerability-management program: for internet-facing systems, the reaction window you're optimizing against no longer reliably exists.

Patching still matters. But when a third of the flaws that hurt you are hit before disclosure, patch speed alone is a losing race. The leverage moves upstream — to reducing what an attacker can reach in the first place.

Stop asking "how fast can we patch?" Start asking "what is exposed, to whom, and does it need to be?"

#CyberSecurity #VulnerabilityManagement #CISO #RiskManagement #CISA #ExposureManagement #ThreatIntelligence
```

## X POST

Nearly 3 in 10 actively-exploited vulnerabilities in 2025 were weaponized on or before the day they were disclosed.

For those, "patch faster" was never an option. The exploit arrived before the fix.

VulnCheck 2026: 28.96% of 2025 CISA KEV entries exploited on/before their CVE publication date (up from 23.6%). Verizon's DBIR, separate dataset, put it at 29%.

Case study: SharePoint "ToolShell." Patched July 8 → 11 days later Microsoft admits the patch was incomplete → attackers already exploiting the bypass. #2 most-exploited vuln of 2025.

For internet-facing systems, the reaction window no longer reliably exists. Patch speed alone is a losing race — the leverage is reducing what's reachable in the first place.

#CyberSecurity #VulnerabilityManagement

---

## SOURCE DATA

**Editorial Frame:**
INTEL-30 extracts the single most alarming quantitative finding from E91 — the collapse of pre-disclosure lead time — into a standalone VULNERABILITY brief for vulnerability-management and infrastructure leaders. The board-level reframe is from patch speed to exposure reduction.

**Primary Sources:**
- VulnCheck — 2026 Exploit Intelligence Report (28.96% figure, ToolShell case study, 884/160+ CVE figures)
- Corroborating: Verizon 2026 DBIR (independent 29% pre-disclosure figure) — see FIR E90

**Fact-Check Notes (verified against source):**
- CONFIRMED: 28.96% of 2025 KEV entries exploited on/before CVE publication date, up from 23.6% in 2024.
- CONFIRMED: Verizon DBIR independent figure of 29% (per E90 fact-check).
- CONFIRMED: ToolShell timeline — CVE-2025-49704/49706 patched July 8, 2025; incomplete-patch bypass (CVE-2025-53770/53771) disclosed 11 days later; active pre-fix exploitation; three China-nexus actors incl. Warlock ransomware; ranked #2 exploited vuln of 2025.
- CONFIRMED: 884 CVEs with first-time 2025 exploitation evidence; 160+ from CVE-2024.
- EXCLUDED: the debunked "27% KEV coverage / 73% blind spot" claim (source's 27% is a CNA-source distribution stat, not KEV coverage) — not used.

**FIR Risk Editorial Position:**
- Leads with the strongest verified number and the ToolShell case study; frames the action as exposure reduction, consistent with E91's thesis.
- Voice: declarative, board-readable.
