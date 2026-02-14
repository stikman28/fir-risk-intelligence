# FIR Risk Tuesday — Best of E52

**Original Publish Date:** April 29, 2025
**Source:** [Mandiant M-Trends 2025](https://cloud.google.com/security/resources/m-trends)
**Analysis:** FIR Risk Platform

---

# FIR Risk — Best of E52: 450,000 Hours on the Front Lines

![FIR Risk Best of E52 - Mandiant M-Trends 2025](images/best-of-e52-mandiant-m-trends-2025.png)

By FIR Risk Platform | Cybersecurity Risk Intelligence

---

## What You Need to Know

Mandiant's M-Trends 2025 report distills findings from **over 450,000 hours of incident response engagements** conducted globally. If the Verizon DBIR is the census of the breach landscape, M-Trends is the field report — written by the teams who show up after the breach and work the cases.

This year's findings reveal a threat landscape where **exploits dominate initial access at 33%**, stolen credentials have surpassed phishing as an entry vector, and North Korean operatives are literally getting hired by the companies they're targeting. Dwell time has dropped to 11 days — but that's not because defenders are faster. It's because attackers are moving to extortion, which announces itself.

These are the trends executives can't afford to ignore.

---

## How Attackers Get In: The Initial Access Breakdown

M-Trends maps exactly how adversaries breach organizations, and the 2025 data shows a clear hierarchy:

| Vector | Share | Trend |
|--------|-------|-------|
| **Exploits** | 33% | Still #1 — unpatched vulnerabilities remain the top door |
| **Stolen credentials** | 16% | Surpassed phishing — infostealers are fueling this |
| **Phishing** | 14% | Now #3 — includes Adversary-in-the-Middle (AiTM) variants |
| **North Korean IT workers** | 5% | Fraudulent employees gaining insider access |
| **Brute force** | Significant | Driving ransomware intrusions specifically |

The stolen credentials finding is the one to watch. At 16%, credential theft has overtaken phishing (14%) as the second most common initial access vector. This reflects the explosion of infostealer malware — tools like LummaC2 and Raccoon that harvest credentials at scale from compromised endpoints and sell them on dark web marketplaces.

Phishing hasn't gone away — it's evolved. Adversary-in-the-Middle (AiTM) attacks now intercept MFA tokens in real time, turning what organizations thought was their strongest defense into a bypassed control.

> **INTEL [GLOBAL THREAT]:** Stolen credentials surpassing phishing as an initial access vector signals a structural shift. Attackers increasingly buy access rather than earn it through social engineering. Organizations should monitor dark web credential markets, deploy endpoint detection for infostealer families, and assume that username/password combinations alone — even with basic MFA — are insufficient.

---

## The North Korean Insider Problem

Five percent of attack vectors now involve **North Korean IT workers who get hired as legitimate employees** at target organizations. This isn't espionage through hacking — it's espionage through HR.

These operatives use fraudulent identities, pass technical interviews, and secure remote employment at Western companies. Once inside, they have legitimate credentials, VPN access, and the trust of their teams. They're not breaking in. They're being invited in.

The scheme serves dual purposes: generating revenue for the DPRK regime and providing persistent insider access to corporate networks and intellectual property. It's social engineering at the organizational level — not targeting an employee, but becoming one.

> **INTEL [TECHNIQUE]:** North Korean fraudulent employment operations represent a novel insider threat that bypasses traditional perimeter defenses entirely. Organizations should strengthen identity verification in hiring processes, validate employment history through independent channels, and implement behavioral analytics for remote employees with access to sensitive systems.

---

## The Dwell Time Paradox

The headline metric looks good: **median global dwell time has dropped to 11 days.** Faster detection, right?

Not exactly. The drop is driven largely by the rise of ransomware and extortion — attacks that announce themselves. When an attacker encrypts your systems and drops a ransom note, dwell time drops to near-zero by design. **14% of breaches are now discovered because the attacker tells you** via ransom notification.

The real detection story is in the split:

| Detection Method | Share |
|-----------------|-------|
| **External notification** | 57% — someone else tells you |
| **Ransom/extortion notice** | 14% — the attacker tells you |
| **Internal detection** | 29% — you find it yourself |

When **57% of breaches are detected externally** — by law enforcement, partners, or third parties — it means most organizations still aren't finding intrusions on their own. The 11-day median is an output metric, not a capability metric.

> **INTEL [INDUSTRY PATTERN]:** The 11-day median dwell time masks a detection gap: 57% of breaches are found externally and 14% by the attackers themselves. Only 29% are detected internally. Organizations citing improved dwell time as evidence of security maturity should examine whether the improvement reflects actual detection capability or simply faster attacker monetization.

---

## Ransomware and the Extortion Evolution

Ransomware appeared in **21% of all M-Trends investigations**, with brute-force attacks serving as a primary entry point. But the data reveals a more nuanced picture:

- **Data theft** occurred in **37% of investigations** — nearly double the ransomware rate
- **Multifaceted extortion** (data theft + encryption combined) appeared in **6% of cases**
- Attackers are increasingly stealing data without deploying ransomware at all

This is the extortion evolution: why encrypt systems (which is noisy, detectable, and often recoverable from backups) when you can quietly steal data and threaten to publish it? The economics favor theft over encryption — lower operational risk, fewer detection triggers, and victims can't recover stolen data the way they can restore encrypted files.

---

## Living Off the Land: Your Tools Are Their Tools

Mandiant continues to document extensive use of **"living off the land" techniques** — attackers using legitimate tools already present in the environment. PowerShell, WMI, RDP, PsExec, and native OS utilities serve as both administrative tools and attack infrastructure.

This is why M-Trends data shows such a gap between internal and external detection. Traditional security tools are built to flag known malicious software. When the attacker uses the same tools your IT team uses daily, the signal disappears into the noise.

**FIR Risk Platform MITRE ATT&CK Analysis:**
- Initial Access: T1190 (Exploit Public-Facing Application) — 33% of intrusions
- Initial Access: T1078 (Valid Accounts) — stolen credentials at 16%
- Initial Access: T1566 (Phishing) — including AiTM variants
- Execution: T1059 (Command and Scripting Interpreter) — living off the land
- Lateral Movement: T1021 (Remote Services) — RDP, PsExec abuse
- Impact: T1486 (Data Encrypted for Impact) — ransomware at 21%
- Exfiltration: T1041 (Exfiltration Over C2 Channel) — data theft at 37%

---

## Cloud and SaaS: The Expanding Attack Surface

M-Trends highlights **cloud environments and SaaS platforms** as increasingly targeted — and often poorly defended. Weak credentials, misconfigured identity providers, and overprivileged service accounts give attackers lateral movement paths that don't touch traditional network monitoring.

Unsecured data repositories — SharePoint, GitHub, cloud storage buckets — continue to be low-hanging fruit. When organizations migrate to the cloud without migrating their security posture, they're not modernizing — they're expanding the attack surface.

---

## What Organizations Should Actually Do

The M-Trends data points to five priorities:

1. **Patch what matters, fast** — Exploits lead at 33%. Prioritize edge devices, VPNs, and internet-facing infrastructure. The window between disclosure and exploitation is shrinking.

2. **Treat credentials as a primary attack vector** — Stolen credentials at 16% means infostealer defense is now as important as phishing defense. Deploy endpoint detection for credential harvesting tools, monitor dark web marketplaces, and implement phishing-resistant MFA (FIDO2/WebAuthn).

3. **Verify your people** — North Korean IT worker infiltration at 5% means hiring processes are now a security control. Strengthen identity verification, validate employment history independently, and monitor remote worker behavior.

4. **Build detection that finds attackers, not just malware** — With 57% external detection and pervasive living-off-the-land, organizations need behavioral analytics and threat hunting capabilities that identify anomalous use of legitimate tools.

5. **Prepare for data theft without encryption** — 37% of investigations involved data theft. Ransomware-only response plans are incomplete. Build capabilities to detect exfiltration, not just encryption.

---

## What We're Watching

**Infostealer-to-access pipeline.** Stolen credentials surpassing phishing suggests a maturing supply chain: infostealers harvest, markets sell, operators breach. The initial access broker economy is industrializing.

**DPRK employment operations.** 5% today — but this vector is scalable, low-cost, and nearly invisible to traditional security controls. Expect growth.

**Extortion without encryption.** Data theft at nearly 2x the ransomware rate signals where the business model is heading. Quieter, harder to detect, impossible to recover from with backups alone.

**AiTM phishing.** Real-time MFA bypass changes the calculus on authentication. Phishing-resistant MFA isn't a nice-to-have — it's the only MFA that still works against sophisticated adversaries.

---

## The Bottom Line

Mandiant's 450,000 hours of incident response work paint a clear picture: attackers are getting in through unpatched systems, stolen credentials, and — increasingly — the front door of your HR department. Once inside, they use your own tools against you, and most organizations still can't detect them without outside help.

The 11-day dwell time sounds like progress. Look closer, and it's attackers moving faster to monetize — not defenders moving faster to detect.

The organizations that will weather this landscape are the ones treating credential theft like the primary threat vector it's become, investing in detection that goes beyond signature matching, and recognizing that the insider threat now includes people who were never really employees at all.

---

Find all editions on [FIR Risk Tuesday](https://firriskadvisory.com/tuesday/) | [GitHub](https://github.com/stikman28/fir-risk-intelligence)

---

## LINKEDIN POST

Mandiant's M-Trends 2025 report distills 450,000+ hours of incident response.

The findings demand executive attention:

→ Exploits lead initial access at 33% — unpatched systems are still the #1 door
→ Stolen credentials (16%) have surpassed phishing (14%) as an entry vector
→ North Korean IT workers now account for 5% of attack vectors — hired as employees
→ Ransomware in 21% of cases, but data theft in 37% — extortion is evolving past encryption
→ Median dwell time: 11 days — but 57% of breaches are found by someone else, not you

The dwell time headline sounds like progress. Look closer:
- 57% detected externally
- 14% discovered via ransom notice
- Only 29% caught by internal teams

Attackers aren't dwelling less because you're detecting faster. They're monetizing faster.

Five priorities from the data:
1. Patch edge infrastructure (exploits at 33%)
2. Defend against infostealers (credentials surpassed phishing)
3. Strengthen hiring verification (DPRK insider threat)
4. Build behavioral detection (living off the land)
5. Prepare for data theft without encryption

Full analysis: [link]

Source: Mandiant M-Trends 2025

#CyberSecurity #MTrends #Mandiant #ThreatIntelligence #CISO #Ransomware #InsiderThreat

---

## NOTES

- Single edition: E52 (April 29, 2025)
- M-Trends is the gold standard for APT/nation-state IR analysis
- Key SEO terms: "M-Trends 2025", "Mandiant M-Trends", "incident response report 2025", "dwell time", "North Korean IT workers"
- "450,000 Hours on the Front Lines" as title — positions it as field-level intelligence vs DBIR's statistical census
- North Korean IT workers at 5% is the differentiating INTEL — novel insider threat vector
- Dwell time paradox (11 days driven by extortion speed, not detection improvement) is the analytical hook
- Data theft (37%) vs ransomware (21%) disparity shows extortion model evolution
- AiTM phishing bypassing MFA is a critical watch item
- Stolen credentials > phishing represents a structural shift in the initial access economy
- MITRE ATT&CK: T1190, T1078, T1566, T1059, T1021, T1486, T1041
- Hero image: should reference Mandiant/Google Cloud branding or IR field operations theme
