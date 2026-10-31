# FIR Risk INTEL-49 — Plan for the Tail, Not the Average

**Type:** `TREND`
**Date:** November 4, 2026
**Platform Source:** FIR Risk E96 — The Costliest 5%: What Confirmed Losses Teach Us About Planning (Cyentia Institute, IRIS Xtreme 2026)

---

## The INTEL

**Averages are a poor guide to cyber loss planning. For a company under $100 million in revenue, the median cyber incident costs about $357,000, but the 95th-percentile loss, the one-in-twenty bad outcome, is $9.1 million: about 25 times higher. The gap holds at every size, according to the Cyentia Institute's loss data.**

Cyentia's IRIS Xtreme 2026 breaks loss planning down by revenue band, drawing on its IRIS 2025 study of all publicly reported incidents. The median and the 95th percentile for each band:

- **Under $100M:** $357,000 median, $9.1 million at the 95th percentile
- **$100M to $1B:** $466,700 median, $12.3 million
- **$1B to $10B:** $1.8 million median, $61.8 million
- **Over $10B:** $2.2 million median, $266.2 million

Losses don't scale with company size. A $9 million loss is nearly 20% of revenue for a $50 million company; $266 million is about 0.5% for a $50 billion one.

The common shortcut doesn't help either. Many loss estimates multiply records stolen by a cost per record. Across the costliest 5% of cyber events in the study, the number of records stolen told you almost nothing about the loss: Cyentia's regression line is nearly flat, predicting the same cost for a thousand records as for a billion.

---

## Why It Matters

Most organizations experience cyber incidents as a steady run of manageable costs, and plan that way. But Cyentia's simulations show that for most organizations, it takes about seven years of those smaller incidents to add up to a single extreme one. A plan built on the typical case leaves the expensive tail unfunded.

The figures also err on the low side. They count publicly reported, mostly direct losses, so Cyentia treats them as a conservative lower bound. And they keep rising: the 95th-percentile loss across all incidents has grown 19 times since 2008, adjusted for inflation.

The useful part is that this gives every organization a defensible starting point. Cyentia's own test: if your worst-case scenario is a few million dollars and you're a multi-billion-dollar company, you're probably off by an order of magnitude. If every scenario on your risk register is a billion-dollar catastrophe, you're probably overstating it. Either way, insurance limits, cash reserves and security investment end up sized to the wrong number.

---

## What To Do — One Key Action

**Check your worst-case cyber loss estimate against the 95th-percentile figure for your revenue band, and set an upper and lower bound you can defend with evidence. Then use that range for the decisions that depend on it: insurance limits, cash reserves, and how much goes to resilience as well as prevention.**

If the estimate today is a single number from a vendor report or the last headline, the revenue-band range is a better place to start.

---

## MITRE ATT&CK

- **Not technique-specific.** This INTEL is about loss sizing. For scenarios at the tail, E96 covers the technique most tied to extreme losses: T1078 Valid Accounts, present in events accounting for 91% of extreme losses.

---

## Learn More

- [IRIS Xtreme 2026 (Cyentia Institute)](https://www.cyentia.com/iris) — Primary source; Table 1 loss statistics by revenue band (p5), cost per record (Figure 11, pp16–17)
- [FIR Risk Tuesday E96 — The Costliest 5%: What Confirmed Losses Teach Us About Planning](/tuesday/e96-the-costliest-five-percent/) — Full analysis
- [FIR Risk Tuesday E59 — Cyentia Institute's 2025 Information Risk Insights Study](/tuesday/e59-iris-2025-risk-insights/) — The all-incident study behind the revenue bands

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Averages are a poor guide to cyber loss planning.

For a company under $100M in revenue, the median cyber incident costs about $357K. The 95th-percentile loss, the one-in-twenty bad outcome, is $9.1M. That's 25 times higher. (Cyentia IRIS)

And the shortcut many plans use, cost per record, doesn't work at all. Across the costliest 5% of cyber events, the number of records stolen told you almost nothing about the loss.

Three things the evidence supports:
→ Size loss estimates to your revenue band, not to an industry average
→ Fund resilience for high-impact scenarios, not just prevention
→ Build insurance limits and cash reserves around the tail, not the typical case

FIR Risk INTEL-49: plan for the tail, not the average.

#CyberRisk #RiskQuantification #CyberInsurance #CFO #CISO #RiskManagement
```

## X POST

Averages are a poor guide to cyber loss planning.

Under $100M in revenue: median cyber incident ~$357K. The 1-in-20 bad outcome: $9.1M, 25x higher. (Cyentia IRIS)

And cost per record doesn't predict loss at all.

Size your worst case to your revenue band, then build insurance and reserves around it.

Full INTEL → FIR Risk INTEL-49

#CyberRisk #RiskQuantification

---

## SOURCE DATA

**Editorial Frame:**
INTEL-49 = first E96 INTEL (Bruce, 10/31). Angle from a Gemini summary Bruce liked ("averages and cost-per-record shortcuts lead organizations astray"; loss exceedance, resilience, insurance and reserves), rebuilt on verified figures. Gemini's "$266K typical median" was wrong (garbled $266.2M) and is NOT used. Framing: optimization, not fear; hindsight evidence for the risk assessment. Board/action phrased as direction, no mandates.

**Primary Source:**
- Cyentia Institute, *IRIS Xtreme 2026: An Information Risk Insights Study on Extreme Cyber Events* (38 pp PDF). Verified Oct 31, 2026.

**Fact-Check Notes:**
- p5 Table 1 "Summary loss statistics by revenue band" (Source: IRIS 2025, Cyentia Institute) 50% / 95%: More than $10B $2.2M / $266.2M; $1B to $10B $1.8M / $61.8M; $100M to $1B $466.7K / $12.3M; Less than $100M $357.0K / $9.1M. Ratios (FIR arithmetic): 25.5x, 26.4x, 34.3x, 121x — "about 25 times" for <$100M; "the gap holds at every size."
- p5: "A $9M loss for a $50M organization represents nearly 20% of their annual revenue… a $266M loss for a $50B organization represents 0.5% of revenue." NOTE box: direct losses, "a more conservative lower bound."
- pp16–17 Figure 11 (extreme events with known record counts, crypto excluded): "The regression line… is almost perfectly flat, producing the same loss prediction for a breach of a thousand records as for a breach of a billion."
- pp8–9 Figure 4: "on average, it takes 7 years of 'minor cuts' to equal the damage caused by one 'critical hit'" (Figure 5: for >$100B firms, smaller losses overtake in <3 years — hence "for most organizations").
- p6 Figure 2: 95th percentile $14.7M (2008) → $281.3M, 19.1x, inflation-adjusted 2025 USD.
- p32: "If your worst-case ransomware scenario is $5M and you're a multi-billion dollar company, you're off by an order of magnitude… if every scenario on your risk register produces a billion-dollar loss, you're likely catastrophizing… Set an upper and lower bound for the extreme loss scenarios that you can justify with this data." p33: insurance limits vs the 95th percentile; capital reserves.
- p29 Table 3: Valid accounts 58.1% of extreme events, 91.0% of losses (multi-label).

**FIR Risk Editorial Position:**
- "One-in-twenty bad outcome" = plain-language reading of the 95th percentile.
- The key action follows Cyentia's "Now What" decisions 1 and 3; resilience-vs-prevention echoes Cyentia's p10 question.
