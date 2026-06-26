# FIR Risk INTEL-23 — The Permission Problem

**Type:** `TECHNIQUE`
**Date:** June 25, 2026
**Platform Source:** FIR Risk E90 — Refinement, Not Revolution (2026 Verizon DBIR)

---

## The INTEL

**The 2026 DBIR settles a long-running argument: privilege escalation is an identity-and-permissions problem, not a patching one. 83% of escalation incidents involved no vulnerability exploit at all — attackers used the permissions that were already there.**

Most security budgets treat escalation as something you patch your way out of. The data says otherwise. Only about 10% of escalation techniques are mitigated by patching; 65% are mitigated by privilege management. The single most common technique in real breaches isn't an exploit — it's **"valid accounts": logging in with legitimate credentials, at 39%.** Attackers aren't breaking in. They're signing in, then walking the permissions they find.

The clearest picture of why is in the assessment data: in 16% of organizations, any initial foothold gave roughly an 80% chance of reaching a key administrative account — not through exploits, but by chaining together existing Active Directory permissions until the path to domain-admin opened up.

---

## Why It Matters

It's tempting to read "escalation is everywhere" as "we need to patch faster." That's the wrong lesson — and the 83% proves it. When five out of six escalations involve no exploit at all, patch velocity isn't the lever. The permission structure underneath is.

This is a fundamentals problem, and the assessment data shows the fundamentals are slipping. 97% of assessed devices failed the failed-login-lockout configuration check; 90% failed the 15-character minimum password-length check. These aren't exotic gaps — they're the boring, maintainable controls that make valid-account abuse and credential-chaining harder. They degrade quietly when no one is watching them.

There's a sharper warning underneath the numbers, too. Red teams over-index on flashy identity attacks — cracking service-account passwords, forging authentication tokens — that barely register in real incident data. The lesson: defend against what's actually happening in breaches, not against the most cinematic move in the pentest report. The unglamorous work — least privilege, dormant-account cleanup, Active Directory hygiene — is where the real exposure lives.

---

## What To Do — One Key Action

**Pull a report of standing privileged access and the permission paths that lead to your Tier-0 and domain-admin accounts — then systematically right-size and remove them, and keep doing it on a cadence that never lapses.**

Privilege management, not patching, stops the large majority of escalations — 65% versus roughly 10%. So the work isn't a faster scanner; it's a standing privilege inventory and an Active Directory permission map. Find the accounts that carry admin rights they don't need. Find the chains where an ordinary foothold can walk, hop by hop, into a Tier-0 account. Cut them. Then treat least-privilege and AD hygiene the way you'd treat any fundamental — a control that's maintained consistently, not a project that's done once and left to drift back into 97%-fail territory.

The one question for your next review: not "are we patching fast enough?" but **"do we know every standing privileged-access path to our crown-jewel accounts — and are we shrinking it every cycle?"** The full plan is in [E90](/tuesday/e90-refinement-not-revolution/); staying consistent on this fundamental is where it starts.

---

## MITRE ATT&CK

- **T1078 — Valid Accounts:** The #1 technique in real breaches — attackers log in rather than break in. Controls = least privilege, MFA, and disciplined dormant-account disablement.
- **T1098 / T1484 — Account & Permission Manipulation:** The Active Directory permission-chaining behind the ~80% escalation exposure. Control = privileged access management plus Tier-0 isolation.

---

## Learn More

- [FIR Risk Tuesday E90 — Refinement, Not Revolution](/tuesday/e90-refinement-not-revolution/) — The full 2026 DBIR breakdown and prioritization plan
- [2026 Verizon Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/dbir/) — Primary source
- [CIS Critical Security Controls](https://www.cisecurity.org/controls) — The least-privilege and account-management fundamentals at the center of the finding

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
The 2026 Verizon DBIR settles a long-running argument: privilege escalation is an identity-and-permissions problem, not a patching one.

83% of escalation incidents involved no vulnerability exploit at all.

Attackers used the permissions that were already there.

Most security budgets treat escalation as something you patch your way out of. The data says otherwise. Only ~10% of escalation techniques are mitigated by patching. 65% are mitigated by privilege management.

And the most common technique in real breaches isn't an exploit. It's "valid accounts" — logging in with legitimate credentials — at 39%. Attackers aren't breaking in. They're signing in, then walking the permissions they find.

The clearest picture of why: in 16% of organizations, any initial foothold gave roughly an 80% chance of reaching a key administrative account. Not through exploits — by chaining existing Active Directory permissions until the path to domain-admin opened up.

So the lesson is NOT "patch faster." When five out of six escalations involve no exploit, patch velocity isn't the lever.

The fundamentals are. And they're slipping: 97% of assessed devices failed the failed-login-lockout check. 90% failed the 15-character minimum password-length check. Boring, maintainable controls — degrading quietly because no one was watching them.

One more warning in the data: red teams over-index on flashy identity attacks (cracking service-account passwords, forging authentication tokens) that barely appear in real breaches. Defend against the incident data, not the pentest highlight reel.

One action to consider:

→ Pull a report of standing privileged access and the permission paths to your Tier-0 / domain-admin accounts.

→ Systematically right-size and remove them.

→ Keep doing it on a cadence that never lapses.

Privilege management — not patching — stops the large majority of escalations. Make least-privilege and Active Directory hygiene a fundamental you maintain consistently.

The full plan is in this week's edition.

FIR Risk INTEL-23 — The Permission Problem.

#cybersecurity #identitysecurity #CISO #privilegedaccess #activedirectory #riskmanagement #fundamentals #infosec
```

---

## X POST

The 2026 Verizon DBIR settles a long-running argument: privilege escalation is an identity-and-permissions problem, not a patching one. 83% of escalation incidents involved no vulnerability exploit at all.

Attackers used the permissions that were already there.

Only ~10% of escalation techniques are mitigated by patching. 65% are mitigated by privilege management. And the #1 technique in real breaches isn't an exploit — it's "valid accounts," logging in with legitimate credentials, at 39%.

The clearest picture of why: in 16% of organizations, any initial foothold gave ~80% odds of reaching a key admin account — by chaining existing Active Directory permissions, not exploits.

So the lesson is NOT "patch faster." When five out of six escalations involve no exploit, patch velocity isn't the lever. The fundamentals are — and they're slipping. 97% of assessed devices failed the login-lockout check. 90% failed the 15-character password-length check.

One more warning: red teams over-index on flashy identity attacks (cracking service-account passwords, forging authentication tokens) that barely appear in real breaches. Defend against the incident data, not the pentest highlight reel.

One action to consider: pull a report of standing privileged access and the permission paths to your Tier-0 / domain-admin accounts. Right-size and remove them. Keep doing it on a cadence that never lapses.

Privilege management — not patching — stops the large majority of escalations. Make least-privilege and AD hygiene a fundamental you maintain consistently.

INTEL-23 — The Permission Problem.

#cybersecurity #identitysecurity

---

## SOURCE DATA

**Editorial Frame:**
INTEL-23 extends the E90 DBIR series from initial access (INTEL-22's vulnerability-exploitation finding) into post-access movement. It isolates the report's sharpest escalation finding — 83% of escalations involve no exploit, and privilege management mitigates 65% of techniques versus ~10% for patching — and converts it into a single executive action: inventory and right-size standing privileged access, not chase patch velocity. Consistent with E90's "stay consistent on the fundamentals" thesis.

**Primary Source:** FIR Risk E90 — Refinement, Not Revolution (June 23, 2026)
**Supporting Source:** 2026 Verizon Data Breach Investigations Report (May 2026)

**Fact-Check Notes (page-cited to the DBIR):**
- CONFIRMED: 83% of privilege-escalation incidents involved no vulnerability exploit at all (p. 70)
- CONFIRMED: Only ~10% of escalation techniques mitigated by patching; 65% mitigated by privilege management (p. 68)
- CONFIRMED: "Valid accounts" is the #1 technique in real breaches at 39% (p. 69)
- CONFIRMED: In 16% of organizations, any initial foothold gave ~80% chance of reaching a key administrative account by chaining Active Directory permissions, not exploits (p. 71)
- CONFIRMED: 97% of assessed devices failed the failed-login-lockout config check; 90% failed the 15-character minimum password-length check (p. 71)
- CONFIRMED: Red teams over-index on flashy identity attacks (e.g., Kerberoasting, token manipulation) that barely appear in real incident data — defend against the incident data, not the pentest (p. 69)

**FIR Risk Editorial Position:**
- TECHNIQUE-type INTEL; audience = CISO, identity/IAM teams, security operations, risk leaders
- The "83% / no exploit" figure leads because it invalidates the patch-centric framing most escalation budgets run on
- One key action is consistency on the fundamental (standing-privilege inventory + AD hygiene), explicitly *not* "patch faster"; E90 carries the full plan
- No fabricated CVEs, actor names, vendors, or dollar figures; every DBIR figure traces to a specific page
