# FIR Risk INTEL-47 — The Rule of Two

**Type:** `TECHNIQUE`
**Date:** November 2, 2026
**Platform Source:** FIR Risk E95 — The Labs Agree: Govern What Goes In, Limit What Comes Out (OpenAI, Anthropic, Google & OWASP)

---

## The INTEL

**Three things an AI agent can do are each acceptable on their own: read content from outside the organization, work with sensitive data, and take actions or send information out. Put all three in one agent and you have the setup attackers need. OWASP's 2026 Top 10 for LLM Applications turns that into a floor it calls the Rule of Two, credited to Meta AI: "any [A,B,C] agent needs per-action human approval," where A is untrusted input, B is sensitive data and C is "state change or external communication."**

Agents with two of the three don't get a pass either. OWASP says those configurations "need an explicit residual-risk assessment." It also notes that NIST and joint guidance from CISA, the FBI, the NSA and Australia's ACSC endorse the rule.

OpenAI's security engineers describe the same logic in their own terms: "an attacker needs both a source, or a way to influence the system, and a sink, or a capability that becomes dangerous in the wrong context." They also say which combination they see attacked most: attempts to convince ChatGPT "it should take some secret information from a conversation and transmit it to a malicious third-party." That is A, B and C in one sentence.

---

## Why It Matters

Most access reviews look at one permission at a time, and each one usually passes. An email assistant that reads inbound mail is fine. Access to the inbox is fine. Being able to send replies is fine. Together, they mean a stranger's email can instruct the agent to forward your confidential messages to the stranger.

Every AI lab we read for [E95](/tuesday/e95-the-labs-agree/) agrees that hidden instructions will sometimes get through. The Rule of Two doesn't try to stop them. It makes sure that when one gets through, the agent can't do harm without a person seeing it first.

---

## What To Do — One Key Action

**Check every agent in your inventory against the three capabilities: does it read untrusted content, can it reach sensitive data, and can it change things or send information out? Any agent with all three gets human approval for each action, or loses one of the three. Any agent with two gets a documented risk assessment and an owner who signs off on it.**

Removing a capability is often easier than it sounds. An agent that summarizes inbound email may not need to send anything. An agent that sends customer updates may not need to read the open web.

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
Three permissions. Each one passes review. Together, they're the attack.

1. The agent reads content from outside (email, web pages, documents).
2. It can reach sensitive data.
3. It can take actions or send information out.

OWASP's 2026 Top 10 for LLM Applications calls the fix the Rule of Two: an agent with all three needs human approval for each action, or should lose one of the three. Agents with two need an explicit risk assessment.

OpenAI's security team describes the attack it sees most: convincing the assistant to "take some secret information from a conversation and transmit it to a malicious third-party."

That's all three in one sentence.

One action: check every agent against the three. All three = a human approves each action, or remove one. Two = a documented risk assessment with an owner who signs off.

#AIGovernance #AgenticAI #CyberSecurity #OWASP #PromptInjection #CISO #RiskManagement
```

## X POST

Three agent permissions. Each passes review. Together, they're the attack:

1. Reads outside content
2. Reaches sensitive data
3. Can act or send data out

OWASP's Rule of Two: an agent with all three needs human approval for every action, or loses one.

One action: check every agent against the three.

Full INTEL → FIR Risk INTEL-47

#AIGovernance #OWASP

---

## SOURCE DATA

**Editorial Frame:**
INTEL-47 expands E95 §3's most important layer ("Above all, break the dangerous combinations"; Bruce: watch for combined risks that lead to bigger risks) and action 4. Follows INTEL-46: inventory first, then the combination check. Sourcing rule: AI labs + OWASP only.

**Primary Sources:**
- OWASP Top 10 for LLM Applications 2026 v1.0 (CC BY-SA 4.0), LLM01 Prompt Injection, prevention and mitigation strategy 8 (PDF p14). Verified against the PDF on Oct 25, 2026.
- OpenAI, *Designing AI agents to resist prompt injection*, March 11, 2026. Verified in full text on Oct 25, 2026.

**Fact-Check Notes:**
- OWASP p14 CONFIRMED verbatim: "Budget agent capabilities with the Rule of Two as a floor (Meta AI, 2025). Treat simultaneous access to (A) untrusted input, (B) sensitive data, and (C) state change or external communication as high-risk: any [A,B,C] agent needs per-action human approval, and [A,B] or [A,C] configurations need an explicit residual-risk assessment (see Scenario #8). NIST AI 100-2 E2025 and the CISA, FBI, NSA, and ACSC OT guidance (CISA et al., 2025) endorse the rule, which is silent on autonomy depth (Noma Security, 2025)."
- OWASP reference: Meta AI (2025, October 31), "Agents rule of two: A practical approach to AI agent security."
- OpenAI CONFIRMED verbatim: "an attacker needs both a source, or a way to influence the system, and a sink, or a capability that becomes dangerous in the wrong context."
- OpenAI CONFIRMED verbatim: "Attacks we see developed against ChatGPT most often consist of attempting to convince the assistant it should take some secret information from a conversation and transmit it to a malicious third-party." (OpenAI adds that most such attacks fail because safety training causes the agent to refuse.)

**FIR Risk Editorial Position:**
- OWASP's strict text says [A,B] or [A,C] need assessment; [B,C] (no untrusted input) is not named. The action says "any agent with two" as a conservative FIR simplification.
- "NIST and joint guidance ... endorse the rule" is OWASP's statement, attributed to OWASP.
- OWASP notes the rule "is silent on autonomy depth": it's a floor, not the whole answer. The action is framed as a check, not a complete control set.
- The email-assistant example is an FIR illustration.
- MITRE: no ATT&CK technique for prompt injection; T1567 is labeled closest analog.
