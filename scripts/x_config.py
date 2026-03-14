"""Influencer seed list and configuration."""

INFLUENCER_SEED = [
    # Cybersecurity thought leaders
    {"username": "schnaborowski", "category": "cybersecurity", "priority": "high",
     "notes": "Bruce Schneier — foundational security thinking"},
    {"username": "alexstamos", "category": "cybersecurity", "priority": "high",
     "notes": "Stanford, former Facebook/Yahoo CISO"},
    {"username": "briankrebs", "category": "cybersecurity", "priority": "high",
     "notes": "Investigative cybersecurity journalism"},
    {"username": "kimaborowski", "category": "cybersecurity", "priority": "high",
     "notes": "Katie Moussouris — vulnerability disclosure, policy"},
    {"username": "evacide", "category": "cybersecurity", "priority": "high",
     "notes": "Eva Galperin (EFF) — digital rights, surveillance"},

    # Threat intelligence & research
    {"username": "Unit42_Intel", "category": "threat_intel", "priority": "high",
     "notes": "Palo Alto Unit 42 — directly relevant to newsletter sources"},
    {"username": "MsftSecIntel", "category": "threat_intel", "priority": "high",
     "notes": "Microsoft Security Intelligence — MSTIC threat reports"},
    {"username": "Mandiant", "category": "threat_intel", "priority": "high",
     "notes": "Google TI — M-Trends, APT tracking"},
    {"username": "CrowdStrike", "category": "threat_intel", "priority": "high",
     "notes": "Primary source for INTEL-4, INTEL-5, E83"},
    {"username": "RecordedFuture", "category": "threat_intel", "priority": "medium",
     "notes": "Threat intelligence feeds"},
    {"username": "TalosSecurity", "category": "threat_intel", "priority": "medium",
     "notes": "Cisco Talos — vulnerability research"},
    {"username": "SentinelOne", "category": "threat_intel", "priority": "medium",
     "notes": "SentinelLabs threat research"},

    # CISA / Government
    {"username": "CISAgov", "category": "cybersecurity", "priority": "high",
     "notes": "CISA official — KEV, advisories"},
    {"username": "NSACyber", "category": "cybersecurity", "priority": "medium",
     "notes": "NSA Cybersecurity Directorate"},

    # Fraud, risk, financial crime
    {"username": "ABOROWSKI_ACFE", "category": "fraud", "priority": "medium",
     "notes": "ACFE — fraud methodology (verify handle)"},

    # AI security & governance
    {"username": "NISTcyber", "category": "ai_security", "priority": "medium",
     "notes": "NIST Cybersecurity — frameworks, AI governance"},
    {"username": "AnthropicAI", "category": "ai_security", "priority": "medium",
     "notes": "AI safety research"},

    # Security vendors / analysts
    {"username": "Cloudflare", "category": "vendor", "priority": "medium",
     "notes": "Source for E82 Threat Landscape report"},
    {"username": "kaborowski", "category": "cybersecurity", "priority": "medium",
     "notes": "Securosis / Rich Mogull — CISO-focused (verify handle)"},
]

# Handles marked with ABOROWSKI or noted "verify handle" need
# manual verification — X usernames change. Run 'resolve' to find
# which ones are valid.
