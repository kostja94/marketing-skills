# How Skills Work Together

Skill dependency maps as ASCII trees. Workflow order: Technical → On-Page → Content → Off-Page. See each skill's **Related Skills** for the full dependency map.

---

## 1. SEO Foundation (Technical → On-Page → Content → Off-Page)

**Orchestration**: See **seo-strategy** for workflow order, prioritization, Product-Led SEO, and audit approach.

```
                    ┌──────────────────────────────────────────┐
                    │       Technical SEO (Foundation)         │
                    │  robots · sitemap · canonical · indexing │
                    │  indexnow · crawlability                 │
                    └─────────────────────┬────────────────────┘
                                          │
         ┌────────────────────────────────┼────────────────────────────────┐
         ▼                                ▼                                ▼
┌──────────────────┐           ┌──────────────────────┐           ┌──────────────────┐
│     On-Page       │           │      Content        │           │    Off-Page       │
│ title · meta-desc │◄──────────►│ keyword-research    │           │  link-building   │
│ metadata · schema │           │ content-strategy    │           │ backlink-analysis │
│ internal-links    │           │ content-optimization │           └──────────────────┘
│ url-structure ·   │           │ eeat-signals ·      │
│ heading          │           │ competitor-research │
└──────────────────┘           └──────────────────────┘

Cross-refs: metadata ↔ schema ↔ heading │ internal-links ↔ crawlability
```

---

## 2. SERP & Rich Results (Strongly Related)

Schema, SERP features, and Featured Snippets are tightly coupled. Most rich results require schema; SERP features map to schema types.

```
                    ┌─────────────────────────────────────────┐
                    │              serp-features               │
                    │  PAA · sitelinks · breadcrumbs · reviews  │
                    │  AI Overviews · zero-click               │
                    └──────────────┬───────────────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼
    ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
    │  schema-markup   │  │ featured-snippet│  │ faq-page-generator│
    │  JSON-LD · types │◄►│ Position Zero   │◄►│ FAQ schema · PAA │
    └─────────────────┘  │ 40–60 words     │  └─────────────────┘
                         │ H2/H3 · lists   │
                         └─────────────────┘

Cross-refs: schema ↔ serp-features (Strongly related) │ heading-structure → snippet extraction
```

---

## 3. Pages (Apply SEO)

Page skills apply On-Page SEO when optimizing specific page types. Grouped by purpose.

```
                         ┌─────────────────────────────────────────┐
                         │         On-Page SEO (from tree 1)        │
                         └─────────────────────┬───────────────────┘
                                                │
    ┌───────────────────────────────────────────┼───────────────────────────────────────────┐
    ▼                   ▼                       ▼                       ▼                   ▼
┌─────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────┐
│  Brand  │    │    Content       │    │   Marketing     │    │     Legal       │    │ Utility │
│ home ·  │    │ blog · article · │    │ pricing · LP ·  │    │ privacy · terms │    │ 404 ·   │
│ about · │    │ faq · glossary · │    │ alternatives ·  │    │ cookie · refund │    │ changelog│
│ contact │    │ docs · api       │    │ use-cases · ... │    │ shipping · legal │    │ status  │
└─────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────┘

See [page-taxonomy](page-taxonomy.md) for full classification.
```

---

## 4. Growth: Channels, Platforms, Strategies

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Channels                                                                    │
│  affiliate · education · email · egc · influencer · referral · creator · community · dirs · pr│
└─────────────────────────────────────────────────────────────────────────────┘
                                        │
┌───────────────────────────────────────┼───────────────────────────────────────┐
│  Platforms                             │  Strategies                          │
│  x · reddit · linkedin · tiktok ·       │  branding · brand-protection · content-mktg · seo-strategy · paid-ads │
│  youtube · pinterest · medium ·         │  cold-start · indie-hacker · geo · integrated-mktg · pmf · gtm · parasite · programmatic│
│  github · grokipedia                    │  conversion · product-launch · retention · domain/* · pricing/* · rebranding · brand-protection · localization · website-structure        │
└────────────────────────────────────────┼──────────────────────────────────────┘
                                         │
                    ┌────────────────────┴────────────────────┐
                    ▼                                         ▼
         ┌──────────────────────┐                 ┌──────────────────────┐
         │  GEO (AI search)     │                 │  Parasite SEO         │
         │  generative-engine-  │                 │  github · grokipedia  │
         │  optimization        │                 │  medium · reddit · directories  │
         └──────────────────────┘                 └──────────────────────┘
```

---

## 5. Components & Analytics

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Components (used in Pages)                                                 │
│  navigation/ (nav, breadcrumb, footer, sidebar, toc)                          │
│  conversion/ (cta, popup, newsletter-signup, trust-badges, testimonials)       │
│  branding/ (logo, favicon, brand-visual, hero) · content/ (tab-accordion)     │
│  layout/ (card, grid, list, masonry)                                           │
│  utility/ (top-banner, social-share, url-slug)                                │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  Analytics                                                                  │
│  traffic-analysis · analytics-tracking · seo-monitoring                      │
│  ai-traffic-tracking · google-search-console                                │
└─────────────────────────────────────────────────────────────────────────────┘
         │                              │
         └──────────────┬───────────────┘
                        ▼
              ai-traffic-tracking ←→ generative-engine-optimization
              GSC ←→ title-tag · meta-description · indexing
```

---

## Quick Reference

| Tree | Focus |
|------|-------|
| 1 | SEO workflow: technical foundation → on-page → content → off-page; **seo-strategy** for orchestration |
| 2 | SERP enhancements: schema, rich results, featured snippets, FAQ |
| 3 | Page types by purpose (brand, content, marketing, legal, utility) |
| 4 | Growth channels, platforms, GEO, parasite SEO |
| 5 | UI components and analytics |

---

## 6. Brand Protection (Impersonation Response)

```
                    ┌─────────────────────────────────────┐
                    │         brand-protection             │
                    │  Evidence · Report · Prevent · Educate │
                    └─────────────────────┬───────────────┘
                                          │
         ┌────────────────────────────────┼────────────────────────────────┐
         ▼                                ▼                                ▼
┌──────────────────┐           ┌──────────────────────┐           ┌──────────────────┐
│ domain-selection │           │   trust-badges        │           │  about-page      │
│ Defensive reg.   │           │ Official site signal │           │ Identity decl.   │
└──────────────────┘           └──────────────────────┘           └──────────────────┘
         │                                │                                │
         └────────────────────────────────┼────────────────────────────────┘
                                          │
                              ┌───────────┴───────────┐
                              ▼                       ▼
                    ┌──────────────────┐    ┌──────────────────┐
                    │ rebranding-strategy│    │    branding      │
                    │ Sync on rebrand   │    │ Asset protection │
                    └──────────────────┘    └──────────────────┘
```

---

**Skill uniqueness**: Each skill keeps only topic-relevant content. Overlapping topics use **Related Skills** references. See [skills-guide §4.2](skills-guide.md#42-skill-uniqueness-and-cross-references).
