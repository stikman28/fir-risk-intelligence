# FIR Risk INTEL-44 — The Basics Are Working

**Type:** `TREND`
**Date:** October 30, 2026
**Platform Source:** FIR Risk E94 — MDDR 2026: A Shift in the Physics of Cyber Risk (Microsoft Digital Defense Report 2026)

---

## The INTEL

**Some good news from Microsoft's 2026 Digital Defense Report: password attacks are down 26% year over year. Microsoft calls it "strong evidence that security measures such as MFA and passkeys are forcing attackers to pivot to other approaches to achieve access to high-value targets."**

The controls work, so attackers are going around them. Microsoft names where they're going: "new-hire onboarding and account recovery," the side doors that "rely on weaker credentials like SMS or email-based one-time passcode (OTP)." It also saw the share of adversary-in-the-middle phishing and token theft, techniques built to get past MFA, more than double in the first six months of 2026. That share is still comparatively small, Microsoft notes, but "it shows the direction of travel."

Microsoft's answer is passkeys, which "only work on the website or app for which they were created," so a passkey won't work on a lookalike phishing site. The next step, it says, is to "remove all phishable credentials from an account," making not just the login but the account itself phishing-resistant.

---

## Why It Matters

The money spent on MFA and passkeys is paying off, and that's worth telling the board. But an account is only as strong as its weakest way in. If the front door needs a passkey and the recovery flow accepts a text message, attackers will use the recovery flow, and the help desk reset and the new starter's first login become the targets.

---

## What To Do — One Key Action

**Hold account recovery and new-hire onboarding to the same standard as login: no SMS or email codes as the fallback for accounts that matter, and phishing-resistant credentials from day one.**

---

## MITRE ATT&CK

- **T1110 — Brute Force:** Password guessing and spraying, the attacks MFA and passkeys are driving down.
- **T1557 — Adversary-in-the-Middle:** Phishing that relays the login to steal session tokens and get past MFA, now growing as a share of attacks.

---

## Learn More

- [Microsoft Digital Defense Report 2026: Decoding emergence (Microsoft, PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Digital-Defense-Report.pdf) — Primary source, "Identity is at the center of modern cyber risk"
- [FIR Risk Tuesday E94 — MDDR 2026: A Shift in the Physics of Cyber Risk](/tuesday/e94-shift-in-the-physics-of-cyber-risk/) — Full analysis of the report

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Some good news for once: the basics are working.

Microsoft's 2026 Digital Defense Report found password attacks down 26% year over year, which it calls "strong evidence" that MFA and passkeys are forcing attackers to look elsewhere.

Where are they looking? Microsoft names it: new-hire onboarding and account recovery, the side doors that still "rely on weaker credentials like SMS or email-based one-time passcode."

If the front door needs a passkey and the recovery flow accepts a text message, attackers will use the recovery flow.

One action: hold account recovery and new-hire onboarding to the same standard as login. No SMS or email codes as the fallback for accounts that matter, and phishing-resistant credentials from day one.

#CyberSecurity #IdentitySecurity #MFA #Passkeys #Passwordless #CISO #RiskManagement
```

## X POST

Some good news for once: the basics are working.

Microsoft's 2026 Digital Defense Report found password attacks down 26% year over year, "strong evidence" that MFA and passkeys are forcing attackers elsewhere.

Where? New-hire onboarding and account recovery, which still "rely on weaker credentials like SMS or email-based one-time passcode."

One action: hold recovery and onboarding to the same standard as login.

Full INTEL → FIR Risk INTEL-44

#CyberSecurity #Passkeys

---

## SOURCE DATA

**Editorial Frame:**
INTEL-44 is the good-news piece from E94 §6 ("The basics work"), extended with p64's detail on where attackers pivot. Promotes passwordless adoption on Microsoft's evidence; no vendor or FIDO promotion. One action: close the recovery and onboarding side doors.

**Primary Source:**
- Microsoft Digital Defense Report 2026, "Decoding emergence" (reporting period July 2025 – June 2026). Verified against the PDF on Oct 25, 2026.

**Fact-Check Notes:**
- p64 CONFIRMED verbatim: "Overall, password attacks are down 26% year-over-year. This provides strong evidence that security measures such as MFA and passkeys are forcing attackers to pivot to other approaches to achieve access to high-value targets."
- p64 CONFIRMED: "threat actors try to take over accounts by attacking other vulnerable areas—for example, new-hire onboarding and account recovery. These rely on weaker credentials like SMS or email-based one-time passcode (OTP)."
- p64 CONFIRMED: "The next step is therefore to remove all phishable credentials from an account to make not only authentication phishing-resistant but also make the account itself phishing-resistant."
- p64 CONFIRMED: "In the first six months of 2026, the share of AiTM phishing and token theft attacks more than doubled… still comparatively small. Nonetheless, it shows the direction of travel."
- p64 CONFIRMED: passkeys "only work on the website or app for which they were created, meaning if a user lands on a lookalike phishing site, their passkey won't work there."

**FIR Risk Editorial Position:**
- FIDO rule: promote passwordless adoption, no marketing for FIDO. FIDO/NIST/NCSC endorsements on p64 deliberately not used.
- AiTM growth is a SHARE that more than doubled, from a small base; worded with Microsoft's own caveat.
