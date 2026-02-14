# FIR Risk Tuesday — Best of E21

**Original Publish Date:** October 1, 2024
**Source:** [ENISA Threat Landscape 2024](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024)
**Analysis:** FIR Risk Platform

---

# FIR Risk — Best of E21: Europe's Threat Map and the Seven Threats That Define the Landscape

![FIR Risk Best of E21 - ENISA Threat Landscape 2024](images/best-of-e21-enisa-threat-landscape-2024.png)

By FIR Risk Platform | Cybersecurity Risk Intelligence

---

## What You Need to Know

The European Union Agency for Cybersecurity (ENISA) published its annual Threat Landscape report covering **July 2023 through June 2024** — the most comprehensive assessment of cyber threats from a regulatory body that directly shapes EU cybersecurity policy. This isn't a vendor report — it's the intelligence assessment from the agency that writes the rules. When ENISA identifies a threat, regulatory frameworks like NIS2 follow.

The 2024 report identifies **seven prime cybersecurity threats**, maps them to **MITRE ATT&CK techniques**, aligns defensive recommendations to **ISO 27001:2022 and NIST CSF v2.0**, and provides sector-specific targeting data that reveals where attacks are concentrating across the EU. Public administration absorbs **19% of attacks**, transport **11%**, and finance **9%**.

What makes ENISA unique in the Best of collection is the regulatory lens. Every other report tells you what's happening. ENISA tells you what's happening — and what the EU is going to require you to do about it.

---

## The Seven Prime Threats

ENISA's threat taxonomy defines the categories that matter for EU cybersecurity policy:

| Rank | Threat | Trend |
|------|--------|-------|
| 1 | **Ransomware** | Persistent top threat — consecutive years |
| 2 | **Malware** | Information stealers essential to attack chains |
| 3 | **Social Engineering** | BEC sharp increase, AI-enhanced phishing |
| 4 | **Threats Against Data** | Data compromise increasing through 2024 |
| 5 | **Threats Against Availability (DoS)** | DDoS-for-hire accessible to unskilled users |
| 6 | **Information Manipulation and Interference** | AI-enabled, limited but evolving |
| 7 | **Supply Chain Attacks** | Software supply chain targeting accelerating |

Ransomware and threats against availability have ranked at the top for consecutive years — confirming the pattern documented across every major report in the Best of collection. The Verizon DBIR showed ransomware present in 44% of breaches. CrowdStrike documented 442% vishing surge and 79% malware-free intrusions. Microsoft confirmed 4,500 DDoS attacks per day. ENISA's ranking aligns precisely.

The inclusion of **Information Manipulation and Interference** as a prime threat — currently ranked seventh but flagged as evolving — connects directly to the Atlantic Council's IIA research and Microsoft's documentation of nation-state AI manipulation operations. ENISA is signaling that information warfare will climb the regulatory priority list.

> **INTEL [GLOBAL THREAT]:** ENISA's seven prime threats represent the EU's official threat taxonomy — the categories that will drive NIS2 enforcement, regulatory audits, and compliance frameworks. Organizations operating in or selling to EU markets should map their security programs against these seven categories. Gaps aren't just risk — they're potential compliance failures.

---

## Sector Targeting: Where Attacks Concentrate

ENISA's sector data reveals attack distribution across the EU:

| Sector | Share of Attacks |
|--------|-----------------|
| **Public administration** | 19% |
| **Transport** | 11% |
| **Finance** | 9% |
| **Other** | 61% (distributed across healthcare, energy, telecom, etc.) |

Public administration at 19% aligns with the ASD report's finding that 11% of incidents involved critical infrastructure, and with Forescout's 668% increase in critical infrastructure attacks since 2022. Government and public sector organizations remain disproportionately targeted — partly because they're high-value targets for espionage, partly because their security investments lag the private sector.

Transport at 11% reflects the sector's expanding digital attack surface — connected vehicles, logistics platforms, port management systems, and aviation infrastructure all present opportunities. Finance at 9% mirrors the MDDR's fraud-cybercrime convergence findings — financial services face both traditional cyber attacks and financial crime simultaneously.

> **INTEL [SECTOR ALERT]:** EU public administration absorbs 19% of cyber attacks — nearly double the next highest sector. Organizations providing services to government entities should expect heightened scrutiny under NIS2 and prepare for supply chain security assessments. Transport (11%) and finance (9%) organizations should similarly prepare for sector-specific regulatory requirements.

---

## The Techniques That Matter: LOTL and LOTS

ENISA highlights two technique categories that define the current threat landscape:

**Living Off the Land (LOTL)** — Attackers using legitimate tools already present in victim environments for defensive evasion. This is the same pattern CrowdStrike documented (79% malware-free intrusions), Mandiant confirmed (living-off-the-land pervasive), and ASD verified through Five Eyes intelligence (PRC pre-positioning in critical infrastructure using LOTL).

**Living Off Trusted Sites (LOTS)** — A newer evolution where attackers abuse trusted cloud services and legitimate web platforms to host malicious content, exfiltrate data, and establish command-and-control. By operating through services like Google Drive, Microsoft OneDrive, or Slack, attackers bypass security controls that whitelist these domains.

The expansion of LOTS into cloud environments represents the natural evolution of LOTL into the cloud era. As organizations migrate to cloud, attackers follow — using the same trusted infrastructure that businesses rely on.

> **INTEL [TECHNIQUE]:** ENISA identifies Living Off Trusted Sites (LOTS) as an expansion of the LOTL technique into cloud environments. Attackers are abusing legitimate cloud platforms for C2, exfiltration, and payload delivery — bypassing security controls that whitelist these services. Organizations should implement DLP and CASB policies that monitor for anomalous usage of trusted cloud services, not just block known-malicious domains.

---

## AI Threat Landscape: FraudGPT and State-Nexus LLM Usage

ENISA provides the European regulatory perspective on AI-enabled threats:

**State-nexus actors using LLMs** — Russian, North Korean, Iranian, and Chinese threat actors are employing ChatGPT and similar models for scripting assistance, phishing email generation, vulnerability research, and reconnaissance. ENISA notes the primary danger lies in **enhancing existing techniques for massive distribution of manipulated narratives** rather than creating fundamentally new attack types.

**FraudGPT and criminal AI tools** — Purpose-built AI tools designed for crafting scam communications, generating phishing lures, and automating social engineering. These tools lower the barrier to entry for financial crime — a finding that directly supports the MDDR's documentation of Phishing-as-a-Service and synthetic identity proliferation.

**Deepfake escalation** — A multinational corporation lost **over $25 million** when attackers used deepfake technology to impersonate senior executives on video calls. Face-swapping services exploiting stolen facial recognition data are expanding the deepfake threat beyond video to include biometric authentication bypass.

**Social engineering at scale** — 179 ChatGPT users were identified as targets of social engineering attacks. Fake AI services promoted through Facebook ads created additional attack vectors. The convergence of AI tools and social engineering is creating a self-reinforcing cycle.

> **INTEL [EMERGING RISK]:** ENISA documents FraudGPT and state-nexus LLM usage as active threats in the EU threat landscape. The $25M deepfake loss — executives impersonated on video calls — represents the maturation of AI-enabled social engineering from theoretical to operational. Organizations should implement out-of-band verification for high-value transactions and executive communications, and deploy deepfake detection capabilities for video conferencing.

---

## Malware-as-a-Service: The Supply Chain of Cybercrime

ENISA documents the rapid evolution of Malware-as-a-Service (MaaS) since mid-2023:

- **Information stealers** remain essential components of the attack chain — harvesting credentials, session tokens, and browser data that enable subsequent account takeover and lateral movement
- **MaaS platforms** provide subscription access to malware families, infrastructure, and victim management tools — mirroring the legitimate SaaS model
- **DDoS-for-hire** services have made availability attacks accessible to unskilled users — lowering the barrier from technical expertise to a payment method
- **Rapid evolution** of malware families and delivery techniques makes signature-based detection increasingly unreliable

The MaaS ecosystem connects to the MDDR's PhaaS findings and CrowdStrike's documentation of the eCrime ecosystem. The common pattern: cybercrime has industrialized. Professional service models, subscription pricing, customer support, and continuous development cycles characterize the criminal supply chain.

---

## Law Enforcement Impact: Operations Chronos and Endgame

ENISA highlights two significant law enforcement operations during the reporting period:

**Operation Chronos** — An international takedown operation targeting ransomware infrastructure, disrupting criminal operations and demonstrating that law enforcement can impose costs on ransomware operators.

**Operation Endgame** — A coordinated effort against the malware dropper ecosystem, targeting the infrastructure that delivers initial-stage malware to compromised systems.

These operations demonstrate that law enforcement is adapting to the industrialized cybercrime model — targeting infrastructure and services rather than individual actors. The impact is measurable but temporary — disrupted groups reconstitute, and the criminal service model means replacements emerge quickly.

---

## Threat Actor Landscape

ENISA categorizes threat actors into four groups:

| Actor Type | Primary Motivation |
|------------|-------------------|
| **State-nexus actors** | Espionage, destruction, pre-positioning |
| **Cybercrime actors / hacker-for-hire** | Financial gain (primary motivation) |
| **Private Sector Offensive Actors (PSOA)** | Commercial surveillance tools |
| **Hacktivists** | Ideological — disruption and attention |

The inclusion of **Private Sector Offensive Actors** is notable — this category covers commercial spyware vendors (NSO Group, Intellexa) and the "hack-for-hire" market that blurs the line between state and private operations. ENISA's recognition of PSOAs as a distinct threat category signals potential regulatory action targeting commercial surveillance tools in the EU.

Financial gain remains the primary motivation across all threat actors, with **disruption ranked second** — driven primarily by DDoS prevalence targeting operational downtime.

---

## Framework Alignment: MITRE, ISO, and NIST

What distinguishes ENISA from other threat reports is the explicit mapping to compliance frameworks:

- **MITRE ATT&CK** — All seven prime threats mapped to specific techniques and sub-techniques
- **ISO/IEC 27001:2022** — Security controls recommendations aligned to the international standard
- **NIST Cybersecurity Framework v2.0** — Defensive recommendations mapped to NIST CSF functions

This triple mapping is uniquely valuable for organizations navigating the NIS2 directive, DORA (financial sector), and other EU regulatory frameworks. ENISA isn't just telling you what threats exist — it's telling you which controls map to which threats across the frameworks regulators will audit against.

---

## What Organizations Should Actually Do

The ENISA Threat Landscape points to five priorities:

1. **Map your program to ENISA's seven threats** — Use the report's framework alignment to identify gaps between your current controls and the threats ENISA prioritizes. NIS2 enforcement is coming — compliance gaps found during incidents will be costly.

2. **Monitor for LOTS abuse** — Traditional security controls whitelist trusted cloud services. Implement CASB and DLP policies that detect anomalous usage of legitimate platforms for data exfiltration and C2.

3. **Prepare for AI-enabled social engineering** — Deepfakes cost one organization $25M. Implement out-of-band verification for executive communications and high-value transactions. Train employees on deepfake recognition.

4. **Address MaaS and DDoS-for-hire** — The barrier to entry for attacks continues to fall. Ensure DDoS mitigation is in place, credential monitoring covers information stealer output, and incident response plans account for commodity attacks.

5. **Align compliance and security** — ENISA's MITRE/ISO/NIST mapping provides a compliance Rosetta Stone. Use it to demonstrate security posture to auditors in the framework language they expect.

---

## What We're Watching

**NIS2 enforcement impact.** ENISA's threat priorities directly inform NIS2 implementation. As enforcement begins across EU member states, organizations will face regulatory consequences for gaps in these seven threat categories.

**LOTS technique evolution.** Cloud abuse for C2 and exfiltration is growing as organizations trust — and whitelist — cloud services. Detection requires behavioral analytics, not just domain reputation.

**PSOA regulatory action.** ENISA's recognition of commercial surveillance vendors as a distinct threat category could signal EU regulatory action targeting commercial spyware — potentially affecting procurement decisions for security tools with offensive capabilities.

**AI threat trajectory.** ENISA describes AI-enabled threats as "limited but evolving." The trajectory from FraudGPT to $25M deepfake losses suggests the evolution is accelerating faster than "limited" implies.

---

## The Bottom Line

ENISA's Threat Landscape 2024 is the regulatory authority's view of the threat landscape — and in the EU, the regulatory authority writes the rules. The seven prime threats aren't just intelligence categories — they're the framework against which NIS2 compliance will be measured.

Public administration at 19% of attacks. LOTL and LOTS techniques evading traditional defenses. FraudGPT and state-nexus AI deployment operational. MaaS industrializing cybercrime. $25 million lost to a single deepfake operation.

The report's unique value is the compliance bridge — MITRE ATT&CK, ISO 27001, and NIST CSF v2.0 mappings that connect threat intelligence directly to the frameworks regulators audit. For organizations operating in or selling to EU markets, ENISA isn't optional reading — it's the preview of your next audit.

---

Find all editions on [FIR Risk Tuesday](https://firriskadvisory.com/tuesday/) | [GitHub](https://github.com/stikman28/fir-risk-intelligence)

---

## LINKEDIN POST

Your firewall blocks known-malicious domains. Attackers are using Google Drive, OneDrive, and Slack instead.

ENISA's 2024 Threat Landscape — the EU's official cyber threat assessment — identifies seven prime threats and introduces a concept security teams need to understand:

Living Off Trusted Sites (LOTS) — abusing legitimate cloud services for C2, exfiltration, and payload delivery.

Seven prime threats:
→ Ransomware (persistent #1)
→ Malware (info stealers essential to attack chains)
→ Social Engineering (BEC sharp increase, AI-enhanced)
→ Threats Against Data (compromise increasing)
→ Denial of Service (DDoS-for-hire accessible to unskilled users)
→ Information Manipulation (AI-enabled, evolving)
→ Supply Chain Attacks (software supply chain accelerating)

Where attacks concentrate:
→ Public administration: 19%
→ Transport: 11%
→ Finance: 9%

The AI threat is operational:
→ FraudGPT crafting scam communications
→ State actors (Russia, China, NK, Iran) using LLMs for phishing and recon
→ $25M lost to a single deepfake impersonation of executives
→ 179 ChatGPT users targeted in social engineering attacks

What makes ENISA different from vendor reports: it maps every threat to MITRE ATT&CK, ISO 27001:2022, AND NIST CSF v2.0. When NIS2 enforcement begins, these are the categories auditors will measure against.

The regulatory authority's threat assessment IS the compliance preview.

Full analysis: [link]

Source: ENISA Threat Landscape 2024

#CyberSecurity #ENISA #ThreatIntelligence #NIS2 #CISO #AI #Ransomware #Compliance #EU

---

## NOTES

- Single edition: E21 (October 1, 2024)
- ENISA is the EU Agency for Cybersecurity — regulatory authority, not a vendor
- Key SEO terms: "ENISA threat landscape 2024", "EU cyber threats", "NIS2 compliance", "seven prime threats", "LOTS technique", "FraudGPT"
- "Europe's Threat Map" — positions as the EU regulatory perspective vs US-centric reports
- Unique lane in Best of collection — regulatory/compliance angle that no other edition covers
- LOTS (Living Off Trusted Sites) is the cloud evolution of LOTL — newer concept worth highlighting
- $25M deepfake loss is the most concrete AI-enabled financial impact across all Best of editions
- PSOA (Private Sector Offensive Actors) category is unique to ENISA — NSO Group, Intellexa
- Framework triple-mapping (MITRE + ISO + NIST) is uniquely valuable for compliance teams
- NIS2 connection makes this directly actionable for EU-operating organizations
- Connects to MDDR (PhaaS, DDoS), CrowdStrike (LOTL, malware-free), ASD (critical infra targeting), Atlantic Council (information manipulation)
- Operations Chronos and Endgame show law enforcement adapting to industrialized cybercrime
- Hero image: ENISA branding or EU cybersecurity visual
