# FIR Risk INTEL-64 — AI Fixed the Four Tells

**Type:** `TREND`
**Date:** November 28, 2026
**Platform Source:** FIR SIGNALS 2026, Signal 02 "Inside, they look like you." (Microsoft Digital Defense Report 2026, Verizon 2026 DBIR)

---

## The INTEL

**Fraud by impersonation used to give itself away. Microsoft lists four tells: poor forged documents, non-native language, accents that didn't match during interviews, and a thin online presence. Its 2026 report says "AI fixes all four simultaneously."**

What the reports say:

- **The tells are gone.** Microsoft: AI can improve photos in forged documents so they "pass standard visual inspection," write "grammatically flawless" résumés and emails, mask accents with "real-time voice modulation during video calls and phone interviews," and build a believable online history. The result: "all conversations over unauthenticated or poorly-vetted channels (including email) become easy targets."
- **The attacks are live conversations.** Verizon added pretexting, an attacker "on the other side of the phone, text message conversation or email thread," to its initial access tracking this year, after "a significant number of high-profile ransomware breaches" began that way.
- **And they work better than email.** In the simulations Verizon collected, phone-based campaigns drew a median response of about 2%, against 1.4% for email: "an increase of 40%." The phone sample is small (35 data points), and Verizon says so.

---

## Why It Matters

Most verification still depends on someone judging whether a person looks and sounds right: the help desk agent resetting a password, the clerk changing a supplier's bank details, the recruiter on a video interview. Those checks relied on the tells, and AI has removed them.

Verizon puts the hard part plainly: training help desks and support agents "to not be helpful and supportive" when someone is manipulating them "is not as simple" as spotting a suspicious email.

**Our read:** stop asking people to judge. Verification has to come from a channel the company controls, not from how convincing the request is. This is the decision SIGNALS asks leaders to make: help desk resets, payment-detail changes and new-hire identity checks are security controls, not admin.

---

## What To Do — One Key Action

**For three requests (password or MFA resets, changes to payment details, and identity checks for new hires), require confirmation through a channel your company starts: a call back to a number already on file, or an in-person or manager check. Never use contact details supplied in the request itself.**

---

## MITRE ATT&CK

- **T1684.001 — Impersonation** (T1656 in M-Trends): posing as an employee, executive, supplier or candidate
- **T1566.004 — Phishing: Spearphishing Voice:** the live-conversation route, 6.1% of Mandiant's 2025 investigations
- MITRE mitigations listed in SIGNALS: M1017 User Training · M1036 Account Use Policies · M1032 Multi-factor Authentication

**MITRE ATLAS** (attacks on AI systems, v5.6)

- **AML.T0088 — Generate Deepfakes:** ATLAS notes GenAI "reduces the skill and level of effort required" and "makes real-time manipulations feasible," including to "evade AI applications such as biometric identity verification systems"
- **AML.T0052.001 — Deepfake-Assisted Phishing:** fake voice or video "to impersonate trusted individuals, executives, or organizations." ATLAS mitigation: AML.M0034 Deepfake Detection, recommended "especially in impactful applications such as biometric verification." Detection helps; a call back on a known number doesn't depend on it.

---

## Learn More

- [FIR SIGNALS 2026](/reports/signals-2026/) — Signal 02, plus the MITRE ATT&CK appendix in the PDF
- [Microsoft Digital Defense Report 2026](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2026) — Primary source
- [Verizon 2026 Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/dbir/) — Primary source
- [FIR Risk INTEL-44 — The Basics Are Working](/intel/intel-44-the-basics-are-working/) — Account recovery and onboarding as side doors

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
AI fixed the four tells.

Impersonation fraud used to give itself away. Microsoft lists four tells:
→ Poor forged documents
→ Non-native language
→ Accents that didn't match during interviews
→ A thin online presence

Its 2026 Digital Defense Report: "AI fixes all four simultaneously."

Verizon's 2026 DBIR now tracks pretexting, live manipulation by phone, text or email, as its own way in. In the simulations it collected, phone campaigns drew about 40% more responses than email (small sample, Verizon notes).

Most verification still depends on someone judging whether a person looks and sounds right. That judgment relied on the tells.

The action: for password and MFA resets, payment-detail changes and new-hire identity checks, confirm through a channel your company starts, such as a call back to a number already on file. Never use contact details from the request itself.

FIR Risk INTEL-64 · SIGNALS 2026, Signal 02

#CyberRisk #Fraud #Deepfakes #SocialEngineering #CISO #RiskManagement
```

## X POST

Impersonation fraud had four tells: bad forgeries, non-native language, mismatched accents, thin online presence.

Microsoft 2026: "AI fixes all four simultaneously."

Stop asking people to judge. Verify resets and payment changes on a channel you start.

Full INTEL → FIR Risk INTEL-64

#CyberRisk #Deepfakes

---

## SOURCE DATA

**Editorial Frame:**
SIGNALS INTEL series, Signal 02, INTEL 3 of 3. Delivers the SIGNALS Signal 02 decision ("treat verification as a control": help desk resets, payment-detail changes, new-hire identity checks), with the unique insight that AI removed the tells human verification relied on. Distinct from INTEL-8 (help desk calls), INTEL-19 (synthetic insiders in hiring), INTEL-42 (BCI first email asks for nothing) and INTEL-44 (weak recovery credentials).

**Fact-Check Notes (verified Nov 16, 2026 against SIGNALS source texts; page = printed page):**
- MDDR 2026 p13: "Identity-based fraud campaigns previously had four detectable weaknesses: poor-quality document forgeries, non-native language in applications, accent mismatches during interviews, and thin or inconsistent online presence. AI fixes all four simultaneously." Detail boxes: identity documents "producing counterfeits that pass standard visual inspection"; writing assistants "produce grammatically flawless content such as resumes, LinkedIn profiles, GitHub activity summaries, and emails"; "Real-time voice modulation during video calls and phone interviews masks accents"; synthetic digital footprints. "Combined with audio and video deepfakes, these mean that all conversations over unauthenticated or poorly-vetted channels (including email) become easy targets."
- DBIR 2026 p16: "this year, we added Pretexting—our second most frequent social action variety—to our tracked list of initial access vectors"; "there was a significant number of high-profile ransomware breaches in this year's dataset that utilized this Social Engineering technique as the initial action"; pretexting = "the actor is—on the other side of the phone, text message conversation or email thread"; "Training IT help desks and customer support agents to not be helpful and supportive in cases when a threat actor is trying to manipulate them is not as simple as…"
- DBIR 2026 p50: "While the median click rate of email phishing simulation campaigns is 1.4%, we see the median rate of simulations on phone-centric methods is closer to 2% … That is an increase of 40% in the median click rate between those vectors." Figure 56 n=35 (vs n=8,395 email); DBIR: "we struggled to find companies doing simulations of voice- and text message-based campaigns, which leads to this small-ish sample size." Post says "response" for "click rate" because phone-centric includes calls; "about 2%" matches "closer to 2%".
- M-Trends 2026 p86: T1566.004 6.1%. SIGNALS appendix p16: T1684.001 Impersonation (T1656 in M-Trends); mitigations. SIGNALS outline Signal 02 decision: "treat verification as a control."

**MITRE ATLAS (v5.6.0, atlas-data dist/ATLAS.yaml, checked Nov 16, 2026):** AML.T0088 Generate Deepfakes, quoted ("evade AI applications such as biometric identity verification systems"; "GenAI reduces the skill and level of effort required"; "makes real-time manipulations feasible"). AML.T0052.001 Deepfake-Assisted Phishing, quoted. AML.M0034 Deepfake Detection, quoted. FIR mapping; no AI-specific figures claimed.

**FIR Risk Editorial Position:** "stop asking people to judge", the three-request scope and the call-back action are FIR's read, aligned with the SIGNALS Signal 02 decision. Board rule: direction, no patch-speed mandate.
