# FIR Risk Tuesday E76 - DRAFT - Special Friday Edition

**Publish Date:** January 30, 2026
**Source:** [GuidePoint 2026 Ransomware and Cyber Threat Report](https://www.guidepointsecurity.com/resources/grit-2026-ransomware-and-cyber-threat-report/) (gated)
**Analysis:** FIR Risk Platform

---

## NEWSLETTER DRAFT - Special Friday Edition

# FIR Risk E76 - Ransomware's Profit Problem (And Why That Makes It Worse)

![FIR Risk E76 - GuidePoint Ransomware Annual Report 2026](images/e76-guidepoint-ransomware.png)

By FIR Risk Platform | Cybersecurity Risk Intelligence

## Weekly Risk Intelligence Brief

**Source:** [GuidePoint 2026 Ransomware and Cyber Threat Report](https://www.guidepointsecurity.com/resources/grit-2026-ransomware-and-cyber-threat-report/) (gated)

### The Counterintuitive Truth About Ransomware in 2026

Ransomware payments dropped 35% last year. Median ransom demands collapsed from $9.9 million to under $3 million. Sixty-four percent of victims refused to pay—up from 50% just two years ago.

Sounds like progress, right?

Here's the problem: **7,515 organizations were publicly posted as ransomware victims in 2025.** That's 20.6 victims per day. 124 ransomware groups are now active—more than ever.

When profits shrink, attackers don't quit. They industrialize.

---

## The Economics of Desperation

GuidePoint's 2026 report reveals a "free market pressure" effect reshaping the ransomware ecosystem:

| Metric | 2023 | 2024-25 | Trend |
|--------|------|---------|-------|
| Median ransom demand | $9.9M | <$3M | ↓ 70% |
| Victim refusal rate | ~50% | 64% | ↑ |
| Blockchain payments | Baseline | -35% | ↓ |
| Daily victims | — | 20.6 | ↑ |
| Active groups | — | 124 | ↑ |

The math is brutal: if each attack yields less, you need more attacks. Enter AI.

> **INTEL [THREAT EVOLUTION]:** Ransomware groups are adopting AI/LLMs to automate reconnaissance, phishing, and lateral movement—enabling 10x faster attack cycles. Ransom demands now arrive within hours, not days.

---

## AI Turns Ransomware Into an Assembly Line

The 2026 playbook isn't about sophistication. It's about throughput.

GuidePoint documents the industrialization of ransomware operations:

- **Specialized roles**: Initial access brokers, negotiators, and "cashiers" operate like a corporate division
- **LLM target prioritization**: AI analyzes stolen data in minutes to identify who will pay the most
- **Double Extortion 2.0**: Personalized ransom notes generated from victim financial profiles
- **Polymorphic malware**: AI-generated, fileless payloads that evade signature-based detection

This isn't evolution. It's mass production.

> **INTEL [ATTACK TECHNIQUE]:** AI-augmented ransomware groups can now execute end-to-end attacks—from initial access to ransom demand—with minimal human intervention. The attack lifecycle that took weeks now takes hours.

---

## One Breach, Thousands of Victims

The highest-ROI attack in 2026? Compromise a third-party provider.

Ransomware groups have learned that MSPs, managed file transfer platforms, and SaaS providers are force multipliers. One vulnerability, one breach, hundreds of downstream victims.

The playbook is proven:
- **Kaseya (2021)**: REvil encrypted 1,500+ client networks through a single RMM compromise. Demanded $70 million.
- **MOVEit (2023)**: CVE-2023-34362 led to 1,000+ organizations breached—universities, healthcare, Fortune 500.

| Target Type | Why Attackers Love Them |
|-------------|------------------------|
| MSPs | Centralized access to client networks |
| MFT Platforms | Handle bulk sensitive data transfers |
| SaaS Providers | Credential harvesting at scale |
| Cloud Infrastructure | Overprivileged accounts everywhere |

> **INTEL [CRITICAL VULNERABILITY]:** Organizations with weak segmentation between client environments or inconsistent patch management are primary targets. Your vendor's security posture is now your security posture.

**MITRE ATT&CK Mapping:**
- **T1133** (External Remote Services): Exploiting MSP tools like Kaseya
- **T1190** (Exploit Public-Facing Application): Zero-days in MFT platforms like MOVEit

---

## New Target: Law Firms

GuidePoint flags legal services as an emerging high-value vertical—and the numbers back it up.

**2025 by the numbers:**
- **217 law firm breaches** (12% of all ransomware incidents)
- **41% payment rate**—far above the 36% cross-sector average
- **$1.2M average ransom demand** (up 60% from 2024)
- **98% involved double extortion** (encryption + data leak threats)

Why are law firms so attractive? They're the perfect extortion target:

| Factor | Why It Matters |
|--------|---------------|
| **Sensitive data** | M&A deals, litigation strategy, client PII |
| **Third-party gateway** | Compromising one firm exposes multiple corporate clients |
| **Reputation pressure** | Disclosure destroys client trust |
| **Higher payment rate** | 41% pay vs. 36% average—attackers know the math |

**TTPs to watch:**
- **Legal-themed phishing**: Fake court documents, client requests, invoice macros (T1566)
- **Case management exploitation**: Targeting Clio, LexisNexis, e-discovery platforms
- **MFA fatigue attacks**: Session hijacking to bypass authentication (T1078)
- **Backup destruction**: LockBit specifically targeting offsite/cloud backups (T1489)

> **INTEL [SECTOR ALERT]:** Law firms paid ransoms at a 41% rate in 2025—50% higher than the cross-sector average. With average demands up 60% year-over-year, legal services are now a premium target. Firms handling M&A, IP, or high-profile litigation face elevated risk in 2026.

**2026 outlook:** GuidePoint predicts LLMs will analyze stolen legal documents to identify high-value matters (active M&A, pending litigation) and prioritize extortion accordingly. IP law firms in tech hubs are expected to see increased RaaS affiliate targeting.

---

## What Organizations Should Do Now

GuidePoint's findings point to three defensive priorities:

**1. Treat third-party risk as primary risk.**
Your vendors are your attack surface. Enforce zero trust and least privilege for every third-party connection. Audit their security posture regularly—not annually, continuously.

**2. Match AI with AI.**
If attackers use LLMs to find you, you need AI to find them first. Deploy AI-augmented threat detection, behavioral analytics, and automated response playbooks. SOAR platforms should handle routine isolation and credential resets in seconds.

**3. Assume you'll be hit—plan for speed.**
With 20+ victims per day, the question isn't if but when. Your recovery playbooks need to execute faster than attackers can escalate. Tabletop exercises should include AI-driven attack scenarios.

**For law firms specifically:**
- Segment client data with zero-trust architecture
- Audit case management and e-discovery vendors quarterly
- Implement immutable, offline backups (per NIST SP 800-53)
- Run legal-themed phishing simulations (fake court filings, client requests)

---

## What We're Watching

**State-sponsored overlap.** GuidePoint notes increasing convergence between ransomware groups and nation-state actors. Ransomware is becoming a deniable disruption tool—expect more attacks on critical infrastructure with murky attribution.

**Regulatory arbitrage.** Groups are shifting operations toward APAC jurisdictions with unclear ransom payment laws. Geography is becoming a strategic variable.

**The law firm domino.** 217 breaches in 2025, and attackers now know legal pays 50% more often than average. If a major firm gets hit publicly in 2026, expect a feeding frenzy.

---

*Sandra Joyce, VP of Google Threat Intelligence, summarized it plainly: "We expect to see more ransomware and extortion. This problem is going to continue and increase in 2026."*

The economics have shifted. The tactics have industrialized. The question isn't whether you'll face a ransomware attempt—it's whether you can respond faster than attackers can escalate.

---

Stay tuned for more in future FIR Risk Newsletters!

Find all editions on our Blog: https://firriskadvisory.com/blog/

---

## LINKEDIN POST

7,515 organizations were publicly posted as ransomware victims in 2025.

That's 20.6 per day.

Meanwhile:
→ Payments dropped 35%
→ 64% of victims refused to pay
→ Median demands collapsed 70%

The math: fewer payouts = more attacks.
124 ransomware groups are now active.
AI lets them run 10x faster.

This is industrialization.

One finding that should concern every GC and CISO:
Law firms are now premium targets.

→ 217 breaches in 2025 (12% of all incidents)
→ 41% payment rate—50% higher than average
→ Ransom demands up 60% year-over-year

Sensitive client data + reputation pressure + higher payment rates = ideal extortion target.

If your organization handles M&A, IP, or litigation—or relies on vendors that do—this is required reading.

Full analysis in this week's FIR Risk Tuesday: [link]

#CyberSecurity #Ransomware #ThreatIntelligence #CISO #LegalTech

---

## PROMPTS USED

**Prompt 1:** "Tell me about the GuidePoint Ransomware Annual Report 2026 and any unique insights or intelligence in the report"

**Prompt 2:** "Go deeper on third-party provider targeting from the GuidePoint report. How ransomware groups use third-party providers as force multipliers, specific examples, which types are most targeted, and what makes these attacks effective. Flag any critical INTEL for security leaders."

**Prompt 3:** "What does GuidePoint predict will change in 2026 specifically? Any new TTPs, emerging threat actors, or shifts in targeting we should watch for?"

**Prompt 4:** "Give me the key statistics from the GuidePoint report - victim counts, payment rates, ransom amounts, year-over-year trends. Numbers that quantify the 2025-2026 ransomware landscape."

**Prompt 5:** "Tell me more about the law firm attack angle, what details does the report provide, any intel or insights you see?"

---

## NOTES

- Lead angle: "Profit problem → industrialization" ties all sections together
- Law firm section strengthened with 41% payment rate stat (50% higher than average)
- MITRE mappings: T1133, T1190, T1566, T1078, T1486, T1489
- Sandra Joyce quote adds external credibility
- LinkedIn post uses Option C format (single stat punch)
- Consider adding visual: "Economics of Ransomware 2023 vs 2025" comparison chart
- Q1 2025 had 2,302 DLS victims (highest since 2020) - could add if space allows
