# FIR Risk INTEL-35 — The Fuse Is Already Lit

**Type:** `REGULATORY`
**Date:** July 24, 2026
**Platform Source:** FIR Risk E92 — Time Is the Attack Surface (Microsoft/Accenture, Securing Nations in the Intelligent Economy)

---

## The INTEL

**"Harvest now, decrypt later" is already operational — adversaries are stealing encrypted data today and warehousing it against the day quantum computing can open it — and governments have responded with specific, dated migration mandates: US federal systems to post-quantum cryptography by 2035 ($7.1B funded), EU and UK critical infrastructure by 2030 with full migration by 2035, India's National Quantum Mission 2026–28, South Korea standards finalized 2025 for deployment by 2035. Yet only 22% of executives rank quantum as the most game-changing technology, versus 66% for AI. The deadlines and the attention are pointed in opposite directions.**

The timeline pressure comes from a revised technical estimate: the long-standing consensus held that breaking RSA-2048 would require roughly 20 million qubits; newer research cited in the Microsoft/Accenture report (a Google researcher's analysis) suggests an advanced one-million-qubit system — achievable by ~2030 on current trajectories — could do it. Treat that date as a vendor-relayed industry projection, not settled fact: it rests on physical-qubit counts rather than error-corrected logical qubits, and independent academic estimates run wider and later. But the strategic conclusion doesn't depend on the date. Data with a 10–20 year confidentiality shelf life — health records, financial account data, PII, trade secrets — that is exfiltrated *today* is already on the fuse, whether decryption arrives in 2030 or 2040.

The replacement tooling exists: NIST's post-quantum standards (ML-KEM, ML-DSA) are finalized.

---

## Why It Matters

This is the cleanest current example of a risk class that boards systematically underprice: the long fuse. Budget processes naturally fund the risks that produced last quarter's incidents — ransomware has incident reports, so ransomware gets funded. Harvest-now-decrypt-later will never produce an incident report, because the harm detonates years after the theft, retroactively, all at once. By the time there is incident evidence, the window to act has been closed for a decade.

That's why the 66/22 attention gap is the statistic that matters more than any qubit count. It means most organizations will start their cryptographic migration when regulation forces them or when a decryption event makes headlines — which is to say, late, expensive, and simultaneously with everyone else. For regulated firms — financial services and healthcare above all, whose data carries the longest confidentiality obligations in the economy — the inversion is an arbitrage: crypto-inventory work started in 2026 is cheap, differentiating with regulators, and years ahead of the peer group.

The regulatory direction is unambiguous even where the science is uncertain. When the US commits $7.1B and a 2035 statutory deadline, and the EU/UK set 2030 for critical infrastructure, examiners' questions follow. "What is your post-quantum migration plan?" is on its way to joining "what is your ransomware playbook?" as a standard examination item.

---

## What To Do — One Key Action

**Start the cryptographic inventory this year. Catalogue where your long-lived sensitive data lives — anything that must stay confidential for 10+ years — and which encryption protects it in transit and at rest. Today's standard public-key cryptography (RSA/ECC) is the class at risk; the finalized NIST post-quantum standards (ML-KEM, ML-DSA) are the destination. The inventory, not the migration, is the 2026 deliverable — you cannot sequence a multi-year migration you haven't mapped.**

And apply the broader test this risk class teaches: in your next risk-appetite review, name one material risk with zero incident history but a fixed external deadline, and check whether it appears anywhere in your capital plan. If it doesn't, your funding model is driven by memory, not exposure — and harvest-now-decrypt-later is exactly the kind of risk it will miss.

---

## MITRE ATT&CK

- **T1020 — Automated Exfiltration · T1560 — Archive Collected Data:** The techniques behind the harvest. Nothing about harvest-now-decrypt-later requires new attacker tradecraft — the exfiltration looks like any other data theft. What changes is the victim's damage model: encrypted data that would once have been written off as unreadable must now be treated as compromised-on-delay.

---

## Learn More

- [FIR Risk Tuesday E92 — Time Is the Attack Surface](/tuesday/e92-time-is-the-attack-surface/) — The full three-clock analysis, including the evidentiary caveats on the quantum timeline
- [NIST Post-Quantum Cryptography Standards](https://csrc.nist.gov/projects/post-quantum-cryptography) — The finalized replacement standards (ML-KEM, ML-DSA)
- [CISA Post-Quantum Cryptography Initiative](https://www.cisa.gov/quantum) — US migration guidance
- [Securing Nations in the Intelligent Economy (Microsoft & Accenture)](https://wwps.microsoft.com/blog/securing-nations-ai-quantum-disruption) — Primary source for the deadline table and timeline estimates

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
There's a category of cyber risk that will never appear in your incident reports — until the year it becomes the only thing in them.

"Harvest now, decrypt later" is already operational. Adversaries are stealing encrypted data today and warehousing it for the day quantum computing can open it. Health records, financial account data, PII, trade secrets — anything with a 10–20 year confidentiality shelf life is effectively at risk the day it's exfiltrated, whenever decryption day arrives.

Governments are acting on specific deadlines:
→ US: federal migration to post-quantum cryptography by 2035, $7.1B funded
→ EU/UK: critical infrastructure by 2030, full migration by 2035
→ India: National Quantum Mission targets 2026–28
→ South Korea: standards finalized 2025, deployment by 2035

Yet only 22% of executives rank quantum as the most game-changing technology — versus 66% for AI.

Why the gap? Because long-fuse risks never generate incident reports until the fuse ends. Budget processes fund what breached last quarter. Ransomware has incident evidence, so ransomware gets funded. Harvest-now-decrypt-later detonates years after the theft, retroactively, all at once — by the time there's evidence, the window to act closed a decade ago.

For regulated firms, the inversion is an arbitrage: a cryptographic inventory started in 2026 is cheap, differentiating with regulators, and years ahead of the peer group. The inventory — where does 10-year data live, what encryption protects it — is the 2026 deliverable. NIST's replacement standards are finalized. You can't sequence a migration you haven't mapped.

And the broader test: name one material risk with zero incident history but a fixed external deadline, and check whether it appears in your capital plan. If it doesn't, your funding model runs on memory, not exposure.

Full analysis in FIR Risk Tuesday E92 — link in the comments.

#CyberSecurity #QuantumComputing #PostQuantum #DataProtection #CISO #RiskManagement #Compliance
```

## X POST

There's a cyber risk that will never appear in your incident reports — until the year it's the only thing in them.

"Harvest now, decrypt later" is operational. Adversaries are stealing encrypted data today, warehousing it for the day quantum computing can open it.

Anything sensitive for 10+ years — health records, financial data, trade secrets — is at risk the day it's exfiltrated. Whenever decryption day comes.

Governments have set hard deadlines:
US: PQC migration by 2035 ($7.1B funded)
EU/UK: critical infrastructure by 2030
India: 2026–28
South Korea: standards done, deployment by 2035

Yet only 22% of executives rank quantum as game-changing. 66% say AI.

The gap exists because long-fuse risks never generate incident evidence until the fuse ends — and budgets fund what breached last quarter.

That's the arbitrage: a crypto inventory started in 2026 is cheap, impresses regulators, and runs years ahead of peers. Map where your 10-year data lives and what encrypts it. NIST's replacement standards are final.

You can't sequence a migration you haven't mapped.

Full analysis → FIR Risk Tuesday E92

#CyberSecurity #PostQuantum

---

## SOURCE DATA

**Editorial Frame:**
INTEL-35 is the long-fuse leg of the E92 set — HNDL as the canonical example of incident-free, deadline-bound risk that memory-driven budget processes systematically miss. Typed REGULATORY because the actionable pressure comes from the dated government mandates, not from the (uncertain) quantum science.

**Primary Sources:**
- Microsoft & Accenture — Securing Nations in the Intelligent Economy (2026): HNDL and deadline table p. 17 (ref 27), qubit estimates p. 16 (refs 25/26), perception gap p. 8 (ref 9)
- NIST Post-Quantum Cryptography project (independent verification of ML-KEM/ML-DSA finalization)

**Fact-Check Notes (verified against source PDF):**
- CONFIRMED: PQC deadlines — US 2035/$7.1B; EU+UK critical infrastructure 2030, full migration 2035; India National Quantum Mission (₹6,000 crore) 2026–28; South Korea MSIT standards 2025.
- CONFIRMED: prior ~20M-qubit consensus; 1M-qubit "achievable by 2030" per new research (Google researcher analysis via Quantum Insider, ref 25); Caltech 6,100-qubit array (ref 26).
- CONFIRMED: 66% vs 22% executive perception gap (p. 8).
- CAVEAT CARRIED: the 2030 date is labeled a vendor-relayed industry projection resting on physical (not logical) qubit counts; both report authors sell quantum-readiness services; conclusions are constructed to hold whether decryption arrives 2030 or 2040.

**FIR Risk Editorial Position:**
- The 66/22 attention gap, not the qubit count, is treated as the decision-relevant statistic.
- The 2026 deliverable is deliberately scoped to the inventory (cheap, unambiguous) rather than the migration (multi-year capital planning).
- The risk-register test ("zero incident history + fixed external deadline") generalizes the lesson beyond quantum — this is the edition's most durable idea.
- Voice: declarative, board-readable, incentive-aware.
