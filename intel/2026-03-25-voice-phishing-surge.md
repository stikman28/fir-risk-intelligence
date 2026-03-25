# FIR Risk INTEL-8 — The Breach Starts With a Phone Call

**Type:** `THREAT ALERT`
**Date:** March 25, 2026
**Platform Source:** Mandiant M-Trends 2026 | CrowdStrike | MITRE ATT&CK

---

## The INTEL

The most expensive security infrastructure in your organization — email gateways, URL filters, sandbox detonation, attachment scanning — was built for a channel the adversary has already abandoned.

Mandiant's M-Trends 2026, built on over 500,000 hours of frontline incident response across 83 campaigns and 73 countries, documents a shift that should fundamentally change how organizations think about initial access defense:

**Email phishing has collapsed.** From 22% of initial infection vectors in 2022 to just **6% in 2025** — a three-year decline of 73%.

**Voice phishing has surged to 11%** — nearly double email — making it the **#2 initial infection vector** behind only exploits. For cloud-specific investigations, the picture is even starker: **voice phishing was #1 at 23%.**

The cloud that organizations migrated to for better security is being breached primarily through phone calls.

**UNC3944 (Scattered Spider)** specifically researched help desk staff by name and role before calling, impersonating employees requesting password resets and MFA changes. The help desk — the function designed to restore access — became the function that granted it to adversaries.

**UNC6040** ran a multi-phase operation: voice calls convinced targets to authorize attacker-controlled versions of legitimate SaaS applications. Months later, victims received ShinyHunters-branded extortion demands for data stolen during that initial compromise. The time gap between theft and extortion complicated attribution and response.

Your security architecture was designed to analyze bits. The adversary switched to voices.

---

## Why It Matters

Organizations have spent decades and billions building layered defenses against digital threats — email security gateways, browser isolation, endpoint detection, network monitoring. These investments were correct for the threat model they addressed. But Mandiant's data shows the adversary has identified the channel none of those controls cover.

A voice call bypasses every technical control in the stack. There's no URL to scan. No attachment to detonate. No domain to block. No signature to match. The adversary adapts in real time to the target's responses, something no phishing email can do.

The 23% figure for cloud compromises is particularly significant. Organizations that moved critical workloads to cloud platforms — often citing improved security as a driver — now face a reality where nearly one in four cloud breaches begins with someone picking up the phone.

---

## What To Do

**Implement mandatory out-of-band identity verification for all credential and MFA changes initiated by phone.** Your help desk procedures were designed for a world where the caller was probably who they said they were. That world is gone. No password resets, MFA enrollments, or access changes should be completed based solely on a phone conversation — regardless of how much the caller knows about the employee they're impersonating. A callback to a registered number, a push notification to a verified device, or an in-person verification must become the minimum standard. The adversary has already done the research on your help desk staff. Your procedures need to assume the caller is the adversary until proven otherwise.

---

## MITRE ATT&CK

- **T1566.004 — Phishing: Voice Phishing (Vishing):** Social engineering via phone calls to obtain credentials and authorize malicious applications
- **T1078 — Valid Accounts:** Stolen credentials used for persistent access to cloud and SaaS platforms
- **T1199 — Trusted Relationship:** Exploitation of help desk trust relationships and SaaS application authorization flows

---

## Learn More

- [Mandiant M-Trends 2026](https://cloud.google.com/security/resources/m-trends) — Primary source
- [FIR Risk Tuesday E85 — The Responder's Report](/tuesday/e85-responders-report/) — Full M-Trends analysis
- [FIR Risk Tuesday E83 — The Convergence](/tuesday/e83-crowdstrike-global-threat-report/) — CrowdStrike on Scattered Spider
- [FIR Risk Intelligence](https://github.com/stikman28/fir-risk-intelligence) — Source prompts, methodology, and all published INTEL

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

# LINKEDIN POST

```
The breach starts with a phone call.

Mandiant's M-Trends 2026 — built on 500,000+ hours of frontline incident response — documents a shift that should change how every organization thinks about initial access defense.

Email phishing has collapsed. From 22% of initial infection vectors in 2022 to just 6% in 2025. A 73% decline in three years.

Voice phishing has surged to 11% — nearly double email — making it the #2 initial infection vector. For cloud-specific investigations, it's even starker: voice phishing was #1 at 23%.

The cloud organizations migrated to for better security is being breached primarily through phone calls.

Scattered Spider specifically researched help desk staff by name before calling, impersonating employees requesting password resets. The help desk — designed to restore access — became the function that granted it to adversaries.

Your multi-million dollar email security stack — gateways, URL filters, sandbox detonation, attachment scanning — was built for a channel the adversary has already abandoned. A voice call bypasses every one of those controls. No URL to scan. No attachment to detonate. No domain to block. The adversary adapts in real time.

One action: implement mandatory out-of-band identity verification for all credential and MFA changes initiated by phone. No exceptions. Your help desk procedures were designed for a world where the caller was probably who they said they were. That world is gone.

FIR Risk INTEL-8 — full analysis linked below.

#cybersecurity #threatintelligence #socialengineering #CISO #identitysecurity #riskmanagement #vishing #cloudsecurity
```

---

## X POST

The breach starts with a phone call.

Mandiant's M-Trends 2026 — 500,000+ hours of incident response, 83 campaigns, 73 countries — documents a shift every organization needs to see.

Email phishing: 22% in 2022 → 6% in 2025. Collapsed.

Voice phishing: surged to 11%. Nearly double email. Now the #2 initial infection vector.

For cloud-specific breaches? Voice phishing is #1 at 23%. The cloud organizations migrated to for better security is being breached through phone calls.

Scattered Spider researched help desk staff by name. Called impersonating employees. Talked their way past MFA. The help desk — designed to restore access — became the front door.

Your email security stack — gateways, URL filters, sandbox detonation — was built for a channel the adversary has already abandoned. A voice call bypasses every control. No URL. No attachment. No domain. Real-time adaptation.

One action: mandatory out-of-band identity verification for all credential and MFA changes initiated by phone. Your procedures assumed the caller was probably legitimate. That assumption is now a vulnerability.

INTEL-8 — linked below.

#cybersecurity #threatintelligence

---

# SOURCE DATA

**Platform Queries:**
- "What does M-Trends 2026 reveal about the shift from email phishing to voice phishing as an initial infection vector?"

**KB Sources:**
- Mandiant M-Trends 2026 (March 2026)
- CrowdStrike 2026 Global Threat Report
