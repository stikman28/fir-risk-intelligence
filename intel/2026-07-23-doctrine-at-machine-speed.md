# FIR Risk INTEL-34 — Doctrine at Machine Speed

**Type:** `THREAT ALERT`
**Date:** July 23, 2026
**Platform Source:** FIR Risk E92 — Time Is the Attack Surface (Microsoft/Accenture, Securing Nations in the Intelligent Economy) · Anthropic GTG-1002 disclosure

---

## The INTEL

**The first documented largely-autonomous AI intrusion campaign has crossed from frontier-lab warning to mainstream security doctrine. Microsoft and Accenture's new national-security report elevates Anthropic's GTG-1002 disclosure — a suspected state-linked actor that used an agentic AI coding tool to execute 80–90% of an espionage campaign's attack lifecycle, with human operators intervening at only 4–6 decision points across roughly 30 high-value targets — as its centerpiece threat case. When the world's largest security vendor cites a rival AI lab's incident as policy evidence, the agentic threat is no longer a speculative scenario. It's the establishment position.**

The case, disclosed by Anthropic in November 2025 (activity detected that September; MITRE now tracks it as Campaign C0062): the actor, designated GTG-1002, manipulated Claude Code into supporting an espionage campaign against chemical manufacturers, technology firms, financial institutions, and government agencies. Anthropic's estimate — 80–90% of the intrusion lifecycle executed by AI — is the number that resets defensive assumptions, because it means attack velocity is no longer bounded by human attacker bandwidth.

The surrounding tempo data points the same way: public institutions absorbed 2,632 attacks per week in Q2 2025, up 26% year-over-year (Check Point). Per Accenture's survey research — self-reported perception data, labeled as such — 1 in 3 organizations say AI has amplified their existing cyber risk, 87% say AI-generated lures are more convincing, 90% say they are not equipped to withstand an AI-enabled attack, and only 17% have fully built a secure cloud foundation for AI.

---

## Why It Matters

Two things changed, and only one of them is technical.

The technical one: detection and response SLAs were calibrated against human-speed adversaries. The comfortable planning assumption — "we have 24 to 48 hours between initial access and meaningful lateral movement" — reflects how long those steps take a human operator. An intrusion lifecycle that is 80–90% automated does not honor that assumption. Reconnaissance, exploitation, credential harvesting, and data staging can proceed at software speed, pausing only at the handful of decision points where a human steers.

The institutional one matters just as much for a risk leader: the citation chain. For two years, "AI will transform offense" was a claim you could defer — vendor foresight, conference-keynote material. A named, dated, primary-source-disclosed campaign, elevated into a Microsoft/Accenture policy document and formally catalogued by MITRE, is a different class of evidence. It's the kind boards, insurers, and regulators act on. Expect AI-intrusion readiness questions to start appearing in underwriting questionnaires and examination requests — and the organizations that raised the topic in their own board reports first will have the easier conversation.

---

## What To Do — One Key Action

**Re-baseline your incident-response SLAs against a machine-speed adversary, and identify which containment actions can execute without waiting for a human. Isolating a host, suspending an account, revoking a credential, blocking an egress path — each of these should have a pre-authorized, automated trigger for high-confidence detections. If every containment step in your playbook requires a human decision first, your response tempo is calibrated for adversaries who are disappearing.**

Then get ahead of the governance question: put the agentic-threat re-baseline in your next board risk report before your insurer or regulator asks for it. Citing a named campaign (GTG-1002 / MITRE C0062) rather than a hypothetical makes the budget conversation materially easier.

---

## MITRE ATT&CK

- **Campaign C0062 — GTG-1002:** MITRE's formal tracking of the campaign described here.
- **T1595 — Active Scanning · T1119 — Automated Collection · T1020 — Automated Exfiltration:** The technique classes where agentic automation compresses timelines most sharply — the phases that previously consumed human attacker hours now run at software speed, with humans intervening only at decision points.

---

## Learn More

- [FIR Risk Tuesday E92 — Time Is the Attack Surface](/tuesday/e92-time-is-the-attack-surface/) — The full three-clock analysis
- [Disrupting the first reported AI-orchestrated cyber espionage campaign (Anthropic)](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf) — The primary disclosure
- [MITRE ATT&CK Campaign C0062](https://attack.mitre.org/campaigns/C0062/) — Formal technique mapping
- [FIR Risk Tuesday E87 — The Agents Have Keys](/tuesday/e87-the-agents-have-keys/) — Our agentic-AI risk thread, three months before it became doctrine

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
The most important line in Microsoft and Accenture's new national-security report isn't theirs. It's who they're citing.

The report's centerpiece threat case is Anthropic's GTG-1002 disclosure: a suspected state-linked actor used an agentic AI coding tool to run an espionage campaign against ~30 high-value organizations — financial institutions, chemical manufacturers, tech firms, government agencies.

Anthropic's estimate: 80–90% of the attack lifecycle was executed by AI. Human operators intervened at only 4–6 decision points.

When the world's largest security vendor elevates a rival AI lab's incident into a policy document — and MITRE formally catalogues it as Campaign C0062 — the agentic threat has crossed from frontier-lab warning to establishment doctrine. This is no longer a speculative scenario you can defer.

What it breaks: the planning assumption that you have 24–48 hours between initial access and meaningful lateral movement. That number reflects human attacker bandwidth. An intrusion that is 80–90% automated doesn't honor it — reconnaissance, exploitation, credential harvesting, and data staging proceed at software speed.

The one action: identify which containment steps — isolating a host, suspending an account, revoking a credential — can execute automatically on high-confidence detections, without waiting for a human. If every step in your playbook requires a human decision first, your response tempo is calibrated for adversaries who are disappearing.

And put it in your board risk report before your insurer asks. Citing a named, MITRE-catalogued campaign makes that conversation materially easier than citing a hypothetical.

Full analysis in FIR Risk Tuesday E92 — link in the comments.

#CyberSecurity #AISecurity #ThreatIntelligence #IncidentResponse #CISO #RiskManagement #SOC
```

## X POST

The most important line in Microsoft/Accenture's new national-security report isn't theirs. It's who they're citing.

Their centerpiece threat case: Anthropic's GTG-1002 disclosure. A suspected state-linked actor used agentic AI to run an espionage campaign against ~30 high-value targets.

80–90% of the attack lifecycle: executed by AI.
Human intervention: 4–6 decision points.

MITRE now formally tracks it as Campaign C0062. When the largest security vendor cites a rival AI lab's incident as policy evidence, the agentic threat stops being speculative. It's doctrine.

What it breaks: "we have 24–48 hours before lateral movement." That assumption measures human attacker bandwidth. An 80–90% automated intrusion doesn't honor it.

The action: decide which containment steps — isolate the host, suspend the account, revoke the credential — can fire automatically on high-confidence detections. If every step needs a human first, your tempo is calibrated for attackers who are disappearing.

Full analysis → FIR Risk Tuesday E92

#CyberSecurity #AISecurity

---

## SOURCE DATA

**Editorial Frame:**
INTEL-34 is the adversary-tempo leg of the E92 set. The differentiated angle is the citation chain, not the incident: GTG-1002 was already known (INTEL-1, E87) — what's new is its elevation into Microsoft/Accenture doctrine and MITRE's formal catalogue, which changes the evidence class available to risk leaders for budget and board conversations.

**Primary Sources:**
- Anthropic — GTG-1002 disclosure (activity detected Sept 2025; published Nov 13, 2025) — cited directly, not via the report's retelling
- MITRE ATT&CK Campaign C0062
- Microsoft & Accenture — Securing Nations in the Intelligent Economy (2026), p. 13 (case study), p. 14 (tempo data)

**Fact-Check Notes (verified against sources):**
- CONFIRMED: 80–90% AI-executed lifecycle; 4–6 human decision points; ~30 targets across chemical/tech/financial/government (report p. 13, ref 16; consistent with Anthropic's disclosure).
- CONFIRMED: 2,632 attacks/week on public institutions, +26% YoY Q2 2025 (report p. 14, ref 22 — Check Point).
- CONFIRMED (labeled as Accenture survey/perception data): 1-in-3 amplified risk; 87% more convincing lures; 90% not equipped; 17% secure AI foundation.
- DATE PRECISION: activity detected September 2025; disclosure published November 13, 2025 — the report's "In September 2025, Anthropic uncovered" phrasing refers to detection, not publication.

**FIR Risk Editorial Position:**
- Anthropic is cited as the primary source deliberately: its commercial incentive ran *against* publicizing misuse of its own product, which strengthens the evidence class.
- Perception statistics are explicitly labeled as self-reported survey data, not measured outcomes.
- Action pairs an operational step (pre-authorized automated containment) with a governance step (board report before the insurer asks).
- Voice: declarative, board-readable, incentive-aware.
