---
name: email-marketing
description: When the user wants to plan email marketing, EDM, newsletter strategy, or email deliverability. Also use when the user mentions "email marketing," "EDM," "newsletter," "SPF," "DKIM," "DMARC," "email deliverability," "email content strategy," "email campaigns," "newsletter strategy," "email automation," or "cold email."
metadata:
  version: 1.0.0
---

# Channels: Email Marketing

Guides email marketing strategy for AI/SaaS products. Email ROI ~$36 per dollar spent; open/click rates typically higher than social. Covers EDM vs Newsletter, five content types, deliverability (SPF/DKIM/DMARC), and SEO synergy via article delivery.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for audience and content strategy.

Identify:
1. **Goal**: Retention, conversion, brand reach, or SEO synergy
2. **Content mix**: Onboarding, campaign, announcement, features, newsletter
3. **List size**: Bulk sender rules (5,000+/day) require Gmail/Yahoo compliance

## EDM vs Newsletter

| Type | Purpose | Use |
|------|---------|-----|
| **EDM** | Direct marketing; conversion-focused | Promotions, campaigns, announcements; bulk sends |
| **Newsletter** | Ongoing value; relationship | Industry insights, curated articles; regular cadence |

**Combine both**: EDM for push; Newsletter for nurture. Cover different stages and goals.

## Five Content Types

| Type | Use |
|------|-----|
| **Onboarding** | Welcome + first-use guidance; 5-7 day sequence; behavior-triggered; drive "Aha!" moment |
| **Campaign** | Promotions, limited-time; conversion or participation |
| **Announcement** | Product launch, major update; one-time important notice |
| **Features update** | New features, improvements; help users adopt |
| **Blog/Newsletter** | Curated articles, industry insights; sustained touch |

## User Best Practices

| Practice | Guideline |
|----------|-----------|
| **Personalization** | Segment by behavior, source, stage; boosts open/click |
| **Timing** | New users: dense; existing: controlled pace; behavior-triggered > calendar-only |
| **Welcome series** | Send soon after signup; 5-7 emails over days; guide first key action |
| **Unsubscribe** | One-click required (Gmail/Yahoo); honor within 48h; clear entry |
| **Complaint rate** | Keep below 0.3%; list hygiene critical |

## Content Best Practices

| Practice | Guideline |
|----------|-----------|
| **Subject** | One clear topic per email; avoid pure promo |
| **Value first** | Useful info before promotion |
| **CTA** | Single primary CTA; clear next step |
| **Mobile** | 50%+ read on mobile; responsive layout, tappable links |

## Deliverability & Domain Config

**Subdomain**: Use subdomain (e.g. mail.example.com) for marketing; keep transactional (support@, etc.) on main domain. Isolate risk.

### SPF, DKIM, DMARC

| Protocol | Purpose |
|----------|---------|
| **SPF** | Authorizes mail servers for domain |
| **DKIM** | Cryptographic signature; verifies sender |
| **DMARC** | Policy for unauthenticated mail; start p=none, then quarantine, then reject over 60-90 days |

**Order**: SPF first, then DKIM, then DMARC. Gmail/Yahoo require all three for bulk senders (5,000+/day) since Feb 2024.

**Advanced**: TLS-RPT, MTA-STS, BIMI (brand logo). **Postmaster Tools**: Monitor deliverability, spam rate, auth status.

## Delivery Strategy: Articles + SEO Synergy

| Article Type | Use |
|--------------|-----|
| **Retention** | Deep content for existing users; improve retention |
| **ToFu** | Top of funnel; awareness (trends, concepts, problem framing) |
| **MoFu** | Middle of funnel; consideration (comparisons, reviews, best practices) |

**Dual value**: (1) Better email engagement (open, click, stickiness); (2) Drive traffic to article pages from non-search channel; signals to Google that users value content; supports SEO.

**Measurement**: GA4 email source traffic to article pages; GSC rank/click changes.

## Planning Framework

1. **Content mix**: Allocate onboarding, campaign, announcement, features, newsletter
2. **Select articles**: Pick retention, ToFu, MoFu from blog; prioritize SEO target pages
3. **Cadence**: Stable frequency (weekly/biweekly/monthly); avoid over-sending
4. **Monitor**: Open rate, click rate; GA4 email contribution to article traffic; GSC

## Frequency

| Guideline | Note |
|-----------|------|
| **Baseline** | 1 high-value email/week for most brands |
| **Peak times** | Tue-Thu, 8-11am or 2-4pm (recipient timezone) |
| **Segmentation** | New vs loyal need different cadence |
| **Quality** | Relevant, behavior-triggered > calendar volume |

**Data**: ~36% send 1-3/month; ~30% weekly; daily risks high unsubscribe.

## Output Format

- **Content mix** (five types)
- **EDM vs Newsletter** balance
- **Deliverability** (subdomain, SPF/DKIM/DMARC)
- **Article delivery** (Retention, ToFu, MoFu, SEO targets)
- **Cadence** and frequency
- **KPI** (open, click, GA4 email traffic, GSC)

## Related Skills

- **newsletter-signup-generator**: Signup form design
- **traffic-analysis**: Email source attribution, UTM
- **analytics-tracking**: Email click tracking
- **content-strategy**: Article selection for email delivery
- **integrated-marketing**: Email as owned media channel

## References

- [Email Deliverability 2025 - Litmus](https://www.litmus.com/blog/why-email-deliverability-matters)
- [SPF DKIM DMARC Guide - Demandloft](https://demandloft.com/blog/spf-dkim-dmarc-guide/)
- [Email Frequency Best Practices - Foundcoo](https://www.foundcoo.com/blog/email-frequency-best-practices-2026)
- [Onboarding Emails - Mailchimp](https://mailchimp.com/resources/onboarding-email)
