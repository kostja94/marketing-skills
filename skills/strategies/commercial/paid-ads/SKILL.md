---
name: paid-ads-strategy
description: When the user wants to plan paid ads strategy, allocate ad budget, or choose paid channels. Also use when the user mentions "paid ads," "paid media," "PPC," "SEM," "web ads," "app ads," "TV ads," "CTV," "OOH," "banner ads," "ad network," "ad alliance," "Taaft ads," "Shopify App Store ads," "Google Ads," "Meta Ads," "PMF testing," "PMF validation," "test product-market fit with ads," "ad spend," "ad budget," "ROAS," "paid acquisition," "Quality Score," or "ad-to-page alignment." For Google Ads execution, use google-ads. For Meta Ads execution, use meta-ads. For landing page alignment, use landing-page-generator.
metadata:
  version: 1.7.0
---

# Strategies: Paid Ads

Guides paid ads strategy: when to use paid acquisition, channel selection, budget allocation, ad-to-landing-page alignment, and cross-platform best practices. Paid ads (Google Ads, Meta, LinkedIn, Reddit, TikTok, etc.) deliver immediate reach and targeting; use when PMF is validated and budget allows.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

**Platform-specific execution**: Web: **google-ads**, **meta-ads**, **linkedin-ads**, **reddit-ads**, **tiktok-ads**. App: **app-ads**. TV/Streaming: **ctv-ads**.

## Before Starting

**Check for project context first:** If `.agents/project-context.md` or `.claude/project-context.md` exists, read it before asking questions.

Gather this context (ask if not provided):

| Area | Questions |
|------|-----------|
| **Goals** | Primary objective? (Awareness, traffic, leads, sales, app installs) Target CPA/ROAS? Monthly budget? Constraints? |
| **Product & offer** | What are you promoting? Landing page URL? What makes it compelling? |
| **Audience** | Ideal customer? Problem you solve? What do they search for or care about? Existing customer data for lookalikes? |
| **Current state** | Run ads before? What worked/didn't? Pixel/conversion data? Funnel conversion rate? |

## Two Modes: PMF Testing vs Conversion-Driven

| Mode | When | Goal | Budget | Metrics |
|------|------|------|--------|---------|
| **PMF testing** | Pre-PMF; idea validation | Validate demand, messaging, pricing, audience before building | $47–500; small | CTR, sign-up rate, bounce rate; low CTR/high bounce = messaging issue |
| **Conversion-driven** | PMF validated | Commercialization; scale; efficient acquisition | Scale; ROAS target | ROAS, CAC, conversion rate |

**PMF testing**: Use paid ads as a **learning tool**—simple landing page, "Join Waitlist" or "Get Early Access" CTA, test ad variations (value props, price points, audiences). No full product needed. See **google-ads** for PMF testing setup.

**Conversion-driven**: Full funnel; conversion tracking; scale budget. Avoid large-scale paid acquisition before PMF—see **cold-start-strategy**.

**Reference**: [Marketing Cactus – Using Google Ads to Test Product-Market Fit](https://mktcactus.com/en/using-google-ads-to-test-product-market-fit-before-launching/)

## When to Use Paid Ads

| Condition | Rationale |
|-----------|-----------|
| **PMF validated** (conversion mode) | Product-market fit confirmed; scale acquisition |
| **PMF testing** (validation mode) | Small budget; validate demand, messaging, pricing before building |
| **Budget available** | CAC and LTV modeled (conversion); or $47–500 for testing |
| **Need speed** | Organic takes months; paid delivers traffic immediately |

## When NOT to Use Paid Ads

| Condition | Rationale |
|-----------|-----------|
| **Pre-PMF + large scale** | Large-scale paid acquisition before PMF wastes budget; use PMF testing mode or cold-start channels first |
| **No conversion tracking** | Can't measure ROAS; optimize blindly (PMF testing uses CTR/sign-up) |
| **Organic can work** | SEO, content, community may achieve goal at lower cost; see **seo-strategy** |

**Cold start**: For acquisition, use Product Hunt, Reddit, directories, founder-led outbound first. For PMF validation, small-budget Google Ads + landing page is valid. See **cold-start-strategy**, **google-ads**.

## Ad Formats by Medium

Paid ads span multiple media beyond web. Choose by product type and audience.

| Medium | Format | Best for | Skill |
|--------|--------|----------|-------|
| **Web** | Search, Display, Social (landing page) | Websites, SaaS, e-commerce, leads | google-ads, meta-ads, linkedin-ads, reddit-ads, tiktok-ads |
| **Display / Banner** | Ad networks, programmatic, banner ads | Brand awareness; retargeting; publisher sites | display-ads |
| **App** | App install, in-app ads, App Store/Play Store | Mobile apps; user acquisition (UA) | app-ads |
| **TV / Streaming** | CTV, OTT, linear TV | Brand awareness; streaming viewers; 95% ad completion | ctv-ads |
| **Directory / Marketplace** | Taaft, Shopify App Store, G2, Capterra | High-intent directory visitors; app/software discovery | directory-listing-ads |
| **Out-of-home (OOH)** | Billboards, transit, DOOH | Brand reach; unskippable; real-world exposure | — |

**Web** drives to landing pages; **Display** = banner/network on publisher sites; **App** = install or in-app; **TV/CTV** = awareness or QR/URL; **Directory** = paid placements within Taaft, Shopify App Store, G2, Capterra.

## Platform Selection (Web)

| Platform | Best for | Use when |
|----------|----------|----------|
| **Google Ads** | High-intent search traffic | People actively search for your solution |
| **Meta (FB/IG)** | Demand gen, visual products | Creating demand; strong creative assets |
| **LinkedIn Ads** | B2B, decision-makers | Job title/company targeting matters; higher ACV |
| **Reddit Ads** | Niche communities, discussion-driven | Audience in specific subreddits; authentic, value-first messaging |
| **TikTok Ads** | Younger demographics, viral creative | Audience 18–34; video capacity |
| **X (Twitter) Ads** | Tech audiences, thought leadership | Audience active on X; timely content |

**Decision tree**: High intent? → Google Search. No? → Awareness: Meta/TikTok/YouTube. B2B: LinkedIn. E-commerce: Meta + Google Shopping. **App?** → app-ads. **Streaming/TV?** → ctv-ads. **Display/banner?** → display-ads. **Directory (Taaft, Shopify, G2)?** → directory-listing-ads.

## Dual-Channel Strategy

Treat Google Ads and Meta Ads as **complementary**, not competing. Google captures high-intent search at moment of need; Meta creates and shapes demand by introducing brands to new audiences. A dual-channel approach often outperforms single-channel; use unified KPIs (prioritize profit over volume). See **google-ads**, **meta-ads** for platform setup.

## Budget Allocation

| Phase | Approach |
|-------|----------|
| **Testing (2–4 weeks)** | 70% proven/safe; 30% new audiences/creative |
| **Scaling** | Consolidate into winners; increase 20–30% at a time; wait 3–5 days between increases |

## Ad Copy Frameworks (Cross-Platform)

| Framework | Structure |
|-----------|-----------|
| **PAS** | Problem → Agitate pain → Introduce solution → CTA |
| **BAB** | Current painful state → Desired future state → Your product as bridge |
| **Social Proof** | Impressive stat/testimonial → What you do → CTA |

## Creative Best Practices

**Image ads**: Clear product screenshots; before/after; stats as focal point; human faces (real); text overlay &lt;20%.

**Video ads (15–30 sec)**: Hook (0–3s) → Problem (3–8s) → Solution (8–20s) → CTA (20–30s). Captions always; vertical for Stories/Reels; native feel outperforms polished.

**Creative testing order**: 1) Concept/angle 2) Hook/headline 3) Visual style 4) Body copy 5) CTA.

## Retargeting Overview

| Funnel stage | Audience | Message |
|--------------|----------|---------|
| Top | Blog readers, video viewers | Educational, social proof |
| Middle | Pricing/feature visitors | Case studies, demos |
| Bottom | Cart abandoners, trial users | Urgency, objection handling |

**Exclusions**: Existing customers; recent converters (7–14d); bounced visitors (&lt;10s).

## Budget & Metrics

| Metric | Purpose |
|--------|---------|
| **ROAS** | Return on ad spend; primary paid channel metric |
| **CAC** | Cost per acquisition; compare to LTV |
| **Quality Score** (Google) | Ad relevance, LP experience; higher = lower CPC |
| **CPC/CPM** | Cost per click/impression; platform-specific |

**Quantified benchmarks**: Quality Score 5→7 can reduce CPC by 30–50%. Smart bidding (Target CPA/ROAS) typically needs ≥30 conversions in 30 days to work effectively. Proper optimization can increase conversion rates 30–150% and reduce CPA 20–50%.

## Attribution & Incrementality

**Incrementality** measures the *additional* value marketing creates beyond what would occur without it—causal impact, not just correlation. Essential in privacy-first environments (cookies limited, third-party data restricted); incrementality testing does not depend on cross-device tracking.

| Approach | Use when |
|----------|----------|
| **Incrementality testing** | Holdout experiments (geo, channel); isolate true lift; justify budget |
| **Attribution** | UTM, last-click, multi-touch; compare channels; see **traffic-analysis** |
| **Advanced conversion** | Server-side (Enhanced Conversions, CAPI); better accuracy |

**Principle**: Measure incrementality and downstream value, not just cost metrics. Major platforms have lowered experiment thresholds (e.g., Google Ads incrementality experiments from $100K+ to ~$5K minimum spend).

## Ad-to-Landing-Page Alignment

| Principle | Practice |
|-----------|----------|
| **Ad promise on page** | Ad copy (e.g. "15% off") must appear immediately; mismatch increases bounce |
| **Post-click experience** | Ads drive traffic; LPs drive conversions; optimize full funnel |
| **Quality Score** | Well-optimized LPs improve Google Quality Score → lower CPC |
| **Mobile-first** | CTA above fold; thumb-reachable; fast load (&lt;3s) |

See **landing-page-generator** for LP structure and conversion optimization.

## Common Mistakes to Avoid

- Launching without conversion tracking
- Too many campaigns (fragmenting budget)
- Not giving algorithms learning time (2–4 weeks; PMax needs 6+ weeks)
- Single ad per ad set; not refreshing creative (fatigue)
- Spreading budget too thin; big budget changes

## Weekly Optimization Cadence

| Check | Action |
|-------|--------|
| **Creative fatigue** | Refresh when CTR or conversion rate drops; test new concepts |
| **Learning phase** | Ensure sufficient volume (e.g., 50+ conv/week Meta; 30+ conv/30d Google for smart bidding) |
| **Brand term share** | If brand terms &gt;30% of conversions, consider reallocating to non-brand |
| **Placement/spend** | Flag if any single placement exceeds 15% of total spend |

## Affiliate Brand Bidding

When running affiliate programs: prohibit affiliates from bidding on your brand terms in Google Ads. Monitor paid search; use brand monitoring tools. See **affiliate-page-generator**.

## Competitor Brand Bidding

**When**: Bid on "[Competitor] alternative," "[Competitor] vs [You]" to intercept high-intent traffic. Google allows competitor terms as keywords; ad copy cannot use competitor names without permission.

**Landing page**: Use a **dedicated comparison/alternatives page**, not a blog. Users searching competitor brands expect direct alternatives; blog increases bounce. See **alternatives-page-generator**, **google-ads** Competitor Brand Keywords.

## Output Format

- **Channel** recommendation (and route to platform skill if needed)
- **When to start** (PMF check; budget readiness)
- **Budget** approach (test budget; ROAS target)
- **Landing page** requirement (ad-to-page alignment)
- **Metrics** to track (ROAS, CAC, Quality Score)

## Related Skills

- **google-ads**, **meta-ads**, **linkedin-ads**, **reddit-ads**, **tiktok-ads**: Web platform setup
- **reddit-posts**, **linkedin-posts**, **tiktok-captions**, **twitter-x-posts**: Platform (organic) skills; creative alignment with reddit-ads, linkedin-ads, tiktok-ads, X Ads
- **app-ads**: App install, UA; Google App Campaigns, Apple Search Ads
- **ctv-ads**: CTV, OTT, streaming ads
- **display-ads**: Ad networks, banner ads, programmatic display
- **directory-listing-ads**: Taaft, Shopify App Store, G2, Capterra paid placements
- **landing-page-generator**: LP structure for paid traffic; ad-to-page alignment
- **alternatives-page-generator**: Competitor brand keyword ads → dedicated LP (not blog); comparison page structure
- **cold-start-strategy**: When NOT to use paid ads
- **pmf-strategy**: PMF validation; when to use PMF testing vs conversion-driven mode
- **seo-strategy**: Organic vs paid
- **integrated-marketing**: PESO model; paid as one channel
- **keyword-research**: Keywords inform paid search targeting
- **traffic-analysis**: UTM for paid attribution
- **analytics-tracking**: Conversion tracking; ROAS measurement; incrementality experiments
