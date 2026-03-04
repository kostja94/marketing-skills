---
name: app-ads
description: When the user wants to run app install ads, user acquisition (UA), or promote mobile apps. Also use when the user mentions "app ads," "app install ads," "UA," "user acquisition," "Google App Campaigns," "Apple Search Ads," "ASA," "UAC," "App Store ads," "Play Store ads," "CPI," or "app promotion."
metadata:
  version: 1.0.0
---

# Paid Ads: App Ads

Guides app advertising: app install campaigns, user acquisition (UA), and in-app promotion. Use when promoting mobile apps (iOS, Android); conversion = install or in-app action, not landing page.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Key Platforms

| Platform | Best for | Conversion |
|----------|----------|------------|
| **Google App Campaigns** | Android + iOS; automated across Search, YouTube, Display, Play, Discover | Install, in-app event |
| **Apple Search Ads (ASA)** | iOS only; high-intent App Store search | Install |
| **Meta App Install** | Facebook/Instagram; demand gen for apps | Install, in-app event |
| **TikTok App Install** | Younger users; viral creative | Install |

## Google App Campaigns

- **Reach**: Search, YouTube, Display, Google Play, Discover
- **Bidding**: Maximize Conversions (automated) or Target CPI/CPA (30+ conversions/week)
- **Creative**: Provide diverse assets (videos, images, text); algorithm tests combinations
- **iOS**: SKAdNetwork; conversion value mapping; Firebase for in-app events
- **Bid–budget ratio**: ≥10× for CPI, ≥15× for CPA

## Apple Search Ads

- **Placements**: App Store search results, Today tab, Search tab, product pages
- **Modes**: Basic (automated) or Advanced (keywords, audiences, bids)
- **Audience**: High-intent users actively searching in App Store
- **ASO benefit**: Can improve keyword rankings as secondary effect

## Metrics

| Metric | Use |
|--------|-----|
| **CPI** | Cost per install |
| **CPA** | Cost per acquisition (in-app action) |
| **LTV** | Lifetime value; iOS often higher than Android |
| **Retention** | D1, D7, D30; quality signal |

**iOS vs Android**: iOS typically higher LTV, higher CPI; Android greater scale, lower CPI.

## Tracking

- **Firebase**: In-app events, audiences, value-based optimization (Google)
- **SKAdNetwork**: iOS attribution; configure conversion value mapping
- **UTM**: Use `utm_medium=app` or `cpc` with `utm_source` for app campaigns in GA4

## Pre-Launch Checklist

- [ ] App Store / Play Store listing optimized (ASO)
- [ ] Firebase or equivalent connected; in-app events defined
- [ ] Creative assets (video, images, text) prepared
- [ ] Conversion events (install, signup, purchase) configured
- [ ] Bid–budget ratio meets minimum (10× CPI, 15× CPA)

## Related Skills

- **paid-ads-strategy**: Ad formats by medium; when to use app vs web
- **analytics-tracking**: In-app events; conversion setup
- **traffic-analysis**: UTM for app campaigns; attribution
