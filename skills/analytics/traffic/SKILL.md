---
name: traffic-analysis
description: When the user wants to analyze website traffic sources, attribution, or dark traffic. Also use when the user mentions "traffic sources," "dark traffic," "direct traffic," "UTM parameters," "traffic attribution," "channel attribution," "attribution optimization," "channel analysis," "traffic analysis," "traffic diversification," "natural traffic benchmark," or "organic vs paid traffic."
metadata:
  version: 1.1.0
---

# Analytics: Traffic

Guides website traffic analysis across all channels (organic, paid, social, referral, direct). Covers traffic source attribution, dark traffic identification, and multi-channel reporting.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Traffic sources**: Organic, paid, social, referral, direct, email
- **Dark traffic**: Unattributed visits labeled as "Direct / None"
- **Attribution**: UTM tagging, segmenting, reporting accuracy

## Branded vs. Non-Branded Traffic (Organic)

| Type | Characteristics |
|------|-----------------|
| **Branded** | Higher CTR, conversion, purchase intent; users closer to funnel bottom |
| **Non-branded** | Touchpoint with future users; most sites get more non-brand traffic; competition fiercer |

Brand traffic grows over time as brand awareness increases.

## Bot Traffic

A large share of traffic can be **bot traffic**—RPA, search crawlers, spiders, scrapers. Exclude or segment when evaluating real user behavior; use GA4 filters or segments to isolate human traffic.

## Traffic Channels

| Channel | Typical Sources | Attribution |
|---------|-----------------|-------------|
| **Organic** | Google, Bing, other search | Referrer preserved |
| **Paid (web)** | Google Ads, Meta Ads, etc. | UTM required |
| **Paid (app)** | App install ads; Google App Campaigns, Apple Search Ads | UTM; in-app events |
| **Paid (TV/CTV)** | Streaming ads; Hulu, Roku, YouTube TV | UTM for QR/URL; brand lift |
| **Social** | Public posts (Facebook, LinkedIn, etc.) | Often preserved |
| **Referral** | External sites, backlinks | Referrer preserved |
| **Direct** | Typed URL, bookmarks | No referrer |
| **Email** | Newsletters, campaigns | Often dark without UTM |

## Dark Traffic

### What It Is

Traffic without clear origin--analytics tools default to "Direct" when referrer is missing. Common causes:

- **Private/dark social**: WhatsApp, Messenger, Slack, Discord, TikTok shares
- **Email clients**: Many strip referrer headers
- **HTTPS->HTTP**: Referrer not passed
- **Mobile apps**: In-app browsers often omit referrer
- **Ad blockers, privacy tools**: Block tracking

### Misattribution (Research)

When traffic was sent from known sources, analytics often misattributed:

- **100% as direct**: TikTok, Slack, Discord, WhatsApp, Mastodon
- **75%**: Facebook Messenger
- **30%**: Instagram DMs
- **14%**: LinkedIn public posts
- **12%**: Pinterest

### Mitigation

| Action | Purpose |
|--------|---------|
| **UTM parameters** | Tag links in emails, social, campaigns: `?utm_source=X&utm_medium=Y&utm_campaign=Z` |
| **Block internal IPs** | Exclude company visits from reports |
| **Segment direct traffic** | Split by page type to estimate dark vs. genuine direct |

### Segmenting Direct Traffic

1. **Expected direct**: Homepage, short URLs, brand pages--likely real direct
2. **Unexpected direct**: Long URLs, deep pages, product pages--likely dark traffic
3. **Report separately**: Use segments in GA4/analytics to avoid overcounting direct

## Attribution for Channel Optimization

Ads, growth channels, and medium can be optimized by viewing **attribution data**. Clean UTM + conversion tracking feeds attribution models; reliable attribution drives budget allocation and channel decisions.

| Use | Action |
|-----|--------|
| **Optimize ads** | Compare paid channels (Google, Meta, LinkedIn) by attributed conversions; reallocate budget to winners |
| **Optimize growth channels** | Identify which medium (cpc, email, social, referral) drives conversions; scale what works |
| **Multi-touch attribution** | Requires clean UTM data; inconsistent tagging (e.g., `facebook` vs `Facebook`) fragments reports and misattributes |

**GA4 Default Channel Grouping**: Align `utm_medium` and `utm_source` with [GA4's rules](https://support.google.com/analytics/answer/9756891) to avoid "Unassigned" traffic. ~30% of campaigns lack proper UTM markup, leading to wasted ad spend; teams standardizing UTM see 29% improvement in attribution accuracy.

**Reference**: [UTM.io – utm_medium, utm_campaign & utm_source Optimization](https://web.utm.io/blog/utm_medium-utm_campaign-utm_source/), [UTMs for Marketing Attribution](https://web.utm.io/blog/utms-for-marketing-attribution/)

## UTM Best Practices

| Parameter | Use | Example |
|-----------|-----|---------|
| `utm_source` | Origin | `newsletter`, `facebook`, `google` |
| `utm_medium` | Channel type | `email`, `cpc`, `social` |
| `utm_campaign` | Campaign name | `summer_sale`, `product_launch` |
| `utm_content` | Variant (optional) | `banner_a`, `cta_button` |
| `utm_term` | Paid keyword (optional) | `running_shoes` |

**GA4 alignment** (avoid Unassigned):

| Channel | utm_medium | utm_source |
|---------|------------|------------|
| Paid Search | `cpc` | `google`, `bing` |
| Paid Social | `paid-social`, `cpc` | `facebook`, `instagram` |
| Email | `email` | `newsletter`, `mailchimp` |
| Organic Social | `social` | `twitter`, `linkedin` |
| App install | `cpc`, `app` | `google`, `facebook`, `apple` |
| CTV / Streaming | `video`, `ctv` | `hulu`, `roku`, `youtube` |
| Display / Banner | `display`, `cpc` | Publisher or network name |
| Directory ads | `paid`, `cpc` | `taaft`, `shopify`, `g2`, `capterra` |

- **Consistent naming**: Lowercase, hyphens; document conventions; never tag internal links (overwrites session attribution)
- **Apply everywhere**: Every link in emails, social posts, ads
- **Avoid**: Typos, inconsistent values; causes fragmentation

## Traffic Diversification

| Principle | Guideline |
|-----------|-----------|
| **Search share** | Keep organic search below ~75% of total traffic |
| **Health** | Higher direct + referral share = healthier profile |
| **Brand sites** | Diversified traffic is common for strong brands |
| **Engagement** | Content, email, social, free tools drive return visits |

See **seo-monitoring** for full SEO data analysis framework.

## Natural Traffic Benchmark

**Location**: GA4 > Reports > Acquisition > Traffic acquisition

1. Review organic traffic trend
2. Record baseline (e.g., monthly total)
3. Compare periodically to detect growth or decline

## Output Format

- **Traffic source** breakdown
- **Dark traffic** estimate and actions
- **UTM** tagging recommendations
- **Segmentation** approach for reporting

## Related Skills

- **analytics-tracking**: Implement UTM, events, conversions; attribution models
- **google-ads, paid-ads-strategy**: Paid channels; attribution informs budget allocation
- **ai-traffic-tracking**: AI search traffic
- **google-search-console**: GSC performance and indexing analysis
- **seo-monitoring**: Full SEO data analysis system, benchmark, article database
- **email-marketing**: Email strategy; UTM for email links
