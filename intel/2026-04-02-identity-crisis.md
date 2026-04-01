# FIR Risk INTEL — 850% Identity Surge

**Type:** `THREAT ALERT`
**Date:** April 2, 2026
**Platform Source:** Agent Discovery (Red Canary Threat Detection Report 2026 & IBM X-Force 2026)

---

## The INTEL

Red Canary recorded an **850% increase in identity threat detections** in 2025, making identity attacks their #1 threat category at 53% of total detection volume — up from 20% in 2024.

IBM X-Force independently confirms the same pattern: credential theft remained "at the center of many prominent campaigns," with over **300,000 ChatGPT credentials** discovered for sale on dark web markets. A category of credential that didn't exist two years ago.

This isn't two reports saying the same thing. It's two fundamentally different data sources — incident response engagements and endpoint telemetry across 4.5 million protected assets — arriving at the same conclusion independently. Cloud account compromises dominate Red Canary's threat landscape. Browsers have emerged as the primary staging ground for credential theft. The attack doesn't start with malware. It starts with a valid login.

---

## Why It Matters

This is the sixth consecutive 2026 annual threat report to confirm identity as the dominant attack vector. Unit 42: 90% of incidents involved identity compromise. Cloudflare: 63% of human logins use compromised credentials. CrowdStrike: 35% of cloud intrusions via valid accounts. Picus: credential theft double ransomware encryption. Mandiant: voice phishing at 11% because attackers call to get credentials.

Six reports. Six methodologies. One verdict. And the 850% detection surge signals the volume is still accelerating — every new SaaS platform, AI tool, and cloud service creates another credential to harvest. The identity attack surface isn't growing linearly with cloud adoption. It's growing exponentially.

---

## What To Do

**Architect systems that assume identity compromise, not just prevent it.** Prevention alone has failed at scale — the 850% surge proves that. Implement continuous identity monitoring with behavioral baselines that detect anomalous access patterns post-authentication. Reduce credential blast radius through aggressive privilege minimization — every credential should access the minimum needed, not the maximum available. Deploy identity "circuit breakers" that automatically limit account scope when behavior deviates from baseline. The question isn't whether credentials will be compromised. It's how much damage a compromised credential can do.

---

## MITRE ATT&CK

- **T1078 — Valid Accounts:** Dominant technique across both reports — 850% detection increase, cloud accounts as #1 technique in Red Canary data
- **T1586 — Compromise Accounts:** Infostealer ecosystem feeding credential markets at industrial scale (300K+ AI platform credentials)
- **T1528 — Steal Application Access Token:** Browser-based token theft enabling cloud account compromise without password

---

## Learn More

- [Red Canary Threat Detection Report 2026](https://redcanary.com/threat-detection-report/) — Primary source
- [IBM X-Force Threat Intelligence Index 2026](https://www.ibm.com/reports/threat-intelligence) — Primary source
- [FIR Risk Tuesday E86 — Castles on Quicksand](/tuesday/e86-castles-on-quicksand/) — Full dual-report analysis

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Red Canary recorded an 850% increase in identity threat detections in 2025. Identity attacks now account for 53% of total detection volume — up from 20% in 2024.

IBM X-Force independently confirms the same pattern: credential theft at the center of many prominent campaigns, with over 300,000 ChatGPT credentials discovered on dark web markets. A category of credential that didn't exist two years ago.

This is the sixth consecutive 2026 annual threat report to confirm identity as the dominant attack vector. Six reports, six methodologies, one verdict.

The volume is still accelerating. Every new SaaS platform, AI tool, and cloud service creates another credential to harvest. The identity attack surface isn't growing linearly with cloud adoption. It's growing exponentially.

Prevention alone has failed at scale. The fix: architect systems that assume identity compromise, not just prevent it. Behavioral baselines post-authentication. Aggressive privilege minimization. Identity circuit breakers that limit scope when behavior deviates.

The question isn't whether credentials will be compromised. It's how much damage a compromised credential can do.

Full analysis in E86 — Castles on Quicksand.

#cybersecurity #identitysecurity #threatintelligence #riskmanagement #CISO #infosec
```

---

## X POST

Red Canary recorded an 850% increase in identity threat detections in 2025. Identity now accounts for 53% of total detection volume — up from 20% a year ago.

IBM X-Force independently confirms the same: credential theft at the center of many prominent campaigns, with 300,000+ ChatGPT credentials on dark web markets. A credential category that didn't exist two years ago.

This is the sixth consecutive 2026 threat report confirming identity as the dominant attack vector. Six reports, six methodologies, one verdict.

Prevention alone has failed at scale. The fix: assume compromise. Behavioral baselines post-authentication. Aggressive privilege minimization. Identity circuit breakers that limit blast radius automatically.

The question isn't whether credentials will be compromised. It's how much damage a compromised credential can do.

Full analysis in E86 — Castles on Quicksand.

#cybersecurity #identitysecurity

---

## SOURCE DATA

**Platform Query:** "You raised something important — IBM highlights basic security lapses enabling breaches while Red Canary emphasizes increasingly sophisticated attack chains... Walk me through specific examples."

**KB Sources:**
- Red Canary Threat Detection Report 2026
- IBM X-Force Threat Intelligence Index 2026
- FIR Risk Tuesday E81-E86 (series convergence data)
