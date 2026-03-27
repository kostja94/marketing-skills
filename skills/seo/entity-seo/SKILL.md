---
name: entity-seo
description: When the user wants to optimize for entity recognition, Knowledge Graph, or entity-based SEO. Also use when the user mentions "entity SEO," "entity optimization," "Knowledge Graph," "Knowledge Panel," "entity signals," "brand entity," "entity linking," "entity relationships," or "entity-first content." For structured data, use schema-markup.
metadata:
  version: 1.0.1
---

# SEO: Entity SEO

Guides entity-based SEO—making your brand, product, and authors recognizable as distinct entities in search engines' knowledge systems. Google moved from keyword-matching to meaning-based understanding (Hummingbird, RankBrain, BERT, MUM); entity understanding is central to how search processes queries. Content structured around entities can receive ~3.2× more visibility in AI-powered search. References: [Semrush](https://www.semrush.com/blog/entity-based-seo-strategy/), [Search Engine Land](https://searchengineland.com/guide/entity-first-content-optimization).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Entity definition**: Singular, unique, well-defined things (person, place, organization, product, event)
- **Entity vs keyword**: Entities = underlying concepts; keywords = text strings
- **Knowledge Graph**: Google's entity database; powers disambiguation and related concepts
- **Implementation**: Schema (Organization, Person); entity signals in content; consistency across platforms

## What Is an Entity?

An **entity** is a thing or concept that is singular, unique, well-defined, and distinguishable—e.g. person, place, organization, product, event. Entities have:

| Attribute | Meaning |
|----------|---------|
| **Unique identity** | "Apple Inc." ≠ "apple (fruit)" despite same word |
| **Attributes** | Founding date, location, industry |
| **Relationships** | Connections to other entities (e.g. Apple Inc. → Steve Jobs, iPhone) |

**Entity SEO** = optimizing so search engines can identify, categorize, and connect your brand/product/author within the knowledge graph. Keywords are ambiguous; entities maintain consistent meaning across contexts.

## Why Entity SEO Matters

- **Search evolution**: Google uses entities to understand intent, not just match phrases
- **Knowledge Graph**: Billions of entities and relationships; disambiguation, related concepts
- **AI search**: Entity-optimized content ~3.2× more visible in AI results
- **E-E-A-T**: Entity signals support Experience, Expertise, Authoritativeness, Trust. See **eeat-signals**
- **GEO**: AI Overviews, Copilot, Perplexity cite entities; clear identity improves citation. See **generative-engine-optimization**

## Entity Signals (Content Best Practices)

| Practice | Purpose |
|----------|---------|
| **Clear brand/product name** | Consistent naming; avoid confusion with similar entities |
| **Author identity** | Person schema; author bio; link to author page |
| **Organization identity** | Organization schema site-wide; logo, sameAs |
| **Citable paragraphs** | Each block understandable on its own; supports AI extraction |
| **Consistency** | Same name, description, logo across website, social, directories |

## Schema for Entity SEO

### Organization

- **Placement**: **Minimum**—homepage; **Optimal**—root layout / global component (layout.tsx, _document, global header) so it appears on every page. Do **not** confine to About page; About uses AboutPage schema. See **schema-markup** for full placement table.
- **Required**: `@id`, `name`, `url`; add `logo`, `sameAs` (social, Wikidata)
- **Optional**: `description`, `address`, `contactPoint`; use most specific type (LocalBusiness, SoftwareApplication, etc.) when applicable

**@id**: Use stable URL (e.g. `https://example.com/#organization`) for entity linking across pages. Link Organization ↔ WebSite on homepage for sitelinks searchbox.

### Person

- **Use**: Author pages; Article author; team members
- **Properties**: `name`, `url`; `affiliation` (Organization); `sameAs` (LinkedIn, Twitter)
- **@id**: Enables entity linking; e.g. `https://example.com/author/jane/#person`

See **schema-markup** for full VideoObject, Article, Product, etc.; Organization and Person are core for entity SEO.

## Knowledge Panel & Knowledge Card

| Feature | Description | Obtainability |
|---------|-------------|---------------|
| **Knowledge Panel** | Entity info (brand, person, place) in SERP | WikiData, partnerships; most sites cannot directly obtain |
| **Knowledge Card** | Top-of-SERP semantic answer | Same as Knowledge Panel |

**Actions** (limited control):
- **Claim**: Google Business Profile; suggest updates when available
- **Consistency**: Same brand name, description, logo across all platforms
- **Entity Home**: Authoritative About page as primary reference
- **WikiData / Wikipedia**: Can support Knowledge Panel generation

See **serp-features** for Knowledge Panel in SERP context; **multi-domain-brand-seo** for Hub-Spoke entity consistency.

## Entity & Multi-Domain / Brand

When using multiple domains (Hub-Spoke):
- **Consistency**: Same brand name, description, logo across Hub and Spoke
- **Entity Home**: Authoritative About page on Hub as primary reference
- **Schema**: Organization with subOrganization for related entities
- **Entity confusion**: Avoid legacy brands, sub-brands, directories diluting brand perception

See **multi-domain-brand-seo** for full strategy.

## GEO & AI Citation

Entity signals strengthen GEO citation:
- **Direct-answer format** + **entity signals** = clearer AI extraction
- **Citable paragraphs** with clear brand/product/author identity
- **Distribution**: Website, YouTube, forums, Reddit—consistent entity identity across platforms

See **generative-engine-optimization** for full GEO strategy.

## Output Format

- **Entity audit** (brand, product, author identity gaps)
- **Schema** (Organization, Person; @id placement)
- **Consistency** checklist (name, logo, description across touchpoints)
- **Knowledge Panel** (claim if eligible; suggest updates)

## Related Skills

- **schema-markup**: Organization, Person; @id for entity linking
- **eeat-signals**: E-E-A-T; author bio; Person schema
- **generative-engine-optimization**: GEO; entity signals for AI citation
- **serp-features**: Knowledge Panel, Knowledge Card; SERP context
- **multi-domain-brand-seo**: Entity & Knowledge Panel; Hub-Spoke consistency
- **about-page-generator**: Entity Home; authoritative brand reference
