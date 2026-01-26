# Report Analysis Prompt

Use this prompt to extract intelligence from security reports, threat research, and vendor publications.

## Prompt

```
Analyze [REPORT NAME] and extract the key intelligence.

Focus on:
1. **Top 3 Findings** - What are the most significant insights?
2. **What's New** - What does this report reveal that we didn't know before?
3. **Who's At Risk** - Which industries, company sizes, or roles should pay attention?
4. **MITRE Mapping** - What ATT&CK techniques are referenced or implied?
5. **Recommended Actions** - What should organizations do based on this?

Format for executives - concise, actionable, no jargon.

Confidence level for each finding: High / Medium / Low
```

## Example Usage

```
Analyze the Fortinet 2026 Threat Predictions report and extract the key intelligence.

Focus on:
1. Top 3 Findings - What are the most significant insights?
2. What's New - What does this report reveal that we didn't know before?
3. Who's At Risk - Which industries, company sizes, or roles should pay attention?
4. MITRE Mapping - What ATT&CK techniques are referenced or implied?
5. Recommended Actions - What should organizations do based on this?

Format for executives - concise, actionable, no jargon.
```

## Tips

- Upload the report to FIR Risk before running the prompt
- Ask follow-up questions to drill into specific areas
- Cross-reference with CISA KEV or ATT&CK for additional context
