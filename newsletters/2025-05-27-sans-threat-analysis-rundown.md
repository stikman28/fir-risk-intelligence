# FIR Risk Tuesday E56 - SANS Threat Analysis Rundown with Katie Nickels

**Publish Date:** May 27, 2025
**Source:** [SANS — 2025 Cyber Threat Reports: Real-World Lessons for Defenders](https://www.sans.org/)
**Analysis:** FIR Risk Advisory

---

## NEWSLETTER DRAFT

# FIR Risk E56 - 48 Minutes to Breakout

![FIR Risk E56 - SANS Threat Analysis Rundown](images/E56-sans-threat-analysis-rundown.png)

By FIR Risk Advisory | Cybersecurity Fraud Intelligence

## Weekly Risk Intelligence Brief

**Source:** SANS Threat Analysis Rundown with Katie Nickels — synthesizing Mandiant M-Trends, CrowdStrike Global Threat Report, and Verizon DBIR (May 2025)

### The 30-Second Brief

SANS analyst Katie Nickels synthesized findings from three of the industry's most authoritative threat reports — Mandiant M-Trends, CrowdStrike Global Threat Report, and Verizon DBIR. The convergence point: **credential abuse, phishing, and vulnerability exploitation remain the dominant entry points.** Ransomware surged 37%. But dwell time dropped to 11 days. And the average breakout time — how fast attackers move laterally after initial access — is just **48 minutes.**

You have less than an hour to detect and contain before the attacker owns your network.

---

## The Cross-Report View

### Entry Points Haven't Changed — But Speed Has

Across all three reports, the same entry points dominate: **credential abuse, phishing, and vulnerability exploitation.** Breaches frequently stem from exposed secrets (like GitLab tokens) and unpatched edge devices.

What's changed is speed. CrowdStrike measured average breakout time at **48 minutes** — the time from initial access to lateral movement. That's your detection window.

> **INTEL [TREND]:** Credential abuse, phishing, and vulnerability exploitation remain the top three entry points across Mandiant, CrowdStrike, and Verizon data. But breakout time has compressed to 48 minutes. Detection and containment must operate within that window — anything slower means the attacker has already moved laterally.

---

### Ransomware: 37% Surge, 64% Don't Pay

- **37% surge** in ransomware incidents year-over-year
- **64%** of victims declined to pay
- **Average ransom demand:** $115,000

The refusal-to-pay trend is encouraging — but it's driving attackers toward double extortion and data theft as primary monetization.

> **INTEL [SECTOR ALERT]:** Ransomware incidents surged 37% but 64% of victims refused to pay, with average demands at $115K. This non-payment trend is pushing attackers toward data theft and extortion as primary monetization. Ensure your incident response plans account for data exfiltration scenarios, not just encryption.

---

### Detection Is Improving

- **Dwell time reduced to 11 days** — a significant improvement from historical averages
- **45%** of breaches detected within one week
- **Employees reported 14%** of breaches — human detection still matters

> **INTEL [TREND]:** Dwell time dropped to 11 days with 45% of breaches detected within one week. Employee reporting accounts for 14% of detections. Security awareness programs that teach employees what to report — not just what to avoid — are producing measurable detection value.

---

### The Malware Landscape

Mandiant identified **632 new malware families** in 2024. Key trends:

- **Linux malware is rising** — as cloud and container workloads grow, so does Linux-targeted malware
- **79% of CrowdStrike detections** involve legitimate tool misuse — attackers living off the land
- **Generative AI** is being used for phishing and script automation, but the higher risk is employees using personal AI accounts with sensitive corporate data

> **INTEL [ATTACK TECHNIQUE]:** 632 new malware families identified by Mandiant. 79% of CrowdStrike detections involve legitimate tool misuse (living off the land). Linux malware is rising with cloud workload growth. Detection strategies must go beyond malware signatures to behavioral analytics and tool authorization monitoring.

---

## What Leaders Should Do Now

1. **Compress your detection-to-containment window below 48 minutes** — That's the average breakout time. If your SOC can't detect and respond faster, attackers will have lateral movement before you know they're in.

2. **Prioritize credential security** — Credential abuse is the #1 entry point across all three reports. Phishing-resistant MFA, credential monitoring, and secret scanning are non-negotiable.

3. **Patch edge devices aggressively** — Unpatched edge devices and exposed secrets are consistent breach vectors. Treat internet-facing assets as your highest-priority patch targets.

4. **Plan for data exfiltration, not just encryption** — 64% non-payment is shifting attackers to data theft. Incident response plans need exfiltration detection and response playbooks.

5. **Monitor for legitimate tool abuse** — 79% of detections involve legitimate tools. Maintain an authorized software inventory and alert on unauthorized use of RMM tools, scripting utilities, and admin frameworks.

6. **Govern employee AI usage** — The bigger AI risk isn't attacker-generated phishing — it's employees feeding sensitive data into personal AI accounts. Establish acceptable use policies and provide sanctioned AI tools.

---

## The Bottom Line

Three reports. One message: the fundamentals haven't changed, but the clock is running faster. Credential abuse, phishing, and vulnerability exploitation dominate. Breakout time is 48 minutes. Dwell time is down to 11 days. And 79% of detections involve legitimate tools, not malware.

The organizations winning this fight aren't deploying exotic defenses. They're executing the basics faster than attackers can move.

---

Stay tuned for more in future FIR Risk Newsletters!

Find all editions on [FIR Risk Tuesday](https://firriskadvisory.com/tuesday/) | [GitHub](https://github.com/stikman28/fir-risk-intelligence)

---

## LINKEDIN POST

```
FIR Risk Tuesday E56 is out.

SANS Threat Analysis Rundown — Katie Nickels synthesizes
Mandiant M-Trends, CrowdStrike, and Verizon DBIR.

Three reports. One message:

→ Credential abuse, phishing, vuln exploitation still dominate
→ Ransomware surged 37% — but 64% refused to pay
→ Average breakout time: 48 minutes
→ Dwell time down to 11 days
→ 632 new malware families (Linux rising)
→ 79% of detections involve legitimate tool misuse

You have 48 minutes before the attacker moves laterally.
How fast is your SOC?

Full analysis: [link]

#CyberSecurity #SANS #ThreatIntelligence #Mandiant #CrowdStrike #DBIR
```

---

## NOTES

- Source: SANS Threat Analysis Rundown with Katie Nickels (May 2025)
- Synthesizes Mandiant M-Trends, CrowdStrike Global Threat Report, Verizon DBIR
- Content pulled from LinkedIn newsletter via WebFetch for fir-risk-intelligence archive
- Original published May 27, 2025
- Reformatted to match 2026 newsletter template with INTEL callouts added
- Hero image: LinkedIn CDN likely expired, needs manual save from article
- 48-minute breakout time is the standout stat
- Cross-report synthesis format is unique among the newsletter editions

