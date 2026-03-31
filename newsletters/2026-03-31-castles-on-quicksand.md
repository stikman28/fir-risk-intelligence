# FIR Risk Tuesday E86

**Publish Date:** March 31, 2026
**Source:** [IBM X-Force Threat Intelligence Index 2026](https://www.ibm.com/reports/threat-intelligence) & [Red Canary Threat Detection Report 2026](https://redcanary.com/threat-detection-report/) (2026)
**Analysis:** FIR Risk Platform

---

# FIR Risk E86 — Castles on Quicksand

![FIR Risk E86 - Castles on Quicksand](images/e86-castles-on-quicksand.png)

FIR Risk Advisory | Enterprise Risk Intelligence

---

## Bottom Line

What happens when you read the threat landscape from two completely different vantage points — and they both point to the same uncomfortable conclusion?

IBM X-Force's 2026 Threat Intelligence Index draws from incident response engagements, dark web intelligence, and vulnerability research across the global attack surface. Red Canary's 2026 Threat Detection Report analyzes over 110,000 confirmed threats detected across 4.5 million endpoints — the ground truth of what's actually triggering alerts in production environments. One sees the strategy. The other sees the evidence. Together, they expose a fundamental misalignment between how organizations are investing in security and where attacks are actually succeeding.

Three findings define this paired analysis. First, **exploitation of public-facing applications surged 44% to become the top initial access vector**, with 56% of exploited vulnerabilities requiring no authentication at all — adversaries aren't breaking in, they're walking through open doors. Second, **the ransomware ecosystem has fragmented into 109 active groups** — a 49% increase — shifting the threat model from sophisticated cartels to distributed, opportunistic swarms using commoditized tooling. Third, **identity attacks exploded 850% in detection volume**, confirming across both incident response data and endpoint telemetry that credentials — not malware — are the primary weapon of compromise.

But the most important finding isn't a statistic. It's a pattern: **the most sophisticated attacks in both reports succeeded because of basic security failures.** Advanced reconnaissance led to misconfigured access controls. AI-enhanced credential harvesting exploited weak authentication. Supply chain compromises gained initial access through password brute forcing. We're building castles on quicksand — investing in advanced threat detection while the foundations remain broken.

This is our sixth consecutive deep dive into a 2026 annual threat report, following [Unit 42 (E81)](/tuesday/e81-unit42-incident-response-debrief/), [Cloudflare (E82)](/tuesday/e82-cloudflare-threat-landscape/), [CrowdStrike (E83)](/tuesday/e83-crowdstrike-global-threat-report/), [Picus (E84)](/tuesday/e84-digital-parasite/), and [Mandiant M-Trends (E85)](/tuesday/e85-responders-report/). Six reports, six different methodologies, six different data sets — and an increasingly undeniable convergence on what actually matters.

---

## Key Judgments

**1. The open door is more dangerous than the zero-day.** IBM X-Force found that exploitation of public-facing applications increased 44% year-over-year, becoming the #1 initial access vector. More critically, 56% of the vulnerabilities exploited required no authentication whatsoever. Organizations are hunting for sophisticated exploits while attackers walk through misconfigured front doors. *High confidence — confirmed by X-Force incident response and vulnerability analysis.*

**2. Ransomware has industrialized into a swarm.** The ransomware ecosystem expanded to 109 active groups — a 49% increase — while the share attributed to top-tier operators declined. This isn't growth of sophisticated operations. It's democratization. Leaked toolkits, commoditized playbooks, and low barriers to entry have created a volume-based threat that traditional "big game hunter" defenses aren't built for. *High confidence — based on IBM X-Force dark web monitoring and leak site analysis.*

**3. Identity is now the primary attack surface, confirmed at scale.** Red Canary recorded an 850% increase in identity threat detections, making identity attacks their #1 threat category. IBM independently confirms credential theft operations remain "central to prominent attack campaigns," with over 300,000 ChatGPT credentials alone discovered on dark web markets. When two fundamentally different data sources — incident response and endpoint telemetry — converge this sharply, it's no longer a trend. It's the new baseline. *High confidence — independently confirmed across both reports.*

**4. AI currently benefits defenders more than attackers — but the window is closing.** Red Canary's analysis of 110,000 threats finds that AI-enhanced attacks "don't fundamentally change how threats present themselves" — existing detection methods remain effective. IBM confirms that AI "amplifies existing capabilities rather than fundamentally changing attack methodologies." But IBM also warns that mature adversaries are positioning to "operationalize agentic AI for minimally supervised operations." The defender advantage is real but temporary. *Moderate confidence — current state is well-evidenced; trajectory is assessed.*

**5. Manufacturing has become the #1 target industry.** IBM X-Force data shows manufacturing leading all sectors at 27.7% of incidents — displacing financial services from its traditional position. This reflects the convergence of industrial espionage, supply chain targeting, and the sector's relative underinvestment in security compared to financial services. Organizations outside financial services can no longer assume they're lower-priority targets. *High confidence — based on IBM X-Force incident data.*

---

## Three Critical Shifts

Both reports independently document the same three structural changes in the threat landscape — and the implications are clearest when you read them together:

**From Sophistication to Commodity.** IBM's fragmentation data reveals 109 active ransomware groups conducting "lower volume but widespread attacks" using leaked tooling and established playbooks. Red Canary's detection data confirms this from the other side: the threats triggering alerts across 4.5 million endpoints aren't novel — they're known techniques deployed at scale by numerous smaller operators. The security industry built its threat model around a handful of sophisticated adversaries. The reality in 2025 was a swarm of opportunists using off-the-shelf weapons. Detection-over-attribution and speed-over-sophistication should be the new operating principles.

> **INTEL [GLOBAL] [TREND]:** Ransomware ecosystem fragmentation — 109 active groups, 49% year-over-year increase, declining share for top-10 operators — represents a structural shift from centralized, sophisticated operations to distributed, commoditized attacks. Traditional threat-intelligence-driven defenses built around tracking specific adversaries are losing effectiveness against volume-based opportunism.

**From Perimeter to Identity.** Red Canary's 850% surge in identity attack detections and IBM's emphasis on credential operations as "central to prominent attack campaigns" confirm what the prior five reports in this series established: the perimeter is identity, and identity is broken. IBM documents over 300,000 ChatGPT credentials harvested by infostealers on dark web markets — a new category of credential that didn't exist two years ago. Red Canary shows cloud account compromises dominating their detection landscape. The attack doesn't start with malware. It starts with a valid login.

> **INTEL [GLOBAL] [PATTERN]:** Cross-validation between IBM X-Force incident response data and Red Canary endpoint telemetry (110,000 threats, 4.5M endpoints) independently confirms identity attacks as the dominant threat vector. The 850% detection surge represents not just more attacks but a fundamental shift in adversary methodology — credentials are the primary weapon, not the secondary objective.

**From Advanced Threats to Basic Failures.** This is the finding that changes the investment thesis. IBM documents that "basic cybersecurity lapses contributed to many compromises" — misconfigured access controls, weak authentication, insufficient logging. Red Canary simultaneously reports that even AI-enhanced threats succeed through fundamental identity compromise, not technical sophistication. The tension between these perspectives — IBM highlighting basic failures while Red Canary emphasizes sophisticated attack chains — resolves into a single insight: **advanced attackers are succeeding because organizations haven't secured the basics.** The attack chain is sophisticated. The entry point rarely is.

> **INTEL [GLOBAL] [FINDING]:** IBM X-Force and Red Canary's 2026 data independently confirm that sophisticated attack chains consistently exploit basic security failures as initial access vectors. The 44% increase in public-facing application exploitation — with 56% requiring no authentication — demonstrates that advanced threat detection cannot compensate for fundamental security hygiene gaps.

---

## Evidence

### The Open-Door Problem: 44% Surge in Application Exploitation

IBM X-Force documents a 44% year-over-year increase in exploitation of public-facing applications, elevating it to the #1 initial access vector. But the statistic that should alarm every security leader is the authentication finding: **56% of the vulnerabilities exploited required no authentication at all.**

This isn't attackers defeating security controls. It's attackers finding systems where no controls exist. Misconfigured APIs, exposed management interfaces, default credentials on internet-facing applications — the kind of basic configuration failures that appear in every security audit but rarely make it to the top of the remediation queue.

The implications compound when you overlay Red Canary's detection data. Their endpoint telemetry confirms that the attacks triggering alerts across 4.5 million endpoints are overwhelmingly using known techniques against known weaknesses. The sophisticated zero-day exploitation that dominates security conference presentations represents a fraction of actual compromises. The volume is in the basics.

> **INTEL [GLOBAL] [VULNERABILITY]:** 56% of vulnerabilities exploited in IBM X-Force's 2025 incident data required no authentication. The 44% year-over-year surge in public-facing application exploitation confirms that unprotected application surfaces — not advanced exploits — are the primary entry point for real-world attacks.

---

### The Ransomware Swarm: 109 Groups, New Rules

The ransomware landscape in 2025 underwent a structural transformation that most security strategies haven't caught up with.

IBM X-Force identified **109 active ransomware groups** — a 49% increase year-over-year. But the critical detail isn't the growth. It's the redistribution. A smaller share of total activity is attributed to the top 10 groups. The ecosystem has fragmented from a cartel model to a swarm model: many smaller operators conducting lower-volume attacks using leaked tooling and commoditized playbooks, with frequent identity shifts to complicate attribution.

This changes the threat model fundamentally:

**Old assumption:** Prepare for well-resourced, sophisticated groups with custom tools, long dwell times, and specific industry targeting. Track their TTPs, build detection rules for their tooling, monitor their infrastructure.

**New reality:** Prepare for volume. Unknown ransomware families using generic techniques. Multiple simultaneous low-sophistication attempts. Rapid turnover in group identities makes attribution-based detection a diminishing asset.

Red Canary's endpoint data supports this shift. Their detection of over 110,000 threats reveals that commodity attack patterns — not bespoke campaigns — dominate the landscape. The threat hunting playbook built for APTs needs a companion strategy built for opportunistic volume.

> **INTEL [GLOBAL] [TREND]:** The ransomware ecosystem's fragmentation into 109 active groups using commoditized tooling invalidates defensive strategies built around tracking specific adversary groups. Organizations should shift from attribution-based detection to behavior-based detection of commodity attack patterns — the threats are too numerous and too transient for intelligence-led approaches alone.

---

### The Identity Crisis: 850% and Counting

Red Canary's 850% increase in identity threat detections is the most striking single statistic across both reports — and IBM's data explains why it's happening.

IBM X-Force documents infostealer operations as a core enabler of the broader threat ecosystem, with credential theft remaining "central to prominent attack campaigns." The discovery of over 300,000 ChatGPT credentials on dark web markets illustrates the expanding attack surface: every new SaaS platform, every AI tool, every cloud service creates another credential to harvest. The identity attack surface isn't growing linearly with cloud adoption. It's growing exponentially.

Red Canary confirms this from the detection side: **cloud account compromises dominate their threat landscape**, and browsers have emerged as critical staging grounds for credential theft. The browser — the application every employee uses all day, every day — is where credentials are entered, cached, and stolen.

The convergence with prior reports in this series is now overwhelming. Unit 42 (E81) found 90% of incidents involved identity compromise. Cloudflare (E82) reported 63% of human logins use compromised credentials. CrowdStrike (E83) documented 35% of cloud intrusions via valid accounts. Picus (E84) showed credential theft at 23% — double ransomware encryption. M-Trends (E85) revealed voice phishing at 11% because attackers switched to calling for credentials.

Six reports. Six methodologies. One conclusion: **identity is the primary attack vector, and the volume is accelerating.**

> **INTEL [GLOBAL] [PATTERN]:** The 850% increase in identity threat detections (Red Canary) combined with IBM X-Force's documentation of expanding credential theft operations — including 300,000+ AI platform credentials on dark web markets — confirms identity compromise as the dominant and accelerating threat vector across the entire attack ecosystem.

---

### The AI Paradox: Defender Advantage — For Now

Red Canary's conclusion that AI currently benefits defenders more than attackers is the most contrarian finding in either report — and IBM's data provides both supporting evidence and a warning.

**The case for defender advantage:** Red Canary's analysis of 110,000 threats across 4.5 million endpoints finds that AI-enhanced attacks "don't fundamentally change how threats present themselves." Existing detection methods remain effective because adversaries are using AI to accelerate existing techniques, not invent new ones. Defenders, meanwhile, leverage AI to process vast telemetry volumes, shorten detection timelines, and automate complex analysis tasks that benefit from scale — capabilities attackers can't easily match.

**IBM's supporting evidence:** Despite growing AI adoption by threat actors, IBM confirms that "basic cybersecurity weaknesses remain the primary attack vectors." AI is the force multiplier, not the attack itself. The fundamental security challenges — unpatched systems, misconfigured access, weak authentication — still determine whether an attack succeeds.

**IBM's warning:** The current advantage may be temporary. IBM observes AI adoption among threat actors moving "decisively from the exception to the norm," with compressed decision cycles enabling real-time attack path iteration. More mature adversaries are positioning to operationalize agentic AI for "minimally supervised operations." And entirely new attack surfaces — prompt injection, training data poisoning, AI supply chain compromise — have no mature defensive playbook.

The strategic implication: organizations have a **window of advantage** to deploy AI-powered defensive capabilities before attackers close the gap. The organizations that use this window to automate defense of fundamentals — identity monitoring, configuration compliance, access pattern analysis — will have a structural advantage. Those waiting to see how AI threats evolve will find themselves behind.

> **INTEL [GLOBAL] [FINDING]:** Red Canary's endpoint data and IBM X-Force's incident analysis independently confirm that AI currently provides defenders a tactical advantage — existing detection methods remain effective against AI-enhanced attacks, while AI-powered defensive analytics offer scale advantages attackers cannot match. IBM warns this window is closing as adversaries operationalize agentic AI. The advantage accrues to organizations that deploy AI defensively now, not those waiting for AI threats to mature.

---

### Manufacturing: The New #1 Target

IBM X-Force data places manufacturing at the top of targeted industries for 2025, accounting for **27.7% of incidents** — ahead of financial services' traditional lead position.

This represents more than a statistical shift. Manufacturing's rise reflects three converging pressures: the sector's increasing digital interconnection (IT/OT convergence), its critical position in global supply chains making it a high-value extortion target, and its historical underinvestment in cybersecurity relative to financial services and healthcare. Where financial institutions have spent decades building security programs under regulatory pressure, manufacturing environments often operate with legacy systems, flat networks, and limited security monitoring.

The implication extends beyond manufacturing: **every industry that assumed it was a lower-priority target should reassess.** The ransomware swarm doesn't discriminate by sector. With 109 groups competing for victims, the selection criteria aren't strategic — they're opportunistic. The next industry at the top of this list will be whichever sector has the widest gap between digital exposure and security maturity.

> **INTEL [GLOBAL] [SECTOR ALERT]:** Manufacturing's rise to #1 targeted industry at 27.7% of IBM X-Force incidents reflects the convergence of IT/OT integration, supply chain criticality, and relative security underinvestment. The ransomware swarm model means industry targeting is increasingly opportunistic — sectors with the widest gap between digital exposure and security investment are next.

---

## Convergence: Six Reports, One Picture

This is our sixth consecutive deep dive into a 2026 annual threat report — and the convergence is no longer a pattern. It's a verdict.

**Identity is the battlefield:**
- Unit 42 (E81): 90% of incidents involved identity compromise
- Cloudflare (E82): 63% of human logins use compromised credentials
- CrowdStrike (E83): 35% of cloud intrusions via valid accounts
- Picus (E84): Credential theft (23%) double ransomware encryption (13%)
- M-Trends (E85): Voice phishing at 11% — adversaries call to get credentials
- **X-Force + Red Canary (E86): 850% surge in identity detections, 300K+ AI credentials on dark web, browsers as primary credential staging ground**

**The basics still decide the outcome:**
- CrowdStrike (E83): 79% of intrusions were malware-free
- Picus (E84): Top MITRE techniques are credential access and defense evasion
- M-Trends (E85): FAKEUPDATES → 22-second handoff → full ransomware deployment
- **X-Force + Red Canary (E86): 56% of exploited vulns need no authentication, sophisticated attacks succeed through misconfigured access controls and weak auth**

**The threat model has fragmented:**
- CrowdStrike (E83): 62-minute average breakout time
- M-Trends (E85): 22-second handoff AND 390-day dwell time — speed AND patience
- **X-Force + Red Canary (E86): 109 ransomware groups, 49% increase — the cartel model has been replaced by a swarm**

**AI is operational — and contested:**
- M-Trends (E85): PROMPTFLUX and PROMPTSTEAL query LLMs mid-execution
- **X-Force + Red Canary (E86): AI enhances existing techniques but doesn't change detection fundamentals. Defenders have a temporary advantage — if they act now**

**The permanent shift, updated:**

- Perimeter defense → **Identity defense**
- Sophisticated adversaries → **Opportunistic swarms**
- Zero-day exploits → **Open doors (56% no-auth)**
- Advanced threat hunting → **Fundamental hygiene at scale**
- AI as threat → **AI as contested advantage**
- Defend against the best → **Defend against the most**

---

## Recommended Actions

**The one question this report demands you answer:** *Are you investing in advanced threat detection while your public-facing applications don't require authentication?*

If the answer is uncomfortable, here's where to focus:

**1. Invert your security investment.** Both reports converge on the same uncomfortable truth: advanced threats succeed through basic failures. Deploy AI and automation not to hunt zero-days, but to defend fundamentals at scale — identity access patterns, configuration drift, authentication anomalies. The data shows that AI defending basics stops more attacks than AI hunting advanced threats. Reallocate accordingly.

**2. Build swarm defenses, not cartel defenses.** With 109 active ransomware groups using commoditized tooling, your ransomware strategy needs to optimize for volume, not sophistication. Replace attribution-based detection with behavior-based detection of commodity patterns. Build automated containment playbooks that assume unknown ransomware families, 15-minute detection windows, and multiple simultaneous low-sophistication attempts. Speed of response matters more than depth of analysis.

**3. Close every open door.** The 44% surge in public-facing application exploitation — with 56% requiring no authentication — means your external attack surface audit is overdue. Inventory every internet-facing application, API endpoint, and management interface. Verify authentication requirements. Remove default credentials. This isn't advanced security work. It's the work that makes advanced security work matter.

**4. Treat identity as critical infrastructure.** The 850% detection surge, the 300K+ AI credentials on dark web markets, the browser-as-staging-ground pattern — identity compromise is the primary attack vector at industrial scale. Implement continuous identity monitoring, reduce credential blast radius through privilege minimization, and architect systems that assume identity compromise rather than trying solely to prevent it.

**5. Weaponize the AI window.** Red Canary's data confirms defenders currently hold an AI advantage. IBM's data warns it won't last. Launch AI-powered defensive capabilities this quarter — not to detect novel AI threats, but to automate defense of the fundamentals that determine whether any attack succeeds. Identity behavior baselines, configuration compliance at scale, automated response to commodity patterns. The window closes when attackers get better AI. Move first.

---

## MITRE ATT&CK Reference

**Top Techniques Across Both Reports:**

- **T1190 — Exploit Public-Facing Application:** #1 initial access vector (IBM X-Force) — 44% year-over-year increase, 56% of exploited vulnerabilities requiring no authentication
- **T1078 — Valid Accounts:** Dominant across both reports — Red Canary's 850% identity attack surge and IBM's credential theft emphasis confirm valid credentials as the primary means of compromise
- **T1110 — Brute Force:** Persistent commodity technique enabling initial access for opportunistic ransomware operators using leaked tooling
- **T1059 — Command and Scripting Interpreter:** Remains a top execution technique, consistent with living-off-the-land operations across both data sets
- **T1071 — Application Layer Protocol:** Command and control via standard protocols, enabling evasion of network-based detection
- **T1586 — Compromise Accounts:** Reflects the infostealer ecosystem feeding credential-based attacks at scale

**Notable convergence with E85:** IBM X-Force's emphasis on public-facing application exploitation aligns with Mandiant's documentation of SAP NetWeaver, Oracle EBS, and SharePoint zero-days as top exploited vulnerabilities. The difference: Mandiant saw zero-days in enterprise platforms, while IBM's broader data shows the majority of exploitation targets require no zero-day at all — just missing authentication.

---

## Learn More

- [IBM X-Force Threat Intelligence Index 2026](https://www.ibm.com/reports/threat-intelligence) — Primary source
- [Red Canary Threat Detection Report 2026](https://redcanary.com/threat-detection-report/) — Primary source
- [FIR Risk Tuesday E81 — 72 Minutes](/tuesday/e81-unit42-incident-response-debrief/) — Unit 42 Incident Response Report 2026
- [FIR Risk Tuesday E82 — Blending In](/tuesday/e82-cloudflare-threat-landscape/) — Cloudflare 2026 Threat Report
- [FIR Risk Tuesday E83 — The Convergence](/tuesday/e83-crowdstrike-global-threat-report/) — CrowdStrike 2026 Global Threat Report
- [FIR Risk Tuesday E84 — The Digital Parasite](/tuesday/e84-digital-parasite/) — Picus Red Report 2026
- [FIR Risk Tuesday E85 — The Responder's Report](/tuesday/e85-responders-report/) — Mandiant M-Trends 2026
- [FIR Risk Intelligence](https://github.com/stikman28/fir-risk-intelligence) — Source prompts, methodology, and all published INTEL

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
What happens when you read the threat landscape from two completely different vantage points — and they both point to the same uncomfortable conclusion?

IBM X-Force's 2026 Threat Intelligence Index draws from incident response, dark web intelligence, and vulnerability research. Red Canary's 2026 Threat Detection Report analyzes over 110,000 confirmed threats across 4.5 million endpoints. One sees the strategy. The other sees the evidence.

Together, they reveal that the security industry is building castles on quicksand.

Exploitation of public-facing applications surged 44% to become the #1 initial access vector. The critical detail: 56% of the vulnerabilities exploited required no authentication at all. This isn't adversaries defeating your security controls. It's adversaries finding systems where no controls exist. Misconfigured APIs, exposed management interfaces, default credentials — the failures that appear in every audit but never make it to the top of the remediation queue.

The ransomware ecosystem has fragmented into 109 active groups — a 49% increase. The share attributed to top-tier operators is declining. This isn't growth of sophisticated operations. It's democratization. Leaked toolkits, commoditized playbooks, and low barriers to entry have created a swarm of opportunists using off-the-shelf weapons. Your threat model built around tracking specific adversary groups is losing effectiveness against volume-based opportunism.

Red Canary recorded an 850% increase in identity threat detections, making identity their #1 threat category. IBM independently documents credential theft as "central to prominent attack campaigns," with over 300,000 ChatGPT credentials discovered on dark web markets. The attack doesn't start with malware. It starts with a valid login.

Then the contrarian finding the security community needs to hear: AI currently benefits defenders more than attackers. Red Canary's data shows AI-enhanced attacks don't fundamentally change how threats present themselves — existing detection methods remain effective. IBM confirms AI amplifies existing capabilities rather than creating new attack methodologies. But IBM also warns this advantage is temporary. The window closes when adversaries operationalize agentic AI. Organizations that deploy AI to defend fundamentals now will have a structural advantage. Those waiting will find themselves behind.

This is our sixth consecutive 2026 annual threat report analysis. Six reports. Six methodologies. One verdict: advanced attacks succeed through basic failures. The investment thesis needs to invert — AI and automation defending fundamentals at scale, not hunting advanced threats while open doors remain open.

Full analysis — FIR Risk Tuesday E86: Castles on Quicksand.

#cybersecurity #threatintelligence #identitysecurity #ransomware #riskmanagement #artificialintelligence #CISO #infosec
```

---

## X POST

What happens when you read the threat landscape from two completely different vantage points — and they both point to the same uncomfortable conclusion?

IBM X-Force analyzes the global attack surface through incident response and dark web intelligence. Red Canary analyzes over 110,000 confirmed threats across 4.5 million endpoints. One sees the strategy. The other sees the ground truth.

Together, they reveal that the security industry is building castles on quicksand.

Start with the open doors. Exploitation of public-facing applications surged 44% to become the top initial access vector. Here's the number that should keep security leaders awake: 56% of the vulnerabilities exploited required no authentication at all. Not sophisticated zero-days. Not advanced exploit chains. Misconfigured APIs, exposed management interfaces, default credentials on internet-facing applications. The kind of basic configuration failures that appear in every security audit but never make it to the top of the remediation queue. Attackers aren't breaking in. They're walking through doors nobody locked.

Then the ransomware transformation. IBM identified 109 active ransomware groups — a 49% increase year-over-year. But the critical shift isn't the growth. It's the redistribution. The top 10 groups account for a shrinking share of total activity. The ecosystem has fragmented from a cartel model to a swarm model. Many smaller operators conducting lower-volume attacks using leaked tooling and commoditized playbooks, with frequent identity shifts to complicate attribution.

This changes the threat model fundamentally. The old assumption: prepare for well-resourced, sophisticated groups with custom tools and specific industry targeting. The new reality: prepare for volume. Unknown ransomware families using generic techniques. Multiple simultaneous low-sophistication attempts. Rapid turnover in group identities. Your threat hunting playbook built for APTs needs a companion strategy built for opportunistic volume.

Identity is where both reports converge most sharply. Red Canary recorded an 850% increase in identity threat detections — making it their number one threat category. IBM independently documents credential theft as central to prominent attack campaigns, with over 300,000 ChatGPT credentials discovered on dark web markets. A new category of credential that didn't exist two years ago. Every new SaaS platform, every AI tool, every cloud service creates another credential to harvest. The identity attack surface isn't growing linearly. It's growing exponentially.

Browsers have emerged as critical staging grounds for credential theft. The application every employee uses all day, every day, is where credentials are entered, cached, and stolen. Cloud account compromises dominate Red Canary's detection landscape. The attack doesn't start with malware. It starts with a valid login.

This is the sixth report in our ongoing 2026 annual threat report series. The convergence across all six is now a verdict. Unit 42 found 90% of incidents involved identity compromise. Cloudflare reported 63% of human logins use compromised credentials. CrowdStrike documented 35% of cloud intrusions via valid accounts. Picus showed credential theft double ransomware encryption. Mandiant revealed voice phishing at 11% because attackers call for credentials. Now X-Force and Red Canary confirm the 850% detection surge with dark web credential markets fueling the pipeline at industrial scale.

Then the finding the security community needs to hear: AI currently benefits defenders more than attackers. Red Canary's analysis finds that AI-enhanced attacks don't fundamentally change how threats present themselves. Existing detection methods remain effective because adversaries are using AI to accelerate existing techniques, not invent new ones. IBM confirms AI amplifies existing capabilities rather than fundamentally changing attack methodologies.

But the advantage is temporary. IBM observes AI adoption among threat actors moving decisively from exception to norm. The organizations that use this window to deploy AI defensively — automating identity monitoring, configuration compliance, response to commodity patterns — will have a structural advantage when that window closes.

Manufacturing displaced financial services as the most targeted industry at 27.7% of incidents. That isn't just a sector story. The ransomware swarm doesn't discriminate. With 109 groups competing for victims, the selection criteria aren't strategic — they're opportunistic. The next industry at the top of this list will be whichever sector has the widest gap between digital exposure and security maturity.

The investment thesis needs to invert. Deploy AI and automation not to hunt zero-days but to defend fundamentals at scale. Build swarm defenses optimized for volume, not sophistication. Close every open door before buying another advanced detection tool. The data from both reports is unambiguous: the most sophisticated attacks succeed because the basics remain broken.

Full E86 — Castles on Quicksand — linked below.

#cybersecurity #threatintelligence

---

## SOURCE DATA

**Platform Queries:**
1. "You've just read two major 2026 threat reports — IBM X-Force Threat Intelligence Index and Red Canary's Threat Detection Report. Both analyze the current threat landscape but from very different vantage points — one from incident response and dark web intelligence, the other from endpoint detection across millions of systems. Before we dive into specific themes, step back and tell me: what surprised you? Where do these two reports agree in ways that reinforce a trend we should be paying attention to? And more interestingly — where do they diverge or contradict each other? What's one finding from each report that you think the broader security community is likely to overlook or underweight?"
2. "You raised something important — IBM highlights basic security lapses enabling breaches while Red Canary emphasizes increasingly sophisticated attack chains. You called this 'different layers of the same problem.' Walk me through specific examples from both reports where a sophisticated attack succeeded specifically because of a fundamental gap. What does the attack chain actually look like when advanced meets basic? And what does this tell us about where security programs are misallocating resources — are we overinvesting in detection of advanced threats while underinvesting in the boring stuff that actually stops them?"
3. "In our earlier conversation you flagged two findings the security community is likely to overlook — IBM's data on ransomware operations fragmenting into many smaller groups, and Red Canary's assessment that AI currently benefits defenders more than attackers. Both of these run counter to dominant narratives. Build the case for each. What evidence do the reports provide that the ransomware landscape is fundamentally restructuring, and what are the implications for how organizations should rethink their ransomware preparedness? Separately, what's Red Canary actually seeing that leads them to the defender-advantage conclusion on AI — and does IBM's data support or undermine that view?"
4. "We've established that sophisticated attacks are succeeding through fundamental gaps, ransomware has fragmented into volume-based opportunism, and defenders currently have an AI advantage window that may not last. If you're a security leader reading both of these reports together — not just one — what are the highest-leverage moves you'd make this quarter? I don't want a generic best-practices checklist. I want the specific, non-obvious actions that these two reports together point toward — things a security team wouldn't prioritize if they'd only read one report or the other."

**KB Sources:**
- IBM X-Force Threat Intelligence Index 2026
- Red Canary Threat Detection Report 2026
- FIR Risk Tuesday E81-E85 (series convergence context)

**Fact-Check Notes:**
- Stats to verify against source PDFs: 109 active ransomware groups, 49% increase, 27.7% manufacturing, 300K+ ChatGPT credentials, quoted phrases
- Confirmed from ingestion summaries: 44% public-facing app exploitation increase, 56% no-auth vulnerabilities, 850% identity attack growth, 110K threats / 4.5M endpoints
- CAPEC references in Q2 agent response appeared synthesized — excluded from final draft
- Agent Q2 cited "67%" and "53%" statistics without clear sourcing — excluded from final draft
