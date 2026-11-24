# FIR Risk INTEL-66 — Their Fix Takes Eight Months

**Type:** `TECHNIQUE`
**Date:** December 2, 2026
**Platform Source:** FIR SIGNALS 2026, Signal 03 "Half your attack surface belongs to someone else." (Verizon DBIR 2025 and 2026, Mandiant M-Trends 2026)

---

## The INTEL

**When a vendor has a security gap, you share it until they fix it, and that can take a long time. Verizon tracked how quickly third parties fixed weaknesses in their cloud accounts. For weak passwords and permission errors, getting even half of them resolved took almost eight months.**

What Verizon's 2026 DBIR found across 7,513 third-party cloud exposures:

- **Missing or weak MFA:** only 23% of third-party organizations fully fixed missing or improperly secured MFA on their cloud accounts. Half of these findings were resolved within a month; the rest lingered.
- **Weak passwords and permission errors:** the time to resolve half the findings was "much worse, reaching almost eight months."
- **Leaked secrets:** the 2025 DBIR, in a year with "notable incidents involving credential reuse in a third-party environment," found a median of 94 days to fix leaked secrets discovered in a GitHub repository.

---

## Why It Matters

You can't fix a vendor's systems. But the vendor's way into yours runs through controls you own: the accounts you gave them, what those accounts can reach, where they can sign in from, and how long their tokens stay valid.

Mandiant puts the stakes plainly: "a risk accepted in a third-party application deployed into an interconnected environment is also a risk in the production core." Its advice for vendor connections is to grant "only the specific scopes required," avoid "wildcard permissions," and give "unique identities and credentials for each integration."

**Our read:** an open finding at a vendor is a reason to tighten your side for as long as it stays open. Waiting on their fix is not a control.

---

## What To Do — One Key Action

**When a vendor has an open security finding, reduce what its access can reach on your side until the finding is closed: fewer permissions, sign-in only from known locations or devices, and tokens that expire. Agree a fix-by date, and lift the limits when it's met.**

---

## MITRE ATT&CK

- **T1550.001 — Application Access Token** (5.3% of Mandiant's 2025 investigations) and **T1199 — Trusted Relationship** (0.5%): a vendor's token or access used to reach you
- MITRE mitigations listed in SIGNALS: M1018 User Account Management · M1032 Multi-factor Authentication · M1036 Account Use Policies

**MITRE ATLAS** (attacks on AI systems, v5.6)

- **AML.T0091.000 — Application Access Token:** stolen tokens "used in lieu of login credentials," common across "software-as-a-service (SaaS), and AI-as-a-service." A vendor's token into your AI services is the same exposure. ATLAS mitigation: AML.M0028 AI Agent Tools Permissions Configuration, "applying the principle of least privilege along with delegated access"

---

## Learn More

- [FIR SIGNALS 2026](/reports/signals-2026/) — Signal 03, plus the MITRE ATT&CK appendix in the PDF
- [Verizon 2026 Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/dbir/) — Primary source
- [Mandiant M-Trends 2026](https://cloud.google.com/security/resources/m-trends) — Primary source
- [FIR Risk INTEL-38 — Three Hours to Admin](/intel/intel-38-three-hours-to-admin/) — How fast a stolen vendor token turns into control

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Their fix takes eight months.

When a vendor has a security gap, you share it until they fix it.

Verizon's 2026 DBIR tracked 7,513 third-party cloud exposures:
→ Only 23% of third parties fully fixed missing or weak MFA
→ Weak passwords and permission errors took almost eight months to get half resolved

You can't fix a vendor's systems. But their way into yours runs through controls you own: the accounts you gave them, what those accounts reach, where they sign in from, how long their tokens last.

Mandiant: "a risk accepted in a third-party application … is also a risk in the production core."

The action: when a vendor has an open security finding, reduce what its access can reach on your side until it's closed. Fewer permissions, known sign-in locations, tokens that expire. Agree a fix-by date.

FIR Risk INTEL-66 · SIGNALS 2026, Signal 03

#ThirdPartyRisk #CyberRisk #IdentitySecurity #CISO #RiskManagement
```

## X POST

Your vendor's security gap is yours until they fix it.

Verizon: weak passwords and permission errors at third parties took almost 8 months to get half resolved.

Open finding at a vendor? Shrink what their access reaches on your side until it's closed.

Full INTEL → FIR Risk INTEL-66

#ThirdPartyRisk #CyberRisk

---

## SOURCE DATA

**Editorial Frame:**
SIGNALS INTEL series, Signal 03, INTEL 2 of 3. Unique insight: the vendor's remediation clock, and the controls on your side that limit the exposure while it runs. Distinct from INTEL-25 (said only "a minority" fixed MFA; inventory action), INTEL-31 (contract MFA), INTEL-32 (mentioned ~8 months in passing as corroboration) and INTEL-38 (token-revocation question to vendors).

**Fact-Check Notes (verified Nov 20, 2026 against SIGNALS source texts; page = printed page):**
- DBIR 2026 p11, Figure 6 "Survival analysis of third-party, cloud-based MFA exposures (n=7,513)": "only 23% of third-party organizations fully remediated missing or improperly secured multifactor authentication (MFA) on their cloud accounts, with 50% of all findings being resolved within a month. For weak passwords and permission misconfigurations, the time to resolve 50% of all findings was much worse, reaching almost eight months." Post says "7,513 third-party cloud exposures" for the figure's n.
- DBIR 2025 p11: "There were notable incidents this year involving credential reuse in a third-party environment—in which our research found the median time to remediate leaked secrets discovered in a GitHub repository was 94 days."
- M-Trends 2026 p77: "By recognizing that a risk accepted in a third-party application deployed into an interconnected environment is also a risk in the production core…"; "Enforcing the principle of least privilege for all integrations … This includes avoiding wildcard permissions and granting only the specific scopes required for the integration to function, as well as assigning unique identities and credentials for each integration."
- SIGNALS appendix p16 (Signal 03): T1550.001 5.3%, T1199 0.5%; mitigations M1018, M1032, M1036.

**MITRE ATLAS (v5.6.0, atlas-data dist/ATLAS.yaml, checked Nov 20, 2026):** AML.T0091.000 Application Access Token, quoted ("used in lieu of login credentials"; "software-as-a-service (SaaS), and AI-as-a-service(AIaaS)"). AML.M0028 AI Agent Tools Permissions Configuration, quoted. FIR mapping; no AI-specific figures claimed.

**FIR Risk Editorial Position:** "waiting on their fix is not a control," the temporary-limits action and the fix-by date are FIR's read, aligned with Mandiant's least-privilege guidance. Board rule: direction, no patch-speed mandate (the fix-by date is agreed with the vendor, not set as a board deadline).
