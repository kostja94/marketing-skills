---
name: programmatic-seo
description: When the user wants to create SEO pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "programmatic SEO pages," "template pages," "scale content," "location pages," "city pages," "comparison pages at scale," "X vs Y pages," "integration pages," "pages from data," "automated landing pages," or "programmatic landing pages." For user-facing template galleries or marketplaces (browse → use), use template-page-generator.
metadata:
  version: 1.1.0
---

# SEO: Programmatic SEO

Guides programmatic SEO—creating large numbers of SEO-optimized pages automatically using templates and structured data, rather than writing each page manually. Works like a mail merge for web pages: one template + data yields hundreds or thousands of unique pages targeting long-tail keyword patterns.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Definition

**Programmatic SEO** = Building a single template and populating it with data from a database, API, or spreadsheet to generate hundreds or thousands of unique pages. Each page targets a long-tail keyword (e.g., "best SEO tool in [city]," "[App A] + [App B] integration").

**Key differences from traditional SEO**: Technical (SEOs + engineers); long-tail focus; data-driven (data quality = success); automation; built for scale.

## Three-Part Framework

| Component | Role |
|-----------|------|
| **Templates** | Reusable page structures: layout, headings, internal links, content blocks; conditional logic for empty fields |
| **Data** | Structured information: locations, products, prices, features—must be accurate, complete, and add genuine value |
| **Automation** | Systems connecting data to templates; pages generated dynamically or published in bulk |

## Template Structure (Recommended)

| Section | Purpose |
|---------|---------|
| **Intro** | Introduction; matches user intent |
| **Evidence block** | Data-driven content unique to each page (tables, lists, verified stats); differentiates from thin content |
| **Decision** | Comparison, recommendation, or next steps |
| **FAQ** | Frequently asked questions |
| **CTA** | Call-to-action |

**Evidence block** = Real, structured data per page (business listings, pricing, reviews, verified stats). Ensures each page delivers genuine value, not recycled boilerplate with swapped variables.

## Data Foundation

| Requirement | Practice |
|-------------|----------|
| **Provenance** | Log data sources; track origin |
| **Freshness rules** | e.g., ratings every 90 days, prices every 30 days |
| **First-party / licensed** | Prefer over scraped content |
| **Clean & merge** | Deduplicate; ensure depth |

## Ideal Use Cases

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

- **template-page-generator**: Template structure; aggregation (gallery) + detail pages; programmatic template design; user-facing templates (CMS, design, vibe coding)
- **landing-page-generator**: Conversion-focused programmatic pages; programmatic landing pages; LP structure for template CTA
- **tools-page-generator**: Free tools pages; toolkit hub; programmatic tool pages; lead gen
- **alternatives-page-generator**: Alternatives/comparison pages at scale; competitor brand traffic
- **category-page-generator**: Category pages; template-based structure; faceted navigation
- **content-strategy**: Content clusters, pillar pages; programmatic pages as cluster nodes
- **url-structure**: URL hierarchy for programmatic pages
- **schema-markup**: Structured data (Product, Place, FAQ, ItemList)
- **faq-page-generator**: FAQ as programmatic page type; FAQPage schema; Q&A template structure
- **internal-links**: Linking programmatic pages
- **xml-sitemap**: Sitemap segmentation for large programmatic sites
- **canonical-tag**: Duplicate/thin content handling
- **seo-strategy**: SEO workflow; programmatic SEO as alternative strategy
