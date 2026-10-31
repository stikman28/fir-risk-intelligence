# FIR Risk INTEL-50 — The Costliest Cyber Events Are Disruption, Not Data Theft

**Type:** `TREND`
**Date:** November 5, 2026
**Platform Source:** FIR Risk E96 — The Costliest 5%: What Confirmed Losses Teach Us About Planning (Cyentia Institute, IRIS Xtreme 2026)

---

## The INTEL

**Most cyber incidents are data exposure. The costliest ones mostly aren't. Across all incidents, about 91% are mainly data exposure; among the costliest 5% of events over five years, that falls to 33%, and operational disruption rises from 8% to 43%, according to the Cyentia Institute.**

Cyentia's IRIS Xtreme 2026 classifies each event by its primary outcome: data exposure, disruption, or fraud. The shift at the extreme end is large:

- **Exposure:** 91% of all incidents, 33% of extreme events
- **Disruption:** 8% of all incidents, 43% of extreme events
- **Fraud:** under 1% of all incidents, 24% of extreme events, much of it cryptocurrency theft

Set the crypto thefts aside and the pattern is clearer still. For the remaining extreme events, business interruption and lost sales are the largest share of losses (20%), ahead of response and notification costs (18%), which are reported more often but cost less.

The impact also travels. Nearly half of extreme events (46%) spread into the victim's supply chain, and those events account for 55% of losses.

---

## Why It Matters

Most risk registers are built from what happens most often, and what happens most often is data exposure. That puts the planning effort on breach response and notification, while the losses that reach the top of the scale come from operations stopping: production halted, orders unfilled, systems down for weeks.

This is hindsight evidence. Cyentia's data runs to early 2025, because the cost of a cyber event takes many months to become known. But the pattern held after the data closed: the 2026 Verizon DBIR describes the Jaguar Land Rover ransomware attack, which halted production for five weeks and rippled across about 5,000 downstream organizations.

The useful part is that disruption is something an organization can plan and rehearse for. How long operations can run without key systems, and how fast they come back, is largely within its control.

---

## What To Do — One Key Action

**Check whether your risk register includes a multi-week outage, both of your own operations and of a supplier you depend on. If it doesn't, add those scenarios, estimate the cost of the downtime, and check that your insurance covers business interruption at a matching level, not just response costs.**

---

## MITRE ATT&CK

- **T1486 Data Encrypted for Impact** — ransomware, the leading pattern behind disruption losses among extreme events
- **T1489 Service Stop** — the operational outcome this INTEL is about

---

## Learn More

- [IRIS Xtreme 2026 (Cyentia Institute)](https://www.cyentia.com/iris) — Primary source; primary outcomes (Figure 9, p15), loss types (Table 2, p18), secondary impacts (Figure 13, p19)
- [FIR Risk Tuesday E96 — The Costliest 5%: What Confirmed Losses Teach Us About Planning](/tuesday/e96-the-costliest-five-percent/) — Full analysis
- [FIR Risk Tuesday E90 — Refinement, Not Revolution](/tuesday/e90-refinement-not-revolution/) — The 2026 Verizon DBIR, including the Jaguar Land Rover case

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Most cyber incidents are data exposure. The costliest ones mostly aren't.

Cyentia's IRIS Xtreme 2026 looked at the costliest 5% of cyber events over five years:
→ Data exposure: 91% of all incidents, 33% of extreme events
→ Operational disruption: 8% of all incidents, 43% of extreme events
→ Outside crypto theft, business interruption is the largest share of losses

And nearly half of extreme events spread into the victim's supply chain.

If your risk register is mostly data-breach scenarios, it is planned around what happens most, not what costs most.

One check: does it include a multi-week outage of your own operations, and of a supplier you depend on?

FIR Risk INTEL-50: disruption, not data theft.

#CyberRisk #OperationalResilience #RiskManagement #BusinessContinuity #CFO #CISO
```

## X POST

Most cyber incidents are data exposure. The costliest ones mostly aren't.

Data exposure: 91% of all incidents, 33% of extreme events. Disruption: 8% → 43%. (Cyentia IRIS Xtreme 2026)

Does your risk register include a multi-week outage?

Full INTEL → FIR Risk INTEL-50

#CyberRisk #OperationalResilience

---

## SOURCE DATA

**Editorial Frame:**
INTEL-50 = second E96 INTEL (lineup agreed with Bruce 10/31). Framing: optimization, not fear; hindsight evidence for the risk assessment. Fraud kept as one bullet with the crypto caveat (Bruce asked 10/31 what we say about fraud; Cyentia: "a good chunk of those fraud events involve cryptocurrency theft").

**Primary Source:**
- Cyentia Institute, *IRIS Xtreme 2026: An Information Risk Insights Study on Extreme Cyber Events* (38 pp PDF). Verified Oct 31, 2026.

**Fact-Check Notes:**
- p15 Figure 9 (by count, overall → extreme): exposure 91% → 32.8%; disruption 7.8% → 43%; fraud 0.9% → 24.1%. p16 text: "a good chunk of those fraud events involve cryptocurrency theft."
- p18 Table 2 (non-crypto, frequency / loss share): business interruptions & lost sales 29.2% / 20.4%; response & notification 45.8% / 17.8%. Text: business interruptions "drive the largest share of actual losses"; "disruption is the defining outcome of non-crypto extreme events."
- p19 Figure 13: supply chain impact 46.4% of extreme events; text: "over half (55%) of all associated losses."
- p27–28 Figures 18–19: ransomware "the undisputed heavyweight risk champion for extreme cyber events" (basis for T1486).
- p7 Figure 3: quarterly events end early 2025 (reporting lag) — "runs to early 2025" is FIR's reading.
- 2026 Verizon DBIR (via E90, verified 6/2026): Jaguar Land Rover five-week production halt, ~5,000 downstream organizations.

**FIR Risk Editorial Position:**
- "Disruption is something an organization can plan and rehearse for" = FIR position.
- T1489 is FIR's mapping of the outcome; Cyentia's technique analysis (Table 3) covers initial access only.
