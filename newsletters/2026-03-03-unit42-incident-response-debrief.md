# FIR Risk Tuesday E81

**Publish Date:** March 3, 2026
**Source:** [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report) (February 2026)
**Analysis:** FIR Risk Platform

---

# FIR Risk E81 — 72 Minutes

![FIR Risk E81 - 72 Minutes](images/e81-unit42-incident-response-debrief.png)

By FIR Risk Platform | Cybersecurity Risk Intelligence

---

## What You Need to Know

Unit 42 responded to over 750 major cyber incidents in 2025, across 50+ countries and every major industry. The findings are not subtle.

**90% of breaches were preventable.** Not zero-days. Not nation-state sophistication. Misconfigurations, excessive permissions, and gaps in basic coverage. Attackers are winning with familiar tactics executed at machine speed.

This is a debrief. Here's what matters.

> **INTEL [GLOBAL] [THREAT ALERT]:** 90% of breaches enabled by preventable security gaps — misconfigurations, excessive identity permissions, and inconsistent security coverage across attack surfaces.

---

## The 72-Minute Window

The fastest 25% of attacks reached exfiltration in **72 minutes**. Down from 285 minutes. AI-assisted simulations achieved it in 25. Threat actors begin scanning for new CVEs within 15 minutes of disclosure.

The math for defenders no longer works.

| Metric | Before AI | With AI |
|--------|-----------|---------|
| Time to exfiltration (top quartile) | 285 minutes | 72 minutes |
| CVE-to-scanning | Hours/days | 15 minutes |
| Attack surface | Single vector | 87% multi-surface |
| Extortion operations | Manual, sequential | Automated, parallel |

Attackers scale with compute and operate 24/7. Defenders scale with hiring and need approval chains.

**If your mean time to contain exceeds 72 minutes, you are losing by default.**

> **INTEL [GLOBAL] [TREND]:** Exfiltration speeds quadrupled in 2025. AI compresses the full attack lifecycle — reconnaissance through impact — into hours. IR teams operating at human speed cannot match machine-speed attack progression.

---

## Identity Is the Skeleton Key

Identity was the attack vector in **90% of incidents**. 65% used identity-driven initial access. This is not a supporting finding — it is the finding.

When attackers compromise Active Directory, everything else falls:

- **Cloud:** Reset admin credentials, log in through the front door
- **SaaS:** SSO tokens grant access to every connected application
- **Endpoints:** Group Policy becomes a malware distribution system
- **Network:** Legitimate credentials bypass every perimeter control

Your SSO is their skeleton key. Your cloud management tools become their deployment infrastructure. Your Group Policy becomes their ransomware delivery mechanism.

87% of intrusions spanned multiple attack surfaces. They aren't moving sequentially — they're hitting cloud, endpoint, SaaS, and identity **simultaneously**. Traditional defense-in-depth fails when identity compromise unlocks every layer at once.

> **INTEL [GLOBAL] [PATTERN]:** Multi-surface attacks exploit identity federation as force multiplier. Single credential compromise enables simultaneous access across on-premises, cloud, and SaaS within 45 minutes. 23% of cases involved SaaS data, up from 6% in 2022.

---

## Supply Chains Are Nation-State Highways

Software supply chain risks and nation-state tactics are evolving together. These are not separate problems — they are the same strategy.

**The economics are simple:** Why hack 1,000 companies when you can hack their shared vendor and reach all 1,000 at once?

Nation-state actors are weaponizing trust:

- **SaaS integrations** — Compromise one OAuth app, inherit access to thousands of downstream customers
- **Remote management tools** — 39% of cases used RMM/MDM platforms as command-and-control highways
- **Dependency chains** — 60% of cloud-native vulnerabilities live in transitive libraries that nobody audits

The most insidious capability: **weaponizing uncertainty itself.** When a major vendor is compromised, thousands of organizations enter assessment mode simultaneously. Operations pause. Security teams are overwhelmed. The real target continues operating while everyone else is distracted.

> **INTEL [GLOBAL] [PATTERN]:** Nation-state actors leverage supply chain compromise for 1-to-many access. Trusted vendor channels, OAuth integrations, and remote management platforms provide legitimate-appearing persistence at scale.

---

## What Risk Leaders Must Do

**Stop:**
- **Buying more security tools.** You have a speed problem, not a coverage problem
- **Treating identity as just another control.** Identity IS your perimeter
- **Assuming vendors are secure.** Your trusted business relationships are attack vectors

**Start:**
- **Automating containment at machine speed.** If it requires human approval, it's too slow
- **Auditing every identity with admin access.** Emergency. Assume some are already compromised
- **Building breakglass procedures for vendor isolation.** Test quarterly. Disconnect in minutes, not days

**The strategic shift:** From "how do we prevent breaches" to "how do we limit damage when breaches happen."

---

## What This Means for You

**If you're a CEO or Board Director:** This report is your mandate to ask one question: *How fast can we contain a breach?* If nobody can answer in minutes, your security investment is misaligned. Authorize autonomous containment. Fund identity infrastructure. Demand vendor breakglass procedures. The 72-minute window is a board-level metric now.

**If you're a CISO:** Stop adding tools and start measuring speed. Your mean time to contain is the only number that matters against AI-accelerated attacks. Audit every privileged identity this week — not next quarter. Build automated playbooks that execute without waiting for human approval. Your job is shifting from prevention architect to speed architect.

**If you lead a cyber or SOC team:** The sequential detect-analyze-escalate-contain workflow is broken. Attackers move in parallel across every surface while you work one alert at a time. Push for autonomous containment triggers. Map your visibility gaps across cloud, SaaS, and identity — the 87% multi-surface stat means single-surface monitoring is blind by design.

**If you lead fraud or financial crime:** Identity compromise at this scale means account takeover, synthetic identity, and insider threat vectors are all accelerating. When attackers own credentials in 90% of cases, your fraud detection models need to account for legitimate-looking access. Watch for anomalous identity behavior, not just anomalous transactions.

**If you're in risk or compliance:** Third-party risk assessments based on annual questionnaires are obsolete. Nation-states are using your vendor relationships as highways. Demand real-time security posture visibility from critical vendors. Build contractual breakglass provisions. And update your risk register — identity and supply chain are not supporting risks, they are primary risks.

---

## What We're Watching

**AI defense parity.** Organizations deploying autonomous detection and containment will separate from those still operating manual IR playbooks. The gap will become measurable in 2026.

**Identity infrastructure consolidation.** Expect accelerated investment in identity threat detection, continuous verification, and privilege-on-demand architectures.

**Supply chain accountability.** Regulatory pressure will force vendors to demonstrate security posture. Organizations will demand real-time visibility into third-party risk, not annual questionnaires.

**Browser as attack surface.** 48% of incidents involved browser activity intersecting with routine workflows. This vector is underdefended and growing.

---

## The Bottom Line

This report confirms what many suspected but few have acted on: the threat landscape has fundamentally shifted. Attackers operate at machine speed, exploit identity as a master key, orchestrate across every surface simultaneously, and weaponize your own infrastructure against you.

And 90% of it is preventable.

The organizations that survive the next wave won't be the ones with the most security tools. They'll be the ones that can match machine-speed attacks with machine-speed defense.

The window is 72 minutes. The clock is already running.

---

Find all editions: [FIR Risk Tuesday](https://firrisk.ai/tuesday/)

Source: [GitHub - FIR Risk Intelligence](https://github.com/stikman28/fir-risk-intelligence)

---

## LINKEDIN POST

72 minutes.

That's how long it takes the fastest attackers to go from initial access to data exfiltration. Down from 285 minutes. In one year.

Unit 42 just released their Global Incident Response Report analyzing 750+ major incidents from 2025. The findings should reshape every security strategy:

→ 90% of breaches were preventable
→ Identity was the attack vector in 90% of incidents
→ 87% of intrusions spanned multiple attack surfaces simultaneously
→ AI-powered attacks are compressing the entire kill chain into hours

The most important stat isn't the speed. It's this: attackers are winning with familiar tactics — not revolutionary techniques. Misconfigurations. Excessive permissions. Gaps in basic coverage.

Your SSO is their skeleton key. Your cloud management tools are their deployment infrastructure. Your vendor relationships are nation-state highways.

The question for every board: Can your organization detect, contain, and recover faster than 72 minutes?

If not, the math doesn't work.

Full debrief in this week's FIR Risk Tuesday → [link]

#cybersecurity #incidentresponse #threatintelligence #identitysecurity #AI #riskmanagement #CISO #Unit42

---

## X POST

Unit 42 analyzed 750+ major cyber incidents from 2025 across 50 countries. The number that should concern every executive: 72 minutes. That's how fast the top 25% of attackers now reach data exfiltration, down from 285 minutes last year. With AI-assisted attacks it drops to 25 minutes. Threat actors start scanning for new vulnerabilities within 15 minutes of disclosure. The math for defenders no longer works.

Here's what makes this worse — 90% of those breaches were preventable. Not zero-days. Not nation-state sophistication. Misconfigurations, excessive permissions, and gaps in basic security coverage. Familiar problems executed at unfamiliar speed. Identity was the attack vector in 90% of incidents. When attackers compromise Active Directory, everything falls. Your SSO becomes their skeleton key. Cloud admin credentials get reset through the front door. SSO tokens grant access to every connected SaaS app. Group Policy becomes a malware distribution system. 87% of intrusions spanned multiple attack surfaces simultaneously — cloud, endpoint, SaaS, and identity hit at the same time.

Then there's the supply chain. Nation-state actors figured out the economics — why hack 1,000 companies when you can compromise their shared vendor and reach all of them at once? 39% of cases used remote management platforms as command-and-control highways. 60% of cloud-native vulnerabilities sit in transitive libraries nobody audits. One compromised OAuth app cascades access to thousands of downstream customers. The most insidious part is how they weaponize uncertainty itself — when a major vendor is compromised, thousands of organizations enter assessment mode simultaneously. Operations pause. Security teams are overwhelmed. The real target continues operating while everyone else is distracted.

What should organizations do? Stop buying more security tools — this is a speed problem, not a coverage problem. If containment requires human approval, it's too slow. Treat identity as your perimeter, not just another control. Audit every admin account this week and assume some are already compromised. Build breakglass procedures for vendor isolation, test them quarterly, and be ready to disconnect in minutes not days.

If you're a CEO or board director, this report is your mandate to ask one question — how fast can we contain a breach? If nobody can answer in minutes, your security investment is misaligned. Authorize autonomous containment. Fund identity infrastructure. The 72-minute window is a board-level metric now.

If you're a CISO, stop adding tools and start measuring speed. Your mean time to contain is the only number that matters against AI-accelerated attacks. Audit every privileged identity this week, not next quarter. Build automated playbooks that execute without waiting for human approval. Your job is shifting from prevention architect to speed architect.

If you lead a SOC team, the sequential detect-analyze-escalate-contain workflow is broken. Attackers move in parallel across every surface while you work one alert at a time. Push for autonomous containment triggers. Map your visibility gaps across cloud, SaaS, and identity — the 87% multi-surface stat means single-surface monitoring is blind by design.

If you lead fraud or financial crime, identity compromise at this scale means account takeover, synthetic identity, and insider threat vectors are all accelerating. When attackers own credentials in 90% of cases, your fraud detection models need to account for legitimate-looking access. Watch for anomalous identity behavior, not just anomalous transactions.

If you're in risk or compliance, third-party risk assessments based on annual questionnaires are obsolete. Nation-states are using your vendor relationships as highways. Demand real-time security posture visibility from critical vendors. Build contractual breakglass provisions. Identity and supply chain aren't supporting risks anymore — they are primary risks.

Looking ahead, organizations deploying autonomous detection and containment will separate from those still running manual IR playbooks. That gap becomes measurable this year. Expect accelerated investment in identity threat detection, continuous verification, and privilege-on-demand architectures. Regulatory pressure will force vendors to demonstrate security posture in real time, not through annual questionnaires. And the browser as an attack surface is growing fast — 48% of incidents involved browser activity intersecting with routine workflows. That vector is underdefended.

This report confirms what many suspected but few have acted on — the threat landscape has fundamentally shifted. Attackers operate at machine speed, exploit identity as a master key, orchestrate across every surface simultaneously, and weaponize your own infrastructure against you. And 90% of it is preventable. The organizations that survive the next wave won't be the ones with the most security tools. They'll be the ones that can match machine-speed attacks with machine-speed defense. The window is 72 minutes. The clock is already running.

#cybersecurity #incidentresponse

---

## SOURCE DATA

**Primary Source:**
- Unit 42 Global Incident Response Report 2026, Palo Alto Networks (February 2026) — [Full Report](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report)

**FIR Risk Platform KB Sources:**
- Document: "Paloalto Global Incident Response Report 2026" (threat_report, ingested 2026-03-02)
- MITRE ATT&CK techniques referenced: T1566 (Phishing), T1078 (Valid Accounts), T1110 (Brute Force), T1190 (Exploit Public-Facing Application), T1068 (Exploitation for Privilege Escalation)
- Threat actors referenced: Muddled Libra, North Korean IT workers

**Key Statistics:**
- 750+ incident responses across 50+ countries
- 90% of breaches enabled by preventable gaps
- 87% of intrusions involved multiple attack surfaces
- 65% used identity-driven initial access methods
- 72 minutes to exfiltration (fastest quartile, down from 285)
- 48% involved browser-based activity
- 23% involved SaaS data (up from 6% in 2022)
- 39% used remote access tools as C2
- 60% of cloud-native vulnerabilities in transitive libraries
- Exfiltration speeds quadrupled in 2025
