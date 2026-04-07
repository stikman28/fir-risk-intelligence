# FIR Risk Tuesday E87

**Publish Date:** April 7, 2026
**Source:** [Anthropic 2026 Agentic Coding Trends Report](https://www.anthropic.com/research/agentic-coding-trends-2026) & [Anthropic 2026 State of AI Agents Report](https://www.anthropic.com/research/state-of-ai-agents-2026) (2026)
**Analysis:** FIR Risk Platform

---

# FIR Risk E87 — The Agents Have Keys

![FIR Risk E87 - The Agents Have Keys](images/e87-the-agents-have-keys.png)

FIR Risk Advisory | Enterprise Risk Intelligence

---

## Bottom Line

What happens when the fastest-growing category of enterprise software is also the least governed?

Anthropic released two companion reports in April 2026 that, read together, paint a picture every risk leader needs to understand. The *2026 State of AI Agents Report* — a survey of over 500 technical leaders conducted with research firm Material — maps how organizations are actually deploying AI agents today. The *2026 Agentic Coding Trends Report* projects where this technology is heading. One shows the current state. The other shows the trajectory. Together, they reveal that enterprises are handing autonomous AI systems the keys to production environments faster than their security and governance programs can keep up.

Three findings define this paired analysis. First, **57% of organizations now deploy AI agents for multi-stage workflows, with 42% trusting agents to lead development with limited human review** — a delegation of authority that most security programs haven't accounted for. Second, **80% of organizations report measurable financial returns from AI agents, yet integration challenges (46%), data quality issues (42%), and security concerns (40%) remain unresolved** — meaning organizations are scaling systems they know have governance gaps because the ROI is too compelling to wait. Third, **Anthropic's research acknowledges that agentic AI is a dual-use technology that "transforms security in two directions at once"** — the same capabilities that let eSentire compress threat analysis from 5 hours to 7 minutes also let threat actors scale attacks at machine speed.

But the most important finding isn't about AI agents as tools. It's about AI agents as a new category of enterprise identity. These systems hold credentials, access production data, make autonomous decisions, and operate across organizational boundaries. They're the newest employees in your organization — and most security programs are treating them like software licenses rather than privileged users. FIR Risk Platform analysis finds that **only 15% of organizations report confidence in their non-human identity governance** — while 57% are already deploying agents with production credentials. That's not a gap. It's a chasm.

This is a departure from our six-edition annual threat report series (E81-E86). Those reports documented what adversaries are doing today. This one documents what your own organization is building — and the risk surface it creates when agents have the keys but nobody designed the lock.

---

## Key Judgments

**1. Enterprise AI agent adoption has crossed the governance gap.** Anthropic's survey finds 57% of organizations deploy multi-stage agent workflows, 16% have progressed to cross-functional processes spanning multiple teams, and 81% plan to implement more complex agents in 2026. Meanwhile, 46% cite integration with existing systems as their top challenge and 40% flag security or compliance concerns. The adoption curve has outrun the governance curve. Organizations are deploying agents into production with known security gaps because the business returns justify the risk — a calculation that works until it doesn't. *High confidence — based on survey of 500+ technical leaders across company sizes and industries.*

**2. AI agents are becoming autonomous identities without identity governance.** The Agentic Coding report documents agents that work autonomously for extended periods, build complete systems with minimal human intervention, and coordinate across teams through multi-agent architectures. Each of these agents requires credentials, API keys, and access to production systems. But the State of AI report shows that 47% of organizations take a hybrid approach — mixing off-the-shelf and custom-built agents — creating a fragmented identity landscape where no single team controls what agents can access. When 42% of organizations trust agents to lead development with limited human review, the agent's credentials effectively become privileged accounts with minimal oversight. FIR Risk Platform analysis indicates only 15% of organizations report confidence in non-human identity governance — meaning 85% are deploying privileged machine identities without the frameworks to manage them. Unsanctioned AI adoption across non-engineering teams compounds this further, creating **shadow agent identities** that security teams may not even know exist. *High confidence — based on both reports' documentation of agent capabilities and deployment patterns, corroborated by FIR Risk Platform threat analysis.*

**3. The dual-use problem is no longer theoretical.** Anthropic's Agentic Coding Trends Report is transparent about this reality — Trend 8 states: "While agents will benefit defensive uses, they will also benefit offensive uses too." The eSentire case study demonstrates AI compressing expert-level threat analysis from 5 hours to 7 minutes with 95% alignment to senior SOC analysts. The Palo Alto Networks case study shows junior developers completing complex integrations 70% faster. The same acceleration applies to adversaries. Security knowledge is being democratized — any engineer can now perform security reviews, but any attacker can now generate sophisticated exploit chains. The report warns that "agentic cyber defense systems" will need to match "the pace of autonomous threats." We are entering a machine-speed security environment. *High confidence — based on Anthropic's own assessment and case study evidence.*

**4. The delegation shift creates a new class of supply chain risk.** The Economic Index data within the State of AI report reveals that enterprise automation usage jumped from 27% to 39% in eight months — the first time automation exceeded augmentation. Organizations are handing complete tasks to AI, not collaborating on them. Combined with the finding that 47% use hybrid agent approaches (mixing vendor and custom), this creates supply chain dependencies that most third-party risk programs don't assess. An AI agent with access to your customer data, code repositories, and internal APIs represents a concentration of access that would trigger a full security review for any human contractor — but rarely does for software. *Moderate-to-high confidence — automation trend data from Economic Index; supply chain risk assessment is analytical.*

**5. The security talent gap may narrow — but the governance gap will widen.** The Agentic Coding report predicts security knowledge will be "democratized" — any engineer can leverage AI for security reviews, hardening, and monitoring. This is genuinely positive. But the same report warns that "it will become more important for engineers to build in security from the start." The State of AI survey shows 39% of organizations cite employee resistance and training needs as a barrier, and 35% lack internal expertise. Democratized security tools without security governance creates a false sense of protection — more code gets reviewed, but nobody owns the review process for the AI reviewers themselves. *Moderate confidence — based on trend projections and current adoption barriers.*

---

## Three Critical Shifts

Both reports independently document the same three structural changes in how organizations relate to AI — and the security implications are clearest when you read them together:

**From Tools to Teammates.** The Agentic Coding report describes a fundamental shift: engineers are moving "from implementer to orchestrator," managing teams of AI agents rather than writing code directly. The State of AI survey confirms this from the enterprise side — 42% trust agents to lead development, and organizations report AI freeing time across the entire development lifecycle: planning (58%), code generation (59%), testing (59%), and documentation (59%). These aren't productivity tools. They're autonomous actors making implementation decisions. When an agent decides how to implement a feature, which dependencies to use, and how to handle authentication — with limited human review — it's making security-relevant decisions at a scale no individual developer could match.

> **INTEL [GLOBAL] [TREND]:** The shift from AI-as-tool to AI-as-teammate fundamentally changes the enterprise threat model. With 42% of organizations trusting AI agents to lead development with limited human review, security-relevant implementation decisions are increasingly made by systems that aren't subject to security training, awareness programs, or accountability frameworks designed for human developers.

**From Single Access to Distributed Authority.** The Agentic Coding report predicts single agents will evolve into "coordinated teams" — multi-agent architectures where an orchestrator agent delegates to specialized sub-agents for architecture, implementation, testing, and review. The State of AI survey shows this is already happening: 57% deploy multi-stage workflows, and enterprises lead at 62%. Each agent in these architectures needs its own context, credentials, and access scope. The Fountain case study describes "hierarchical multi-agent orchestration" for candidate screening — coordinating sub-agents for document generation and sentiment analysis. When agent architectures distribute authority across multiple autonomous systems, the blast radius of a single compromised credential multiplies. A compromised orchestrator agent doesn't just lose one capability — it compromises every sub-agent in the hierarchy.

> **INTEL [GLOBAL] [TECHNIQUE]:** Multi-agent orchestration architectures — now deployed by 57% of organizations — create hierarchical credential chains where compromising a single orchestrator agent can cascade access across all specialized sub-agents. Traditional identity governance frameworks designed for human-to-system access patterns do not account for agent-to-agent delegation chains.

**From Experimentation to Infrastructure.** The State of AI survey's most striking finding: 80% of organizations say AI agents are already delivering measurable financial returns, and 88% expect continued or increased returns. This isn't pilot-phase investment. It's production infrastructure. The Agentic Coding report confirms the trajectory — long-running agents will work for "days at a time, building entire applications and systems." When AI agents become load-bearing infrastructure — integrated into CI/CD pipelines, customer-facing workflows, and cross-functional business processes — they become high-value targets. The same characteristics that make them valuable (autonomous operation, broad access, cross-system integration) make them attractive targets for adversaries and dangerous vectors for supply chain compromise.

> **INTEL [GLOBAL] [FINDING]:** AI agents have crossed from experimental to production infrastructure — 80% of organizations report measurable ROI and 88% expect continued returns. This transition elevates AI agents from productivity tools to high-value targets. Autonomous operation, broad system access, and cross-functional integration create an attack surface that combines the persistence of infrastructure with the access of privileged users.

---

## Evidence

### The Governance Gap: Adoption Outpacing Controls

The State of AI Agents survey reveals a dangerous asymmetry. On the adoption side, the numbers are unambiguous: 86% of organizations use coding agents across the software development lifecycle, 57% deploy multi-stage agent workflows, and 81% plan to implement more complex agents in 2026. Enterprises lead — 91% adoption for coding agents, 62% for multi-stage workflows.

On the governance side, the picture is less reassuring. The top barriers to AI agent adoption are integration with existing systems (46%), data quality and access (42%), cost of implementation (43%), security and compliance concerns (40%), and employee resistance or training needs (39%). These aren't edge cases. They're the majority experience.

The critical insight is in the ROI data. Despite these unresolved challenges, 80% report measurable financial returns. This creates a rational but dangerous incentive: organizations are scaling agent deployments they know have governance gaps because the returns justify the risk. Every security professional recognizes this pattern — it's the same dynamic that drove cloud adoption ahead of cloud security programs, and mobile deployment ahead of mobile device management.

The difference is speed. Cloud migration played out over a decade. The State of AI survey shows enterprise AI agent adoption moving from experimentation to cross-functional production deployment in months. The governance gap isn't just present — it's accelerating.

> **INTEL [GLOBAL] [TREND]:** Enterprise AI agent adoption has crossed the inflection point — 80% report measurable ROI, 81% plan more complex deployments — while 46% cite unresolved integration challenges and 40% flag security concerns. The rational incentive to deploy despite known gaps mirrors the cloud adoption pattern but is compressing a decade of governance debt into months.

---

### The Identity Problem: Agents as Privileged Users

The convergence of both reports points to a fundamental identity governance challenge that most organizations haven't recognized.

The Agentic Coding report documents agents that operate autonomously for extended periods — Rakuten's test had Claude Code work autonomously for seven hours across 12.5 million lines of code. The report predicts agents will work "for days at a time" in 2026. Each work session requires persistent credentials, access to code repositories, deployment pipelines, and production systems.

The State of AI survey shows where these agents are deployed: software development (57% expect biggest impact), customer service (55%), marketing and sales (46%), supply chain and operations (44%). These aren't sandboxed environments. They're production systems handling customer data, financial transactions, and operational decisions.

The hybrid deployment model compounds the risk. 47% of organizations combine off-the-shelf agents with custom-built components. 21% rely entirely on pre-built agents. 20% build their own using APIs and open-source models. This fragmentation means no single team — security, engineering, or operations — has visibility into the full landscape of agent identities, their credential scopes, or their access patterns.

When the Agentic Coding report describes multi-agent teams where an orchestrator delegates to specialized agents — and these agents work across "frontend, backend, databases, and infrastructure" — the identity surface isn't one agent with broad access. It's a hierarchy of agents, each with its own credentials, coordinating autonomously across system boundaries.

The detection problem amplifies the governance problem. Traditional security tools were designed to monitor human user behavior — login times, access patterns, session durations. AI agents generate high-volume API traffic with dynamic, autonomous behavior patterns that don't fit human baselines. FIR Risk Platform analysis confirms that most security tools cannot reliably distinguish between normal autonomous agent behavior, a compromised agent operating under adversary control, malicious agent spawning, or legitimate-but-anomalous API usage at scale. The tools that would detect a compromised human account are effectively blind to a compromised agent account.

This is the identity governance challenge of the next 12 months: treating AI agents as the privileged users they are — and building the detection capabilities to know when they've been turned.

> **INTEL [GLOBAL] [VULNERABILITY]:** AI agents operating autonomously across production systems — for hours or days at a time — represent a new class of privileged identity that traditional IAM frameworks were not designed to govern. The hybrid deployment model (47% of organizations) fragments visibility across vendor and custom agents, while traditional security monitoring tools cannot reliably distinguish normal agent behavior from compromised agent activity — creating blind spots in credential management, access auditing, and compromise detection.

---

### The Dual-Use Acceleration: Defenders and Attackers at Machine Speed

Anthropic's candor about the dual-use nature of agentic AI deserves attention. Trend 8 of the Agentic Coding report states: "Agentic coding is transforming security in two directions at once."

**The defender case is compelling.** eSentire compressed expert-level threat analysis from 5 hours to 7 minutes, with AI matching senior SOC analysts 95% of the time across 1,000 real-world investigations. Palo Alto Networks accelerated junior developer integration by 70%, with new developers contributing meaningfully "in weeks instead of months" — directly addressing the security talent shortage. The report predicts "security knowledge becomes democratized" — any engineer can deliver security reviews, hardening, and monitoring that previously required specialized expertise.

**The attacker case is equally clear.** As the report notes: "While agents will benefit defensive uses, they will also benefit offensive uses too. In order to defend against this dual-use technology, it will become more important for engineers to build in security from the start." The same capabilities that let eSentire analyze threats at machine speed let adversaries generate, test, and deploy attacks at machine speed. The democratization of security knowledge is symmetric — it lowers barriers for defenders and attackers simultaneously.

**The asymmetry is in the deployment timeline.** Defenders need to integrate AI agents into existing security architectures, navigate procurement cycles, and manage organizational change. Attackers face none of these constraints. The State of AI survey confirms this friction: 46% cite integration challenges, 43% cite implementation costs, 39% cite training needs. Every month of governance delay is a month where adversaries operate with fewer constraints.

This connects directly to our E86 finding: Red Canary and IBM X-Force independently confirmed that AI currently benefits defenders — but the window is closing. Anthropic's adoption data suggests the window is narrower than most organizations assume.

> **INTEL [GLOBAL] [FINDING]:** Anthropic's 2026 research documents the dual-use nature of agentic AI — the same capabilities powering eSentire's 5-hour-to-7-minute threat analysis compression are available to adversaries. The asymmetry favors attackers: defenders face integration challenges (46%), implementation costs (43%), and training needs (39%) that adversaries do not. The defender advantage documented in E86 is real but the deployment friction gap determines how long it lasts.

---

### The Automation Threshold: From Collaboration to Delegation

The Economic Index data embedded in the State of AI report documents a critical inflection point that has direct security implications.

Over eight months, directive conversations — where users delegate complete tasks to AI — jumped from 27% to 39%. For the first time, automation usage exceeds augmentation in enterprise settings. Business API usage shows an even starker pattern: **77% of enterprise interactions are automation patterns** — organizations handing off complete tasks rather than collaborating with AI.

This isn't a productivity metric. It's a trust metric with security consequences. When organizations augment work with AI, humans remain in the decision loop. They review outputs, validate choices, and catch errors — including security-relevant ones. When organizations automate with AI, the human steps back. The agent makes decisions, executes actions, and produces outputs that may not receive meaningful human review before reaching production.

The Agentic Coding report describes this exact dynamic: engineers describe using AI for tasks that are "well-defined, or repetitive, while keeping high-level design decisions and anything requiring organizational context or 'taste' for themselves." But when 42% of organizations trust agents to lead development with limited human review, the boundary between "well-defined tasks" and "security-relevant decisions" is drawn by the agent, not the human.

The research reveals a "collaboration paradox" — engineers use AI in 60% of their work but can only fully delegate 0-20% of tasks. This gap represents the current safety margin. As agent capabilities improve and organizations become more comfortable with delegation, that margin will compress. The security implications scale with the delegation.

> **INTEL [GLOBAL] [TREND]:** Enterprise AI usage has crossed the automation threshold — directive task delegation (39%) now exceeds augmentation (27%) for the first time, with 77% of enterprise API interactions being automation patterns. This shift from human-in-the-loop to human-on-the-loop reduces security review coverage at the exact moment agent access to production systems is expanding.

---

### The Supply Chain Multiplier: Agents Inside the Perimeter

The State of AI report documents a supply chain risk vector that connects directly to the threat landscape documented in our E86 convergence analysis.

47% of organizations take a hybrid approach to AI agents — combining off-the-shelf solutions with custom-built components. Another 21% rely entirely on pre-built vendor agents. These agents operate inside the security perimeter, with access to code repositories, customer data, and production infrastructure.

Consider the attack surface: an off-the-shelf AI agent from a third-party vendor, integrated into your CI/CD pipeline, with credentials to your code repository and deployment infrastructure. That agent's model provider, API endpoints, training data, and update mechanisms are all potential compromise vectors. If the agent is part of a multi-agent architecture (deployed by 57% of organizations), compromising the vendor agent could cascade through the entire orchestration chain.

The Agentic Coding report amplifies this concern by documenting that agents are extending beyond engineering teams into "cybersecurity, operations, design, and data science." Legal teams, marketing teams, and operations teams are building their own agent workflows — each creating new integration points, credential stores, and data access patterns that security teams may not even know exist.

The Novo Nordisk case study in the State of AI report illustrates the scope: their NovoScribe platform uses Claude on Amazon Bedrock with MongoDB Atlas, combining retrieval-augmented generation with domain expert-approved content to produce regulatory documentation. This is precisely the kind of high-stakes, data-rich, compliance-sensitive workflow that represents both immense value and immense risk if the agent's access is compromised.

The organizations in our E86 analysis that are losing to identity-based attacks — the 850% surge in identity threats, the 300K+ AI credentials on dark web markets — are the same organizations now creating an entirely new category of machine identity to defend.

> **INTEL [GLOBAL] [SECTOR ALERT]:** The hybrid AI agent deployment model (47% of organizations) creates a new supply chain attack surface where third-party vendor agents operate inside security perimeters with production credentials. Combined with the 850% surge in identity attacks documented in E86, machine identities for AI agents represent the next frontier of credential-based compromise — and most third-party risk programs don't assess AI agent access as a supply chain dependency.

---

## Convergence: The Agent Threat Model

Our E81-E86 series documented the threat landscape as it exists today. This edition documents the risk surface organizations are building for tomorrow. The convergence is direct:

**Identity is the battlefield — and agents are new combatants:**
- E86 convergence: Identity attacks surged 850%, credentials are the primary weapon
- **E87: AI agents require persistent credentials with broad access to production systems. 47% of organizations deploy hybrid agent models with fragmented identity governance. Multi-agent architectures create credential chains that multiply blast radius.**

**The basics still decide the outcome — including for agent security:**
- E86: 56% of vulnerabilities require no authentication to exploit
- **E87: 42% of organizations trust agents to lead development with limited review. 77% of enterprise AI interactions are automation (not collaboration). The "basics" now include agent identity governance, credential scoping, and autonomous access controls — and most organizations haven't started.**

**The threat model continues to fragment:**
- E86: 109 ransomware groups, swarm model replaces cartel model
- **E87: Anthropic's research documents agentic AI as dual-use — same capabilities empower defenders and attackers. The 46% integration friction for defenders doesn't apply to adversaries. Machine-speed offense will meet governance-speed defense.**

**AI is operational — and the stakes just escalated:**
- E86: AI benefits defenders today, but the window is closing
- **E87: 80% of organizations report measurable AI agent ROI. 88% expect continued returns. 81% plan more complex deployments. AI agents aren't optional — they're infrastructure. The security question is no longer "should we deploy agents?" but "can we govern what we've already deployed?"**

**The updated permanent shift:**

- Identity defense → **Machine identity defense**
- Opportunistic swarms → **AI-accelerated opportunistic swarms**
- Open doors → **Open doors + new doors (agent access points)**
- Fundamental hygiene at scale → **Agent governance at scale**
- AI as contested advantage → **AI as both asset and attack surface**
- Defend against the most → **Govern what you deploy, defend against what others deploy**

---

## Recommended Actions

**The one question this report demands you answer:** *Do you know how many AI agents have credentials to your production systems — and who reviews what they do with that access?*

If the answer is uncomfortable, here's where to focus:

**1. Inventory every AI agent identity.** Before you can govern agents, you need to know they exist. Catalog every AI agent — vendor, custom, and hybrid — operating in your environment. Map their credentials, access scopes, data touchpoints, and integration chains. Most organizations will discover agent deployments they didn't know existed, especially in non-engineering teams building their own workflows. This is your external attack surface audit, but for the inside.

**2. Apply identity governance to machine identities.** AI agents that access production systems, customer data, or code repositories should be subject to the same identity governance as privileged human users — credential rotation, least-privilege access, session monitoring, and anomaly detection. Move beyond static API keys to dynamic, context-aware authentication using OIDC and OAuth tokens with scoped permissions that adjust based on agent task and data sensitivity. Classify agents by autonomy level and risk profile. The 850% surge in identity attacks (E86) is about to meet an entirely new category of identity. Architect agent access controls before adversaries discover you haven't.

**3. Build review gates into the delegation chain.** The automation threshold has crossed — 77% of enterprise AI interactions are delegation, not collaboration. Insert security review gates at the boundaries where agent autonomy meets production impact. This doesn't mean reviewing every agent action. It means defining the blast radius of each agent's autonomous scope and requiring human authorization for actions that exceed it. The Agentic Coding report's concept of "intelligent collaboration" — agents that learn when to ask for help — should be a security design requirement, not just a productivity feature.

**4. Assess AI agents as supply chain dependencies.** Every third-party AI agent in your environment is a supply chain dependency — with access to your data, your systems, and your customers. Include AI agent vendors in your third-party risk assessment program. Evaluate their model security, update mechanisms, data handling, and credential management. The 47% hybrid deployment model means most organizations have a mix of vendor and custom agents — and no unified view of the supply chain risk.

**5. Deploy agentic defense before adversaries deploy agentic offense.** The dual-use reality documented in Anthropic's research validates what E86 established: the defender AI advantage is real but temporary. The eSentire model (5 hours to 7 minutes for threat analysis, 95% expert alignment) should be the benchmark, not the exception. Deploy AI-powered security operations this quarter — not to detect AI threats specifically, but to match the speed at which adversaries will use AI to exploit every other vulnerability in your environment.

---

## MITRE ATT&CK Reference

**Techniques Most Relevant to AI Agent Risk:**

- **T1078 — Valid Accounts:** AI agents with persistent production credentials create a new category of valid account that adversaries can target — through agent compromise, credential theft from agent keystores, or hijacking agent-to-agent authentication chains
- **T1199 — Trusted Relationship:** Third-party AI agents operating inside security perimeters exploit trusted vendor relationships — the same vector documented in supply chain attacks but with autonomous operational capability
- **T1098 — Account Manipulation:** Multi-agent orchestration architectures create delegation chains where compromising an orchestrator agent can modify sub-agent permissions and access scopes
- **T1059 — Command and Scripting Interpreter:** AI coding agents with autonomous execution capability represent a legitimate but exploitable command execution path — agents that write and execute code are, by design, command interpreters
- **T1195 — Supply Chain Compromise:** Hybrid agent deployment models (47% of organizations) introduce supply chain risk through vendor agent updates, model changes, and integration dependencies
- **T1053 — Scheduled Task/Job:** Long-running autonomous agents operating on schedules or in CI/CD pipelines create persistent execution mechanisms that blend legitimate automation with potential compromise

**Connection to E86 series:** The MITRE techniques most relevant to AI agent risk (Valid Accounts, Trusted Relationship, Supply Chain Compromise) are the same techniques driving the identity-based attack surge documented across E81-E86. The agent risk surface doesn't create new attack categories — it amplifies existing ones by adding machine identities to the identity attack surface that is already under siege.

---

## Learn More

- [Anthropic 2026 Agentic Coding Trends Report](https://www.anthropic.com/research/agentic-coding-trends-2026) — Primary source
- [Anthropic 2026 State of AI Agents Report](https://www.anthropic.com/research/state-of-ai-agents-2026) — Primary source
- [FIR Risk Tuesday E86 — Castles on Quicksand](/tuesday/e86-castles-on-quicksand/) — IBM X-Force + Red Canary convergence
- [FIR Risk Tuesday E85 — The Responder's Report](/tuesday/e85-responders-report/) — Mandiant M-Trends 2026
- [FIR Risk Tuesday E84 — The Digital Parasite](/tuesday/e84-digital-parasite/) — Picus Red Report 2026
- [FIR Risk Tuesday E83 — The Convergence](/tuesday/e83-crowdstrike-global-threat-report/) — CrowdStrike 2026 Global Threat Report
- [FIR Risk Intelligence](https://github.com/stikman28/fir-risk-intelligence) — Source prompts, methodology, and all published INTEL

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Do you know how many AI agents have credentials to your production systems?

Anthropic just released two companion reports that every security leader needs to read together. The 2026 State of AI Agents Report surveyed over 500 technical leaders. The 2026 Agentic Coding Trends Report projects where the technology is heading. One shows the current state. The other shows the trajectory.

Together, they reveal that enterprises are handing autonomous AI systems the keys to production environments faster than their security programs can govern them.

The adoption numbers are staggering. 57% of organizations now deploy AI agents for multi-stage workflows. 42% trust agents to lead development with limited human review. 86% use coding agents across the full software development lifecycle. 81% plan to implement more complex agents this year.

The governance numbers tell a different story. 46% cite integration with existing systems as their top challenge. 42% flag data quality and access issues. 40% have security or compliance concerns. These aren't edge cases — they're the majority experience.

Here's the dangerous part: 80% report measurable financial returns despite these unresolved gaps. Organizations are scaling agent deployments they know have governance problems because the ROI is too compelling to wait. Every security leader recognizes this pattern — it's the same dynamic that drove cloud adoption ahead of cloud security. The difference is speed. This is compressing a decade of governance debt into months.

Anthropic's Agentic Coding Trends Report is transparent about this: agentic AI "transforms security in two directions at once." The same capabilities that let eSentire compress expert threat analysis from 5 hours to 7 minutes — with 95% alignment to senior SOC analysts — are available to adversaries. Security knowledge is being democratized symmetrically. It lowers barriers for defenders and attackers simultaneously.

But the real risk isn't dual-use capability. It's the identity problem. AI agents require persistent credentials, broad access to production systems, and operate autonomously for hours or days. 47% of organizations use a hybrid model mixing vendor and custom agents — fragmenting visibility across agent identities. Multi-agent architectures create credential chains where compromising one orchestrator cascades access across every sub-agent.

These are privileged users. Most organizations are governing them like software licenses. Only 15% of organizations report confidence in non-human identity governance — while 57% are deploying agents with production credentials. Traditional security tools can't reliably distinguish normal agent behavior from compromised agent activity. And unsanctioned AI adoption across business teams is creating shadow agent identities that security teams don't even know exist.

Enterprise AI automation usage just crossed 39% — exceeding augmentation for the first time. 77% of enterprise AI interactions are now full task delegation, not collaboration. The human is leaving the loop at the exact moment agent access to production systems is expanding.

The question facing security leaders in 2026 isn't whether to deploy AI agents. It's whether you can govern what you've already deployed before adversaries discover you haven't.

Full analysis — FIR Risk Tuesday E87: The Agents Have Keys.

#cybersecurity #AIagents #identitysecurity #riskmanagement #enterpriseAI #agenticAI #CISO #infosec
```

---

## X POST

Do you know how many AI agents have credentials to your production systems?

Anthropic just released two companion reports that, read together, paint a picture every security leader needs to understand. The State of AI Agents Report surveyed over 500 technical leaders on how organizations are actually deploying AI agents. The Agentic Coding Trends Report projects eight trends that will define where this technology goes in 2026.

One shows the current state. The other shows the trajectory. Together, they reveal that enterprises are handing autonomous AI systems the keys to production environments faster than their security programs can govern them.

Start with the adoption. 57% of organizations now deploy AI agents for multi-stage workflows spanning multiple steps and systems. 42% trust agents to lead development with limited human review. 86% use coding agents across the full software development lifecycle — from planning and ideation through code generation, testing, documentation, and review. Enterprises lead at 91% adoption. 81% plan to implement more complex agents this year.

These aren't experimental pilots. 80% report measurable financial returns. 88% expect continued or increased returns. AI agents have crossed from tooling to infrastructure.

Now the governance side. 46% cite integration with existing systems as their top challenge. 42% flag data quality and access issues. 43% point to implementation costs. 40% have security or compliance concerns. 39% face employee resistance and training needs.

The dangerous asymmetry: organizations are scaling agent deployments they know have governance gaps because the ROI is too compelling to wait. Every security leader recognizes this pattern. Cloud adoption ran ahead of cloud security programs for a decade. Mobile deployment outpaced mobile device management. AI agent adoption is compressing that same governance gap from years into months.

Then the dual-use reality. Anthropic's Agentic Coding Trends Report is transparent about this: agentic AI transforms security in two directions at once. The same capabilities helping defenders help attackers.

The evidence on the defender side is compelling. eSentire compressed expert-level threat analysis from 5 hours to 7 minutes, with AI matching their most senior SOC analysts 95% of the time across 1,000 real-world investigations. Palo Alto Networks accelerated junior developer onboarding by 70%. The report predicts security knowledge will be democratized — any engineer will be able to perform security reviews that previously required specialized expertise.

But the democratization is symmetric. It lowers barriers for defenders and attackers simultaneously. And the deployment asymmetry favors attackers: defenders face integration challenges, procurement cycles, and organizational change management. Adversaries face none of these constraints.

This connects directly to our E86 analysis. Red Canary and IBM X-Force confirmed that AI currently benefits defenders, but the window is closing. Anthropic's data suggests the window may be narrower than most organizations assume — because the friction is on the defender side.

But here's the finding that should reshape how security teams think about AI agents: the identity problem.

AI agents operating in production require persistent credentials. They access code repositories, deployment pipelines, customer databases, and internal APIs. They operate autonomously for hours — Rakuten tested Claude Code working independently for seven hours across 12.5 million lines of code. The Agentic Coding report predicts agents will work for days at a time in 2026.

47% of organizations use a hybrid approach — mixing off-the-shelf vendor agents with custom-built components. Multi-agent architectures are already deployed by 57% of organizations, where orchestrator agents delegate to specialized sub-agents for different functions. Each agent in these architectures needs its own credentials and access scope.

This is a machine identity problem at enterprise scale. And it's landing in organizations that are already losing the identity fight. Our E86 analysis documented an 850% surge in identity attack detections, 300,000 AI platform credentials on dark web markets, and six consecutive annual threat reports confirming that credentials are the primary weapon of compromise.

Now add a new category of identity to defend: autonomous AI agents with production access, persistent credentials, and limited human oversight. Operating inside your security perimeter through trusted vendor relationships that most third-party risk programs don't assess for AI agent access.

The Economic Index data within the State of AI report reveals the final piece. Enterprise automation usage jumped from 27% to 39% in eight months — the first time automation exceeded augmentation. 77% of enterprise AI interactions are now full task delegation, not collaboration. The human is leaving the loop.

When organizations augment work with AI, humans remain in the decision chain. They review outputs and catch errors, including security-relevant ones. When organizations automate with AI — which is now the dominant pattern — the agent makes decisions and executes actions that may not receive meaningful human review before reaching production.

The Agentic Coding report describes a collaboration paradox: engineers use AI in 60% of their work but can only fully delegate 0-20% of tasks. That gap is the current safety margin. As agents improve and organizations grow more comfortable with delegation, the margin compresses. The security implications scale with the delegation.

Five things security leaders should do this quarter:

Inventory every AI agent identity in your environment — vendor, custom, and hybrid. Most organizations will discover agents they didn't know existed, especially in non-engineering teams.

Apply the same identity governance to machine identities that you apply to privileged human users. Credential rotation, least-privilege access, session monitoring, anomaly detection.

Build security review gates at the boundaries where agent autonomy meets production impact. Not reviewing every action — defining the blast radius of each agent's scope and requiring authorization when it exceeds boundaries.

Assess AI agent vendors as supply chain dependencies with the same rigor as any third party with access to your production data and systems.

Deploy agentic defense now. The eSentire benchmark — 5 hours to 7 minutes, 95% expert alignment — should be the standard, not the exception. Match machine-speed offense with machine-speed defense before the window closes.

The question isn't whether to deploy AI agents. It's whether you can govern what you've already deployed.

Full E87 — The Agents Have Keys — linked below.

#cybersecurity #AIagents

---

## SOURCE DATA

**Platform Queries:**
1. "You've read two new Anthropic reports released in April 2026 — the 2026 Agentic Coding Trends Report (8 trends defining how coding agents reshape software development) and the 2026 State of AI Agents Report (survey of 500+ technical leaders on enterprise AI agent deployment). These aren't cybersecurity reports — they're AI industry reports from the model vendor itself. But they contain significant security and risk implications. Before we get into specific themes, tell me: what surprised you from a risk perspective? Where do these two reports converge on findings that should alarm a security leader? And what's the most important finding that the AI community is likely to celebrate but the security community should scrutinize?"
2. "You raised the identity governance gap — agents operating as privileged users without identity governance frameworks. Build that case with specific evidence from both reports. Walk me through the attack surface: what does a multi-agent architecture actually look like from an adversary's perspective? What credentials do these agents hold, what systems do they access, and where are the weakest links in the delegation chain? Connect this to our E86 findings on identity attacks — how does the 850% surge in identity threats intersect with organizations creating an entirely new category of machine identity?"
3. "Anthropic's own Trend 8 warns about dual-use risk — same capabilities for defenders and attackers. But the State of AI report is overwhelmingly optimistic about ROI and adoption. Examine the tension between these two messages. What does the survey data tell us about whether organizations are actually addressing the security implications, or whether the ROI narrative is drowning out the risk narrative? Use specific numbers from both reports. And assess: given the deployment friction data (46% integration challenges, 43% costs, 39% training), does the asymmetry favor defenders or attackers in 2026?"
4. "We've established that AI agents create a new identity attack surface, the dual-use problem is accelerating, and governance is lagging adoption by months. If you're a CISO reading both reports together — connecting them to our E81-E86 threat landscape series — what are the highest-leverage moves you'd make this quarter? Not generic AI governance frameworks. Specific actions that address the intersection of agent deployment patterns documented in these reports and the active threat landscape documented in our series."

**KB Sources:**
- Anthropic 2026 Agentic Coding Trends Report
- Anthropic 2026 State of AI Agents Report
- Anthropic 2025 Economic Index (embedded in State of AI report)
- FIR Risk Tuesday E81-E86 (series convergence context)

**Fact-Check Notes (verified against source PDFs):**
- CONFIRMED: 57% multi-stage workflows, 16% cross-functional, 42% trust agents to lead with limited review, 81% plan more complex agents, 80% measurable ROI, 88% expect continued returns
- CONFIRMED: 46% integration challenges, 42% data quality, 43% cost, 40% security/compliance, 39% employee resistance
- CONFIRMED: 47% hybrid approach, 21% off-the-shelf only, 20% custom build
- CONFIRMED: 86% use coding agents across SDLC, enterprises at 91%
- CONFIRMED: eSentire 5 hours to 7 minutes, 95% alignment, 1,000 investigations
- CONFIRMED: Palo Alto Networks junior developers 70% faster, weeks instead of months
- CONFIRMED: Rakuten 12.5 million lines, 7 hours autonomous, 99.9% accuracy
- CONFIRMED: Economic Index automation 27% to 39%, 77% enterprise automation patterns
- CONFIRMED: Trend 8 dual-use quote: "While agents will benefit defensive uses, they will also benefit offensive uses too"
- CONFIRMED: Collaboration paradox: 60% usage, 0-20% full delegation
- CONFIRMED: 500+ technical leaders surveyed with Material research firm
- NOTE: Report URLs are placeholder — actual Anthropic publication URLs should be verified at time of publish

**FIR Risk Platform Agent Analysis (supplemental):**
- Agent query: "What documented incidents, emerging threat patterns, or framework guidance exist for governing autonomous AI agents as privileged machine identities — and where are the biggest blind spots?"
- Key findings incorporated: 15% non-human identity governance confidence, shadow agent identities from unsanctioned adoption, detection gap (traditional tools blind to compromised agent behavior), emerging agentic identity management frameworks (OIDC/OAuth dynamic auth), MITRE ATT&CK alignment for agent-specific attack patterns
- Agent classification: Both source documents classified as `industry_intelligence` / `research` — Anthropic's reports focus on AI adoption and capability (as expected from an AI developer). FIR Risk adds the security and risk analysis layer, which is the value of E87.
