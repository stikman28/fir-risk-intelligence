# FIR Risk Tuesday E79

**Publish Date:** February 17, 2026
**Source:** [GTIG AI Threat Tracker: Distillation, Experimentation, and (Continued) Integration of AI for Adversarial Use](https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use) (February 12, 2026)
**Analysis:** FIR Risk Platform

---

# FIR Risk E79 — Same AI, Different Mission

![FIR Risk E79 - GTIG AI Threat Tracker](images/E79-gtig-ai-threat-tracker.png)

By FIR Risk Platform | Cybersecurity Risk Intelligence

---

## What You Need to Know

Google Threat Intelligence Group just published their latest AI Threat Tracker — and the findings should change how every security leader thinks about AI deployment.

In Q4 2025, GTIG documented government-backed threat actors from **China, Iran, North Korea, and Russia** actively misusing Google's Gemini AI across the entire attack lifecycle. Not just reconnaissance. Not just phishing. From initial access to malware development to command and control.

And this report introduced something new: **malware that calls AI APIs at runtime to generate its own code.** The line between AI tool and AI weapon just disappeared.

> **INTEL [GLOBAL THREAT]:** AI platforms are becoming attack infrastructure. State-sponsored actors from China, Iran, and North Korea are weaponizing LLMs like Gemini for full-lifecycle attacks — from AI-generated phishing (T1566) to runtime API-based malware (HONESTCUE/COINBAIT). Underground services like Xanthorox enable model extraction and jailbreaking, creating scalable, evasive threats. Defenders face attribution challenges and detection fatigue from polymorphic, AI-generated attacks.

---

## The Model Is the Target: 100,000 Prompts

Before we get to who's using AI — someone is trying to steal it.

Google DeepMind and GTIG identified a surge in **model extraction attacks**, also known as "distillation attacks." Adversaries systematically probe frontier AI models to clone their proprietary reasoning capabilities. One identified campaign sent **over 100,000 prompts** to Gemini — attempting to replicate its reasoning ability across non-English languages and a wide variety of tasks.

This isn't hypothetical research. It's industrial-scale intellectual property theft.

The attackers aren't nation-states. They're **private sector companies and researchers** seeking to clone proprietary logic and specialized training data. While GTIG has not observed successful extraction of frontier models by APT actors, the technique is proven and the scale is growing.

For any organization that has fine-tuned a model for competitive advantage — financial analysis, legal reasoning, medical diagnosis — this is your risk. Your model's logic is extractable through its API. The same black-box attack that targets Gemini can target yours.

> **INTEL [EMERGING RISK]:** Model extraction attacks ("distillation attacks") are rising as a method of AI intellectual property theft. One campaign used 100,000+ prompts to attempt replication of Gemini's reasoning. Organizations deploying custom AI models should monitor API access for extraction patterns and implement rate limiting on inference endpoints.

---

## Four Nations, One Playbook: APTs Weaponize Gemini

GTIG documented specific government-backed threat actors misusing Gemini across the attack lifecycle. The details are striking — not for their sophistication, but for how *operational* AI has become in state-sponsored campaigns.

### China: The Most Prolific

China leads in both volume and variety. GTIG tracked at least four distinct groups:

- **APT31** employed a highly structured approach — prompting Gemini with an expert cybersecurity persona to automate vulnerability analysis, WAF bypass techniques, and SQL injection testing against specific US-based targets. They fabricated scenarios involving Hexstrike MCP tooling to generate penetration test prompts.

- **UNC795** relied on Gemini throughout their *entire* attack lifecycle. GTIG observed the group engaging with Gemini multiple days a week to troubleshoot code, conduct research, and build an **AI-integrated code auditing capability** — a clear move toward agentic AI for intrusion support.

- **APT41** leveraged Gemini for malware tooling development, including knowledge synthesis, real-time troubleshooting, and code translation between architectures.

- **Temp.HEX** used Gemini and other AI tools to compile detailed profiles on individuals in Pakistan and map separatist organizations across multiple countries.

### Iran: The Social Engineer

**APT42** stands out for how deeply it has integrated AI into social engineering. The group feeds Gemini target biographies to craft believable personas and engagement scenarios. It uses Gemini for translation, cultural context, and researching non-native language phrases — erasing the traditional "tells" that once made phishing detectable.

But APT42 isn't just phishing. GTIG observed it actively developing offensive tools with Gemini: a Python-based Google Maps scraper optimized for Farsi, a SIM card management system in Rust, a covert screen mirroring client for Windows, and a proof-of-concept exploit for **CVE-2025-8088** (WinRAR).

### North Korea: The Recruiter

**UNC2970** has consistently focused on impersonating corporate recruiters to target defense and cybersecurity professionals. The group uses Gemini to synthesize OSINT, profile high-value targets, map organizational hierarchies, and identify specific technical job roles and salary information — building the components for tailored, high-fidelity phishing personas.

### The One That Connected to Real Attacks

**UNC6418**, an unattributed actor, used Gemini to gather sensitive account credentials and email addresses. Shortly after, GTIG observed the actor **target those exact accounts** in a phishing campaign focused on Ukraine and the defense sector. This is the clearest example of AI-augmented reconnaissance translating directly into operational targeting.

| Threat Actor | Nation | Primary AI Use |
|-------------|--------|----------------|
| **APT31** | China | Vulnerability analysis, WAF bypass, SQL injection |
| **UNC795** | China | Full lifecycle: recon, weaponization, C2, code auditing |
| **APT41** | China | Malware development, code translation |
| **Temp.HEX** | China | Target profiling, organizational mapping |
| **APT42** | Iran | Social engineering, persona crafting, offensive tool dev |
| **UNC2970** | North Korea | Recruiter impersonation, defense sector profiling |
| **UNC6418** | Unattributed | Credential harvesting → Ukraine/defense phishing |

> **INTEL [THREAT ALERT]:** Seven tracked threat actor groups from four nations are actively using Gemini to accelerate cyber operations. China-linked APT31 is using AI personas to automate vulnerability research against US targets. Iran-linked APT42 is building offensive tools with AI assistance. UNC6418's Gemini reconnaissance translated directly into a phishing campaign against Ukraine's defense sector. AI is now operational infrastructure for state-sponsored campaigns.

---

## Malware That Writes Itself: HONESTCUE and COINBAIT

This is where the report gets genuinely new.

### HONESTCUE: AI-Generated, Fileless, In-Memory

In September 2025, GTIG identified **HONESTCUE**, a downloader and launcher framework that sends a prompt to Google Gemini's API and receives C# source code as the response. The malware then:

1. Calls Gemini API to generate second-stage code
2. Uses the legitimate .NET **CSharpCodeProvider** framework to compile the code
3. Executes the payload **directly in memory** — no files written to disk
4. Downloads and executes a third-stage payload from **Discord CDN**

Every infection generates unique code. There are no static signatures to detect. The traffic to Gemini looks like normal API usage. And the fileless execution leaves no artifacts for forensic analysis.

GTIG hasn't attributed HONESTCUE to an existing threat cluster, but the iterative progression of samples and single VirusTotal submitter suggest a single actor or small group in the proof-of-concept stage.

The proof-of-concept stage. That's the part that matters. This is early.

### COINBAIT: Phishing Kits Built by AI

GTIG also identified **COINBAIT**, a phishing kit whose construction was likely accelerated by AI code generation tools. The evidence:

- Built using the **Lovable AI** platform (identified by lovableSupabase client and lovable.app image hosting)
- Wrapped in a full **React Single-Page Application** with complex state management — indicative of high-level AI prompts like "Create a Coinbase-style UI for wallet recovery"
- Verbose, developer-oriented **`? Analytics:`** log messages left in the source code — a unique fingerprint of AI-generated code
- Linked to **UNC5356**, a financially motivated threat actor

COINBAIT masquerades as a major cryptocurrency exchange, targeting passwords, MFA backup codes, and account recovery keys. It hosts on Supabase (a legitimate BaaS platform) to bypass network security filters that would block suspicious domains.

> **INTEL [TECHNIQUE]:** HONESTCUE represents a paradigm shift: malware that calls AI APIs at runtime to generate fileless, unique payloads. Traditional signature-based detection is ineffective. COINBAIT demonstrates that AI coding platforms can accelerate phishing kit development to production quality. Defenders should monitor for anomalous AI API traffic patterns and implement behavioral detection for in-memory code compilation.

---

## Your Trust Is Their Infrastructure

GTIG documented a campaign where threat actors abuse the **public sharing feature** of AI chat platforms to deliver malware. The technique is called ClickFix, and it works like this:

1. Attacker crafts a malicious command that installs malware
2. Attacker manipulates an AI service into presenting it as a legitimate fix (e.g., "clearing disk space")
3. Attacker creates a **shareable link** to the AI conversation — now hosted on a trusted domain
4. Victim finds the link via malicious ads, clicks through, and copies the command into their terminal

The campaign targets both Windows and macOS, delivering variants of **ATOMIC**, an information stealer that harvests browser data, cryptocurrency wallets, and files from Desktop and Documents folders. The threat actors have used **ChatGPT, CoPilot, DeepSeek, Gemini, and Grok** — every major AI platform.

The genius is in the trust chain. The malicious instructions are hosted on Google's infrastructure, or OpenAI's, or Microsoft's. Your security tools trust those domains. Your users trust those brands. That trust is the weapon.

Meanwhile, underground services are commercializing AI misuse. **Xanthorox** advertises itself as a custom offensive AI capable of autonomous malware generation. GTIG investigated and found it's not custom at all — it's **commercial models including Gemini**, stitched together via MCP servers using open-source tools (Crush, Hexstrike AI, LibreChat-AI, Open WebUI). The underground isn't building new AI. It's wrapping stolen access to yours.

> **INTEL [TREND]:** AI chat platforms are becoming attack infrastructure. ClickFix campaigns hosted on Gemini, ChatGPT, and other trusted platforms bypass traditional domain-based security controls. Underground services like Xanthorox commoditize AI misuse using stolen API keys and open-source wrappers — not custom models. The barrier to AI-augmented attacks is falling, fast.

---

## What This Means for You

**If you deploy AI models:** Your proprietary logic is extractable. Monitor API access patterns for distillation attacks. Implement rate limiting and anomaly detection on inference endpoints. A custom model tuned for financial analysis or coding could be cloned by a competitor — or an adversary seeking to replicate capabilities without guardrails.

**If you're a CISO:** The phishing you trained your team to spot is about to get much harder to detect. AI-generated lures are culturally nuanced, grammatically perfect, and personalized from OSINT. "Rapport-building phishing" — multi-turn conversations that build trust before delivering a payload — is now documented at the state-sponsored level. Rethink your awareness programs.

**If you run security operations:** Signature-based detection won't catch AI-generated malware. HONESTCUE generates unique code every execution. COINBAIT was built by an AI platform. Your detection needs to be behavioral — monitor for in-memory code compilation, anomalous AI API traffic, and process chains that don't match your baseline.

**If you use AI chat platforms:** Your shared conversations can be weaponized. ClickFix campaigns are hosted on the AI platforms your team uses every day. Establish policies for evaluating shared AI links the same way you evaluate email links.

---

## What We're Watching

**HONESTCUE evolution.** It's in proof-of-concept stage now. When it matures — or when the technique is adopted by a funded APT — the implications for detection are severe. AI-generated, fileless, polymorphic malware is the next frontier.

**Agentic AI for offense.** GTIG observed interest in agentic AI capabilities — autonomous multi-step operations without human oversight. APT31 and UNC795 are already experimenting. The jump from "AI-assisted" to "AI-autonomous" attacks is coming.

**API key economics.** Stolen AI API keys are a growing underground commodity. As organizations deploy more AI infrastructure, compromised keys enable adversaries to weaponize your compute budget for their operations.

**Model extraction at scale.** 100,000 prompts in one campaign. As frontier models become more valuable, extraction attacks will become more sophisticated — and the targets won't just be Google.

---

## The Bottom Line

Google just showed us the dashboard of how threat actors are using AI. Not in theory. Not in a red team exercise. In observed operations, tracked to named threat actors, across four nations.

The AI your organization is deploying for productivity is the same AI being weaponized for reconnaissance, phishing, malware development, and infrastructure attacks. The tools are identical. The missions are not.

The question isn't whether to deploy AI — that ship sailed. The question is whether your security program has adapted to a world where AI is simultaneously your most powerful tool and your adversary's most powerful weapon.

Same AI. Different mission. Plan accordingly.

---

Find all editions: [firrisk.ai/tuesday](https://firrisk.ai/tuesday/)

All 2026 newsletters and source materials: [github.com/stikman28/fir-risk-intelligence](https://github.com/stikman28/fir-risk-intelligence)

---

## LINKEDIN POST

There's a new kind of malware. It doesn't come with a payload.

It calls Google's Gemini API. Asks it to write one. Compiles it in memory. Leaves nothing on disk.

Every infection is unique. There are no signatures to detect.

Google's Threat Intelligence Group just published their latest AI Threat Tracker, and the findings go well beyond one malware family.

Seven state-sponsored groups — from China, Iran, and North Korea — are using the same AI platforms your teams rely on to accelerate the entire attack lifecycle. Reconnaissance. Phishing. Vulnerability research. Offensive tool development.

Not experimentally. Operationally.

A few things that stood out:

APT42 (Iran) feeds target biographies into Gemini to craft believable personas — then builds offensive tools with the same session.

APT31 (China) prompts Gemini with an "expert cybersecurity researcher" persona to generate penetration testing plans against US targets.

A phishing kit built entirely with Lovable AI is harvesting crypto wallet credentials at scale.

And ClickFix campaigns are now hosted on ChatGPT, Gemini, CoPilot, DeepSeek, and Grok — turning trusted AI platforms into malware delivery infrastructure.

Same tools your organization is deploying. Same AI your teams use every day.

Different mission.

Full analysis in this week's FIR Risk Tuesday E79: [link]

Source: Google Threat Intelligence Group — GTIG AI Threat Tracker, Feb 12, 2026

#CyberSecurity #ThreatIntelligence #AI #CISO #RiskManagement #ArtificialIntelligence

---

## PROMPTS USED

**Prompt 1:** "I just ingested the GTIG AI Threat Tracker from February 2026. What are the most significant findings in this report, and what should security leaders take away from it?"

**Prompt 2:** "Which threat actors stood out to you in the GTIG report, and how are they using AI differently from each other? Any MITRE ATT&CK connections worth highlighting?"

**Prompt 3:** "The report mentions malware that calls AI APIs at runtime — HONESTCUE and COINBAIT. What makes this approach different from traditional malware, and why should defenders be concerned?"

**Prompt 4:** "What are the broader implications of AI platforms being used as attack infrastructure? The report covers model extraction, ClickFix campaigns hosted on AI chat platforms, and underground jailbreak services like Xanthorox."

**Prompt 5:** "Given everything in the GTIG report, what defensive priorities would you recommend for organizations deploying AI? Are there frameworks that address these emerging risks?"

---

## NOTES

- Lead angle: "Same AI, Different Mission" — the tools enterprises deploy are the same ones being weaponized by state-sponsored actors
- GTIG source is a Google Cloud Blog post, not a gated report — freely available for linking
- Report published Feb 12, 2026 — covers Q4 2025 activity. Part of a recurring GTIG series (prior edition January 2025). Not confirmed as strictly quarterly cadence.
- 7 tracked threat actors documented: APT31, UNC795, APT41, Temp.HEX (all China), APT42 (Iran), UNC2970 (NK), UNC6418 (unattributed)
- HONESTCUE is the paradigm-shift finding — malware generating its own code via AI API at runtime
- COINBAIT built with Lovable AI is the "AI lowers the barrier" story — phishing kits at production quality from prompts
- ClickFix campaigns span ALL major AI platforms (Gemini, ChatGPT, CoPilot, DeepSeek, Grok) — not just Google
- Xanthorox debunked as commercial model wrapper — important counter-narrative to "custom offensive AI" hype
- 100,000+ prompts in model extraction campaign — concrete stat for LinkedIn hook
- Agent INTEL synthesis baked into opening INTEL callout
- Agent provided broader KB context on APT42 and UNC2970 — cross-referenced against GTIG source for accuracy
- Agent correctly identified MITRE ATLAS as the relevant framework for AI-specific threats
- Google's defensive response documented: account disabling, classifier strengthening, SAIF framework, Big Sleep vulnerability finder, CodeMender auto-fixer
- IO operations section (China, Iran, Russia, Saudi Arabia) kept brief — productivity gains, no breakthroughs
- Hero image: AI duality / same tool different mission visual
- CVE-2025-8088 (WinRAR) appears in both E78 (CERT-EU) and this report (APT42 building PoC via Gemini) — recurring vulnerability worth tracking
- Information Operations not deep-dived — would dilute the core AI weaponization narrative
