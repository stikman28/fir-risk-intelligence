# FIR Risk INTEL-9 — 22 Seconds

**Type:** `THREAT ALERT`
**Date:** March 26, 2026
**Platform Source:** Mandiant M-Trends 2026 | MITRE ATT&CK

---

## The INTEL

In 2022, the median time between an initial access broker gaining entry to a network and a ransomware operator beginning operations was **over 8 hours.** Security teams had a window — narrow, but real — to detect the initial compromise, triage the alert, and contain the threat before escalation.

That window is gone.

Mandiant's M-Trends 2026 documents that the median handoff time has collapsed to **22 seconds.** A 1,300x compression in three years. Initial access partners now deliver malware directly on behalf of ransomware operators rather than advertising access on underground forums. The cybercrime supply chain has industrialized to the point where a low-impact browser infection and a full ransomware deployment are essentially the same event.

Mandiant documented this pattern through the partnership between **UNC1543 and UNC2165** (linked to Evil Corp). UNC1543 gains access opportunistically through drive-by downloads distributing FAKEUPDATES — the kind of infection that typically sits in a SOC queue as a low-priority alert. Once active, UNC2165 established persistent SSH tunnels, dumped credentials, moved laterally throughout the network, staged terabytes of data using cloud file sync utilities — and then destroyed system backups before deploying RansomHub ransomware.

The minor browser infection your SOC would normally triage tomorrow morning? **It may have already become a ransomware deployment.**

---

## Why It Matters

Most security operations are built around a prioritization model: high-severity alerts get immediate attention, low-severity alerts queue for review. This model assumes that low-impact initial infections and high-impact ransomware deployments are separated by enough time to allow escalation. That assumption was valid when the gap was measured in hours. At 22 seconds, it's a fiction.

The FAKEUPDATES infection that generates a medium-priority alert — a drive-by download, a suspicious browser process — is no longer a precursor event. It *is* the ransomware event. The distinction between initial access and ransomware deployment has collapsed. An organization that triages FAKEUPDATES as a routine browser infection may be closing a ticket on an active ransomware operation.

This also explains why traditional detection timelines are failing. If you're hunting for ransomware indicators, you're looking for something that happened 22 seconds after an event you classified as low priority. Your detection strategy may be optimized for threats that no longer give you time to detect them.

---

## What To Do

**Build correlation rules that link low-impact initial access indicators to known handoff patterns, and escalate them to the same urgency as ransomware indicators.** FAKEUPDATES, SocGholish, and similar drive-by download infections should no longer be treated as routine browser hygiene issues. When your SOC sees an initial access broker TTP — particularly opportunistic download infections on endpoints with access to critical systems — the response window is not hours. It's seconds. If your triage model still separates "initial access" from "ransomware" as different severity tiers, that separation is the gap the adversary is exploiting.

---

## MITRE ATT&CK

- **T1189 — Drive-by Compromise:** FAKEUPDATES drive-by downloads as initial access vector for ransomware handoff
- **T1572 — Protocol Tunneling:** UNC2165 SSH tunnels for persistent C2 and lateral movement
- **T1486 — Data Encrypted for Impact:** RansomHub deployment following 22-second handoff from initial access broker
- **T1490 — Inhibit System Recovery:** Systematic backup destruction before ransomware deployment

---

## Learn More

- [Mandiant M-Trends 2026](https://cloud.google.com/security/resources/m-trends) — Primary source
- [FIR Risk Tuesday E85 — The Responder's Report](/tuesday/e85-responders-report/) — Full M-Trends analysis
- [FIR Risk INTEL-7 — A New Risk Has Entered the Top 5](/intel/intel-7-risk-profile-inversion/) — Risk landscape shift from E81-E84
- [FIR Risk Intelligence](https://github.com/stikman28/fir-risk-intelligence) — Source prompts, methodology, and all published INTEL

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

# LINKEDIN POST

```
22 seconds.

That's the median time between an initial access broker gaining entry to your network and a ransomware operator beginning operations. Mandiant M-Trends 2026. Down from over 8 hours in 2022.

A 1,300x compression in three years.

The cybercrime supply chain has industrialized. Initial access partners now deliver malware directly on behalf of ransomware operators — no more forum listings, no more waiting. The handoff is near-instantaneous.

Mandiant documented this through the UNC1543/UNC2165 (Evil Corp-linked) partnership. UNC1543 gains access through drive-by downloads distributing FAKEUPDATES — the kind of infection that sits in most SOC queues as a medium-priority alert. Once active, UNC2165 established SSH tunnels, dumped credentials, moved laterally, staged terabytes of data, destroyed backups, and deployed RansomHub ransomware.

The minor browser infection your SOC would normally triage tomorrow morning may have already become a ransomware deployment.

Most security operations are built around a prioritization model that assumes low-impact infections and high-impact ransomware are separated by enough time to allow escalation. At 22 seconds, that model is broken.

One action: correlate initial access broker TTPs — especially drive-by downloads on critical-access endpoints — with ransomware handoff patterns. Escalate them to the same urgency as ransomware indicators. If your triage model still separates "initial access" from "ransomware" as different severity tiers, that separation is the gap the adversary is exploiting.

FIR Risk INTEL-9 — full analysis linked below.

#cybersecurity #threatintelligence #ransomware #incidentresponse #CISO #riskmanagement #SOC #securityoperations
```

---

## X POST

22 seconds.

That's the median time between an initial access broker gaining entry and a ransomware operator starting operations. Mandiant M-Trends 2026.

In 2022, it was over 8 hours. A 1,300x compression in three years.

The cybercrime supply chain has industrialized. Initial access partners now deliver malware directly on behalf of ransomware operators. No more forum listings. No more waiting.

Mandiant documented UNC1543 gaining access through FAKEUPDATES — drive-by downloads. The kind of infection that sits in a SOC queue as medium-priority. Then UNC2165 (Evil Corp-linked) takes over: SSH tunnels, credential dumping, lateral movement, terabytes staged, backups destroyed, RansomHub deployed.

That browser infection your SOC would triage tomorrow morning? It may already be a ransomware deployment.

Your detection strategy is optimized for threats that no longer give you time to detect them. When the gap between initial access and ransomware was 8 hours, triage worked. At 22 seconds, the distinction between "precursor" and "attack" has collapsed.

One action: stop treating initial access broker TTPs as low-priority. FAKEUPDATES on a critical-access endpoint isn't a browser hygiene issue. It's a ransomware event that already started.

INTEL-9 — linked below.

#cybersecurity #threatintelligence

---

# SOURCE DATA

**Platform Queries:**
- "What does M-Trends 2026 reveal about the compression of handoff times between initial access brokers and ransomware operators?"

**KB Sources:**
- Mandiant M-Trends 2026 (March 2026)
