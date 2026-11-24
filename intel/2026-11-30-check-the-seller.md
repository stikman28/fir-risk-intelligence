# FIR Risk INTEL-65 — Cyber Monday: Check the Seller

**Type:** `TREND`
**Date:** November 30, 2026
**Platform Source:** FIR SIGNALS 2026, Signal 03 "Half your attack surface belongs to someone else." (Verizon DBIR 2024, 2025 and 2026; IBM X-Force Threat Intelligence Index 2026)

---

## The INTEL

**Happy Cyber Monday. Before you buy anything today, you'll probably check the seller. Your vendors deserve the same look: across four editions of Verizon's DBIR, the share of breaches involving a third party rose every time, from 9% to 48%.**

Breaches with a third party involved, by DBIR edition:

- **2023: 9% · 2024: 15% · 2025: 30% · 2026: 48%.** More than five times the share in three editions.
- **One caveat, stated plainly.** Verizon widened its definition in 2024 to include flaws in third-party software, and said that year's rise was "mostly fueled by the use of zero-day exploits for Ransomware and Extortion attacks." The climb didn't stop there: the share doubled the next year, then rose another 60%.
- **A second dataset agrees.** IBM X-Force counts "a nearly 4-fold increase in major supply chain or third-party compromises over the last 5 years," and notes that "a single breach at a trusted supplier spread to many downstream customers." Techniques "once largely confined to nation-state actors" are now used by criminal groups.

---

## Why It Matters

Most companies give their biggest suppliers the closest look, because that's where the money goes. Attackers rank vendors differently: by what each one can reach. A small vendor that holds an admin login to your systems, a copy of your customer data, or a live connection between its software and yours can be worth more to an attacker than your largest supplier.

**Our read:** on Cyber Monday you check the seller before you pay. For vendors, the check that matters is not what they cost but what they can reach. That is where the SIGNALS decision starts: a living list of who holds access to us.

---

## What To Do — One Key Action

**Re-rank your top 20 vendors by what they can reach, not by what they cost: admin rights in your systems, copies of your data, and live tokens or integrations. Start your third-party reviews at the top of that list, even where the contract is small.**

---

## MITRE ATT&CK

- **T1199 — Trusted Relationship** (0.5% of Mandiant's 2025 investigations) and **T1195 — Supply Chain Compromise** (1.7%): a vendor's access or software used to reach you. Rare as techniques in Mandiant's cases, yet present in 48% of DBIR breaches: Mandiant counts techniques, Verizon counts breaches
- MITRE mitigations listed in SIGNALS: M1018 User Account Management · M1032 Multi-factor Authentication · M1036 Account Use Policies

**MITRE ATLAS** (attacks on AI systems, v5.6)

- **AML.T0010 — AI Supply Chain Compromise:** attackers "compromising the unique portions of the AI supply chain," including the data, the AI software stack or "the Model itself." AI providers belong on the same ranked list. ATLAS mitigation: AML.M0023 AI Bill of Materials, "a full listing of artifacts and resources that were used in building the AI," which helps "enable rapid response to reported vulnerabilities"

---

## Learn More

- [FIR SIGNALS 2026](/reports/signals-2026/) — Signal 03, plus the MITRE ATT&CK appendix in the PDF
- [Verizon 2026 Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/dbir/) — Primary source
- [IBM X-Force Threat Intelligence Index 2026](https://www.ibm.com/reports/threat-intelligence) — Primary source
- [FIR Risk INTEL-25 — The Third-Party Half](/intel/intel-25-the-third-party-half/) — The 2026 jump and the living inventory

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Cyber Monday: check the seller.

Before you buy anything today, you'll probably check who's selling. Your vendors deserve the same look.

Breaches involving a third party, by Verizon DBIR edition:
→ 2023: 9%
→ 2024: 15%
→ 2025: 30%
→ 2026: 48%

Verizon widened its definition in 2024, and the share still doubled and then rose 60% after that. IBM X-Force, counting differently, sees a nearly 4-fold rise in major supply chain and third-party compromises over five years.

Most companies give their biggest suppliers the closest look. Attackers rank vendors by what they can reach. A small vendor with an admin login or a copy of your customer data can matter more than your largest contract.

The action: re-rank your top 20 vendors by what they can reach (admin rights, your data, live tokens and integrations), not by what they cost. Start third-party reviews at the top of that list.

FIR Risk INTEL-65 · SIGNALS 2026, Signal 03

#CyberMonday #ThirdPartyRisk #SupplyChainSecurity #CyberRisk #CISO #RiskManagement
```

## X POST

Cyber Monday: you check the seller before you buy. Check your vendors too.

Breaches involving a third party (Verizon DBIR): 9% → 15% → 30% → 48%.

Rank your top 20 vendors by what they can reach, not what they cost.

Full INTEL → FIR Risk INTEL-65

#CyberMonday #ThirdPartyRisk

---

## SOURCE DATA

**Editorial Frame:**
SIGNALS INTEL series, Signal 03, INTEL 1 of 3. Cyber Monday-themed (Bruce 11/20: "Monday 11/30 gets a Cyber Monday theme"). Theme: check the seller / rank vendors by reach, not spend. "Why it's a signal": persistence, the four-edition trend line (the SIGNALS hero chart), corroborated by X-Force. Distinct from INTEL-25 (2026 jump +60%, JLR, living-inventory action), INTEL-31 (48% as corroboration, contract MFA) and INTEL-38 (3 hours, ~200 downstream, token question). The JLR "~5,000 downstream entities" figure is not used (unverified in the claims register).

**Fact-Check Notes (verified Nov 20, 2026 against SIGNALS source texts; page = printed page):**
- DBIR 2024 p13: supply chain interconnection "is present in 15% of the breaches we saw, a significant growth from 9% last year." p8: "we are introducing an expanded concept of a breach involving a third party that includes partner infrastructure being affected and direct or indirect software supply chain issues—including when an organization is affected by vulnerabilities in third-party software … We see this figure at 15% this year, a 68% increase from the previous year, mostly fueled by the use of zero-day exploits for Ransomware and Extortion attacks."
- DBIR 2025 p11: "the percentages of breaches where a third party was involved doubled, going from 15% to 30%."
- DBIR 2026 p11: "breaches with third-party involvement have increased by 60% from last year's dataset, reaching 48% of total breaches."
- 9% → 48% = 5.3×, "more than five times the share in three editions" (2023 → 2026 editions).
- X-Force 2026 p5: "~4x increase in the number of major supply chain or third party breaches over 5 years"; "Once largely confined to nation-state actors, these supply chain attack techniques are now being adopted by financially motivated and other criminal threat groups." p12: "There has been a nearly 4-fold increase in major supply chain or third-party compromises over the last 5 years. Often, a single breach at a trusted supplier spread to many downstream customers."
- SIGNALS appendix p16 (Signal 03): T1199 0.5%, T1195 1.7% (M-Trends 2026 pp. 85–101); "Rare as techniques in Mandiant's cases, yet present in 48% of DBIR breaches: Mandiant counts techniques, Verizon counts breaches." Mitigations M1018, M1032, M1036 (M1021 also listed). SIGNALS outline Signal 03 decision: "a living inventory of who holds access to us."

**MITRE ATLAS (v5.6.0, atlas-data dist/ATLAS.yaml, checked Nov 20, 2026):** AML.T0010 AI Supply Chain Compromise, quoted ("compromising the unique portions of the AI supply chain"; "the Model itself"). AML.M0023 AI Bill of Materials, quoted. FIR mapping; no AI-specific figures claimed.

**FIR Risk Editorial Position:** the Cyber Monday framing, "rank by reach, not spend," the examples of what a vendor can reach and the top-20 action are FIR's read. No Cyber Monday statistics are claimed.
