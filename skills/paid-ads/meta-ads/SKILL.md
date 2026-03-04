---
name: meta-ads
description: When the user wants to set up, optimize, or manage Meta (Facebook/Instagram) Ads. Also use when the user mentions "Meta Ads," "Facebook Ads," "Instagram Ads," "Meta Pixel," "Conversions API," "Advantage+," "lookalike audience," or "Meta retargeting."
metadata:
  version: 1.0.0
---

# Paid Ads: Meta Ads

Guides Meta (Facebook/Instagram) Ads setup, campaign structure, audience targeting, and creative optimization. Meta excels at demand generation and visual products; use when creating demand or when creative assets are strong.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Campaign Structure

**Hierarchy**: Campaign → Ad Set → Ad (3 levels)

```
Account
├── Campaign: Prospecting
│   ├── Ad Set: Lookalike 1%
│   └── Ad Set: Broad (Advantage+)
├── Campaign: Retargeting
└── Campaign: Testing
```

**Naming**: `META_[Objective]_[Audience]_[Offer]_[Date]` (e.g., `META_Conv_Lookalike-Customers_FreeTrial_2024Q1`)

## Campaign Objectives

| Objective | Use when |
|-----------|----------|
| Awareness | Reach; brand recall |
| Traffic | Clicks to site |
| Conversions | Leads; sales; app installs |
| Engagement | Video views; post engagement |

## Audience Targeting

| Type | Best for |
|------|----------|
| **Lookalikes** | Base on best customers (by LTV), not all customers |
| **Interest/behavior** | Broad; let algorithm optimize |
| **Advantage+** | Automated; fewer manual controls |
| **Retargeting** | Website visitors; engagers; custom audiences |

**Exclusions**: Existing customers; recent converters (7–14d).

## Creative Best Practices

- **Image**: Clear product; before/after; human faces; text &lt;20%
- **Video (15–30s)**: Hook 0–3s; problem 3–8s; solution 8–20s; CTA 20–30s
- **Placements**: Feed (FB/IG); Stories/Reels; vertical for Stories
- **Volume**: 3–5 ad variants per ad set for testing

## Optimization

- **Learning phase**: 50+ conversions per ad set per week to exit
- **CBO vs ABO**: Campaign Budget Optimization consolidates spend; use when scaling
- **Frequency**: &lt;3 to avoid fatigue

## Tracking

- **Meta Pixel** + **Conversions API**: Server-side for better attribution
- **Events API**: App events; server-to-server

## Pre-Launch Checklist

- [ ] Pixel installed; Conversions API configured
- [ ] Conversion events firing correctly
- [ ] Landing page mobile-friendly; fast load
- [ ] 3+ ad creatives per ad set
- [ ] Audience exclusions set

## Related Skills

- **paid-ads-strategy**: Channel selection; creative frameworks; budget allocation
- **landing-page-generator**: LP for paid traffic
- **analytics-tracking**: Conversion tracking; ROAS
