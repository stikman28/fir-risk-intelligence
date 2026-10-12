# FIR Risk INTEL-39 — Your Prompts Went Somewhere Else

**Type:** `REGULATORY`
**Date:** October 19, 2026
**Platform Source:** FIR Risk E93 — The Attacks Aren't New. The Economics Are. (Anthropic, Detecting and countering misuse of AI: September 2026)

---

## The INTEL

**The AI tool your employee chose may not be the AI that answers them. Anthropic's September 2026 threat report alleges that China-based AI labs silently forwarded their own customers' requests to Claude and kept the exchanges to train their models; at least two, Moonshot AI and DeepSeek, served Claude's answers back as their own. In one case, Moonshot AI relayed almost 300,000 customer requests in ten days. In one example, the report says a user "had no way of knowing" their requests were being forwarded to Claude.**

The data in those prompts was sensitive. Anthropic reports that many of the relayed exchanges came from users of third-party model routing services "commonly used by users in the United States and Europe," and that the sessions contained names, email addresses, company data and other sensitive information from hundreds of end users in at least a dozen languages. Its redacted examples include a pharmaceutical company's internal capital expenditure forecasts and a developer's live access credentials. Anthropic says these practices are "likely inconsistent with privacy laws."

A caution on independence: Anthropic competes with the labs it names, and these are its allegations, based on its own platform data. Anthropic also says it has no indication US persons' data was exposed, though the routing platforms involved are commonly used in the US and Europe. The compliance lesson holds either way.

---

## Why It Matters

This is a data-protection problem, not just a security one. When an employee pastes customer data or a financial model into an AI tool, your organization is responsible for where it goes. If the tool quietly passes it to an undisclosed third party, you may have an unreported sub-processor, a cross-border transfer you never approved, and possibly a notifiable disclosure.

Model routers and low-cost coding assistants are attractive precisely because they're cheap and flexible. That's also why they rarely go through procurement, and why their data path is often invisible.

---

## What To Do — One Key Action

**Inventory the AI tools your employees actually use, including model routers, browser extensions and coding assistants, and approve only those whose data path you can see in writing: who processes the prompt, where, under what terms, and whether it's retained or used for training. Block the rest, and add AI sub-processors to your privacy and vendor-risk reviews.**

Anthropic's report makes the same point from the other side: buy AI access only through authorized channels, because a discount that routes your traffic through an unknown intermediary "introduces tremendous risk to user data and systems."

---

## MITRE ATT&CK

- **T1557 — Adversary-in-the-Middle (closest analog):** The relays sat between users and the model they thought they were using, seeing and keeping every exchange. It isn't a classic network attack, but the risk to your data is the same: a middle party you never approved.

---

## Learn More

- [Detecting and countering misuse of AI: September 2026 (Anthropic)](https://www.anthropic.com/threat-intelligence-report-september-2026) — Primary source, section on illicit distillation (cases GTG-16001, GTG-16002 and GTG-16008)
- [FIR Risk Tuesday E93 — The Attacks Aren't New. The Economics Are.](/tuesday/e93-the-economics-changed/) — Full analysis of the report
- [FIR Risk INTEL-37 — Loot, Compute, Cover](/intel/intel-37-loot-compute-cover/) — The criminal market for AI access

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
The AI tool your employee chose may not be the AI that answers them.

Anthropic's September threat report alleges that China-based AI labs silently forwarded their customers' requests to Claude and kept the exchanges for training. Many came through third-party model routers popular in the US and Europe. Those prompts held names, email addresses, company data, and in one example, a developer's live credentials. In one example, Anthropic says the user "had no way of knowing."

A fair caveat: Anthropic competes with the labs it names. But the compliance lesson stands either way. If a tool passes your data to an undisclosed party, you may have an unapproved sub-processor and a cross-border transfer you never signed off on.

One action: approve only AI tools whose data path you can see in writing.

Full INTEL — link in the comments.

#DataPrivacy #AIGovernance #Compliance #ThirdPartyRisk #RiskManagement
```

## X POST

The AI tool your employee chose may not be the AI that answers them.

Anthropic's September threat report alleges that China-based AI labs silently forwarded their customers' requests to Claude and kept the exchanges for training. Many came through third-party model routers popular in the US and Europe. Those prompts held names, email addresses, company data, and in one example, a developer's live credentials. In one example, Anthropic says the user "had no way of knowing."

A fair caveat: Anthropic competes with the labs it names. But the compliance lesson stands either way. If a tool passes your data to an undisclosed party, you may have an unapproved sub-processor and a cross-border transfer you never signed off on.

One action: approve only AI tools whose data path you can see in writing.

Full INTEL → FIR Risk INTEL-39

#DataPrivacy #AIGovernance

---

## SOURCE DATA

**Editorial Frame:**
INTEL-39 is the data-protection leg of the E93 set, drawn from the report's illicit-distillation section. It is the most compliance-relevant finding for privacy officers, and it carries an explicit independence caveat.

**Primary Sources:**
- Anthropic — Detecting and countering misuse of AI: September 2026 (published Sept 10, 2026; 154-page PDF; activity disrupted Dec 2025 – Aug 2026). Read from the PDF; quotes and figures verified against it on Oct 11, 2026.

**Fact-Check Notes (verified against the report PDF, Oct 11, 2026):**
- CONFIRMED: DeepSeek, Xiaomi and Moonshot fed user conversations into Claude; many exchanges relayed from users of third-party model routing services "commonly used by users in the United States and Europe"; sessions contained names, email addresses, company data and other sensitive data of hundreds of end users "in at least a dozen languages"; "likely inconsistent with privacy laws."
- CONFIRMED: redacted examples of a pharmaceutical company's capex forecasts and a developer's live access credentials.
- CONFIRMED: Moonshot (GTG-16002) relayed almost 300,000 customer requests over a ten-day period; a user (an engineer building a system for a PRC state-owned company) "had no way of knowing."
- CONFIRMED: "introduces tremendous risk to user data and systems" (authorized-channels guidance).

**FIR Risk Editorial Position:**
- Independence caveat stated in the piece: Anthropic competes with the labs it names; these are its allegations from its own platform data.
- MITRE mapping labeled as the closest analog (T1557), not a literal technique match.
- Voice: declarative, board-readable, incentive-aware.
