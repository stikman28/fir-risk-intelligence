# FIR Risk Tuesday E67 - CrowdStrike Threat Hunting Briefing

**Publish Date:** August 19, 2025
**Source:** [CrowdStrike 2025 Threat Hunting Report](https://www.crowdstrike.com/en-us/resources/reports/threat-hunting-report/)
**Analysis:** FIR Risk Advisory

---

## NEWSLETTER DRAFT

# FIR Risk E67 - Attackers Are Running Like a Business

![FIR Risk E67 - CrowdStrike Threat Hunting](images/E67-crowdstrike-threat-hunting.png)

By FIR Risk Advisory | Cybersecurity Fraud Intelligence

## Weekly Risk Intelligence Brief

**Source:** [CrowdStrike 2025 Threat Hunting Report](https://www.crowdstrike.com/en-us/resources/reports/threat-hunting-report/) (July 2024 – June 2025)

### The 30-Second Brief

CrowdStrike's threat hunting team observed a fundamental shift: attackers are operating like businesses — fast, credential-led, and cloud-competent. Interactive intrusions increased 27% year-over-year. 81% are malware-free. Electronic crime now represents 73% of all interactive activity.

If your defenses still depend on catching malware, you're defending against last year's attacks.

---

## Four Trends Every Leader Should Track

### 1. Faster and Stealthier — 81% Malware-Free

Interactive intrusions are up 27% year-over-year, and 81% don't use traditional malware at all. Attackers are living off the land — using legitimate tools, stolen credentials, and built-in system utilities. Antivirus is necessary but nowhere near sufficient.

Electronic crime represents 73% of interactive activity. This isn't nation-state espionage driving the numbers — it's organized crime running at scale.

> **INTEL [TREND]:** 81% of interactive intrusions are malware-free. Detection strategies built around malware signatures and endpoint scanning are missing the majority of attacks. Behavioral analytics, identity monitoring, and cross-domain telemetry are now the primary detection surface.

---

### 2. Cloud Intrusions Surged 136%

Cloud intrusions in the first half of 2025 already surpassed all of 2024 — a 136% increase. China-nexus actors account for 40% of the year-over-year growth. Control planes, IAM misconfigurations, and instance metadata services (IMDS) are the primary attack vectors.

> **INTEL [SECTOR ALERT]:** Cloud control planes are critical infrastructure. Enable IAM and control-plane audit logging, monitor IMDS access anomalies, and review third-party service principals and tenant trust relationships. The 136% surge isn't slowing down.

---

### 3. Vishing Exploded — 442% Growth

Voice phishing volume jumped 442% from first half to second half of 2024 — and had already exceeded all of 2024's volume by mid-2025. Attackers are calling help desks, impersonating employees, and manipulating MFA resets.

This bypasses every email filter you have. The attack vector is a phone call.

> **INTEL [ATTACK TECHNIQUE]:** Vishing is now a primary initial access vector, growing at 442%. Help-desk password and MFA reset procedures are the specific target. Restrict reset capabilities, implement callback verification, and train help-desk staff on social engineering recognition — this is the #1 growth vector in CrowdStrike's data.

---

### 4. Sector-Specific Escalation

The targeting isn't random:

- **Government:** Intrusions up 71% overall, with a **185% increase** in nation-state activity (primarily Russia-linked)
- **Telecom:** Up 53% overall, with a **130% increase** in nation-state activity (primarily China-linked)
- **Technology:** Remains the #1 targeted sector across all threat types

> **INTEL [SECTOR ALERT]:** Government and telecom sectors face exponential increases in nation-state targeting. If you're in these sectors — or in their supply chain — threat hunting should be continuous, not periodic. The 185% and 130% increases in nation-state activity aren't fluctuations, they're escalation.

---

## Five Actions for Leaders

1. **Harden identity infrastructure** — Phishing-resistant MFA for executives and admins. Restrict help-desk password and MFA reset capabilities. Monitor bulk user exports.

2. **Eliminate cross-domain gaps** — Unify endpoint, identity, cloud, and edge telemetry through next-gen SIEM and XDR. Attackers move across domains — your visibility must too.

3. **Treat cloud control planes as critical infrastructure** — Enable audit logging, monitor IMDS access, review third-party service principals and tenant trust relationships.

4. **Prepare for malware-free ransomware** — Block remote encryption over SMB. Isolate unmanaged hosts. If your ransomware playbook assumes malware delivery, update it.

5. **Assume patch bypass** — Combine exposure management with post-exploitation hunting during active zero-day windows. Patching is necessary but not sufficient during active exploitation.

---

## Dashboard Metrics to Track

**Identity Security:**
- Phishing-resistant MFA adoption ≥95% for admins and VIPs
- Mean time from suspicious password reset to containment: ≤60 minutes
- After-hours administrative change audit coverage

**Cloud Security:**
- Critical account control-plane audit logging coverage
- IMDS access anomaly monitoring
- Monthly removal tracking for unnecessary roles and API keys

**Resilience:**
- Elimination of unmanaged systems
- Immutable and offline backup success rates

**Exposure Management:**
- Mean time to patch critical internet-facing vulnerabilities
- Post-exploitation behavior detection counts during active exploit cycles

---

## The Bottom Line

"Attackers are acting like businesses: fast, credential-led, and cloud-competent."

That's CrowdStrike's summary. Ours is simpler: if your security operations still run in silos — endpoint team, identity team, cloud team — you're giving attackers the gaps they need. Unified telemetry, identity as critical infrastructure, and cloud control-plane defense aren't roadmap items. They're survival requirements.

---

Stay tuned for more in future FIR Risk Newsletters!

Find all editions on [FIR Risk Tuesday](https://firriskadvisory.com/tuesday/) | [GitHub](https://github.com/stikman28/fir-risk-intelligence)

---

## LINKEDIN POST

```
FIR Risk Tuesday E67 is out.

CrowdStrike's Threat Hunting Report (July 2024 – June 2025).
Attackers are running like a business now.

The data:

→ Interactive intrusions up 27% — 81% are malware-free
→ Cloud intrusions surged 136% (first half 2025 > all of 2024)
→ Vishing exploded 442% — attackers are calling your help desk
→ Government nation-state targeting up 185% (Russia-linked)
→ Telecom nation-state targeting up 130% (China-linked)

If your defenses still depend on catching malware,
you're defending against last year's attacks.

Full analysis: [link]

#CyberSecurity #ThreatHunting #CrowdStrike #CISO #Vishing
```

---

## NOTES

- Source: CrowdStrike 2025 Threat Hunting Report (July 2024 – June 2025)
- Content pulled from LinkedIn newsletter via WebFetch for fir-risk-intelligence archive
- Original published August 19, 2025
- Reformatted to match 2026 newsletter template with INTEL callouts added
- Hero image downloaded from LinkedIn CDN
- Vishing 442% stat is the standout data point
