# FIR Risk INTEL-46 — Know Your Agents

**Type:** `TREND`
**Date:** November 1, 2026
**Platform Source:** FIR Risk E95 — The Labs Agree: Govern What Goes In, Limit What Comes Out (OpenAI, Anthropic, Google & OWASP)

---

## The INTEL

**Before a board can ask who owns an AI agent, or whether it could be stopped, someone has to be able to answer a simpler question: how many agents do we run? OpenAI's enterprise security guide puts it first on its checklist for CISOs: "Know your agents. Maintain an inventory of pilot and production agent deployments that records the accountable owner, business purpose, systems and data each can reach and actions each can take."**

The second item on the same checklist is what turns a list into a decision: "Prioritize by potential impact. Assess each deployment's effective blast radius: what it can affect, which actions can complete without another decision point and how difficult those effects are to reverse." OpenAI's closing advice follows the same order: begin by "identifying existing agent deployments, assigning accountable owners, and assessing their potential impact."

Google reaches the same starting point from a different direction. The first of its three principles for secure AI agents: "Agents must have well-defined human controllers."

---

## Why It Matters

Agents don't only arrive through a formal project. They come switched on inside software the company already pays for, as pilots nobody retired, and as tools a team connected to get work done faster. An agent missing from the inventory has no owner, no limits anyone set on purpose and no one watching for it to go wrong.

The inventory is also what makes control affordable. Not every agent needs the same scrutiny. One that summarizes public documents is a different risk from one that can pay invoices or change customer records. A risk assessment of the inventory tells you where tight control is needed and where a lighter touch will do.

---

## What To Do — One Key Action

**A good starting point is an inventory of every AI agent in pilot or production, recording its owner, purpose, the systems and data it can reach and the actions it can take. A risk assessment of each one, by what it can affect, what it can do without a person deciding, and how hard its actions are to undo, then shows where controls matter most.**

An agent that nobody is willing to own deserves a hard look: give it an owner, or consider switching it off. The board question that follows is the one from [E95](/tuesday/e95-the-labs-agree/): do we know every AI agent we run, and for each one, who owns it, what can it do on its own, and could we stop it if it were tricked?

---

## MITRE ATT&CK

- **T1078 — Valid Accounts (closest analog):** Agents act with real credentials and real access. An agent no one has inventoried is a set of valid credentials no one is watching.

---

## Learn More

- [Agent security in the enterprise (OpenAI, PDF)](https://cdn.openai.com/pdf/6546a5a6-170a-41e8-bf2f-979ff3484db1/agent-security-enterprise.pdf) — Primary source, including the CISO first-actions checklist
- [Google's Approach for Secure AI Agents (Google)](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/) — The three principles
- [FIR Risk Tuesday E95 — The Labs Agree: Govern What Goes In, Limit What Comes Out](/tuesday/e95-the-labs-agree/) — Full analysis

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
How many AI agents does your company run?

If the answer takes more than a minute, that's the first risk.

OpenAI's enterprise security guide puts it at the top of its CISO checklist: "Know your agents." Keep an inventory of every pilot and production agent, with its accountable owner, business purpose, the systems and data it can reach, and the actions it can take.

The next item turns the list into a decision: assess each agent's "blast radius," meaning what it can affect, what it can do without another decision point, and how hard its actions are to reverse.

Not every agent needs the same scrutiny. One that summarizes public documents isn't one that pays invoices. The inventory and the risk assessment tell you where control belongs.

A good place to start: build the inventory, risk-assess every agent on it, and let the results show where controls matter most. An agent nobody is willing to own deserves a hard look.

#AIGovernance #AgenticAI #CyberSecurity #RiskManagement #CISO #BoardGovernance #Compliance
```

## X POST

How many AI agents does your company run?

OpenAI's enterprise security guide puts it first on its CISO checklist: "Know your agents." Inventory every agent with its owner, purpose, reach and actions.

Then assess each one's "blast radius": what it can affect, what it can do alone, how hard it is to undo.

Start with the inventory, then let a risk assessment show where controls matter most.

Full INTEL → FIR Risk INTEL-46

#AIGovernance #AgenticAI

---

## SOURCE DATA

**Editorial Frame:**
INTEL-46 expands E95's board sentence and action 1. Bruce's point (10/25): once there's an AI inventory, a risk assessment on it directs how much control is needed and where. OpenAI's checklist says the same in its second item ("Prioritize by potential impact"). Sourcing rule for E95 INTELs: AI labs + OWASP only.

**Primary Sources:**
- OpenAI, *Agent security in the enterprise*, August 2026 (CDN PDF). Verified against the PDF on Oct 25, 2026.
- Google, *Google's Approach for Secure AI Agents* (research.google, 2025).

**Fact-Check Notes:**
- p29 CONFIRMED verbatim (CISO checklist, item 1): "Know your agents. Maintain an inventory of pilot and production agent deployments that records the accountable owner, business purpose, systems and data each can reach and actions each can take."
- p29 CONFIRMED verbatim (item 2): "Prioritize by potential impact. Assess each deployment's effective blast radius: what it can affect, which actions can complete without another decision point and how difficult those effects are to reverse."
- p30 CONFIRMED verbatim: "Begin by identifying existing agent deployments, assigning accountable owners, and assessing their potential impact."
- p24 CONFIRMED (supporting): "enterprises should maintain an inventory that identifies the agents operating within their environment."
- Google CONFIRMED (also quoted in the Google Cloud CISO post, June 12, 2025): "Agents must have well-defined human controllers."

**FIR Risk Editorial Position:**
- How agents arrive (embedded in existing software, unretired pilots, team-connected tools) and the "summarizes public documents vs pays invoices" contrast are FIR illustrations, not lab statements.
- MITRE: no ATT&CK technique covers an uninventoried agent; T1078 is the closest analog and is labeled as such.
- Board message rule: an ownership/inventory question and a risk-based control decision, not a technical mandate.
