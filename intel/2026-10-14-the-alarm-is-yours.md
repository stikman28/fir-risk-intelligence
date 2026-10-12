# FIR Risk INTEL-36 — The Alarm Is Yours

**Type:** `DEFENDER TAILWIND`
**Date:** October 14, 2026
**Platform Source:** FIR Risk E93 — The Attacks Aren't New. The Economics Are. (Anthropic, Detecting and countering misuse of AI: September 2026)

---

## The INTEL

**Anthropic has announced Enterprise Frontier Safeguards (EFS), a new control model for its most capable models that splits AI misuse defense between the lab and the customer. Anthropic runs automated detection across sessions and accounts, looking for offensive cyber activity, biological misuse, and stolen or leaked credentials. The customer keeps the monitoring data in its own cloud account (Amazon S3, Azure Blob Storage or Google Cloud Storage), under its own encryption keys, and receives every flag directly. No Anthropic human review is required; flags go straight to your team. There is no Anthropic fee. It was designed with more than 100 enterprises, including the CISOs of the largest US banks through the Analysis and Resilience Center for Systemic Risk.**

The reason it exists: Anthropic says the most sophisticated misuse is spread across many sessions and accounts, so analyzing each interaction alone and then discarding it isn't enough. Starting with Fable 5, it began retaining data for 30 days to correlate activity over time. Regulated customers pushed back. EFS is the compromise: the correlation Anthropic needs, with the custody regulated firms require.

Status as of October 11, 2026: EFS is rolling out in phases to *eligible* customers, with broad availability targeted for this fall. Anthropic confirms eligibility and hasn't published the criteria. Anthropic says eligible Fable 5 and 5.1 customers will receive zero data retention in the meantime. It will be supported on Claude Code, Claude Enterprise, the Claude Platform, Amazon Bedrock, Claude Platform on AWS, Google's Agent Platform and Microsoft Foundry.

**What's a "flag"?** An alert that one of your AI accounts or keys may be in the wrong hands or being used for harm: a stolen key in use, or activity that looks like attack tooling. EFS is one source of these alerts. Your own monitoring of AI usage, spend and logs is the other, and you don't need EFS for that.

---

## Why It Matters

This is one of the first times a frontier lab has handed misuse monitoring to the customer as an operating responsibility. That's a genuine tailwind: regulated firms can now run frontier models with the data, keys and reviewers they already trust. But it also moves accountability. Under EFS, a flag that arrives at 2 a.m. doesn't require any Anthropic human review. It's your team, your playbook and your clock. A flag nobody acts on is no control at all.

The timing lines up with the threat picture. Anthropic's September 2026 threat report documents access to AI (compromised API keys, session tokens and devices) becoming the sole objective of multiple criminal groups, attackers using customers' stolen API keys, and a fake reseller harvesting account credentials. EFS is the vendor-side answer to the credential problem. But Anthropic only sees activity on its own platform: if your organization uses several AI providers, only you can see all of your own AI usage.

Three caveats belong in any board briefing. Anthropic has not yet published detection-performance data, flag thresholds or eligibility rules, so treat EFS as a promising control whose effectiveness is still unproven. Anthropic also has a commercial interest: EFS is its product, announced days before its threat report. And smaller organizations may never be eligible, which leaves them running frontier AI without this layer at all.

---

## What To Do — One Key Action

**Name the owner of every AI misuse flag before EFS reaches you. Pick a primary and a backup, write a triage playbook for the signal types Anthropic has named (credential compromise, offensive cyber, biological misuse), route flags into your SIEM and incident response process, and decide in advance who is cleared to look at flagged content that may include privileged or regulated data. Then submit Anthropic's eligibility form so you're in the queue.**

The storage bucket and encryption keys take a day. The people and process take a quarter. Start with the part that takes longer. Our free [EFS Readiness Guide](/efs-readiness/) has the full checklist, including compensating controls for organizations that aren't eligible.

---

## MITRE ATT&CK

- **T1078 — Valid Accounts · T1552 — Unsecured Credentials:** The techniques EFS's credential signals are aimed at. Stolen or leaked AI API keys and enterprise accounts let an attacker run frontier models under your name, and keys left in shared files or chat are the easiest way in. Treat AI keys and agent integrations like production credentials: inventory, vault, scope and rotate them.

---

## Learn More

- [FIR Risk EFS Readiness Guide](/efs-readiness/) — Free availability status and readiness checklist
- [Developing Enterprise Frontier Safeguards with our customers (Anthropic)](https://www.anthropic.com/news/enterprise-frontier-safeguards) — Primary announcement
- [Enterprise Frontier Safeguards eligibility form (Anthropic)](https://claude.com/form/enterprise-frontier-safeguards) — Request access
- [Detecting and countering misuse of AI: September 2026 (Anthropic)](https://www.anthropic.com/threat-intelligence-report-september-2026) — The threat picture EFS responds to
- [FIR Risk Tuesday E93 — The Attacks Aren't New. The Economics Are.](/tuesday/e93-the-economics-changed/) — Full analysis of the September 2026 report
- [FIR Risk Tuesday E87 — The Agents Have Keys](/tuesday/e87-the-agents-have-keys/) — When agentic AI got production access

---

*Powered by [FIR Risk Platform](https://firrisk.ai/platform/) — AI-driven threat intelligence for enterprise risk leaders.*

---

## LINKEDIN POST

```
Anthropic is moving AI misuse monitoring into the customer's own cloud.

Enterprise Frontier Safeguards (EFS) keeps monitoring data in your cloud account, under your encryption keys. Alerts about stolen credentials or attack activity go straight to your team, and there's no Anthropic fee. More than 100 enterprises helped design it, including the CISOs of the largest US banks.

The part risk leaders need to hear: Anthropic doesn't require any of its own employees to review those alerts. A flag at 2 a.m. is your team, your playbook and your clock. A flag nobody acts on is no control at all.

EFS is rolling out in phases to eligible customers this fall. One action now: name who owns AI misuse alerts, before the first one arrives.

Our free EFS Readiness Guide has the full checklist, including steps for organizations that won't be eligible.

Full INTEL and the free guide — link in the comments.

#AIGovernance #CISO #RiskManagement #AISecurity #Compliance
```

## X POST

Anthropic is moving AI misuse monitoring into the customer's own cloud.

Enterprise Frontier Safeguards (EFS) keeps monitoring data in your cloud account, under your encryption keys. Alerts about stolen credentials or attack activity go straight to your team, and there's no Anthropic fee. More than 100 enterprises helped design it, including the CISOs of the largest US banks.

The part risk leaders need to hear: Anthropic doesn't require any of its own employees to review those alerts. A flag at 2 a.m. is your team, your playbook and your clock. A flag nobody acts on is no control at all.

EFS is rolling out in phases to eligible customers this fall. One action now: name who owns AI misuse alerts, before the first one arrives.

Our free EFS Readiness Guide has the full checklist, including steps for organizations that won't be eligible.

Full INTEL + free EFS Readiness Guide → firrisk.ai

#AIGovernance #RiskManagement

---

## SOURCE DATA

**Editorial Frame:**
INTEL-36 is the control-response leg of the E93 set: Anthropic's Enterprise Frontier Safeguards as a genuine defender tailwind that also transfers response accountability to the customer. The one action targets the gap most organizations will have: no named owner for AI misuse alerts.

**Primary Sources:**
- Anthropic — Detecting and countering misuse of AI: September 2026 (published Sept 10, 2026; 154-page PDF; activity disrupted Dec 2025 – Aug 2026). Read from the PDF; quotes and figures verified against it on Oct 11, 2026.
- Anthropic — Developing Enterprise Frontier Safeguards with our customers (Sept 1, 2026)
- Anthropic — EFS access form (claude.com/form/enterprise-frontier-safeguards)

**Fact-Check Notes (verified against the report PDF, Oct 11, 2026):**
- CONFIRMED (EFS announcement): customer-controlled storage (S3, Azure Blob, GCS), customer-managed keys, automated monitoring for offensive cyber, bio and stolen/leaked credentials; flags go to the customer; no Anthropic human review required; opt-in controls don't change model behavior, pricing or rate limits; no Anthropic fee (cloud provider bills storage/egress); 100+ enterprises including ARC; supported platforms as listed; interim ZDR for eligible Fable 5/5.1 customers.
- CONFIRMED (access form): "rolling out to eligible customers in phases, with the goal of making it broadly available this fall"; form does not guarantee access.
- STATUS: no general-availability announcement found as of Oct 11, 2026. Re-check before publishing.
- CONFIRMED (threat report): AI access has become the sole objective of multiple criminal groups; customers' stolen keys; fake reseller harvesting credentials.

**FIR Risk Editorial Position:**
- Three caveats carried into the piece: unpublished detection performance and eligibility, Anthropic's commercial interest, and SMBs likely outside EFS.
- "Flag" defined in plain language; own monitoring named as a second source that doesn't require EFS.
- Voice: declarative, board-readable, incentive-aware.
