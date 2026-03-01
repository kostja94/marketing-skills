---
name: paid-ads-strategy
description: When the user wants to plan paid ads strategy, allocate ad budget, or choose paid channels. Also use when the user mentions "paid ads," "paid media," "PPC," "SEM," "Google Ads," "Meta Ads," "LinkedIn Ads," "ad spend," "ad budget," "ROAS," "paid acquisition," "Quality Score," or "ad-to-page alignment."
metadata:
  version: 1.0.0
---

# Strategies: Paid Ads

Guides paid ads strategy: when to use paid acquisition, channel selection, budget allocation, and ad-to-landing-page alignment. Paid ads (Google Ads, Meta, LinkedIn, etc.) deliver immediate reach and targeting; use when PMF is validated and budget allows.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## When to Use Paid Ads

| Condition | Rationale |
|-----------|-----------|
| **PMF validated** | Product-market fit confirmed; you know who buys and why |
| **Budget available** | CAC and LTV modeled; ROAS target set |
| **Need speed** | Organic takes months; paid delivers traffic immediately |
| **Targeting clarity** | Audience segments defined; can target precisely |

## When NOT to Use Paid Ads

| Condition | Rationale |
|-----------|-----------|
| **Pre-PMF** | Paid ads before product-market fit waste budget; validate demand first. See **cold-start-strategy** |
| **No conversion tracking** | Can't measure ROAS; optimize blindly |
| **Organic can work** | SEO, content, community may achieve goal at lower cost; see **seo-strategy** |
| **Budget too small** | Need minimum scale to test; $500–1K often insufficient for statistical significance |

**Cold start**: Avoid paid ads before PMF validation. Use Product Hunt, Reddit, directories, founder-led outbound first. See **cold-start-strategy**.

## Channel Selection

| Channel | Best for | Typical use |
|---------|----------|--------------|
| **Google Ads (Search)** | High-intent queries; commercial/transactional | PPC; keyword-targeted; landing page critical |
| **Google Ads (Display/YouTube)** | Awareness; retargeting | Broader reach; lower intent |
| **Meta (Facebook/Instagram)** | B2C; demographic targeting | Awareness, consideration; creative-driven |
| **LinkedIn Ads** | B2B; professional targeting | Lead gen, thought leadership |
| **TikTok Ads** | Younger audience; short-form | Awareness; viral-style creative |

**Principle**: Match channel to audience and funnel stage. Search = high intent; social = awareness/consideration.

## Budget & Metrics

| Metric | Purpose |
|--------|---------|
| **ROAS** | Return on ad spend; primary paid channel metric |
| **CAC** | Cost per acquisition; compare to LTV |
| **Quality Score** (Google) | Ad relevance, LP experience; higher = lower CPC, better rank |
| **CPC/CPM** | Cost per click/impression; platform-specific |

**Budget allocation**: Start with one channel; prove ROAS before scaling. Test 2–3 ad creatives; double down on winners.

## Ad-to-Landing-Page Alignment

When landing pages receive **paid traffic** (Google Ads, Meta, etc.):

| Principle | Practice |
|-----------|----------|
| **Ad promise on page** | Ad copy (e.g. "15% off") must appear immediately on the page; mismatch increases bounce |
| **Post-click experience** | Ads drive traffic; landing pages drive conversions; optimize the full funnel |
| **Quality Score** | Well-optimized LPs improve Google Ads Quality Score → lower CPC, better ad rank |
| **Mobile-first** | Majority of traffic on mobile; CTA above fold, thumb-reachable, fast load |

See **landing-page-generator** for LP structure, 5-step flow, and conversion optimization.

## Affiliate Brand Bidding

When running affiliate programs: affiliates may bid on your brand terms in Google Ads; you pay commission for traffic you already own. Prohibit in affiliate terms; monitor paid search; use brand monitoring tools. See **affiliate-page-generator**.

## Output Format

- **Channel** recommendation (Google, Meta, LinkedIn, etc.)
- **When to start** (PMF check; budget readiness)
- **Budget** approach (test budget; ROAS target)
- **Landing page** requirement (ad-to-page alignment; see **landing-page-generator**)
- **Metrics** to track (ROAS, CAC, Quality Score)

## Related Skills

- **landing-page-generator**: LP structure for paid traffic; ad-to-page alignment; conversion flow
- **cold-start-strategy**: When NOT to use paid ads; cold start channels first
- **seo-strategy**: Organic vs paid; when SEO can achieve goal
- **integrated-marketing**: PESO model; paid as one channel in IMC
- **keyword-research**: Keywords inform paid search targeting
- **pricing-page-generator**: LP often sends to pricing; CTA destination
- **alternatives-page-generator**: Alternatives pages used for paid ads; apply LP principles
- **traffic-analysis**: UTM for paid attribution; channel reporting
- **analytics-tracking**: Conversion tracking; ROAS measurement
