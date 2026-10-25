# FIR Risk INTEL-41 — The Browser Reads Your AI Chats

**Type:** `TREND`
**Date:** October 27, 2026
**Platform Source:** FIR Risk E94 — MDDR 2026: A Shift in the Physics of Cyber Risk (Microsoft Digital Defense Report 2026)

---

## The INTEL

**Malicious browser extensions posing as AI assistants reached about 900,000 installs and was active inside more than 20,000 enterprise tenants, quietly collecting AI chat histories, prompts and responses from platforms such as ChatGPT and DeepSeek. Microsoft says that exposed "proprietary code, business strategies, and other sensitive information."**

The finding comes from Microsoft's 2026 Digital Defense Report, which calls AI browsers "a material enterprise risk" because they combine three conditions security leaders rarely face at the same time: "broad adoption, high-trust access, and limited security visibility." Microsoft sees AI browsers in daily use at more than 40% of organizations in its dataset. Attackers have noticed: in a May 2026 analysis, Microsoft found AI browsers were the initial infection vector in incidents involving 57 distinct malware families.

The disguise is getting better. Microsoft describes malicious "AI productivity" apps with professional branding and valid code-signing certificates that install a backdoor stealing credentials, payment data and files, and an extension impersonating Perplexity AI that recorded users' searches while showing them normal results.

---

## Why It Matters

Employees now paste contracts, financials, source code and strategy into AI chats every day. The browser that holds those chats can also read untrusted web pages and act inside live business sessions with the user's own access. When something goes wrong, Microsoft notes, it "may present as ordinary software-as-a-service (SaaS) usage rather than malware execution," so it doesn't look like an attack.

Most organizations govern which AI tools are approved. Far fewer govern the browser extensions sitting on top of them. That gap is where this campaign lived.

---

## What To Do — One Key Action

**Decide which AI browsers and browser extensions are approved, enforce that list through your browser management, and block the rest. Then treat AI chat histories as sensitive business data, covered by the same data-protection rules as the documents people paste into them.**

That's Microsoft's own third priority for organizations: "maintain visibility into approved AI tools, services, and agentic capabilities while monitoring for unauthorized or unmanaged use."

---

## MITRE ATT&CK

- **T1176 — Browser Extensions:** Malicious extensions disguised as AI assistants harvest chat histories, page content and session material from inside the browser.

---

## Learn More

- [Microsoft Digital Defense Report 2026: Decoding emergence (Microsoft, PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Digital-Defense-Report.pdf) — Primary source, "AI as the new attack surface"
- [FIR Risk Tuesday E94 — MDDR 2026: A Shift in the Physics of Cyber Risk](/tuesday/e94-shift-in-the-physics-of-cyber-risk/) — Full analysis of the report
- [FIR Risk INTEL-39 — Your Prompts Went Somewhere Else](/intel/intel-39-your-prompts-went-somewhere-else/) — Another route for AI conversations to leak

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Your team's AI chats hold contracts, financials, source code and strategy. Who else is reading them?

Microsoft's 2026 Digital Defense Report documented a malicious extension campaign with about 900,000 installs, active in more than 20,000 enterprise tenants. The extensions posed as AI assistants and quietly collected AI chat histories, prompts and responses.

Microsoft calls AI browsers "a material enterprise risk": broad adoption (daily use at 40%+ of organizations in its data), high-trust access, and limited security visibility. In a May 2026 analysis, AI browsers were the initial infection vector for 57 distinct malware families.

The hard part: it doesn't look like an attack. It looks like ordinary SaaS use.

One action: approve a short list of AI browsers and extensions, block the rest, and treat AI chat histories as sensitive business data.

#CyberSecurity #AISecurity #DataProtection #CISO #RiskManagement #AIGovernance
```

## X POST

Your team's AI chats hold contracts, financials, source code and strategy. Who else is reading them?

Microsoft's 2026 Digital Defense Report documented a malicious extension campaign with about 900,000 installs, active in more than 20,000 enterprise tenants. The extensions posed as AI assistants and quietly collected AI chat histories, prompts and responses.

Microsoft calls AI browsers "a material enterprise risk": broad adoption, high-trust access, limited security visibility.

One action: approve a short list of AI browsers and extensions, block the rest, and treat AI chat histories as sensitive business data.

Full INTEL → FIR Risk INTEL-41

#CyberSecurity #AISecurity

---

## SOURCE DATA

**Editorial Frame:**
INTEL-41 carries the AI-browser material cut from E94 for length (Bruce, 10/15). One action: an enforced allow-list of AI browsers and extensions, plus treating AI chat histories as sensitive data.

**Primary Source:**
- Microsoft Digital Defense Report 2026, "Decoding emergence" (reporting period July 2025 – June 2026). Read from the PDF; quotes and figures verified on Oct 15, 2026 (PDF page numbers below).

**Fact-Check Notes:**
- p27 CONFIRMED: AI browsers "a material enterprise risk because they combine three conditions security leaders rarely face at the same time: broad adoption, high-trust access, and limited security visibility."
- p27 CONFIRMED: daily use "across more than 40% of organizations in its dataset."
- p27 CONFIRMED: May 2026 analysis, AI browsers as initial infection vector "in incidents involving 57 distinct malware families."
- p27 CONFIRMED: malicious extension campaign "affected more than 900,000 installs across Chromium-based browsers (including agentic browsers)" with "confirmed telemetry activity across more than 20,000 enterprise tenants"; harvested browsing history, AI chat histories, prompts and responses, delegated session material. The same page says "nearly 900,000" in another passage, so we use "about 900,000."
- p27 CONFIRMED: extensions "masquerading as AI assistants"; collect "URLs, page content, metadata, and AI chat histories from platforms such as ChatGPT and DeepSeek, exposing proprietary code, business strategies, and other sensitive information."
- p27 CONFIRMED: EvilAI, professional branding and valid code-signing certificates, persistent backdoor stealing credentials, payment data and sensitive files; extension impersonating Perplexity AI silently collected search activity.
- p27 CONFIRMED: "may present as ordinary software-as-a-service (SaaS) usage rather than malware execution."
- p7 CONFIRMED: priority #3 "Maintain visibility into approved AI tools, services, and agentic capabilities while monitoring for unauthorized or unmanaged use."
- NOT USED: "roughly 85% of work now happens" in the browser (Microsoft cites outside industry research).

**FIR Risk Editorial Position:**
- Malware-family names (EvilAI) kept out of the body text for a board audience; the vendor names are Microsoft's own examples.
- Voice: declarative, board-readable, incentive-aware.
- 10/25 (Bruce): dated Tue 10/27; opener now leads with the extension campaign (strongest fact); primary link = official MDDR PDF (security-insider URL 404s).
