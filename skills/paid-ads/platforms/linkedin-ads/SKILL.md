---
name: linkedin-ads
description: When the user wants to set up, optimize, or manage LinkedIn Ads. Also use when the user mentions "LinkedIn Ads," "LinkedIn Campaign Manager," "Sponsored Content," "Lead Gen Forms," "Sponsored Messaging," "Message Ads," "Conversation Ads," "Accelerate," "Classic ad set," "Audience Network," "objective-based pricing," "Insight Tag," "job title targeting," "company targeting," "Matched Audiences," or "B2B paid ads." For organic posts, use linkedin-posts.
metadata:
  version: 1.2.0
---

# Paid Ads: LinkedIn Ads

Guides LinkedIn Ads setup, targeting, and optimization. LinkedIn excels at B2B and professional targeting; use when job title/company targeting matters and ACV is higher.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Account and product context

- **Campaign Manager** is the main UI: [campaignmanager.linkedin.com](https://www.linkedin.com/campaignmanager) · [Get started (help)](https://www.linkedin.com/help/lms/answer/a9509136)
- **Marketing Solutions** = ads for brands/leads; **Talent Solutions** = hiring products (separate when choosing objectives).
- **Sponsored Content** in-feed and **Sponsored Messaging** generally require a free **[LinkedIn Page](https://business.linkedin.com/advertise/ads/best-practices/what-you-need-to-get-started)** (per official getting-started guidance—confirm in your account).
- **Review**: build **at least ~1–2 days** before go-live; last-minute changes may miss launch. [Ad set best practices](https://www.linkedin.com/help/lms/answer/a422123)

## Campaign structure (naming and hierarchy)

**Naming (example)**: `LI_[Objective]_[Audience]_[Offer]_[Date]` (e.g. `LI_LeadGen_CMOs-SaaS_Whitepaper_Mar24`)

**Hierarchy in Campaign Manager (names vary slightly over time):**

| Level | Role |
|-------|------|
| **Campaign group** | Groups related programs; shared **status and budgets** (optional). |
| **Campaign** | **Marketing objective**; budget/scheduling as configured. |
| **Ad set** | **Accelerate** or **Classic**; **audience, placements, format, budget, schedule, bid**; conversion/URL params. [Compare types](https://www.linkedin.com/help/lms/answer/a1642380) |
| **Ads** | Creative; multiple ads per ad set for A/B. |

**Billing model**: [Objective-based pricing](https://www.linkedin.com/help/lms/answer/a427513) — **billed on the action tied to the objective** (e.g. clicks for traffic-oriented objectives). [Pricing overview](https://business.linkedin.com/advertise/ads/pricing)

**Budget pacing**: Auction-based; on **daily** budgets, spend on a day may **exceed the daily number by a margin**; **pacing** smooths so **7-day** spend does not exceed about **7× daily** (per LinkedIn’s public budget article—**always** confirm the latest text). [Budgets and pacing](https://www.linkedin.com/help/lms/answer/a422101)

**Minimum spend**: There is **no one global fixed** minimum across all cases; very low daily/lifetime budgets are often **rejected in UI**. A common **practical** floor cited in the industry is on the order of **~$10 USD/day per ad set** (not a platform guarantee). Use Campaign Manager as source of truth.

## Marketing objectives (funnel, abbreviated)

| Funnel | Example objectives (names evolve—pick in UI) | Typical use |
|--------|-----------------------------------------------|------------|
| Awareness | Brand awareness | Broad reach |
| Consideration | Website visits, Engagement, Video views | Traffic, company/page engagement, video |
| Conversion | Lead generation, Website conversions | Leads, **Lead Gen Forms**, on-site events |
| Talent | Job applicants, Talent leads (where eligible) | Hiring |

Full list: [Marketing objectives](https://www.linkedin.com/help/lms/answer/a424570)

## Ad formats and placements (high level)

[Ads Guide (authoritative for specs)](https://business.linkedin.com/advertise/ads/ads-guide)

### Sponsored Content (feed and related)

Aligns with **organic** shapes in **linkedin-posts** (image, video, document, etc.) as **paid** delivery:

- **Single image, video, carousel** (carousel ad cards often **2–10** in guide) · **Document** (PDF/DOC/PPT-style; large page/file limits in guide)
- **Event** ads (promote a LinkedIn Event) · **Job** ads (boost an existing job post)
- **Thought Leader** ads: amplify **qualified** members’ posts (eligibility rules in Ads Guide)
- **Article and Newsletter** ads: promote in-platform long-form/series
- **CTV (Connected TV)**: in-stream **reach**-oriented video with LinkedIn **targeting**; not a feed click campaign by default
- Placements can include **LinkedIn Audience Network (LAN)**—third-party app/site inventory. Toggle/availability is in the ad set. [LAN (help)](https://www.linkedin.com/help/lms/answer/a423409)

### Lead Gen Forms

- Native forms on ads; **profile pre-fill**; typically **~12 fields and ~3 custom questions** at most (verify current product)
- Minimize fields for higher completion; sync to CRM/Marketing automation

### Sponsored Messaging (inbox)

| Type | Notes |
|------|--------|
| **Message Ads** | One focused **message** + CTA; body often **~1,500 characters** in product docs (check Ads Guide) |
| **Conversation Ads** | **Branching** buttons; long body allowance (often **~8,000 characters** in docs); **up to ~5 CTA** buttons (check guide) |

### Text and Dynamic Ads

- **Text ads**: **Desktop**-oriented; small image + text; often CPC/CPM. [Placements (help)](https://www.linkedin.com/help/lms/answer/a417880)
- **Dynamic / Follower / Spotlight** variants: personalized right-rail; see Ads Guide

**Tracking**

- **Insight Tag** for site retargeting and conversion lift · [Conversion tracking hub](https://www.linkedin.com/help/lms/answer/a420536)
- **UTM/URL parameters**: [URL tracking parameters](https://www.linkedin.com/help/lms/answer/a5968064)

## Targeting strengths

| Signal | Use |
|--------|-----|
| **Job title, function, seniority** | ICP and committees |
| **Company** | Industry, size, name lists (ABM) |
| **Skills, interests, groups** | Technical or topical |
| **Matched Audiences** | **Contact/company** lists, retargeting (Insight Tag) |
| **Exclusions, expansion** | **Audience expansion** (when offered)—broaden carefully |

**Lookalike audiences**: As of current LinkedIn public documentation, **Lookalike** is **not** the default expansion path; it has been **deprecated/removed** in many accounts—rely on **first-party lists**, **Matched Audiences**, and **exclusion/expansion** options shown in the UI. See [Target audience size / practices](https://www.linkedin.com/help/lms/answer/a423690) and the live Campaign Manager for your tenant.

**Principle**: LinkedIn is **expensive**; start **narrow, high-intent**; then scale with measured expansion.

**Audience size**: A common **operational** band mentioned in industry is **hundreds+** in targetable size; the UI will warn if the audience is too small—follow it.

## Creative best practices

- **Professional** tone; align Sponsored copy with your **Page** and organic voice (**linkedin-posts**)
- **Headline + first line** clear value; match landing experience
- **Lead Gen Forms**: **fewer** fields; clear next step for SDRs
- **Document ads**: gating a PDF/deck; pair with a strong CTA
- **Creative limits**: e.g. image **~5MB** and **~1200×627** in many specs—**always** take from [Ads Guide](https://business.linkedin.com/advertise/ads/ads-guide) for the format you use

## Benchmark costs (illustrative, not guaranteed)

- LinkedIn is typically **higher** **CPC/CPM** than Meta and Google in comparable B2B use cases. Third-party **ranges** (USD, very rough) often cite e.g. **CPC ~$5–8** as a **ballpark** middle; real costs swing with audience, **CTR**, **quality**, and season. **Never** use these as a commitment—use in-account reporting. [Why pricing varies](https://business.linkedin.com/advertise/ads/pricing)
- **CTR** for feed is often **well under ~1%** in reported benchmarks; optimize creative and ICP, not the benchmark alone

## Bidding (short)

- Start with **strategies** appropriate to the objective; move to **automated/goal-based** when **enough** weekly conversions exist for the system to learn
- Manual caps help when **volume** is too low to automate

## Pre-launch checklist

- [ ] **Insight Tag** (if site conversions/retargeting) · **Lead** routing to CRM if using LGF
- [ ] **Page** and billing **ready**; **naming** at group/campaign/ad set level
- [ ] **Objective** and **ad set** type (**Accelerate** vs **Classic**) set intentionally
- [ ] **Audience** defined; **exclusions** for existing customers (where needed)
- [ ] **Creatives** meet policy; **UTMs** for non-LGF web flows
- [ ] **Budget** realistic for the account’s CPM/CPC; **pacing** understood

## Related Skills

- **linkedin-posts**: Organic formats and copy; align Sponsored with same patterns
- **paid-ads-strategy**: Channel mix; B2B vs B2C; budget allocation
- **landing-page-generator**: Web LPs for non–Lead Gen Form flows
- **analytics-tracking**: Attribution, ROAS, pipeline

## Official link index

| Topic | URL |
|------|-----|
| Ads Guide (formats) | https://business.linkedin.com/advertise/ads/ads-guide |
| Pricing and auction | https://business.linkedin.com/advertise/ads/pricing |
| Create campaigns | https://www.linkedin.com/help/lms/answer/a9509136 |
| Objectives | https://www.linkedin.com/help/lms/answer/a424570 |
| Placements (Text ads, etc.) | https://www.linkedin.com/help/lms/answer/a417880 |
| Targeting options | https://www.linkedin.com/help/lms/answer/a424655 |
| LMS help home | https://www.linkedin.com/help/lms |
| Get started (what you need) | https://business.linkedin.com/advertise/ads/best-practices/what-you-need-to-get-started |
