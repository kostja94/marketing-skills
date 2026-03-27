---
name: retention-strategy
description: When the user wants to reduce churn, improve customer retention, or plan lifecycle marketing. Also use when the user mentions "retention," "churn," "customer lifecycle," "churn prevention," "at-risk customers," or "loyalty program." For lifecycle, use growth-funnel.
metadata:
  version: 1.1.1
---

# Strategies: Retention

Guides customer retention and churn prevention. Acquiring new customers costs 5–25× more than retaining; 5% retention improvement can increase profitability 25–95%. Use this skill when reducing churn, building retention programs, or identifying at-risk customers.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read Sections 4 (Audience), 9 (Documentation).

Identify:
1. **Churn type**: Voluntary (active cancel) vs involuntary (payment failure)
2. **Signals**: Login frequency, feature usage, support tickets
3. **Stage**: Onboarding, expansion, renewal

## Churn Types

| Type | Share | Causes |
|------|-------|--------|
| **Voluntary** | 60–80% | Pricing, missing features, poor onboarding, relationship |
| **Involuntary** | 20–40% | Payment failures, expired cards, billing |

**Predictability**: Most churn is predictable 30–90 days before cancellation via behavioral signals.

## Proactive vs Reactive

| Approach | Conversion |
|----------|------------|
| **Reactive** (after cancel) | 15–20% |
| **Proactive** (before decision) | 60–80% |

Move from lagging indicator to early warning systems.

## Retention Strategies

| Strategy | Use |
|----------|-----|
| **Health scoring** | Behavioral + transactional + relationship signals |
| **Loyalty programs** | 5–15 percentage point retention lift |
| **Segmentation** | Predictive modeling for at-risk |
| **Onboarding** | Prevent low value realization early |
| **Dunning** | Retry logic; pre-expiry card updates for involuntary |

## User Value & Feedback

| Dimension | Use |
|-----------|-----|
| **Product value** | Registration; feature usage; payment |
| **Marketing value** | Testimonials; customer stories; webinar guests; feedback, bug reports, feature requests |
| **Feedback analysis** | Email, community, reviews—AI-assisted analysis; prioritize by impact; route to product vs ops |

**Avoid**: Treating users only as MAU/registration denominators. See **creator-program** for creator ecosystem.

## Lifecycle Integration

Retention occurs after conversion; ongoing investment in customer success, not isolated campaigns. Map touchpoints: onboarding → adoption → expansion → renewal.

## Output Format

- **Churn analysis** (voluntary vs involuntary; signals)
- **Retention tactics** (by stage)
- **Health score** framework (if applicable)
- **Intervention** playbook (at-risk triggers)

## Related Skills

- **email-marketing**: Onboarding sequences; win-back campaigns
- **pmf-strategy**: Retention as PMF signal; churn as anti-signal
- **cold-start-strategy**: First users; differs from retention
- **analytics-tracking**: Usage data; churn signals
- **traffic-analysis**: Attribution; retention cohort analysis
