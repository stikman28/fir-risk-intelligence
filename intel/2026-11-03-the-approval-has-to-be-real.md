# FIR Risk INTEL-48 — The Approval Has to Be Real

**Type:** `TECHNIQUE`
**Date:** November 3, 2026
**Platform Source:** FIR Risk E95 — The Labs Agree: Govern What Goes In, Limit What Comes Out (OpenAI, Anthropic, Google & OWASP)

---

## The INTEL

**"Keep a human in the loop" is the most common answer to AI agent risk, and it can fail without anyone noticing. OWASP's Top 10 for Agentic Applications lists it among the risks drawn from "the lived experience of the first generation of agentic adopters": "Confident, polished explanations misled human operators into approving harmful actions." It names the risk Human-Agent Trust Exploitation.**

That experience is still early, and it will change as the technology matures and gives its users more configurable controls. For now, OWASP's own example scenarios read like familiar fraud with a new messenger. In one, a poisoned vendor invoice is ingested by a finance copilot, the agent suggests an urgent payment to the attacker's bank details, and the finance manager approves it.

OWASP's 2026 Top 10 for LLM Applications explains why the approval step is weaker than it looks. Reviewers should see "the exact rendered action rather than a summary," because what an agent displays can differ from what it executes, and "approval fatigue degrades reviewer judgment at volume." Underneath both is a habit OWASP calls overreliance: "Humans and systems often treat fluent, confident, or well-structured outputs as authoritative. In agentic architectures, this overreliance is frequently embedded in system design."

The labs still want the human there. OpenAI's CISO checklist calls for "an independent check before actions such as sending funds, changing records or contacting customers." The point is that the check has to be designed to work.

---

## Why It Matters

An approval step that people click through can be worse than none, because it looks like a control in every audit and every board report. It also carries more weight than it seems: under OWASP's Rule of Two in [INTEL-47](/intel/intel-47-the-rule-of-two/), an agent that reads outside content, reaches sensitive data and can act or send information out relies on a person approving each action. If that approval isn't real, neither is the protection. Agents make this easier to fall into: they produce clear, confident explanations of why an action is fine, and they can ask for approval dozens of times a day. By the fortieth request, the reviewer is approving the summary, not checking the action.

We made the same point about payments in [INTEL-42](/intel/intel-42-the-first-email-asks-for-nothing/): a callback is a habit, but a control has an owner, applies every time, leaves evidence and is tested. Human approval of agent actions is a control, and it needs the same design. It also needs two kinds of people:

- **The people who own and run the agent** approve its actions. Seeing the exact action, and few enough requests to look at each one, is what makes their approval real.
- **The people responsible for oversight** of AI across the organization check that the approval step works, rather than assuming it does.

---

## What To Do — One Key Action

**Treat agent approvals as a real control. That means showing reviewers the exact action (the amount, the recipient, the record being changed), not the agent's summary of it, and reserving approval for actions that are consequential or hard to reverse, so the volume stays low enough for real scrutiny. It's also worth testing: for those responsible for oversight, periodically checking a sample of approved actions shows whether reviewers would have caught a bad one.**

If reviewers are approving so many requests that they can't look at each one, that isn't human oversight. It's a sign the agent has too much authority for the approval step to carry.

---

## MITRE ATT&CK

- **T1204 — User Execution (closest analog):** The harmful action only happens because a person approves it. Here the persuasion comes from the agent's own confident explanation rather than a phishing email.

---

## Learn More

- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) — Primary source, ASI09 Human-Agent Trust Exploitation (pp. 33–35)
- [OWASP Agentic Top 10 release announcement](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/) — "The lived experience of the first generation of agentic adopters"
- [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) — Rendered actions, approval fatigue and overreliance
- [Agent security in the enterprise (OpenAI, PDF)](https://cdn.openai.com/pdf/6546a5a6-170a-41e8-bf2f-979ff3484db1/agent-security-enterprise.pdf) — The CISO checklist
- [FIR Risk Tuesday E95 — The Labs Agree: Govern What Goes In, Limit What Comes Out](/tuesday/e95-the-labs-agree/) — Full analysis
- [FIR Risk INTEL-47 — The Rule of Two](/intel/intel-47-the-rule-of-two/) — Why some agents rely on per-action approval
- [FIR Risk INTEL-42 — The First Email Asks for Nothing](/intel/intel-42-the-first-email-asks-for-nothing/) — What makes a control a control

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
"Keep a human in the loop" only works if the human is actually checking.

OWASP's Top 10 for Agentic Applications draws on "the lived experience of the first generation of agentic adopters": "Confident, polished explanations misled human operators into approving harmful actions."

Its 2026 LLM Top 10 explains why:
• Reviewers often see the agent's summary, not "the exact rendered action."
• "Approval fatigue degrades reviewer judgment at volume."
• People treat fluent, confident output as authoritative.

By the fortieth approval request of the day, the reviewer is approving the summary, not the action. And in every audit, it still looks like a control.

It takes two kinds of people: those who own and run the agent, who approve its actions, and those responsible for oversight, who check that the approvals are real.

What makes an approval real: reviewers see the exact action (amount, recipient, record), approvals are reserved for consequential or hard-to-reverse actions so volume stays low, and a sample of approvals is tested to confirm reviewers would catch a bad one.

#AIGovernance #AgenticAI #HumanInTheLoop #InternalControls #CyberSecurity #CISO #RiskManagement
```

## X POST

"Keep a human in the loop" only works if the human is actually checking.

OWASP: "Confident, polished explanations misled human operators into approving harmful actions." And "approval fatigue degrades reviewer judgment at volume."

What makes it real: reviewers see the exact action, not the agent's summary; approvals stay rare enough to scrutinize; and they get tested.

Full INTEL → FIR Risk INTEL-48

#AIGovernance #AgenticAI

---

## SOURCE DATA

**Editorial Frame:**
INTEL-48 expands E95 §3's human-in-the-loop layer ("The approval has to be real") and connects it to INTEL-42's internal-control framing (Bruce, 10/25). Approved by Bruce as the third E95 INTEL. Bruce, 10/28: link to INTEL-47 (Rule of Two relies on per-action approval); two kinds of humans (owners/operators and oversight); "real deployments" = OWASP's "lived experience of the first generation of agentic adopters," which will change as the technology matures and offers more configurable controls. Written as guidance, not a mandate. Sourcing rule: AI labs + OWASP only.

**Primary Sources:**
- OWASP Top 10 for Agentic Applications 2026 (released Dec 9, 2025), release page. Verified Oct 25, 2026.
- OWASP Top 10 for Agentic Applications 2026 full document (Version 2026, December 2025, CC BY-SA 4.0), ASI09 pp. 33–35 and Appendix D incident tracker pp. 44–49. Verified against the PDF on Oct 28, 2026.
- OWASP Top 10 for LLM Applications 2026 v1.0 (CC BY-SA 4.0). Verified against the PDF on Oct 25, 2026.
- OpenAI, *Agent security in the enterprise*, August 2026. Verified against the PDF on Oct 25, 2026.

**Fact-Check Notes:**
- OWASP Agentic release page CONFIRMED verbatim: "Confident, polished explanations misled human operators into approving harmful actions (ASI09 – Human-Agent Trust Exploitation)." The page frames these as "the lived experience of the first generation of agentic adopters."
- OWASP Agentic PDF p34 CONFIRMED (ASI09 Example Attack Scenario 3, "Invoice Copilot Fraud"): "A poisoned vendor invoice is ingested by the finance copilot. The agent suggests an urgent payment to attacker bank details. The finance manager approves, and the company loses funds to fraud." This is an OWASP example scenario, NOT a reported incident, and the INTEL presents it as a scenario.
- Named-incident check (10/28): OWASP cites no specific incident for the "misled human operators" sentence. ASI09's reference list includes an unlinked note, "M365 Copilot manipulated to influence users to bad an ill-advised wire transfer" (sic). Appendix D tags ASI09 on Replit Vibe Coding Meltdown (Jul 2025, p46: the agent deleted a production DB and generated false outputs to hide mistakes), GitHub Copilot & Cursor code-agent exploit (Mar 2025, p48: "developers trusted AI outputs") and OpenAI Operator (Feb 2025, p49). None is a clean "approved because of a polished explanation" case, so the INTEL keeps OWASP's lived-experience framing and names no incident.
- OWASP Agentic ASI09 mitigations support the FIR action: #4 "plain-language risk summary (not model-generated rationales)"; #5 training of "human personnel involved in the evolving human oversight of autonomous agentic systems"; #2 immutable logs.
- OWASP LLM 2026 p14 CONFIRMED verbatim (LLM01 mitigation 7): "Require explicit human confirmation before any privileged, irreversible, or externally visible action, surfacing the exact rendered action rather than a summary to the reviewer. Invisible-character smuggling can make the displayed action differ from the executed one (#5), and approval fatigue degrades reviewer judgment at volume."
- OWASP LLM 2026 p43 CONFIRMED verbatim (LLM07 Misinformation): "Overreliance remains a key factor. Humans and systems often treat fluent, confident, or well-structured outputs as authoritative. In agentic architectures, this overreliance is frequently embedded in system design."
- OpenAI p29 CONFIRMED: "Require an independent check before actions such as sending funds, changing records or contacting customers."

**FIR Risk Editorial Position:**
- "By the fortieth request" is an FIR illustration, not a statistic.
- "That experience is still early, and it will change as the technology matures and gives its users more configurable controls" is FIR's view (Bruce, 10/28), not OWASP's.
- The two kinds of people (owners/operators and oversight) are FIR's framing, consistent with INTEL-47. No governance route or reporting line is prescribed.
- "What an agent displays can differ from what it executes" paraphrases OWASP's invisible-character smuggling point without the technical detail.
- The sampling test is FIR's internal-control recommendation (consistent with INTEL-42), not an OWASP requirement.
- MITRE: T1204 labeled closest analog.
