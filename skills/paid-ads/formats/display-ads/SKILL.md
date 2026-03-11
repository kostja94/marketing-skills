---
name: display-ads
description: When the user wants to run display, banner, or ad network campaigns. Also use when the user mentions "display ads," "banner ads," "ad network," "ad alliance," "programmatic display," "native ads," or "retargeting display."
metadata:
  version: 1.0.0
---

# Paid Ads: Display / Banner

Guides display advertising: ad networks, banner ads, and programmatic buying. Use when placing ads on publisher sites (websites, apps) for brand awareness or retargeting.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## What Is Display / Banner

- **Ad networks**: Aggregate inventory from many publishers; buy placements programmatically or via direct deals
- **Banner ads**: IAB standard sizes (300×250, 728×90, 160×600, 320×50 mobile); static or animated
- **Programmatic**: Automated buying via DSPs; real-time bidding (RTB); audience targeting

## Formats

| Format | Use |
|--------|-----|
| **Display banner** | IAB sizes; CPM or CPC; brand, retargeting |
| **Native** | Blends with page content; higher engagement |
| **Video pre-roll** | Pre-roll on publisher video; see **ctv-ads** for streaming |
| **Rich media** | HTML5; expandable, interactive |
| **Mobile interstitial** | Full-screen between content |

## Buying Options

| Option | Use |
|-------|-----|
| **Google Display** | Part of Google Ads; automated placements; retargeting |
| **Programmatic DSP** | The Trade Desk, Magnite, etc.; audience-based; scale |
| **Direct publisher** | Deal with specific site; guaranteed placement |
| **Ad network** | Network aggregates inventory; simpler than full programmatic |

## Metrics

| Metric | Use |
|--------|-----|
| **CPM** | Cost per thousand impressions |
| **CPC** | Cost per click |
| **CTR** | Click-through rate; typically low for banners (0.1–0.5%) |
| **Viewability** | % of impressions actually seen |
| **Completion rate** | For video; % who watch full ad |

## Creative

- **IAB sizes**: 300×250 (medium rectangle), 728×90 (leaderboard), 160×600 (skyscraper), 320×50 (mobile)
- **File types**: Static image, animated GIF, HTML5
- **Message**: Clear CTA; minimal text; brand visible in 3 seconds

## UTM

Use `utm_medium=display` or `cpc` with `utm_source` (publisher or network name) for attribution. See **traffic-analysis** for GA4 alignment.

## Pre-Launch Checklist

- [ ] Creative in required sizes
- [ ] Landing page aligned with ad message
- [ ] UTM parameters set
- [ ] Retargeting audience defined (if applicable)
- [ ] Viewability target set

## Related Skills

- **paid-ads-strategy**: Ad formats by medium; when to use display
- **google-ads**: Google Display Network; retargeting campaigns
- **traffic-analysis**: UTM for display; attribution
- **analytics-tracking**: Conversion tracking; viewability
