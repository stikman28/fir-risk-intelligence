# FIR Risk INTEL-40 — Obscurity Is Not a Control

**Type:** `TREND`
**Date:** October 20, 2026
**Platform Source:** FIR Risk E93 — The Attacks Aren't New. The Economics Are. (Anthropic, Detecting and countering misuse of AI: September 2026)

---

## The INTEL

**The quiet corner of your network is no longer safe. Anthropic's September 2026 threat report says it plainly: "The old adage of 'security through obscurity' is no longer viable in this new AI-assisted world: everything connected to the internet is a potential target for exploitation." With AI, the report says, diverse target environments become "trivial to understand," and unique and obscure configurations "are made clear and exploitable."**

The economics explain why. AI lowers the skill and labor an attacker needs per campaign "while leaving potential payoffs largely unchanged," which the report says "makes previously marginal targets viable and encourages higher-volume, lower-touch operations." Opportunistic groups now race to exploit newly published vulnerabilities before victims apply patches, and mass-scan internet-facing devices for anything they can open.

Exploit supply is no longer the bottleneck it was. The report describes a Chinese-speaking espionage group (GTG-10007), including two undergraduate students, that ran an automated exploit foundry: AI conducted vulnerability research around the clock and kept working while the operators were away. The group targeted roughly fifty organizations across education, retail, energy, healthcare, finance and government.

---

## Why It Matters

Many organizations, especially smaller ones, carry an unspoken assumption: we're not interesting enough to attack, and our odd legacy setup is too obscure to bother with. Both halves of that assumption just failed. Attackers don't need to find you interesting if finding you costs almost nothing, and AI reads an unusual configuration as easily as a common one.

The systems most at risk are the ones nobody remembers: the old VPN appliance, the test server left online, the admin panel a contractor set up years ago. You can't patch what you don't know you have.

---

## What To Do — One Key Action

**Build a complete inventory of everything your organization exposes to the internet (domains, IP ranges, VPN and firewall appliances, admin panels, cloud services and forgotten test systems) and assign a named owner to each one. Anything without an owner gets reviewed and either secured or shut down.**

Use an external scan to find what your own records miss. Attackers are already running one against you.

---

## MITRE ATT&CK

- **T1595 — Active Scanning · T1190 — Exploit Public-Facing Application:** Opportunistic actors scan the internet at scale and exploit whatever responds. AI doesn't change these techniques; it removes the labor that once made small or unusual targets not worth the effort.

---

## Learn More

- [Detecting and countering misuse of AI: September 2026 (Anthropic)](https://www.anthropic.com/threat-intelligence-report-september-2026) — Primary source, cases GTG-50014 and GTG-10007
- [FIR Risk Tuesday E93 — The Attacks Aren't New. The Economics Are.](/tuesday/e93-the-economics-changed/) — Full analysis of the report
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Prioritize the internet-facing flaws attackers are actively using

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
"The old adage of 'security through obscurity' is no longer viable."

That's Anthropic, in its September threat report. AI makes unusual configurations easy to understand and exploit, and it lowers attacker costs enough to make previously marginal targets worth attacking.

The report even describes two undergraduate students in a Chinese-speaking espionage group running an automated exploit foundry, with AI researching vulnerabilities around the clock while they were away.

The systems most at risk are the ones nobody remembers: the old VPN appliance, the forgotten test server, the admin panel a contractor set up years ago.

One action: build a complete inventory of everything you expose to the internet, and give every item an owner.

Full INTEL — link in the comments.

#CyberSecurity #SMB #AttackSurfaceManagement #CISO #RiskManagement
```

## X POST

"The old adage of 'security through obscurity' is no longer viable."

That's Anthropic, in its September threat report. AI makes unusual configurations easy to understand and exploit, and it lowers attacker costs enough to make previously marginal targets worth attacking.

The report even describes two undergraduate students in a Chinese-speaking espionage group running an automated exploit foundry, with AI researching vulnerabilities around the clock while they were away.

The systems most at risk are the ones nobody remembers: the old VPN appliance, the forgotten test server, the admin panel a contractor set up years ago.

One action: build a complete inventory of everything you expose to the internet, and give every item an owner.

Full INTEL → FIR Risk INTEL-40

#CyberSecurity #RiskManagement

---

## SOURCE DATA

**Editorial Frame:**
INTEL-40 is the attack-surface leg of the E93 set, aimed especially at smaller organizations that rely on being unremarkable. The one action is an owned inventory of everything internet-facing.

**Primary Sources:**
- Anthropic — Detecting and countering misuse of AI: September 2026 (published Sept 10, 2026; 154-page PDF; activity disrupted Dec 2025 – Aug 2026). Read from the PDF; quotes and figures verified against it on Oct 11, 2026.
- CISA Known Exploited Vulnerabilities Catalog (linked for prioritization)

**Fact-Check Notes (verified against the report PDF, Oct 11, 2026):**
- CONFIRMED: "The old adage of 'security through obscurity' is no longer viable in this new AI-assisted world: everything connected to the internet is a potential target for exploitation."
- CONFIRMED: "trivial to understand"; "unique and obscure configurations are made clear and exploitable."
- CONFIRMED: "while leaving potential payoffs largely unchanged"; "makes previously marginal targets viable and encourages higher-volume, lower-touch operations."
- CONFIRMED: racing N-day patches and mass scanning of internet-facing devices (opportunistic attacks).
- CONFIRMED: GTG-10007 "automated exploit foundries"; two operators identified as undergraduate students; research around the clock; capabilities "kept operating while its owners were away"; roughly fifty organizations across education, retail, energy, technology, healthcare, finance, manufacturing and government.

**FIR Risk Editorial Position:**
- "Exploit foundry" used descriptively (the report's phrase is plural, "exploit foundries").
- Voice: declarative, board-readable, incentive-aware.
