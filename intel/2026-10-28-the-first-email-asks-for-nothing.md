# FIR Risk INTEL-42 — The First Email Asks for Nothing

**Type:** `TECHNIQUE`
**Date:** October 28, 2026
**Platform Source:** FIR Risk E94 — MDDR 2026: A Shift in the Physics of Cyber Risk (Microsoft Digital Defense Report 2026)

---

## The INTEL

**Microsoft detected more than 46 million business impersonation attacks in 12 months, and almost none of them opened by asking for money. By June 2026, just 3% of first messages contained a financial or document request, down from 17% in October 2025. The rest said things like "Are you at your desk?" or "Do you have a moment?"**

Microsoft's 2026 Digital Defense Report is retiring the catch-all "BEC" label for these scams and calling them business contact impersonation (BCI): an attacker poses as an executive, employee, vendor or partner and starts a conversation. In Microsoft's words, "BCI is, overwhelmingly, a conversation starter. The fraud comes later, in follow-up messages, once the attacker has established rapport and confirmed the target is engaged." The first email is "deliberately bland," built to slip past content-based filters "precisely because it contains nothing overtly malicious to detect."

The scams also keep office hours. Payroll diversion attempts, where the attacker tries to redirect an employee's direct deposit, peak on Monday, decline through the week and go "nearly silent on weekends." 51% land on a Monday or Tuesday, when payroll and HR staff are working through the prior week's requests and, Microsoft says, are "most likely to action a quick ask without much scrutiny."

---

## Why It Matters

Email security is built to catch the ask: the invoice, the wire instruction, the bank change. When the opening message asks for nothing, there's nothing to catch, and by the time the request arrives it comes inside a conversation that already feels trusted. Volume isn't easing either: monthly attacks surged 121% in April 2026, more than double any previous month in the year.

The defense has to move from the inbox to the moment money moves.

---

## What To Do — One Key Action

**Put every change to vendor bank details or employee direct deposit under a formal internal control that the organization designs, documents, audits and verifies is working. At a minimum, the control should require verification by calling back a known number (never one supplied in the request), approval by a second person before the change takes effect, and regular review of every change made.**

A callback on its own is a good habit. A control is different: it has an owner, it applies to every change with no exceptions for urgency or seniority, it leaves evidence, and it's tested. The test is simple: can you show your auditors that every bank-detail and payroll change last quarter went through it? Then make sure payroll and HR know that Monday and Tuesday are when these requests peak.

---

## MITRE ATT&CK

- **T1656 — Impersonation:** The attacker poses as a trusted business contact and builds rapport before making the fraudulent request.

---

## Learn More

- [Microsoft Digital Defense Report 2026: Decoding emergence (Microsoft, PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Digital-Defense-Report.pdf) — Primary source, "How modern intrusions begin"
- [FIR Risk Tuesday E94 — MDDR 2026: A Shift in the Physics of Cyber Risk](/tuesday/e94-shift-in-the-physics-of-cyber-risk/) — Full analysis of the report
- [FBI Internet Crime Complaint Center (IC3)](https://www.ic3.gov/) — Report business email compromise and payroll diversion

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
"Are you at your desk?"

That's how most business impersonation scams start now. Microsoft detected more than 46 million of them in 12 months, and by June 2026 only 3% of first messages asked for money or documents (down from 17% last October).

Microsoft's words: "BCI is, overwhelmingly, a conversation starter. The fraud comes later."

The first email is bland by design, so filters have nothing to catch. The ask arrives later, inside a conversation that already feels trusted.

And the scams keep office hours: 51% of payroll diversion attempts land on a Monday or Tuesday, when payroll and HR are clearing last week's requests.

One action: put every change to vendor bank details or employee direct deposit under a formal internal control, one you design, audit and verify actually works. At a minimum: a call back to a known number, a second approver, and regular review of every change. A callback is a habit. A control is something you can prove to your auditors.

#CyberSecurity #FraudPrevention #BEC #CFO #Payroll #RiskManagement #SocialEngineering
```

## X POST

"Are you at your desk?"

That's how most business impersonation scams start now. Microsoft detected more than 46 million in 12 months, and by June 2026 only 3% of first messages asked for money or documents, down from 17%.

"BCI is, overwhelmingly, a conversation starter. The fraud comes later."

51% of payroll diversion attempts land on a Monday or Tuesday.

One action: put every bank-detail and direct-deposit change under a formal internal control: a call back to a known number, a second approver, and regular audits that prove it works.

Full INTEL → FIR Risk INTEL-42

#CyberSecurity #FraudPrevention

---

## SOURCE DATA

**Editorial Frame:**
INTEL-42 expands E94 §3 (BCI) with page detail E94 didn't carry: the sample openers, the "deliberately bland" design, the April spike and the weekly payroll cadence. One action (strengthened by Bruce 10/25): a formal internal control over payment-detail changes, designed, documented, audited and verified effective, with callback, second-person approval and regular review as minimum elements; early-week awareness.

**Primary Source:**
- Microsoft Digital Defense Report 2026, "Decoding emergence" (reporting period July 2025 – June 2026). Verified against the PDF on Oct 25, 2026 (PDF page numbers below).

**Fact-Check Notes:**
- p50 CONFIRMED: "Over the past 12 months, Microsoft detected more than 46 million BCI attacks."
- p50 CONFIRMED: volume spiked "in April 2026, when volume surged 121%—more than double any previous month observed in the past year."
- p50 CONFIRMED: first-contact messages contain "only generic outreach, such as 'Are you at your desk?' or 'Do you have a moment?' with no mention of money, invoices, or documents."
- p50 CONFIRMED: explicit financial/document request share "from 17% in October 2025 to just 3% by June 2026."
- p50 CONFIRMED verbatim: "BCI is, overwhelmingly, a conversation starter. The fraud comes later, in follow-up messages, once the attacker has established rapport and confirmed the target is engaged."
- p50 CONFIRMED: initial email "deliberately bland, designed to avoid triggering content-based detection rules precisely because it contains nothing overtly malicious to detect."
- p50 CONFIRMED: BCI definition (impersonating executive, employee, vendor, supplier, or partner); excludes credential phishing and ATO.
- p50 CONFIRMED: payroll diversion "volume peaks sharply on Monday, then declines steadily each day through Friday before going nearly silent on weekends. Over half of all payroll diversion attacks (51%) land on a Monday or Tuesday"; "payroll and HR staff are processing requests from the prior week and recipients are most likely to action a quick ask without much scrutiny."

**FIR Risk Editorial Position:**
- "121%" describes the April month-over-month surge, not a year-over-year rise; worded as "monthly attacks surged 121% in April 2026."
- Board-readable; no actor names. The action is framed as an internal control the organization owns and audits (Bruce 10/25): a callback is a procedure; a control has an owner, applies every time, leaves evidence and is tested.
