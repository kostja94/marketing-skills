---
name: programmatic-seo
description: When the user wants to create SEO pages at scale using templates and data—including AI-assisted, grounded copy for per-URL differentiation (vs rigid mail-merge templates). Also use when the user mentions "programmatic SEO," "programmatic SEO pages," "template pages," "scale content," "location pages," "city pages," "comparison pages at scale," "X vs Y pages," "integration pages," "pages from data," "automated landing pages," or "programmatic landing pages." Uses a playbook matrix aligned to skills under skills/pages. For user-facing template galleries or marketplaces (browse → use), use template-page-generator.
metadata:
  version: 1.4.1
---

# SEO: Programmatic SEO

Guides programmatic SEO—creating large numbers of SEO-optimized pages automatically using templates and structured data, rather than writing each page manually. **Classic “mail merge” pSEO** (one rigid template + swapped variables) often produced **low differentiation** and thin-feeling URLs. **With AI used responsibly on top of the same data spine**, you can scale **per-URL customization**—intent-aligned copy, section depth, FAQs, tone, localization—while still following **evidence blocks**, **data tiers**, and **QA** (see **Data strength hierarchy** and **AI-assisted generation** below).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

**Project context**: If `.claude/project-context.md` or `.cursor/project-context.md` exists, read product/ICP sections before proposing playbooks or page types.

## Definition

**Programmatic SEO** = Building a single template and populating it with data from a database, API, or spreadsheet to generate hundreds or thousands of unique pages. Each page targets a long-tail keyword (e.g., "best SEO tool in [city]," "[App A] + [App B] integration").

**Key differences from traditional SEO**: Technical (SEOs + engineers); long-tail focus; data-driven (data quality = success); automation; built for scale.

## Classic limits vs AI-enhanced differentiation

| Era | What breaks | What helps |
|-----|-------------|------------|
| **Rigid pSEO** | One template, minimal variance → similar titles/bodies, weak **E-E-A-T**, “obvious mail merge” | Still needs **unique evidence per URL** and selective indexation |
| **AI-enhanced pSEO** | Same **structured rows** (facts, SKUs, metrics) drive the page, but models add **per-URL narrative**: intros, FAQ depth, persona angles, localization, internal-link suggestions—**higher differentiation** at scale | **Facts stay in your data layer**; AI shapes **phrasing and structure**, not invented numbers—see **AI-assisted generation** |

**Best-practice stance**: AI is an **accelerator and customizer**, not a substitute for **data defensibility** (Tiers 1–5) or **technical SEO** (URLs, schema, CWV). Used well, it aligns with **quality over quantity**: fewer thin URLs, more **distinct** useful pages.

## Three-Part Framework

| Component | Role |
|-----------|------|
| **Templates** | Reusable page structures: layout, headings, internal links, content blocks; conditional logic for empty fields |
| **Data** | Structured information: locations, products, prices, features—must be accurate, complete, and add genuine value |
| **Automation** | Systems connecting data to templates; pages generated dynamically or published in bulk |
| **AI layer (optional)** | On **grounded inputs** (row JSON + rules), generates **varied copy**, FAQ expansions, and section emphasis **per URL**—reduces “same template” fatigue while staying auditable |

## Page Playbook Matrix (`skills/pages`)

Page types in this library live under `pages/{brand|content|legal|marketing|utility}/`. Use the matrix below to map **search pattern → playbook → which `*-page-generator` skill** to open for structure, copy, and schema—not every folder is a good fit for mass-generated URLs.

| Playbook | Example intent / keyword pattern | Page skill (`name`) | Path (reference) |
|----------|----------------------------------|---------------------|------------------|
| **Alternatives / comparisons** | "[Competitor] alternatives", "X vs Y" | alternatives-page-generator | `pages/marketing/alternatives` |
| **Integrations** | "[Product A] [Product B] integration" | integrations-page-generator | `pages/marketing/integrations` |
| **Category / catalog** | Faceted listings, product grids | category-page-generator, products-page-generator | `pages/marketing/category-pages`, `products` |
| **Glossary / definitions** | "what is [term]", term landings | glossary-page-generator | `pages/content/glossary` |
| **FAQ / Q&A** | Question banks, PAA-style pages | faq-page-generator | `pages/content/faq` |
| **How-to / procedures** | Step libraries, "[how to] [task]" blocks in templates | howto-section-generator | `components/content/howto-section` |
| **Comparison matrix (blocks)** | Feature/criteria grids, "vs" cells from data feed | comparison-table-generator | `components/content/comparison-table` |
| **Tools & lead magnets** | "free [x] tool/calculator" | tools-page-generator | `pages/content/tools` |
| **Template gallery** | Browse → detail (your templates) | template-page-generator | `pages/content/template-page` |
| **Resource hub** | Guides, hubs, download centers | resources-page-generator | `pages/content/resources` |
| **Use cases / solutions** | "for [role]", "by industry" | use-cases-page-generator, solutions-page-generator | `pages/marketing/use-cases`, `solutions` |
| **Migration / switching** | "migrate from [X]" | migration-page-generator | `pages/marketing/migration` |
| **Campaign landing** | Paid/segment LPs | landing-page-generator | `pages/marketing/landing-page` |
| **Blog / article** | Long-tail articles at scale | blog-page-generator, article-page-generator | `pages/content/blog`, `article` |
| **Docs / features / API** | Scalable doc sections, feature landings, `/api` marketing | docs-page-generator, features-page-generator, api-page-generator | `pages/content/docs`, `features`, `api` |
| **Social proof** | Logos, case studies, galleries | press-coverage-page-generator, customer-stories-page-generator, showcase-page-generator | `pages/marketing/press-coverage`, `customer-stories`, `showcase` |
| **Programs & offers** | Startups/education, contests, downloads, affiliate, media kit | startups-page-generator, contest-page-generator, download-page-generator, affiliate-page-generator, media-kit-page-generator | `pages/marketing/*` |
| **Pricing / services** | Plans, offerings (use sparingly for pSEO) | pricing-page-generator, services-page-generator | `pages/marketing/pricing`, `services` |

**Usually not mass programmatic** (single primary URL or compliance-heavy): `pages/brand/*` (home, about, contact), `pages/legal/*`, most `pages/utility/*` (404, status, signup-login, etc.)—treat as one-off or policy-driven, not template×data scale.

## Choosing a Playbook

| If you have… | Lean toward… | Open first… |
|----------------|--------------|-------------|
| Competitor list + positioning | Alternatives / comparisons | alternatives-page-generator |
| Integration directory (your + partners') | Integrations matrix | integrations-page-generator |
| Product catalog or SKUs | Category / product grids | category-page-generator, products-page-generator |
| Term / definition database | Glossary | glossary-page-generator |
| Support tickets / PAA mined questions | FAQ scale | faq-page-generator |
| How-to step banks / procedure templates | HowTo sections in scaled pages | howto-section-generator |
| Competitor/feature matrix from data | Comparison table blocks in scaled pages | comparison-table-generator (+ alternatives-page-generator for URL intent) |
| Lead magnets, calculators | Tools hub + per-tool | tools-page-generator |
| **Your own templates** (exports, gallery items) | Template marketplace | template-page-generator |
| ICP × industry matrix | Use cases / solutions | use-cases-page-generator, solutions-page-generator |
| Import paths from competitors | Migration | migration-page-generator |
| Campaign or geo LPs | Landing pages | landing-page-generator |
| Long-form SEO articles | Blog index + single post | blog-page-generator, article-page-generator |

## Template Structure (Recommended)

| Section | Purpose |
|---------|---------|
| **Intro** | Introduction; matches user intent |
| **Evidence block** | Data-driven content unique to each page (tables, lists, verified stats); differentiates from thin content |
| **Decision** | Comparison, recommendation, or next steps |
| **FAQ** | Frequently asked questions |
| **CTA** | Call-to-action |

**Evidence block** = Real, structured data per page (business listings, pricing, reviews, verified stats). Ensures each page delivers genuine value, not recycled boilerplate with swapped variables.

## Data strength hierarchy (defensibility)

**Strongest programmatic pages are fueled by what only your product (or your customers inside your product) can produce**—especially **templates, exports, and generated artifacts**. Third-party or scraped lists alone are the weakest foundation.

| Tier | Source | Examples | Relative risk |
|------|--------|----------|----------------|
| **1 — Product-generated** | Assets created or rendered by your product: page/layout **templates**, email/Notion/code templates, export packs, generated previews, branded snippets, “built with [Product]” examples | Template gallery rows tied to real `.json` / CMS fields; screenshots of exports; unique preview URLs | **Lowest** when each URL shows distinct generated output |
| **2 — Product-derived** | Telemetry and in-product data you own: aggregates, cohorts, benchmarks, feature adoption | “Teams in [industry] median time-to-value” from your warehouse (aggregated) | Low if aggregated / anonymized and policy-compliant |
| **3 — UGC / customer** | Reviews, submissions, showcase items, moderated community content | Showcase grid; verified quotes | Medium—needs moderation + consent |
| **4 — Licensed / partner** | Exclusive feeds, co-marketing datasets | Partner pricing tiers; licensed industry stats | Medium—contract and citation discipline |
| **5 — Public / scraped** | Open web, directories, generic enrichment | Name/address fills; commodity facts | **Highest**—needs editorial layer, fact-checking, and a real **Evidence block** |

**Why Tier 1 (templates & generated content) wins**: Pages built from **your** template system carry proprietary structure, variables, and brand-safe blocks—harder for competitors to copy verbatim and easier to prove uniqueness (embeds, downloads, IDs). Pair with **template-page-generator** when the UX is “browse gallery → use template.”

### Tier 2 — Product-derived (practical)

| What it is | What to watch |
|------------|----------------|
| Metrics from **your** backend, data warehouse, or support/CRM exports: activation rates by segment, integration popularity, error budgets, time-to-value—not generic “industry reports.” | **Privacy & ToS**: Minimum cell sizes; no individual identification; document what was aggregated and over what window. |
| Good fit when you can show **“only we could know this because it runs in our product.”** | **Stale data** hurts trust: pipeline jobs, “as of [date]” labels, automated invalidation. |

**AI here**: Use models to **turn structured aggregates into prose** (intro paragraphs, “what this means for [segment]”)—**input must be verified numbers/tables from your pipeline**, not free-form invention. Keep a **machine-readable table or JSON** on-page or in appendix so claims stay auditable.

### Tier 3 — UGC / customer (practical)

| What it is | What to watch |
|------------|----------------|
| Quotes, reviews, showcase submissions, community templates—**per-user artifacts** with consent. | **Moderation**: spam, PII, competitor attacks; **consent** for name/logo use; **schema** (Review, CreativeWork) only when accurate. |
| Strong when combined with **Tier 1** (e.g. “customer-built template” gallery). | **Volume without quality** → thin pages; cap or score submissions. |

**AI here**: Summarize long reviews into bullets; **generate draft alt text** for images; **cluster** submissions into topic pages—always **human approve** before publish. Do not fabricate testimonials.

### Tier 4 — Licensed / partner (practical)

| What it is | What to watch |
|------------|----------------|
| Partner price lists, co-marketed reports, API-fed **allowed** fields (logos, SKUs). | **Contract scope**: Which fields can appear on which URLs; attribution line; **DMCA / trademark** on logos. |
| Often **one feed → many URLs**; uniqueness must come from **your framing**, comparison logic, or calculator—not the raw feed alone. | **Refresh cadence** tied to partner SLAs. |

**AI here**: Draft **comparison copy** and **FAQs** from a **fixed attribute table** (license + partner rules); never invent SKUs or prices—**pull from feed**, let AI phrase and shorten.

### Tier 5 — Public / scraped (practical)

| What it is | What to watch |
|------------|----------------|
| Open data, directories, Wikipedia-style facts, **enrichment** of public entities. | **Highest** duplicate/thin risk: everyone has the same facts; **you must add** synthesis, editorial angle, or a **unique tool** (calculator, filter) on top. |
| **Entity SEO** and **citations** matter: link to authoritative sources; date-stamp volatile facts. | Plan for **pruning** or **noindex** on low-traffic thin URLs. |

**AI here**: Use models to **structure** messy public text into tables, **outline** sections, **suggest** internal links—then **fact-check** names, numbers, and dates. **Do not** use AI to invent statistics or citations; treat output as **draft** until verified.

### AI-assisted generation (cross-tier)

**Why AI fits modern pSEO**: Early programmatic SEO earned a bad reputation because **templates were frozen** and **copy was interchangeable**—little real differentiation per query. **LLMs**, when **grounded** on each row’s facts and your brand rules, make it practical to **customize** headlines, intros, FAQs, and “why this page matters” **per URL** without hand-writing thousands of pages. That moves execution closer to **best practices** (intent match, helpful content, unique value) **at scale**, provided you **do not** let the model invent data.

| Principle | Why |
|-----------|-----|
| **Ground AI in structured inputs** | Pass JSON/CSV rows (tier, source URL, metrics) into prompts; **forbid** hallucinated numbers in system prompts. |
| **Separate “facts” from “phrasing”** | Data layer = source of truth; AI = tone, shortening, localization, FAQs, **per-segment emphasis**—never the other way around. |
| **Vary structure, not only adjectives** | Ask for different **section order**, FAQ count, or “beginner vs power user” angles **by intent flags** in the row—reduces template sameness. |
| **Human or automated QA** | Spot-check high-traffic URLs; block publish if required fields empty or citation missing. |
| **Disclose when useful** | e.g. “Intro generated with AI; figures from [internal report, Q3 2025].” Builds trust and matches policy trends. |

**When AI generation is a strong lever**: Tiers **2–5**—where raw material is already tabular or repetitive but **needs readable, differentiated copy at scale**. Tier **1** still benefits from AI (drafts from export JSON), but the **differentiator remains** the product artifact itself.

### Operational requirements (all tiers)

| Requirement | Practice |
|-------------|----------|
| **Provenance** | Log data sources; track origin per field |
| **Freshness rules** | e.g., ratings every 90 days, prices every 30 days, template version bumps when layouts change |
| **Prefer 1–2 over 5** | Fill evidence with product-generated or product-derived data before reaching for public scraping |
| **AI governance** | Structured inputs only; no unverified numbers; moderation on UGC; optional disclosure |
| **Clean & merge** | Deduplicate keys; drop rows that produce duplicate intents |

## Ideal Use Cases

For **which page-generator skill to use**, see **Page Playbook Matrix** above. Generic patterns:

| Use case | Example |
|----------|---------|
| **Location-specific pages** | "Plumber in [city]," "Best restaurants in [neighborhood]" with real local data |
| **Product comparison** | "[Product A] vs [Product B]" with structured specs |
| **Alternatives pages** | "[Competitor] alternatives" at scale; 50+ competitors; see **alternatives-page-generator** |
| **Software integration** | "[App A] + [App B]" integration pages (e.g., Zapier 50K+ pages) |
| **Free tools** | "[X] checker," "[Y] calculator," "[Z] generator" — standalone tool pages; toolkit hub; same ICP as main product; lead gen |
| **Travel / destination** | City + attraction combinations with reviews, photos |
| **E-commerce** | Category pages, product variations (size, color, material) |
| **FAQ / Q&A** | Pages powered by user question databases |
| **Salary / pricing** | Comparison pages with structured data |

**Avoid when**: Site structure is weak; page differences are superficial (city/name swaps only); content requires original expertise or UGC participation.

## Real-World Examples

*Examples are illustrative; no endorsement implied.*

| Company | Scale | Pattern |
|---------|-------|---------|
| **Zapier** | 50,000+ pages | "[App A] + [App B]" integration |
| **Airbnb** | — | Location search; destination × property |
| **Review platforms** | — | User reviews + automated comparison pages |
| **Travel sites** | — | Destination, hotel, flight, activity pages |
| **NomadList** | 2,000+ city pages | Cost-of-living, internet speed (dynamic data) |
| **Semrush, Ahrefs** | 50+ free tools | SEO checker, keyword tool, backlink checker; toolkit hub + per-tool pages |

## Content Requirements

| Requirement | Purpose |
|-------------|---------|
| **300+ words per page** | Avoid thin content penalties |
| **Unique, verifiable data** | Each page must add meaningful page-specific content beyond simple data swaps |
| **Evidence block** | Tables, lists, examples with real numbers/attributes on every page |
| **Semantic HTML** | Proper structure; conditional logic to avoid empty or repetitive sections |
| **Internal linking** | Link related programmatic pages; compounds traffic and indexation |

## Technical Considerations

| Topic | Practice |
|-------|----------|
| **Subfolder vs subdomain** | Prefer **subfolders** (`yoursite.com/integration/slack-notion/`) over **subdomains** (`integrations.yoursite.com/...`) so authority consolidates on the primary domain; see **url-structure**, **domain-architecture** if restructuring |
| **Selective indexation** | Don't index all pages; use noindex rules for low-value pages |
| **Sitemap segmentation** | By country, language, division; manage crawl budget |
| **URL structure** | Descriptive URLs; clean hierarchy; see **url-structure** |
| **Schema** | JSON-LD: Product, Place, FAQ, ItemList per page type |
| **Performance** | Caching, static generation; Core Web Vitals |

## Critical Pitfalls

| Pitfall | Consequence |
|---------|-------------|
| **Thin content** | Minimal info beyond keyword; generic copy; placeholder sections → penalties |
| **Duplicate pages** | Same content with only data swaps → thin content penalties |
| **Index bloat** | Generating pages that should never be indexable → crawl budget waste |
| **Large dumps** | Publishing many similar pages at once → spam signals |
| **Filter URLs** | Using filters instead of unique URLs/titles → cannibalization |

Pages with only a title, one paragraph, and swapped city names will not rank and may incur Google penalties.

## Step-by-Step Workflow

1. **Research** — Niche, intent; include low-volume keywords; SEO tools, question databases
2. **Collect data** — Provenance log, freshness rules; first-party/licensed; define template fields
3. **Choose stack** — Next.js + DB, Webflow CMS, WordPress, headless; API + template reuse
4. **Design template** — Intro, Evidence, Decision, FAQ, CTA; schema; conditional logic
5. **Build database** — Map fields to template slots; hide empties
6. **Generate pages** — Descriptive URLs; optimize performance
7. **Deploy & monitor** — Sitemaps; indexation, rankings, CTR, bounce, conversions
8. **Optimize** — Prune weak pages; refresh data; A/B test layout, CTA

## Best Practices

| Practice | Purpose |
|----------|---------|
| **Quality over scale** | Each page must provide genuinely unique, verifiable value |
| **Differentiation over clone** | Prefer **AI-grounded** copy variance + evidence blocks over one static paragraph with `{city}` swaps |
| **Launch in batches** | Small batches you can measure; avoid large dumps |
| **Strong IA** | Internal links to related guides/categories |
| **Visual elements** | Tables, maps, comparisons where relevant |
| **Match intent** | Avoid generic template text; precise user intent |

## Timeline & Expectations

- **Typical time to ranking**: ~6 months
- **Reported gains**: 40%+ traffic increases from well-designed topic clusters
- **AI search**: Structured, data-rich content performs better in AI Overviews and citation layers

## Output Format

- **Template design** (Intro, Evidence, Decision, FAQ, CTA; required data fields)
- **Data requirements** (provenance, freshness, accuracy)
- **Internal linking** (hub-and-spoke, related pages)
- **Indexation strategy** (selective indexation, sitemap segmentation)
- **Checklist** for audit

## Related Skills

- **template-page-generator**: Template structure; aggregation (gallery) + detail pages; **Tier 1 product-generated** template URLs
- **landing-page-generator**: Conversion-focused programmatic pages; LP structure for campaign CTA
- **tools-page-generator**: Free tools pages; toolkit hub; programmatic tool pages; lead gen
- **alternatives-page-generator**: Alternatives/comparison pages at scale; competitor brand traffic
- **category-page-generator**, **products-page-generator**: Category / catalog grids
- **glossary-page-generator**, **faq-page-generator**, **howto-section-generator**, **comparison-table-generator**, **resources-page-generator**: Definitions, Q&A banks, HowTo step blocks, comparison matrices, content hubs
- **use-cases-page-generator**, **solutions-page-generator**, **migration-page-generator**: ICP/industry matrix, migration SEO
- **integrations-page-generator**: Integration pair pages at scale
- **blog-page-generator**, **article-page-generator**, **docs-page-generator**, **features-page-generator**, **api-page-generator**: Long-form and product surface scale
- **press-coverage-page-generator**, **customer-stories-page-generator**, **showcase-page-generator**: Proof at scale
- **startups-page-generator**, **contest-page-generator**, **download-page-generator**, **affiliate-page-generator**, **media-kit-page-generator**, **pricing-page-generator**, **services-page-generator**: Programs and offers (use selectively for pSEO)
- **content-strategy**: Content clusters, pillar pages; programmatic pages as cluster nodes
- **website-structure**: Site IA before scaling URL sets
- **url-structure**, **domain-architecture**: Paths, subfolder strategy
- **schema-markup**: Structured data (Product, Place, FAQ, ItemList)
- **internal-links**: Linking programmatic pages
- **xml-sitemap**: Sitemap segmentation for large programmatic sites
- **canonical-tag**: Duplicate/thin content handling
- **seo-strategy**, **seo-audit**: Roadmap and post-launch audits
