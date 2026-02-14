# FIR Risk Tuesday — Best of E24

**Original Publish Date:** October 22, 2024
**Source:** [Microsoft Digital Defense Report 2024](https://www.microsoft.com/en-us/security/security-insider/microsoft-digital-defense-report-2024)
**Analysis:** FIR Risk Platform

---

# FIR Risk — Best of E24: $1 Trillion in Fraud and 775 Million Malware Emails

![FIR Risk Best of E24 - Microsoft Digital Defense Report 2024](images/best-of-e24-microsoft-digital-defense-report-2024.png)

By FIR Risk Platform | Cybersecurity Risk Intelligence

---

## What You Need to Know

Microsoft's 2024 Digital Defense Report draws from a dataset no other organization can match: **100 trillion security signals processed daily** across Windows, Azure, Microsoft 365, LinkedIn, Xbox, and Bing. When you protect 1.5 billion users and host the world's largest cloud, you see the threat landscape from a vantage point nobody else has.

The 114-page report covering July 2023 through June 2024 reveals a landscape where **global fraud losses exceeded $1 trillion**, **775 million malware-laden emails** targeted Microsoft accounts, DDoS attacks hit **~4,500 per day**, and **83% of organizations experienced multiple breaches**. But the most striking shift is the convergence of cybercrime and fraud — the report treats them as a single continuum, not separate problems.

This is the fraud edition. The one that speaks to both security teams and financial crime investigators.

---

## The $1 Trillion Fraud Landscape

The financial scale of cybercrime and fraud has crossed a threshold:

| Metric | Value |
|--------|-------|
| **Global fraud losses (2023)** | Over $1 trillion USD |
| **Corporate losses** | Average 1.5% of profits |
| **Consumer losses** | $8.8 billion USD (up 30% YoY) |
| **Microsoft payment fraud evaluations** | 1.6 billion risk assessments annually |
| **Fraudulent transactions rejected** | $1.58 billion USD |
| **Projected e-commerce fraud (2028)** | Exceeding $90 billion USD |

One trillion dollars. That's not a cybersecurity statistic — it's a macroeconomic event. When fraud consumes 1.5% of corporate profits on average, it's a line item that CFOs and audit committees can't ignore.

The $8.8 billion in consumer losses — up 30% year-over-year — reflects the democratization of fraud tooling. Phishing-as-a-Service, synthetic identity kits, and AI-powered social engineering have lowered the barrier to entry for financial crime. The projected trajectory toward $90 billion in e-commerce fraud by 2028 suggests the current defenses aren't keeping pace.

Microsoft's own data provides a window: **1.6 billion payment fraud risk assessments** annually, rejecting **$1.58 billion in fraudulent transactions**. That's one company's defensive surface — and it barely dents the trillion-dollar total.

> **INTEL [GLOBAL THREAT]:** Global fraud losses exceeding $1 trillion with consumer losses up 30% YoY signals that fraud has become a macroeconomic force. The projected trajectory to $90B in e-commerce fraud by 2028 demands that organizations treat fraud prevention as a core business function, not a cost center. Security and fraud teams that operate in silos are structurally unable to address a threat that spans both domains.

---

## 775 Million Malware Emails: The Scale of the Problem

Microsoft detected **775 million malware-laden emails** targeting its accounts — and that's just the emails carrying payloads. Phishing emails surged **58%** in 2023, and these numbers represent only what Microsoft sees across its ecosystem.

The volume is important because it reveals the economics of email-based attacks. At 775 million attempts, even a fraction-of-a-percent success rate produces millions of compromised accounts. This is why email compromise leads business cybercrime categories (as the ASD report confirmed at 33% of top crimes) — the funnel is massive and the conversion rate doesn't need to be high.

The 58% phishing surge aligns with CrowdStrike's 442% vishing increase and the Verizon DBIR's finding that GenAI-powered phishing emails doubled. The social engineering attack surface is expanding across every channel — email, voice, and SMS — simultaneously.

---

## DDoS: 4,500 Attacks Per Day

DDoS attacks reached approximately **4,500 per day** by June 2024, with Microsoft mitigating **1.25 million attacks** — a fourfold increase from the prior year.

The fourfold increase reflects both the growing availability of DDoS-for-hire services and the use of DDoS as a component of larger attack campaigns. DDoS is no longer just about taking sites offline — it's used as a distraction (occupying security teams while the real attack unfolds elsewhere), as extortion (pay or stay offline), and as a geopolitical weapon (state-sponsored disruption of adversary infrastructure).

---

## The Fraud-Cybercrime Convergence

The MDDR's most important contribution is treating **cybercrime and fraud as a single continuum**. The report identifies the attack vectors that bridge both worlds:

**E-commerce payment fraud** — Card-not-present transactions are the primary target. Stolen credentials, synthetic identities, and compromised payment sessions enable fraud at scale. Microsoft evaluates 1.6 billion payment transactions annually through this lens.

**AI-powered phishing and social engineering** — Deepfakes, voice cloning, and AI-generated content make social engineering scalable and convincing. The 58% phishing surge is the opening act.

**Synthetic identities** — AI-generated identities that combine real and fabricated data to create personas that pass KYC checks. These aren't stolen identities — they're manufactured ones, making traditional fraud detection less effective.

**SIM swapping** — Hijacking phone numbers to bypass SMS-based MFA, enabling account takeover for both cyber intrusions and financial fraud.

**Phishing-as-a-Service (PhaaS)** — Subscription platforms that provide phishing kits, hosting, and victim management tools. The barrier to entry for phishing campaigns is now a monthly fee, not technical expertise.

> **INTEL [EMERGING RISK]:** The convergence of cybercrime and fraud — driven by AI-powered social engineering, synthetic identities, and PhaaS platforms — means that security teams and fraud teams must integrate their operations. Organizations running these functions in separate departments with separate tools are creating gaps that attackers exploit at the seam.

---

## 83% Multiple Breaches: The New Normal

**83% of organizations experienced multiple breaches** during the reporting period. Not a single incident — multiple.

This finding reframes the security conversation. The question isn't "will we be breached?" or even "when will we be breached?" It's "how many times will we be breached, and can we limit the damage each time?"

When 83% of organizations are experiencing repeat breaches, the value proposition shifts from prevention to resilience. Detection speed, containment capability, and recovery time become the metrics that matter — not whether the perimeter holds.

---

## Patch Windows: From Weeks to Hours

The vulnerability exploitation window has **narrowed from 14-30 days to 24-72 hours**. The time between vulnerability disclosure and active exploitation has compressed to the point where traditional patch cycles can't keep up.

This connects to every vulnerability finding in the Best of collection: the Verizon DBIR's 20% initial access via exploitation, CrowdStrike's 8x zero-day increase on edge devices, and Forescout's 73% of exploited vulns not in CISA KEV. The compression of exploit timelines means the window to patch is no longer measured in sprint cycles — it's measured in hours.

---

## Nation-State AI Operations

Microsoft documented state-sponsored actors using AI for **information manipulation operations** — not just traditional cyber attacks, but influence campaigns that use AI-generated content to shape narratives, create synthetic media, and amplify disinformation at scale.

This extends the AI threat beyond cybersecurity into the broader information warfare domain. When nation-states deploy AI to generate convincing fake content at scale, the trust infrastructure that underpins business communications, media, and democratic processes is at risk.

**FIR Risk Platform MITRE ATT&CK Analysis:**
- Initial Access: T1566 (Phishing) — 775M malware emails, 58% surge
- Initial Access: T1078 (Valid Accounts) — credential theft, SIM swapping
- Resource Development: T1585 (Establish Accounts) — synthetic identities
- Resource Development: T1583 (Acquire Infrastructure) — PhaaS platforms
- Impact: T1498 (Network Denial of Service) — 4,500 DDoS attacks daily
- Impact: T1657 (Financial Theft) — $1 trillion fraud landscape
- Influence: T1583.001 (Social Media Accounts) — nation-state AI manipulation

---

## What Organizations Should Actually Do

The MDDR data points to five priorities:

1. **Converge security and fraud operations** — The $1 trillion fraud landscape spans both domains. Break down organizational silos between cybersecurity and financial crime teams. Share intelligence, tools, and response capabilities across both functions.

2. **Implement passwordless authentication** — SIM swapping bypasses SMS-based MFA. Phishing bypasses password-based auth. Move to FIDO2/WebAuthn passkeys that are resistant to both phishing and replay attacks.

3. **Compress patch timelines** — 24-72 hours is the new exploitation window. Build emergency patching capabilities for critical vulnerabilities. Automate where possible. Accept that some patches will need to bypass change management.

4. **Invest in AI-powered fraud detection** — When attackers use AI to generate synthetic identities and scale social engineering, rule-based fraud detection fails. Deploy behavioral analytics and AI-driven anomaly detection that can adapt to evolving tactics.

5. **Plan for multiple breaches** — 83% of organizations face repeat incidents. Build response capabilities that assume compromise is ongoing. Segment environments to limit blast radius. Rehearse response plans quarterly, not annually.

---

## What We're Watching

**Fraud-as-a-Service maturation.** PhaaS, synthetic identity kits, and AI-powered social engineering tools are creating a fraud supply chain that mirrors the cybercrime-as-a-service model.

**E-commerce fraud trajectory.** $90 billion projected by 2028. Payment platforms and merchants are in an escalating arms race with fraud operators.

**Synthetic identity proliferation.** As AI-generated identities become more convincing, KYC and identity verification controls will need fundamental redesign.

**Patch window compression.** 24-72 hours is already difficult. As AI enables faster exploit development, the window may compress further — potentially to hours.

---

## The Bottom Line

Microsoft's Digital Defense Report 2024 reveals a threat landscape where the boundaries between cybersecurity and fraud have dissolved. $1 trillion in fraud losses. 775 million malware emails. 4,500 DDoS attacks per day. 83% of organizations experiencing multiple breaches. Patch windows compressed to hours.

The report's defining contribution is making the fraud-cybercrime convergence visible. When synthetic identities bypass KYC, phishing-as-a-service replaces technical skill, and AI-powered social engineering scales infinitely — the organizations still running security and fraud as separate functions are fighting a unified threat with a divided defense.

One trillion dollars. That number alone should end every debate about whether cybersecurity and fraud prevention deserve board-level attention.

---

Find all editions on [FIR Risk Tuesday](https://firriskadvisory.com/tuesday/) | [GitHub](https://github.com/stikman28/fir-risk-intelligence)

---

## LINKEDIN POST

Microsoft processes 100 trillion security signals daily. Their 2024 Digital Defense Report reveals what they see:

→ Global fraud losses exceeded $1 trillion in 2023
→ 775 million malware-laden emails detected
→ Phishing surged 58%
→ ~4,500 DDoS attacks per day (1.25M mitigated — 4x increase)
→ 83% of organizations experienced multiple breaches
→ Patch window compressed from weeks to 24-72 hours
→ E-commerce fraud projected to exceed $90B by 2028

The report's biggest insight isn't any single number. It's the convergence of cybercrime and fraud.

Synthetic identities bypass KYC. Phishing-as-a-Service replaces technical skill. SIM swapping defeats SMS-based MFA. AI-powered social engineering scales infinitely.

Organizations still running security and fraud as separate functions are fighting a unified threat with a divided defense.

Consumer losses hit $8.8B (up 30%). Corporate losses average 1.5% of profits. Microsoft alone rejected $1.58B in fraudulent transactions from 1.6B risk assessments.

One trillion dollars. That number alone should end every debate about board-level attention.

Full analysis: [link]

Source: Microsoft Digital Defense Report 2024

#CyberSecurity #Fraud #Microsoft #ThreatIntelligence #CISO #Phishing #DDoS #AI

---

## NOTES

- Single edition: E24 (October 22, 2024)
- MDDR 2024 is the earlier version — we already have E73 covering MDDR 2025 on the website
- Key SEO terms: "Microsoft Digital Defense Report 2024", "MDDR 2024", "global fraud losses", "cybercrime costs", "e-commerce fraud", "synthetic identity"
- "$1 Trillion in Fraud and 775 Million Malware Emails" — leads with the financial scale
- Fraud-cybercrime convergence is the unique angle — no other Best of edition covers financial crime
- Connects to FIR Risk Platform's Fraud Investigation Workbench feature
- 83% multiple breaches reframes from prevention to resilience
- Patch window compression (14-30 days → 24-72 hours) connects to DBIR/CrowdStrike/Forescout vulnerability findings
- PhaaS and synthetic identities represent the fraud supply chain maturation
- 100 trillion signals daily — unmatched dataset gives Microsoft unique authority
- MITRE ATT&CK: T1566, T1078, T1585, T1583, T1498, T1657
- Hero image: Microsoft MDDR branding or fraud/financial crime visual
