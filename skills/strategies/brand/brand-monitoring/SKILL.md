---
name: brand-monitoring
description: When the user wants to monitor brand mentions, detect trademark infringement, or set up brand monitoring. Also use when the user mentions "brand monitoring," "brand watch," "trademark watch," "brand mentions," "impersonation detection," "counterfeit detection," or "brand abuse monitoring."
metadata:
  version: 1.0.0
---

# Strategies: Brand Monitoring

Guides ongoing brand monitoring—detecting impersonation, trademark infringement, counterfeit products, and brand abuse before they cause harm. Complements **brand-protection** (reactive: report, takedown); this skill covers proactive monitoring setup and tool selection.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read for brand name, official domain, and key assets.

Identify:
1. **Scope**: Domain, social, marketplaces, paid search, dark web
2. **Budget**: Manual vs automated; DIY vs vendor
3. **Risk level**: High-value brand, prior incidents, or preventive

## What to Monitor

| Channel | Threats |
|---------|---------|
| **Domains** | Typosquatting, brand+ai, brand+app, impersonation sites |
| **Social media** | Fake accounts, impersonation, unauthorized use |
| **Marketplaces** | Counterfeit products, unauthorized sellers (Amazon, eBay, Temu) |
| **Paid search** | Competitors bidding on brand terms; impersonator ads |
| **App stores** | Fake apps, trademark misuse |
| **Web** | Phishing sites, spoofed pages |

## Manual Monitoring (Low Cost)

| Method | Frequency |
|--------|-----------|
| **Search** | Brand name + variants (brand+ai, brand+app, brand+official) |
| **Google Alerts** | Brand name, product names |
| **Social search** | X, LinkedIn, Instagram for brand mentions |
| **Marketplace search** | Amazon, eBay for counterfeit listings |

**Tip**: Document findings; escalate to **brand-protection** for takedown when infringement is confirmed.

## Automated Tools (Scale)

| Capability | Description |
|------------|-------------|
| **AI detection** | Machine learning, image recognition, NLP to detect abuse across channels |
| **Multi-channel** | Domains, social, marketplaces, paid search, dark web |
| **Enforcement** | Case management, takedown workflows, platform integrations |
| **Trademark watch** | USPTO, trademark office monitoring; litigation insights |

**Vendor types**: BrandShield, Tracer Protect, CompuMark, CounterFind—evaluate by coverage, enforcement rate, and budget.

## Monitoring Cadence

| Level | Cadence | Use |
|-------|---------|-----|
| **Basic** | Weekly search; Google Alerts | Low-risk; preventive |
| **Standard** | Daily alerts; monthly marketplace check | Moderate risk |
| **Enterprise** | Real-time monitoring; dedicated vendor | High-value brand; prior incidents |

## Output Format

- **Monitoring plan** (channels, cadence, tools)
- **Search queries** (brand + variants for manual check)
- **Alert setup** (Google Alerts, social)
- **Escalation path** (when to use brand-protection for takedown)

## Related Skills

- **brand-protection**: Report, takedown, evidence collection—use when infringement is found
- **domain-selection**: Defensive registration; brand variants
- **branding**: Brand asset consistency; what to protect
