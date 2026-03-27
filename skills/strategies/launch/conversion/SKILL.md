---
name: conversion-optimization
description: When the user wants to improve conversion rates, run A/B tests, optimize funnels, or reduce friction. Also use when the user mentions "CRO," "conversion rate optimization," "A/B test," "split test," "funnel optimization," "checkout optimization," "form optimization," or "conversion funnel." For pricing psychology, use pricing-strategy.
metadata:
  version: 1.1.1
---

# Strategies: Conversion Optimization

Guides conversion rate optimization (CRO): increasing the percentage of visitors who complete desired actions. Higher conversion rates mean increased revenue, reduced CAC, and better ROI. Use this skill when optimizing funnels, running experiments, or reducing friction on high-traffic pages.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read Sections 4 (Audience), 5 (Website), 6 (Keywords).

Identify:
1. **Funnel stage**: Awareness, consideration, decision, post-purchase
2. **Conversion goal**: Signup, purchase, download, demo request
3. **Traffic**: Volume; mobile vs desktop split
4. **Current conversion rate**: Baseline for improvement

## CRO Process

| Step | Action |
|------|--------|
| **1. Research** | Map funnel; identify high-traffic, low-conversion pages |
| **2. Hypothesize** | Form testable hypothesis (if X, then Y because Z) |
| **3. Prioritize** | Score by Potential, Importance, Ease (PIE) |
| **4. Test** | A/B or multivariate; adequate sample size |
| **5. Analyze** | Statistical significance; implement winner |

## PIE Prioritization Framework

Score each test idea 1–10:

| Factor | Question |
|--------|----------|
| **Potential** | How much improvement is possible? |
| **Importance** | How much traffic does this page get? |
| **Ease** | How easy to implement? |

Rank backlog by total score; run highest-impact tests first.

## A/B Testing Best Practices

| Practice | Guideline |
|----------|-----------|
| **Sample size** | Calculate minimum before launch; 95% significance without adequate sample = false positives |
| **Duration** | Run full week cycles; account for day-of-week effects |
| **One variable** | Test one element per experiment (or use MVT for multiple) |
| **Mobile separate** | Mobile converts ~50% of desktop; test mobile independently—thumb reach, form complexity differ |
| **Low traffic** | Use Bayesian testing for faster, actionable results |

## Key Testing Areas

| Page Type | Test Ideas |
|-----------|------------|
| **Homepage** | Search bar prominence; personalized content; hero CTA; social proof placement |
| **Landing page** | Headline; form length; CTA copy; above-fold layout |
| **Product/Category** | Quick view; descriptions; add-to-cart placement |
| **Checkout** | Form fields; progress indicator; trust badges; guest checkout |
| **Pricing** | Plan order; anchoring; CTA per tier |

**Personalization**: Personalized experiences generate ~41% more impact than generic ones.

## Commercialization Infrastructure

| Module | Purpose |
|--------|---------|
| **Data & BI** | Data warehouse; user behavior events; agile surveys |
| **A/B testing** | Experiment platform; statistical significance; backend-controlled variants |
| **User education** | Help docs (multi-language); update notifications; EDM |
| **Attribution** | Ad pixels; attribution model; impression-to-click-to-sale tracking |

**Avoid**: Intrusive interstitials; popups that block content. Prefer non-intrusive ad formats.

## Foundational Requirements

- **Analytics**: Map funnels; identify drop-off points (analytics-tracking, traffic-analysis)
- **Qualitative**: Heatmaps, session recordings, user tests—understand *why* drop-off occurs
- **Technical**: Dedicated resources for 2–4 tests/month; maintain momentum

## Output Format

- **Funnel map** (stages, conversion rates, drop-off)
- **Hypothesis** (if X, then Y because Z)
- **Test plan** (variant, metric, sample size, duration)
- **Implementation** checklist

## Related Skills

- **landing-page-generator**: Landing page structure and copy
- **cta-generator**: CTA design and placement
- **analytics-tracking**: GA4, events, conversion tracking
- **traffic-analysis**: Attribution, funnel analysis
- **copywriting**: Headline, CTA copy for tests
