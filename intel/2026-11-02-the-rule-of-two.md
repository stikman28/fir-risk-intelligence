# FIR Risk INTEL-47 — The Rule of Two

**Type:** `TECHNIQUE`
**Date:** November 2, 2026
**Platform Source:** FIR Risk E95 — The Labs Agree: Govern What Goes In, Limit What Comes Out (OpenAI, Anthropic, Google & OWASP)

---

## The INTEL

**Hidden instructions in an email, a web page or a shared document can steer an AI agent. That is prompt injection, and none of the AI labs expects it to be fully solved. OWASP's 2026 Top 10 for LLM Applications offers a floor for limiting the damage, which it calls the Rule of Two, credited to Meta AI. It looks at three capabilities an agent can have: (A) untrusted input, (B) sensitive data, and (C) "state change or external communication." OWASP's guidance: "any [A,B,C] agent needs per-action human approval," and an agent that reads untrusted input and has one of the other two needs "an explicit residual-risk assessment."**

The logic is simple. Each capability is ordinary on its own. An email assistant that reads inbound mail is fine. Access to the inbox is fine. Being able to send replies is fine. Together, they mean a stranger's email can instruct the agent to forward your confidential messages to the stranger. OpenAI's security engineers describe the same pattern: "an attacker needs both a source, or a way to influence the system, and a sink, or a capability that becomes dangerous in the wrong context." The attack they see most often is an attempt to convince the assistant "it should take some secret information from a conversation and transmit it to a malicious third-party." That is A, B and C in one sentence.

OWASP notes that NIST and joint guidance from CISA, the FBI, the NSA and Australia's ACSC endorse the rule. It also says the rule is a floor, not the whole answer.

---

## Why It Matters

OWASP lists the Rule of Two as a prompt-injection defense, and that is where it started. The same three capabilities are also a useful lens for governing AI agents in general. Together they describe how far an agent can be misled, how much it can see, and how much it can do without a person involved.

Capability A is where governance starts, because it is the one an organization can shape before anything goes wrong. That is why [E95](/tuesday/e95-the-labs-agree/) put governing what goes into an agent first. A control over agent inputs can take two forms, and many organizations will want both:

- **A clear policy** on the kinds of content users may give their agents: which sources, which documents, which data, and what stays out.
- **Monitoring** of what agents are actually reading and acting on, so the policy can be checked rather than assumed.

That choice changes the risk itself. A company that allows its agents to read only what a user gives them directly, or content from approved sources, has narrowed capability A on purpose. A company with no rules on what its agents can read has left A wide open, and every agent with sensitive data and the ability to act inherits that exposure. Two agents with identical permissions can carry very different risk, depending on what they are allowed to read.

The third piece is people. The Rule of Two works because a human sits between the agent and a consequential action, and that takes two kinds of human involvement:

- **The people who own and run the agent**, who approve its actions and notice when it behaves unexpectedly.
- **The people responsible for oversight** of AI use across the organization, who need to know which agents hold all three capabilities and whether the controls around them are working.

---

## What To Do — One Key Action

**Consider adding the three capabilities to your AI agent risk assessment. For each agent, ask: does it read content from outside the organization, can it reach sensitive data, and can it change records or send information out?**

Agents with all three are where OWASP recommends human approval for each action. Agents with two are worth a closer look at whether they need every capability they have. For all of them, the answers point to where a control over inputs, and a named person watching, will do the most good.

---

## MITRE ATT&CK

- **T1567 — Exfiltration Over Web Service (closest analog):** The most common attack OpenAI describes tricks an agent into sending secret information to an outside party through the agent's own legitimate channels.

---

## Learn More

- [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) — Primary source, LLM01 Prompt Injection, mitigation 8
- [Designing AI agents to resist prompt injection (OpenAI)](https://openai.com/index/designing-agents-to-resist-prompt-injection/) — Source and sink
- [FIR Risk Tuesday E95 — The Labs Agree: Govern What Goes In, Limit What Comes Out](/tuesday/e95-the-labs-agree/) — Full analysis
- [FIR Risk INTEL-46 — Know Your Agents](/intel/intel-46-know-your-agents/) — Build the inventory first

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Three capabilities. Each one passes review on its own. Together, they're what a prompt injection attack needs.

1. The agent reads content from outside (email, web pages, documents).
2. It can reach sensitive data.
3. It can take actions or send information out.

OWASP's 2026 Top 10 for LLM Applications calls its answer the Rule of Two: an agent with all three needs human approval for each action.

OpenAI's security team describes the attack it sees most: convincing the assistant to "take some secret information from a conversation and transmit it to a malicious third-party." All three in one sentence.

The same three questions are a useful lens for governing AI agents in general. The first one, what goes in, is where governance starts: a clear policy on what users may give their agents, monitoring of what agents actually read, or both. An agent that reads only what a user hands it, or approved sources, is a different risk from one that can read anything. And it takes people: those who own and run each agent, and those responsible for oversight of AI across the organization.

Worth adding to your AI agent risk assessment: Does it read outside content? Can it reach sensitive data? Can it act or send data out?

#AIGovernance #AgenticAI #CyberSecurity #OWASP #PromptInjection #CISO #RiskManagement
```

## X POST

Three agent capabilities. Each passes review alone. Together, they're what prompt injection needs:

1. Reads outside content
2. Reaches sensitive data
3. Can act or send data out

OWASP's Rule of Two: with all three, a human approves each action.

Worth adding to your AI agent risk assessment, along with a control over what goes in.

Full INTEL → FIR Risk INTEL-47

#AIGovernance #OWASP

---

## SOURCE DATA

**Editorial Frame:**
INTEL-47 expands E95 §3's most important layer ("Above all, break the dangerous combinations"; Bruce: watch for combined risks that lead to bigger risks) and action 4, and ties it back to E95's first theme, governing what goes in. Bruce, 10/28: the three capabilities matter both for prompt-injection protection and as a governance lens for agentic workers; this is WHY we recommend a control over agent inputs (monitoring, an explicit input policy, or both), and the human in the loop means both the people who own and run the agent and the people responsible for oversight. Written as guidance to educate readers, not a mandate. Follows INTEL-46 (inventory first). Sourcing rule: AI labs + OWASP only.

**Primary Sources:**
- OWASP Top 10 for LLM Applications 2026 v1.0 (CC BY-SA 4.0), LLM01 Prompt Injection, prevention and mitigation strategy 8 (PDF p14). Verified against the PDF on Oct 25, 2026.
- OpenAI, *Designing AI agents to resist prompt injection*, March 11, 2026. Verified in full text on Oct 25, 2026.

**Fact-Check Notes:**
- OWASP p14 CONFIRMED verbatim: "Budget agent capabilities with the Rule of Two as a floor (Meta AI, 2025). Treat simultaneous access to (A) untrusted input, (B) sensitive data, and (C) state change or external communication as high-risk: any [A,B,C] agent needs per-action human approval, and [A,B] or [A,C] configurations need an explicit residual-risk assessment (see Scenario #8). NIST AI 100-2 E2025 and the CISA, FBI, NSA, and ACSC OT guidance (CISA et al., 2025) endorse the rule, which is silent on autonomy depth (Noma Security, 2025)."
- OWASP reference: Meta AI (2025, October 31), "Agents rule of two: A practical approach to AI agent security."
- "None of the AI labs expects it to be fully solved": E95 §1 sourcing (OpenAI: prompt injection "is unlikely to ever be fully 'solved'"; Anthropic and Google equivalents in E95).
- OpenAI CONFIRMED verbatim: "an attacker needs both a source, or a way to influence the system, and a sink, or a capability that becomes dangerous in the wrong context."
- OpenAI CONFIRMED verbatim: "Attacks we see developed against ChatGPT most often consist of attempting to convince the assistant it should take some secret information from a conversation and transmit it to a malicious third-party." (OpenAI adds that most such attacks fail because safety training causes the agent to refuse.)

**FIR Risk Editorial Position:**
- OWASP places the Rule of Two under LLM01 Prompt Injection. Using the three capabilities as a general governance lens is FIR's view and is labeled as such in the text ("also a useful lens").
- OWASP's text names [A,B] or [A,C] for residual-risk assessment; [B,C] (no untrusted input) is not named. The INTEL attributes only what OWASP says; "agents with two are worth a closer look" is FIR guidance.
- The input-scope example (agents limited to user-provided content or approved sources vs no governance over inputs) is Bruce's 10/28 framing, an FIR illustration.
- The input-control recommendation (policy, monitoring, or both) and the two kinds of human involvement (owners/operators and oversight) are FIR's guidance, consistent with E95's "govern what goes in." No governance route or reporting line is prescribed.
- "NIST and joint guidance ... endorse the rule" is OWASP's statement, attributed to OWASP. "Silent on autonomy depth" is reflected as "a floor, not the whole answer."
- The email-assistant example is an FIR illustration.
- MITRE: no ATT&CK technique for prompt injection; T1567 is labeled closest analog.
