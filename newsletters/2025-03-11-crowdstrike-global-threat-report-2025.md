# FIR Risk Tuesday — Best of E45

**Original Publish Date:** March 11, 2025
**Source:** [CrowdStrike 2025 Global Threat Report](https://www.crowdstrike.com/global-threat-report/)
**Analysis:** FIR Risk Platform

---

# FIR Risk — Best of E45: 51 Seconds to Breakout

![FIR Risk Best of E45 - CrowdStrike 2025 Global Threat Report](images/best-of-e45-crowdstrike-global-threat-2025.png)

By FIR Risk Platform | Cybersecurity Risk Intelligence

---

## What You Need to Know

CrowdStrike's 2025 Global Threat Report delivers the most visceral metric in cybersecurity: **breakout time — the speed at which attackers move laterally after initial access — now averages just 48 minutes.** The fastest observed breakout? **51 seconds.**

That's less time than it takes most security teams to triage an alert.

But speed is only half the story. **79% of attacks are now malware-free**, relying on stolen credentials, legitimate tools, and hands-on-keyboard techniques that bypass traditional endpoint protection. Voice phishing (vishing) surged **442%**. The access broker economy expanded nearly **50%**. And China-nexus cyber espionage activity spiked **150%**.

This report doesn't describe a future threat landscape. It describes the one you're operating in right now.

---

## The Speed Problem: 48 Minutes to Own Your Network

CrowdStrike's breakout time metric has become the industry's benchmark for attacker velocity — and it's accelerating:

| Metric | Value |
|--------|-------|
| **Average breakout time** | 48 minutes |
| **Fastest observed breakout** | 51 seconds |
| **Malware-free intrusions** | 79% of all attacks |
| **Vishing increase** | 442% YoY |
| **Access broker growth** | ~50% expansion |

The 48-minute average means that once an attacker gains initial access, security teams have less than an hour before the intrusion spreads beyond the initial foothold. At 51 seconds, the fastest adversaries are moving laterally before most SIEM alerts even fire.

This is the "1-10-60" challenge that CrowdStrike has been tracking for years — detect in 1 minute, investigate in 10, contain in 60. At current attacker speeds, most organizations can't meet any of these benchmarks.

> **INTEL [GLOBAL THREAT]:** The 48-minute average breakout time — with a floor of 51 seconds — means traditional incident response timelines are obsolete. Organizations relying on manual triage and human-speed response are structurally unable to contain fast-moving adversaries. Automated detection and response capabilities aren't a luxury — they're the minimum viable defense.

---

## 79% Malware-Free: The Death of Signature-Based Defense

Nearly four out of five intrusions observed by CrowdStrike involved **no malware at all**. Attackers are using:

- **Stolen credentials** to authenticate as legitimate users
- **Living-off-the-land techniques** with native OS tools (PowerShell, WMI, RDP)
- **Hands-on-keyboard activity** that mimics normal administrative behavior
- **Legitimate remote access tools** for command and control

This is the fundamental challenge: when the attack looks like normal IT operations, signature-based detection is blind. Antivirus doesn't trigger. Firewall rules don't fire. The attacker is already inside, using your own tools, authenticated with valid credentials.

The 79% figure should force a question in every security program: **what percentage of your detection capability relies on identifying known malware?** If the answer is "most of it," you're missing four out of five attacks.

> **INTEL [EMERGING RISK]:** With 79% of intrusions malware-free, organizations still anchored to signature-based detection are operating with a structural blind spot covering the majority of real-world attacks. The shift to behavioral detection, identity analytics, and threat hunting is no longer aspirational — it's the baseline requirement.

---

## The Vishing Explosion: 442% and Climbing

Voice phishing — vishing — surged **442%** year-over-year, making it one of the fastest-growing attack vectors in CrowdStrike's dataset.

The technique works because it exploits a gap in most security programs: voice calls aren't monitored, recorded, or analyzed the way email is. An attacker calls an employee, impersonates IT support, and walks them through "troubleshooting steps" that actually install remote access tools or harvest credentials.

Combined with AI-generated voice cloning and deepfake technology, vishing is evolving from a crude social engineering tactic into a sophisticated, scalable attack vector. When the voice on the phone sounds exactly like your IT director, the usual red flags disappear.

The access broker economy's **~50% expansion** feeds directly into this. More stolen credentials mean more convincing pretexts for vishing calls — attackers already know the target's name, role, systems, and sometimes even their manager's name.

---

## China's 150% Surge

China-nexus cyber espionage activity increased **150%** — the largest single-year jump CrowdStrike has documented. Key characteristics:

- **Targeted sectors:** Technology, telecommunications, government, defense
- **Operational tempo:** Multiple concurrent campaigns across geographies
- **Tradecraft:** Zero-day exploitation of edge devices, supply chain compromise, and long-dwell espionage operations
- **Sophistication:** Custom tooling, operational security improvements, and reduced forensic footprint

This acceleration mirrors the geopolitical tension cycle. As strategic competition intensifies, cyber espionage serves as both intelligence collection and pre-positioning for potential future conflict. The 150% increase isn't a spike — it's likely a new baseline.

> **INTEL [THREAT ALERT]:** China-nexus cyber espionage surged 150% with particular focus on technology and telecommunications. Organizations in these sectors — and their supply chains — should conduct threat hunts specifically for Chinese APT indicators, review network segmentation around sensitive IP, and assume that espionage-motivated adversaries are already present in environments they haven't actively searched.

---

## Cloud: Valid Accounts Are the New Perimeter

**35% of cloud security incidents** involved abuse of valid accounts — attackers using legitimate credentials to access cloud environments without triggering traditional security controls.

The cloud attack surface is different from on-premises. There's no network perimeter to breach. If an attacker has valid credentials — from infostealers, phishing, or purchased from access brokers — they authenticate directly into cloud workloads, storage, and administrative consoles.

Cloud misconfigurations, overprivileged service accounts, and the absence of cloud-native detection capabilities compound the problem. Many organizations have extended their on-premises security models to the cloud without recognizing that the threat model is fundamentally different.

**FIR Risk Platform MITRE ATT&CK Analysis:**
- Initial Access: T1190 (Exploit Public-Facing Application) — zero-day exploitation
- Initial Access: T1078 (Valid Accounts) — 35% of cloud incidents
- Initial Access: T1566 (Phishing) — including vishing at 442% growth
- Execution: T1059 (Command and Scripting Interpreter) — living off the land
- Lateral Movement: T1021 (Remote Services) — 48-minute breakout
- Defense Evasion: T1070 (Indicator Removal) — malware-free at 79%
- Resource Development: T1583 (Acquire Infrastructure) — access broker economy

---

## What Organizations Should Actually Do

CrowdStrike's data points to five priorities:

1. **Deploy automated detection and response** — At 48-minute average breakout (51 seconds at the floor), human-speed response isn't fast enough. Invest in automated containment that can isolate compromised endpoints and revoke credentials in seconds, not hours.

2. **Shift from signature to behavioral detection** — 79% malware-free means signature-based tools miss the majority of attacks. Implement identity threat detection, behavioral analytics, and proactive threat hunting.

3. **Defend against vishing** — 442% growth demands a response. Train employees specifically on voice-based social engineering. Implement callback verification procedures for any request to install software or share credentials by phone.

4. **Secure cloud identity** — 35% of cloud incidents start with valid accounts. Enforce least-privilege access, implement cloud-native detection, and monitor for anomalous authentication patterns across all cloud services.

5. **Assume nation-state targeting** — China's 150% surge means espionage isn't limited to defense contractors. Technology, telecom, and their supply chains are active targets. Conduct regular threat hunts for APT indicators.

---

## What We're Watching

**Breakout time compression.** 48 minutes is the average — but 51 seconds is the floor. As automation tools become more available to attackers, expect the average to continue dropping.

**Vishing + AI voice cloning.** 442% growth before AI-generated voice deepfakes go mainstream. The next CrowdStrike report may show this number as the beginning of the curve.

**Access broker industrialization.** 50% growth in one year. The initial access economy is maturing into a professional supply chain — with specialization, pricing tiers, and guarantees.

**China pre-positioning.** 150% espionage growth alongside increased targeting of telecom and technology infrastructure raises questions about whether the objective is intelligence collection alone — or preparation for potential future disruption.

---

## The Bottom Line

CrowdStrike's 2025 Global Threat Report captures a threat landscape that has moved beyond what traditional security architectures can handle. When the fastest attackers break out in 51 seconds, 79% of attacks carry no malware, and voice phishing is up 442%, the defensive playbook from even two years ago is obsolete.

The report's implicit message is clear: speed is the variable that determines outcomes. Organizations that can detect in minutes and contain automatically will survive. Those still relying on next-day SOC triage and weekly vulnerability scans will not.

Forty-eight minutes. That's your window. What can your security program do in 48 minutes?

---

Find all editions on [FIR Risk Tuesday](https://firriskadvisory.com/tuesday/) | [GitHub](https://github.com/stikman28/fir-risk-intelligence)

---

## LINKEDIN POST

CrowdStrike's 2025 Global Threat Report drops the most visceral metric in cybersecurity:

Breakout time — how fast attackers move laterally — now averages 48 minutes. The fastest? 51 seconds.

The full picture:
→ 79% of attacks are malware-free — no signatures to detect
→ Vishing surged 442% — voice phishing is the fastest-growing vector
→ Access broker economy expanded ~50% — buying access is easier than earning it
→ China-nexus espionage spiked 150% — the largest single-year jump documented
→ 35% of cloud incidents start with valid account abuse

When 4 out of 5 attacks carry no malware, signature-based detection is structurally blind.

When the fastest breakout is 51 seconds, human-speed response is structurally insufficient.

Five priorities from the data:
1. Automate detection and containment (48 minutes is the ceiling, not the floor)
2. Shift from signatures to behavioral detection
3. Train specifically for vishing (442% growth demands a response)
4. Secure cloud identity (valid accounts are the new perimeter)
5. Hunt for nation-state indicators (150% China surge)

The question isn't whether your organization will be tested. It's whether you can respond in 48 minutes.

Full analysis: [link]

Source: CrowdStrike 2025 Global Threat Report

#CyberSecurity #CrowdStrike #ThreatIntelligence #CISO #Ransomware #CloudSecurity #NationState

---

## NOTES

- Single edition: E45 (March 11, 2025)
- CrowdStrike GTR is one of the "big three" annual reports alongside Verizon DBIR and Mandiant M-Trends
- Key SEO terms: "CrowdStrike 2025 Global Threat Report", "breakout time", "malware-free attacks", "vishing", "China cyber espionage"
- "51 Seconds to Breakout" as title — the most visceral stat in the report
- 442% vishing surge is the standout novel finding — most other reports don't track this
- 79% malware-free reinforces the shift from signature to behavioral detection (connects to M-Trends living-off-the-land)
- China 150% surge connects to E78 (CERT-EU Salt Typhoon) — persistent theme across reports
- Access broker economy growth (~50%) connects to M-Trends stolen credentials > phishing finding
- Cloud valid accounts (35%) connects to multiple other editions on cloud security
- MITRE ATT&CK: T1190, T1078, T1566, T1059, T1021, T1070, T1583
- Hero image: CrowdStrike branding / speed/velocity visual
