# FIR Risk Tuesday — Best of E39

**Original Publish Date:** January 28, 2025
**Source:** [Forescout 2024 Global Threat Roundup](https://www.forescout.com/resources/2024-global-threat-roundup-report/)
**Analysis:** FIR Risk Platform

---

# FIR Risk — Best of E39: 900 Million Attacks and the List That Missed 73%

![FIR Risk Best of E39 - Forescout 2024 Global Threat Roundup](images/best-of-e39-forescout-global-threat-roundup-2024-2.png)

By FIR Risk Platform | Cybersecurity Risk Intelligence

---

## What You Need to Know

Forescout Technologies' 2024 Global Threat Roundup analyzed **900 million attacks** observed throughout the year — combining AI-driven analysis with human intelligence across IT, IoT, and OT environments. The dataset is massive. The findings are uncomfortable.

**Critical infrastructure attacks have increased 668% since 2022.** State-sponsored operations now account for **48% of all attacks**. Russia leads as the top attack origin at 16% of malicious traffic. And the finding that should keep every vulnerability management team up at night: **73% of actively exploited vulnerabilities were NOT in CISA's Known Exploited Vulnerabilities (KEV) catalog.**

If your patch prioritization strategy starts and ends with CISA KEV, you're missing nearly three-quarters of what attackers are actually using.

---

## The KEV Gap: 73% of Exploited Vulnerabilities Are Off the List

This is the report's most consequential finding. CISA's KEV catalog has become the de facto prioritization list for vulnerability management across government and enterprise. It's mandated for federal agencies. It's referenced in frameworks. It's the list security teams point to when boards ask "what are we patching first?"

**And it captures only 27% of what's being actively exploited in the wild.**

The 73% gap means that organizations relying exclusively on KEV for patch prioritization have a structural blind spot covering nearly three-quarters of real-world exploitation. These are vulnerabilities that are being weaponized — but haven't made the federal catalog.

This doesn't mean KEV is wrong. It means KEV alone is insufficient. The catalog was never designed to be comprehensive — it's a floor, not a ceiling. But when it becomes the only input to your vulnerability management program, the gap becomes a risk.

> **INTEL [EMERGING RISK]:** 73% of actively exploited vulnerabilities fall outside CISA's KEV catalog. Organizations using KEV as their sole prioritization input are systematically under-patching. Supplement KEV with threat intelligence feeds, exploit prediction scoring (EPSS), and vendor-specific advisories to close the gap between what's cataloged and what's weaponized.

---

## Critical Infrastructure Under Siege: 668% Since 2022

Attacks targeting critical infrastructure — energy, water, transportation, healthcare, manufacturing — have increased **668% since 2022**. This isn't a gradual trend. It's an acceleration that reflects a fundamental shift in attacker targeting.

The drivers are converging:

- **OT/IT convergence** is expanding the attack surface as operational technology networks connect to enterprise IT environments
- **IoT device proliferation** introduces thousands of unmanaged, often unpatched endpoints into critical environments
- **State-sponsored targeting** at 48% means nearly half of all attacks carry a geopolitical motivation — and critical infrastructure is the strategic target
- **Legacy systems** in OT environments often run decades-old software with no patch path

The Forescout data spans IT, IoT, and OT environments — giving it visibility into attack patterns that purely IT-focused reports miss. When a threat actor pivots from an IT network into an OT environment, most endpoint detection tools lose visibility. That's where the 668% lives — in the seams between managed and unmanaged infrastructure.

> **INTEL [THREAT ALERT]:** Critical infrastructure attacks have increased 668% since 2022, driven by OT/IT convergence, IoT proliferation, and state-sponsored targeting. Organizations operating in critical sectors should audit IT/OT network boundaries, inventory all connected IoT devices, and implement segmentation that limits lateral movement between enterprise and operational networks.

---

## The State-Sponsored Landscape: 48% and Rising

Nearly half of all observed attacks — **48%** — are now state-sponsored, correlating directly with geopolitical tensions. The nation-state breakdown reveals clear patterns:

| Origin | Share | Primary Focus |
|--------|-------|---------------|
| **Russia** | 16% of malicious traffic | Leading attack origin — critical infrastructure, espionage, disruption |
| **State-sponsored (total)** | 48% of all attacks | Intelligence collection, pre-positioning, strategic disruption |
| **Threat actor groups** | 800+ identified | Growing ecosystem of state and criminal operators |

The correlation between geopolitical events and cyber operations has moved from theoretical to documented. As tensions escalate, cyber operations intensify. The 48% figure means security teams aren't just defending against criminals — they're operating in a contested space where nearly half the adversary activity carries nation-state resources and sophistication.

Over **800 known threat actor groups** were identified — a number that reflects both the proliferation of state-sponsored programs and the growing ecosystem of contractors, proxy groups, and criminal organizations operating with state tolerance or direction.

---

## Attack Vectors: Web Apps, Remote Management, and Default Credentials

Forescout's data reveals where attackers focus their efforts:

| Vector | Share |
|--------|-------|
| **Web application attacks** | 41% of all attacks |
| **Remote management protocols** | 33% of all attacks |
| **Brute force with generic credentials** | 95% use "admin," "root," or similar defaults |

The 95% generic credential finding is both alarming and actionable. Ninety-five percent of brute-force attempts use default usernames and passwords — "admin," "root," "password." This means the vast majority of brute-force attacks succeed only against systems where nobody changed the defaults.

For IoT and OT devices, this is epidemic. Routers, cameras, industrial controllers, and network appliances ship with default credentials that are documented in public manuals. Many are never changed. Some can't be changed. When Forescout observes 900 million attacks and 95% of brute force uses generic credentials, the implied message is clear: a significant number of those attacks are succeeding.

---

## Operational Relay Boxes: The Infrastructure You Can't See

The report highlights **Operational Relay Boxes (ORBs)** — a relatively novel concept in threat intelligence. ORBs are layered proxy networks that threat actors use to mask the true origin of their operations.

Unlike traditional VPNs or single-hop proxies, ORBs chain multiple compromised devices — often IoT devices, routers, and cloud instances — into multi-layered relay networks. Traffic bounces through several nodes before reaching the target, making attribution and blocking extremely difficult.

ORBs represent the infrastructure layer of advanced persistent threats. When a state-sponsored actor routes operations through a chain of compromised home routers in five countries, blocking any single IP is meaningless. The infrastructure is disposable, distributed, and constantly rotating.

> **INTEL [TECHNIQUE]:** Operational Relay Boxes (ORBs) use layered proxying through compromised IoT devices and cloud instances to mask attack origins. Traditional IP-based blocking is ineffective against ORB infrastructure. Organizations should invest in behavioral analysis that identifies anomalous traffic patterns rather than relying on IP reputation alone.

---

## New Malware Families: The 2024 Crop

Forescout documented a surge in new malware families, including:

- **Lumma** — Infostealer targeting credentials, browser data, and cryptocurrency wallets. Rapidly growing market share in the stealer ecosystem.
- **Gafgyt** — IoT botnet malware targeting Linux-based devices. Focuses on routers and IoT appliances for DDoS and crypto-mining.
- **Healer** — Emerging threat with anti-analysis capabilities designed to evade sandbox detection.
- **Credential Flusher** — Purpose-built for harvesting stored credentials from browsers and credential managers.

The common thread: these families target the seams in security — credentials stored in browsers, unmanaged IoT devices, and the gaps between what endpoint protection covers and what it doesn't.

**FIR Risk Platform MITRE ATT&CK Analysis:**
- Initial Access: T1190 (Exploit Public-Facing Application) — 41% web app attacks
- Initial Access: T1078 (Valid Accounts) — default/stolen credentials
- Initial Access: T1110 (Brute Force) — 95% generic credentials
- Persistence: T1133 (External Remote Services) — 33% remote management protocols
- Defense Evasion: T1090 (Proxy) — Operational Relay Boxes
- Collection: T1555 (Credentials from Password Stores) — Lumma, Credential Flusher
- Impact: T1498 (Network Denial of Service) — Gafgyt botnet

---

## What Organizations Should Actually Do

The Forescout data points to five priorities:

1. **Go beyond CISA KEV for patch prioritization** — KEV captures 27% of what's exploited. Supplement with EPSS scoring, threat intelligence feeds, and vendor advisories. Build a prioritization model that reflects your actual attack surface, not just the federal catalog.

2. **Audit and segment OT/IoT environments** — 668% critical infrastructure growth means the IT/OT boundary is the new front line. Inventory every connected device. Segment aggressively. Monitor traffic crossing IT/OT boundaries for anomalies.

3. **Eliminate default credentials** — 95% of brute force uses "admin" and "root." Conduct a sweep of every device — routers, cameras, controllers, appliances — and change defaults. Where credentials can't be changed, isolate the device behind network segmentation.

4. **Implement zero-trust architecture** — With 48% state-sponsored activity and ORBs masking attack origins, perimeter-based trust is meaningless. Verify every connection. Authenticate every session. Trust nothing by default.

5. **Detect behaviors, not just indicators** — ORBs, living-off-the-land, and rotating infrastructure make IOC-based detection unreliable. Invest in behavioral analytics that identify anomalous patterns regardless of the source IP or tool used.

---

## What We're Watching

**The KEV gap.** If 73% of exploited vulnerabilities aren't cataloged, the gap between what's mandated and what's weaponized will continue to grow as disclosure volumes increase. This finding deserves more industry attention.

**OT/IoT targeting acceleration.** 668% since 2022 with no sign of slowing. As IT/OT convergence continues, the attack surface expands faster than security budgets.

**ORB network evolution.** Layered proxy infrastructure makes attribution increasingly difficult and renders IP-based blocking obsolete. Expect ORBs to become standard operational infrastructure for state-sponsored groups.

**Infostealer market maturation.** Lumma and Credential Flusher represent a growing ecosystem of purpose-built credential theft tools feeding the access broker economy documented in the CrowdStrike and Mandiant reports.

---

## The Bottom Line

Forescout's 900 million observed attacks reveal a threat landscape that most security programs aren't fully seeing. When 73% of exploited vulnerabilities aren't on the list everyone uses for prioritization, when critical infrastructure attacks have surged 668%, and when 95% of brute-force attempts use credentials that should have been changed on day one — the gaps aren't technical. They're operational.

The report's most important contribution is making visible what IT-focused reports miss: the IoT devices nobody inventoried, the OT networks nobody segmented, the default credentials nobody changed, and the vulnerabilities nobody patched because they weren't on the list.

Nine hundred million attacks. The ones that succeed aren't the sophisticated ones. They're the ones that find the gaps we already know about.

---

Find all editions on [FIR Risk Tuesday](https://firriskadvisory.com/tuesday/) | [GitHub](https://github.com/stikman28/fir-risk-intelligence)

---

## LINKEDIN POST

Forescout analyzed 900 million attacks in 2024. The findings challenge some fundamental assumptions.

The headline: 73% of actively exploited vulnerabilities were NOT in CISA's KEV catalog.

If your patch prioritization starts and ends with KEV, you're missing nearly three-quarters of what attackers are actually using.

The full picture:
→ Critical infrastructure attacks up 668% since 2022
→ State-sponsored operations now 48% of all attacks
→ Russia leads attack origin at 16% of malicious traffic
→ 41% target web applications, 33% target remote management
→ 95% of brute-force attempts use "admin" or "root"
→ 800+ threat actor groups identified

Two findings that don't get enough attention:
1. Operational Relay Boxes (ORBs) — layered proxy networks through compromised IoT devices that make IP blocking and attribution nearly impossible
2. New infostealer families (Lumma, Credential Flusher) purpose-built for browser credential theft

Five priorities:
1. Supplement KEV with EPSS and threat intel feeds
2. Audit and segment OT/IoT environments
3. Eliminate default credentials (95% is inexcusable)
4. Implement zero trust
5. Detect behaviors, not just indicators

Full analysis: [link]

Source: Forescout 2024 Global Threat Roundup

#CyberSecurity #ThreatIntelligence #CISO #CriticalInfrastructure #OTSecurity #IoT #Vulnerabilities

---

## NOTES

- Single edition: E39 (January 28, 2025)
- Forescout's unique value: IT + IoT + OT visibility — fills a gap the big three don't cover
- Key SEO terms: "Forescout threat report 2024", "critical infrastructure attacks", "CISA KEV gap", "OT security", "IoT threats"
- "The List That Missed 73%" as title hook — contrarian finding that challenges conventional wisdom
- 668% critical infrastructure stat is board-level — gets cited in risk committee presentations
- 95% generic credentials is embarrassingly actionable — "change the defaults" is the simplest recommendation with highest impact
- ORBs are a forward-looking concept most practitioners haven't encountered yet
- Connects to CrowdStrike (access broker economy feeding credential theft), M-Trends (credential theft > phishing), DBIR (third-party risk)
- Lumma infostealer appears in both Forescout and Red Canary (E57) reports — cross-validation
- MITRE ATT&CK: T1190, T1078, T1110, T1133, T1090, T1555, T1498
- Hero image: Forescout branding or critical infrastructure / OT visual
