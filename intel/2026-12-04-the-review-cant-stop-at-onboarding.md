# FIR Risk INTEL-67 — The Review Can't Stop at Onboarding

**Type:** `TECHNIQUE`
**Date:** December 4, 2026
**Platform Source:** FIR SIGNALS 2026, Signal 03 "Half your attack surface belongs to someone else." (IBM X-Force Threat Intelligence Index 2026, Mandiant M-Trends 2026, MITRE ATLAS)

---

## The INTEL

**MITRE describes an attack built to get past the first review: publish something legitimate, gain users, then push a malicious update. Vendors you rely on, including your AI tools, need checking after they are approved, not only before.**

What the sources show:

- **The update is the way in.** IBM X-Force: in open-source registries such as npm and PyPI, "a single compromised account can propagate malicious updates across thousands of projects." Attackers are "targeting the environments where software is built," including GitHub, GitLab and npm, "rather than traditional endpoints."
- **AI tools follow the same pattern.** MITRE ATLAS, its catalog of attacks on AI systems, calls it a rug pull: "More scrutiny is often placed on a supply chain dependency when it is first being considered," so a later malicious update "may allow adversaries to bypass these defenses." ATLAS also notes that "Adversaries have successfully used a poisoned MCP server to exfiltrate private user data."
- **Mandiant's prescription.** A third-party risk program "to vet SaaS vendors before onboarding and on an ongoing basis." Mandiant adds that organizations "often overlook SaaS applications in traditional asset management."

---

## Why It Matters

An AI assistant connected to your email, a connector that reads your files, or an agent tool that can run actions holds the same kind of access as a software vendor. ATLAS says compromising an agent tool can give attackers "broad accesses and permissions on the victim's system." These tools also change often, through updates you may not see.

If they sit outside your third-party program, nobody reassesses them when they change. If your vendor reviews happen only at the start, the risk that arrives later goes unexamined.

**Our read:** the SIGNALS decision for Signal 03 is a living list of who holds access to us. "Living" means reassessed, not just listed, and AI tools are on it.

---

## What To Do — One Key Action

**Make sure every vendor you rely on, including AI tools and connectors, is inside your third-party risk management program: assessed before onboarding, with risk assessments and vendor reviews updated on a regular schedule, not only at onboarding.**

---

## MITRE ATT&CK

- **T1195 — Supply Chain Compromise** (1.7% of Mandiant's 2025 investigations), including compromised software dependencies (T1195.001) and compromised software (T1195.002): a vendor's update used to reach you
- MITRE mitigations listed in SIGNALS: M1018 User Account Management · M1036 Account Use Policies · M1021 Restrict Web-Based Content

**MITRE ATLAS** (attacks on AI systems, v5.6)

- **AML.T0109 — AI Supply Chain Rug Pull:** attackers "publish legitimate AI components or software, gain user adoption, then push an update with a malicious variant"
- **AML.T0010.005 — AI Agent Tool:** compromising a tool can give "broad accesses and permissions," and in that environment "safeguards are often not in place"
- ATLAS mitigations: AML.M0023 AI Bill of Materials (a listing that helps "enable rapid response to reported vulnerabilities") · AML.M0014 Verify AI Artifacts ("Verify the cryptographic checksum of all AI artifacts")

---

## Learn More

- [FIR SIGNALS 2026](/reports/signals-2026/) — Signal 03, plus the MITRE ATT&CK appendix in the PDF
- [IBM X-Force Threat Intelligence Index 2026](https://www.ibm.com/reports/threat-intelligence) — Primary source
- [Mandiant M-Trends 2026](https://cloud.google.com/security/resources/m-trends) — Primary source
- [MITRE ATLAS](https://atlas.mitre.org/) — Adversarial threat landscape for AI systems
- [FIR Risk INTEL-54 — Your Technology Suppliers Now Call AI Agents Insiders](/intel/intel-54-agents-as-insiders/) — How suppliers describe agent risk

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
The review can't stop at onboarding.

MITRE describes an attack built to get past the first review: publish something legitimate, gain users, then push a malicious update. Its AI catalog calls it a rug pull, noting that "more scrutiny is often placed on a supply chain dependency when it is first being considered."

IBM X-Force sees the same pattern in software: one compromised account in a package registry "can propagate malicious updates across thousands of projects."

Your AI assistants, connectors and agent tools are vendors too. They hold access to your email, files and systems, and they change through updates.

Mandiant's advice: vet vendors "before onboarding and on an ongoing basis."

The action: make sure every vendor you rely on, AI tools and connectors included, is inside your third-party risk management program, with risk assessments and vendor reviews updated on a regular schedule, not only at onboarding.

FIR Risk INTEL-67 · SIGNALS 2026, Signal 03

#ThirdPartyRisk #AISecurity #SupplyChainSecurity #CISO #RiskManagement
```

## X POST

Attackers publish something legitimate, gain users, then push a malicious update. MITRE ATLAS calls it a rug pull.

Your AI tools and connectors are vendors too. Put them in your third-party risk program, with reviews that continue after onboarding.

Full INTEL → FIR Risk INTEL-67

#ThirdPartyRisk #AISecurity

---

## SOURCE DATA

**Editorial Frame:**
SIGNALS INTEL series, Signal 03, INTEL 3 of 3, the AI side. Bruce 11/20: "be sure vendors you rely on, are under 3rd party risk management processes, including risk assessment updates and vendor reviews." Framing deliberately avoids claiming how often companies review vendors: no source measures that (Bruce asked 11/20 whether "vendor review happens once, at onboarding" was supported; it was not, so it was dropped). The support used is ATLAS's description of attacker logic (rug pull) and Mandiant's recommendation (before onboarding and ongoing). Distinct from INTEL-25/31 (inventory, contract MFA), INTEL-38 (token revocation) and INTEL-54 (suppliers' AI-agent disclosures). DBIR shadow-AI figures (45% / 67%) held back for the Signal 05 INTEL.

**Fact-Check Notes (verified Nov 20, 2026 against SIGNALS source texts; page = printed page):**
- X-Force 2026 p12: "attackers are targeting the environments where software is built—and increasingly the SaaS ecosystems that support those workflows—rather than traditional endpoints"; "IBM X-Force has been tracking an increase in attacks against developer platforms such as GitHub, GitLab and npm"; "Open-source registries such as npm and PyPI packages remain high-risk due to their scale and decentralized governance—a single compromised account can propagate malicious updates across thousands of projects."
- M-Trends 2026 p76: "This begins with a robust Third-Party Risk Management program to vet SaaS vendors before onboarding and on an ongoing basis"; "Organizations often overlook SaaS applications in traditional asset management, creating significant visibility gaps."
- SIGNALS appendix p16 (Signal 03): T1195 1.7%; mitigations M1018, M1032, M1036, M1021 (selection). Sub-techniques T1195.001/.002 named from ATT&CK, no frequency claimed for them.

**MITRE ATLAS (v5.6.0, atlas-data dist/ATLAS.yaml, checked Nov 20, 2026):** AML.T0109 AI Supply Chain Rug Pull, quoted ("publish legitimate AI components or software, gain user adoption, then push an update with a malicious variant"; "More scrutiny is often placed on a supply chain dependency when it is first being considered for inclusion in an AI system. Performing a rug pull may allow adversaries to bypass these defenses"). AML.T0010.005 AI Agent Tool, quoted ("broad accesses and permissions on the victim's system"; "Adversaries have successfully used a poisoned MCP server to exfiltrate private user data"; "safeguards are often not in place"). AML.M0023 AI Bill of Materials and AML.M0014 Verify AI Artifacts, quoted. ATLAS's "thousands of MCP servers" count not used. FIR mapping; no AI-specific figures claimed.

**FIR Risk Editorial Position:** "AI tools are vendors too," the examples of AI tool access, "living means reassessed" and the action are FIR's read, built on Bruce's direction and Mandiant's recommendation.
