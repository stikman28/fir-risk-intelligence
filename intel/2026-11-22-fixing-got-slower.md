# FIR Risk INTEL-61 — Fixing Got Slower

**Type:** `TREND`
**Date:** November 22, 2026
**Platform Source:** FIR SIGNALS 2026, Signal 01 "The window is gone. Expose less." (Verizon DBIR 2026; CrowdStrike Global Threat Report 2026; Microsoft Digital Defense Report 2026)

---

## The INTEL

**In 2025, attackers got faster and defenders got slower. Both ends of the window moved the wrong way in the same year, and the reason on the defender's side is volume.**

The defender's side, from the Verizon DBIR 2026:

- Only **26%** of critical known-exploited vulnerabilities (those on CISA's KEV list) were fully fixed in 2025, down from **38%** the year before.
- The median time to fully fix one rose to **43 days**, from **32**.
- The reason: the median organization had **16** of these vulnerabilities to fix, up from 11. "That is almost 50% more."

The attacker's side:

- Microsoft: the median time from a flaw being found in the wild to a working exploit is "well below 24 hours."
- CrowdStrike: once inside, the average attacker moves through the network in **29 minutes**, down from 84 in 2022.

---

## Why It Matters

A 43-day fix cycle against a one-day exploit was already a losing race. What changed this year is the cause. Security teams didn't simply get worse: they were handed about 50% more critical fixes, and the fix rate fell.

**Our read:** this is why SIGNALS says "expose less," not "patch faster." A faster team still loses to rising volume. Fewer exposed systems means fewer critical fixes in the first place, and every fix you don't need is one the attacker can't race you to.

---

## What To Do — One Key Action

**Ask your security leader for two numbers from last year: how many critical known-exploited flaws the company had to fix, and what share were fully fixed. If the workload grew faster than the fixes, the answer is fewer exposed systems, not just a faster team.**

---

## MITRE ATT&CK

- **T1190 — Exploit Public-Facing Application:** the flaws that sit unfixed on exposed systems
- MITRE mitigation listed in SIGNALS: M1016 Vulnerability Scanning, paired with M1042 Disable or Remove Feature or Program

**MITRE ATLAS** (attacks on AI systems, v5.6)

- **AML.T0049 — Exploit Public-Facing Application:** internet-facing AI applications run the same fix race, with the same exploit clock
- **AML.M0023 — AI Bill of Materials:** a full listing of what each AI system is built from, which ATLAS says can "enable rapid response to reported vulnerabilities." You can't fix what you can't find
- **AML.M0016 — Vulnerability Scanning:** extends scanning to AI model files and their software dependencies, which "should be scanned for known vulnerabilities"

---

## Learn More

- [FIR SIGNALS 2026](/reports/signals-2026/) — Signal 01, with every figure checked at the source
- [Verizon 2026 Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/dbir/) — Primary source
- [FIR Risk INTEL-60 — The Door You Opened on Purpose](/intel/intel-60-the-door-you-opened/) — The other half of exposure

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Fixing got slower.

In 2025, both ends of the window moved the wrong way.

Defenders, per the Verizon DBIR 2026:
→ Only 26% of critical known-exploited vulnerabilities were fully fixed, down from 38%
→ The median time to fully fix one rose from 32 days to 43
→ The median organization had 16 of them to fix, up from 11: "almost 50% more"

Attackers:
→ Microsoft: flaw found in the wild to working exploit, "well below 24 hours"
→ CrowdStrike: average breakout time 29 minutes, down from 84 in 2022

Security teams didn't simply get worse. They were handed about 50% more critical fixes, and the fix rate fell. A faster team still loses to rising volume. That's why SIGNALS 2026 says "expose less," not "patch faster."

The action: ask for two numbers from last year. How many critical known-exploited flaws did we have to fix, and what share were fully fixed?

FIR Risk INTEL-61 · SIGNALS 2026, Signal 01

#CyberRisk #VulnerabilityManagement #ExposureManagement #VerizonDBIR #CISO #RiskManagement
```

## X POST

Fixing got slower in 2025.

Verizon DBIR: 26% of critical known-exploited flaws fully fixed (from 38%), 43 days to fix (from 32), with almost 50% more to fix.

Attackers: exploits in under 24 hours, breakout in 29 minutes.

Expose less, so there's less to fix.

Full INTEL → FIR Risk INTEL-61

#CyberRisk #VulnerabilityManagement

---

## SOURCE DATA

**Editorial Frame:**
SIGNALS INTEL series, Signal 01, INTEL 3 of 3. Unique insight: both ends of the window moved the wrong way in one year, and the defender-side cause is VOLUME (median KEV count per org 11 → 16). Distinct from INTEL-45 (MDDR 30–60 day remediation + patch-count metric) and INTEL-22 (DBIR initial-access ranking).

**Fact-Check Notes (verified Nov 16, 2026 against SIGNALS source texts; page = printed page):**
- Verizon DBIR 2026 p10 (summary) and p17 (vulnerability analysis): "Only 26% of the CISA KEV vulnerabilities had been fully remediated, a considerable drop from last year's 38%"; "Our new median time is 43 days, almost two weeks longer than last year's 32 days"; "The median number of KEV vulnerabilities that had to be patched by organizations has risen in 2025 to 16, where this figure was 11 in 2024. That is almost 50% more KEV vulnerabilities to patch in a year." Unremediated share 12% → 16% (not used).
- Microsoft MDDR 2026 p14: median time from vulnerability discovery in the wild to weaponization "well below 24 hours."
- CrowdStrike GTR 2024 p10; 2026 p9: average eCrime breakout 84 min (2022) → 29 min (2025).

**MITRE ATLAS (v5.6.0, atlas-data dist/ATLAS.yaml, checked Nov 16, 2026):** AML.T0049 Exploit Public-Facing Application (Initial Access; ATT&CK T1190). AML.M0023 AI Bill of Materials: "The AI BOM can help mitigate supply chain risks and enable rapid response to reported vulnerabilities." AML.M0016 Vulnerability Scanning: "Model artifacts, downstream products produced by models, and external software dependencies should be scanned for known vulnerabilities." FIR mapping; no AI-specific remediation figures exist in the SIGNALS sources, so none are claimed.

**FIR Risk Editorial Position:** "both ends moved the wrong way" and "volume" framing, and the two-number action, are FIR's read.
