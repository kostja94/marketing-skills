---
name: traffic-analysis
description: When the user wants to analyze website traffic sources, attribution, or dark traffic. Also use when the user mentions "traffic sources," "dark traffic," "direct traffic," "UTM parameters," "traffic attribution," "channel analysis," "traffic analysis," "traffic diversification," "natural traffic benchmark," or "organic vs paid traffic."
metadata:
  version: 1.0.0
---

# Analytics: Traffic

Guides website traffic analysis across all channels (organic, paid, social, referral, direct). Covers traffic source attribution, dark traffic identification, and multi-channel reporting.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Traffic sources**: Organic, paid, social, referral, direct, email
- **Dark traffic**: Unattributed visits labeled as "Direct / None"
- **Attribution**: UTM tagging, segmenting, reporting accuracy

## Traffic Channels

| Channel | Typical Sources | Attribution |
|---------|-----------------|-------------|
| **Organic** | Google, Bing, other search | Referrer preserved |
| **Paid** | Google Ads, Meta Ads, etc. | UTM required |
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

## UTM Best Practices

| Parameter | Use | Example |
|-----------|-----|---------|
| `utm_source` | Origin | `newsletter`, `facebook`, `google` |
| `utm_medium` | Channel type | `email`, `cpc`, `social` |
| `utm_campaign` | Campaign name | `summer_sale`, `product_launch` |
| `utm_content` | Variant (optional) | `banner_a`, `cta_button` |
| `utm_term` | Paid keyword (optional) | `running_shoes` |

- **Consistent naming**: Lowercase, underscores; document conventions
- **Apply everywhere**: Every link in emails, social posts, ads
- **Avoid**: Typos, inconsistent values; causes fragmentation

## Traffic Diversification

| Principle | Guideline |
|-----------|-----------|
| **Search share** | Keep organic search below ~75% of total traffic |
| **Health** | Higher direct + referral share = healthier profile |
| **Brand sites** | Diversified traffic is common for strong brands |
| **Engagement** | Content, email, social, free tools drive return visits |

See seo-monitoring for full SEO data analysis framework.

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

- **analytics-tracking**: Implement UTM and event tracking
- **ai-traffic-tracking**: AI search traffic
- **google-search-console**: GSC performance and indexing analysis
- **seo-monitoring**: Full SEO data analysis system, benchmark, article database
- **email-marketing**: Email strategy; UTM for email links
