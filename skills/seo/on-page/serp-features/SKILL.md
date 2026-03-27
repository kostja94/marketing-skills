---
name: serp-features
description: When the user wants to understand or optimize for SERP feature types (PAA, sitelinks, rich results, AI Overviews). Also use when the user mentions "SERP," "SERP features," "search result features," "People Also Ask," "PAA," "sitelinks," "knowledge panel," "local pack," "rich results," "zero-click," "SERP types," "AI Overviews," "Bing Copilot," or "Yandex AI." For JSON-LD and rich result implementation, use schema-markup. For organic strategy and roadmap, use seo-strategy.
metadata:
  version: 1.1.0
---

# SEO On-Page: SERP Features

Guides SERP (Search Engine Results Page) features: types, obtainability, and optimization. ~98.5% of Google's first page includes SERP features; rich results receive ~58% of clicks vs 41% for standard listings. Understanding SERP features helps prioritize keywords and content strategy.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **SERP feature types**: Organic enhancements, universal results, paid, knowledge
- **Obtainability**: Which features are achievable; which require authority/partnerships
- **Optimization**: Content, schema, and structure for each feature type
- **Impact**: CTR, zero-click, traffic implications

## What Is a SERP Feature?

A **SERP feature** is any result on a search results page that is **not** a traditional organic blue link. Features provide quick answers, visual enhancements, or alternative result types (images, local, news, etc.).

## Rich Results vs Featured Snippets

| Dimension | Rich Results | Featured Snippets |
|-----------|--------------|-------------------|
| **Location** | Within standard organic listings; enhance a blue link | Above organic results; "position zero" |
| **Generation** | Structured data (Schema/JSON-LD) added by site owner | Google extracts from page content; no schema required |
| **Display** | Star ratings, prices, images, breadcrumbs, FAQ dropdowns | Extracted text in highlighted box; paragraph, list, table, or video |
| **Ranking** | Do not require high organic rank to appear | Page must rank in top ~10 for the query |
| **Industry** | Often content-specific (recipes, products, events, reviews) | Versatile; most industries |
| **CTR** | Typically increase CTR (up to ~35%); enhanced visibility | Can increase or reduce clicks (zero-click when answer suffices) |

**Rich results** = schema-powered enhancements to regular listings. **Featured snippets** = Google-extracted answer boxes at position zero. Both are SERP features; rich results are a subset driven by structured data. [Onely](https://www.onely.com/blog/difference-between-featured-snippets-and-rich-results-explained/), [Seranking](https://seranking.com/blog/rich-snippets/)

## SERP Features ↔ Schema ↔ Rich Results (Strongly Related)

**SERP features, schema, and rich results are strongly related.** Most achievable SERP enhancements depend on or benefit from Schema.org structured data. Schema makes content machine-readable so search engines can extract and display rich results.

| SERP Feature | Schema Type | Relationship |
|--------------|-------------|--------------|
| **PAA / FAQ dropdown** | FAQPage | Required or strongly recommended; FAQ schema triggers PAA-style display |
| **Breadcrumbs** | BreadcrumbList | Required; no schema = no breadcrumb rich result |
| **Reviews / Stars** | AggregateRating, Review | Required; star display depends on review schema |
| **Featured Snippet** | FAQPage, HowTo, Article | Supporting; schema helps identify extractable blocks; not required |
| **Sitelinks** | WebSite + SearchAction | Supporting; SearchAction can enable sitelinks |
| **Video** | VideoObject | Required; video thumbnail; Google prioritizes YouTube. See **video-optimization** |
| **Product** | Product, Offer | Required; shopping results |
| **Recipe** | Recipe | Required; recipe rich result |
| **Job** | JobPosting | Required; Google Jobs |
| **Event** | Event | Required; event rich result |
| **In-Depth Articles** | Article + author | Supporting; Article schema, authorship |

**Workflow**: When targeting a SERP feature, check **schema-markup** for the schema type; after implementing schema, use **serp-features** to assess display and optimization.

## SERP Feature Categories

### 1. Organic Enhancements (Achievable)

| Feature | Description | Obtainability |
|---------|-------------|----------------|
| **Featured Snippet** | Direct answer above organic results; paragraph, list, or table | Content that answers query in 40–60 words; positions 2–5 often win. See **featured-snippet** |
| **People Also Ask (PAA)** | Expandable question boxes with brief answers | FAQ-style content; FAQ schema; match question phrasing |
| **Sitelinks** | Additional links below main result (brand queries) | Site structure, internal links, SearchAction schema; mainly branded |
| **Reviews / Stars** | Star ratings on product/service results | Review schema (AggregateRating); eligibility varies by vertical |
| **Breadcrumbs** | Path shown in result | BreadcrumbList schema; clear site structure |
| **Video** | Video thumbnail in results | Video schema; **Google prioritizes YouTube**; see **video-optimization** |
| **Image Pack** | Horizontal row of images | Alt, captions, file names, responsive; see **image-optimization** |

### 2. Universal Results

| Feature | Description | Obtainability |
|---------|-------------|----------------|
| **News Box** | Time-sensitive news block | Google News inclusion; publisher eligibility |
| **In-Depth Articles** | Long-form block (broad terms) | Large publishers; 2000–5000 words; authorship, Article schema |
| **Tweet** | Twitter results in SERP | Brand presence; not directly controllable |
| **Shopping** | Product listings with images/price | Paid (PLAs) or Product schema for organic |

### 3. Knowledge / Entity (Limited Obtainability)

| Feature | Description | Obtainability |
|---------|-------------|----------------|
| **Knowledge Panel** | Entity info (brand, person, place) | WikiData, partnerships; see **entity-seo** |
| **Knowledge Card** | Top-of-SERP semantic answer | Same as Knowledge Panel |
| **Local Pack** | 3 local business results + map | Local SEO; GMB, NAP, reviews |
| **Local Teaser** | Hotels, restaurants with map/sort | Local SEO |

### 4. Paid

| Feature | Description |
|---------|-------------|
| **AdWords (Top/Bottom)** | Sponsored results; [Ad] label |
| **Shopping (PLAs)** | Product ads with images |
| **Google Flights** | Flight search in SERP |

### 5. AI Search Summaries (SERP Feature)

AI-generated answer blocks at the top of search results. These are **SERP features**—they occupy prime SERP real estate and replace or supplement traditional blue links. Optimize via **generative-engine-optimization** (GEO).

| Engine | Feature | Description | Availability |
|--------|---------|-------------|--------------|
| **Google** | AI Overviews | Multi-source AI summary at top; Gemini; cites top 10–12 organic results; 2–3 paragraphs or bullets | ~47% US searches; opt-in/experimental in 120+ countries |
| **Bing** | Copilot Search | Curated summaries with cited sources; GPT-4; grouped answers with resources per section; follow-up questions in-search | bing.com/copilotsearch; Edge; standard across Bing |
| **Yandex** | Search with Yandex AI / Neuro | YandexGPT synthesizes from real-time search; cited sources; conversational follow-ups; image upload; Russia-focused | Yandex Browser, Yandex app; Russia location |
| **Perplexity** | — | Standalone AI search; not a SERP feature; 200B+ URL index; live web search | perplexity.ai |
| **ChatGPT** | — | Web search via GPTbot; not a SERP feature; high-authority, LLM-friendly content | chat.openai.com |

**Source selection**: Google pulls from top organic; Bing uses Bing index (9.81% domain overlap with Google); Yandex uses real-time search; Perplexity has independent crawl. AI Overview citations can drive 20–35% higher CTR than equivalent organic positions. [SEJ](https://searchengineland.com/microsoft-officially-launches-copilot-search-in-bing-453958), [Yandex](https://yandex.com/support/search/en/yandex-ai), [Geneo](https://geneo.app/blog/chatgpt-vs-perplexity-vs-google-ai-overview-geo-comparison/)

### 6. Other Newer (2025+)

| Feature | Description |
|---------|-------------|
| **Related Searches** | Alternative queries at bottom |
| **People Also Search For (PASF)** | Related queries after user bounces from result; 6-8 suggestions; different from PAA; comprehensive content reduces bounce. See **faq-page-generator** |

## Optimization by Feature

| Feature | Key Actions |
|---------|-------------|
| **Featured Snippet** | Answer-first (40–60 words); H2/H3; semantic lists/tables. See **featured-snippet** |
| **PAA** | FAQ content; FAQ schema; natural question phrasing; **faq-page-generator** |
| **Sitelinks** | Clear site structure; internal links; SearchAction; **website-structure** |
| **Reviews** | AggregateRating schema; **schema-markup** |
| **Breadcrumbs** | BreadcrumbList schema; **breadcrumb-generator** |
| **Video** | VideoObject schema; **video-optimization**; Google prioritizes YouTube |
| **Image Pack** | Alt, captions, file names, responsive; see **image-optimization** |
| **Local Pack** | Local SEO; GMB; NAP consistency |
| **AI Overview / Copilot / Yandex AI** | GEO; structured content; citable paragraphs; entity signals; see **generative-engine-optimization**, **entity-seo** |

## Zero-Click: SERP Features That Satisfy Intent Without a Click

**Zero-click** = user gets the answer directly on the SERP and does not click through to any website. SERP features are a major driver of zero-click—they answer queries in-place, reducing organic traffic to publishers.

### SERP Features That Cause Zero-Click

| Feature | Zero-Click Risk | Why |
|---------|-----------------|-----|
| **Featured Snippet** | High | Direct answer in position zero; user may not need to visit |
| **People Also Ask (PAA)** | High | Expandable answers; full answer visible without click |
| **AI Overviews** | Very high | ~83% of searches with AI Overview may end without click |
| **Bing Copilot / Yandex AI** | Very high | Full AI summary with sources; answer in-place |
| **Knowledge Panel / Card** | High | Entity info; no click needed for simple facts |
| **Rich results** (reviews, recipe) | Medium | Can reduce clicks when answer is complete (e.g. recipe steps) |

### Implications

- **Traffic**: Expect lower organic clicks when zero-click features dominate the SERP
- **Strategy**: Prioritize **citation** over click—being cited in AI Overview, Featured Snippet, or PAA still delivers brand visibility and trust
- **GEO**: Optimize for citation (see **generative-engine-optimization**) so your content is used even when users don't click
- **Keyword research**: Screen keywords for zero-click SERP features; adjust traffic forecasts and prioritize commercial/transactional queries where clicks matter more

### When Zero-Click Matters Most

- Informational queries ("what is X," "how to Y")—highest zero-click
- Commercial/transactional—users often need to visit (compare, buy)
- Brand queries—sitelinks and Knowledge Panel can still drive clicks to specific pages

## SERP Analysis for Strategy

- **SERP check**: Search target keyword—observe which features appear
- **Intent signals**: Knowledge card → informational; product lists → commercial; brand → navigational
- **Zero-click assessment**: Identify features that satisfy intent without click; factor into traffic expectations
- **Keyword research**: **keyword-research** uses SERP features (Featured Snippet, PAA, zero-click) in screening

## Rich Results: Types & Impact

**Rich results** are enhanced search listings powered by structured data. They appear *within* organic positions (unlike Featured Snippets at position zero). High-impact types: Product, Review snippets, HowTo (desktop), Article/News, Video, Recipe, LocalBusiness, Event, Breadcrumb, Sitelinks searchbox, JobPosting. Limited/context-dependent: HowTo (mobile), FAQ (restricted to government/health for many sites), Education Q&A, Course, SoftwareApplication. [AISO Hub](https://aiso-hub.com/insights/google-rich-results-types/)

Rich results do not directly boost rankings but can increase CTR by up to 35%. They also make content machine-readable for AI Overviews, Gemini, Copilot, and Perplexity. Validate with [Google Rich Results Test](https://search.google.com/test/rich-results).

## CTR Impact

- **Zero-click trade-off**: SERP features can increase CTR (rich results, sitelinks) or reduce it (Featured Snippet, PAA, AI Overviews when answer suffices). See Zero-Click section above.
- Rich results: ~58% of clicks vs 41% for standard listings
- Featured snippets: ~42.9% CTR boost; position zero ~35% of clicks when present
- Review stars: Higher CTR
- Sitelinks: Dominate SERP for brand queries; faster path to target page

## Output Format

- **SERP features** present for target keyword
- **Zero-click** assessment (which features satisfy intent without click)
- **Obtainability** assessment
- **Optimization** priorities (schema, content, structure; citation vs click)
- **Related** skills for each feature

## Related Skills

- **schema-markup**: **Strongly related**—schema type maps to SERP feature; see mapping table above
- **featured-snippet**: Featured Snippet / Position Zero optimization
- **faq-page-generator**: PAA optimization; FAQ format
- **keyword-research**: SERP features in keyword screening
- **website-structure**: Sitelinks; site architecture
- **generative-engine-optimization**: AI Overviews, Bing Copilot, Yandex AI; GEO strategy
- **image-optimization**: Image Pack; alt, captions, file names
- **video-optimization**: Video SEO; VideoObject; YouTube prioritization
- **entity-seo**: Knowledge Panel; Organization, Person schema
