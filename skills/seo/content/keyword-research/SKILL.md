---
name: keyword-research
description: When the user wants to research keywords, find target keywords, or analyze search intent. Also use when the user mentions "keyword research," "keyword tool," "target keywords," "search volume," "search intent," "keyword difficulty," "topical map," "keyword clustering," "People Also Ask," "Google autocomplete," "autocomplete keywords," or "alphabet method."
metadata:
  version: 1.3.0
---

# SEO Content: Keyword Research

Guides keyword research for SEO: finding target keywords, assessing difficulty, understanding search intent, and building topical maps. ~95% of keywords get fewer than 10 searches/month; low-volume, high-intent terms often yield faster rankings and conversion.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, audience, and positioning.

Identify:
1. **Product/service**: What you offer
2. **Audience**: Who searches for it
3. **Goals**: Traffic, conversions, brand
4. **Tool access**: Google Keyword Planner, Google Trends, or SEO tools

## Discovery Methods

### Base Discovery

| Method | Purpose |
|--------|---------|
| **User perspective** | What pain points? What would they search? Customer language from product context |
| **Tool expansion** | Related keywords, questions, suggestions; Google autocomplete, PAA, Related Searches |
| **Competitor reverse** | Analyze competitor titles, H1, URL; identify topics they rank for; find gaps (#4–10 = opportunity) — see **competitor-research** |
| **Google PAA** | People Also Ask and Related Searches; high-value signals from real user behavior |
| **Extract from article** | When auditing existing content: extract seed keywords from title, H1, H2s, meta keywords, first 100 words; then search `"[primary keyword]"` or `"[primary keyword] related keywords"` for opportunities; use `"[primary keyword]" site:competitor.com` if competitors known |

### Google Autocomplete (Long-Tail Discovery)

Google autocomplete reflects real user searches; suggestions only appear if queries have actual traffic. Free; often uncovers low-volume long-tail that keyword tools miss. ~70% of search traffic is long-tail; lower competition, higher conversion.

**Alphabet method** (seed + space + letter):
- Type seed keyword + space + each letter: `keyword a`, `keyword b`, ... `keyword z`
- Record relevant suggestions; repeat with numbers 0-9
- Example: `SEO a` -> "SEO audit," "SEO agency"; `SEO b` -> "SEO basics," "SEO best practices"

**Position variants** (seed in different positions):
- **Prefix**: `a keyword`, `b keyword` (discover what users add before)
- **Suffix**: `keyword a`, `keyword b` (most common; alphabet method)
- **Middle**: `how to keyword a`, `best keyword for` (question + modifier combos)

**Question modifiers**:
- `how to keyword`, `what is keyword`, `why keyword`, `when to keyword`, `keyword vs`
- `keyword for beginners`, `keyword for small business`, `keyword without`

**Why it works**: Keyword tools filter low-volume terms; autocomplete only shows queries with real traffic. Use with PAA and Related Searches for full coverage. Categorize results by intent (informational, commercial, transactional).

### Incremental Discovery

- **User feedback**: Support, community, reviews, NPS—high-frequency questions = unmet search demand
- **Multi-platform search**: Reddit, Quora, X (Twitter), Hacker News—real questions and discussions

## Search Intent

| Intent | Content type | Example |
|--------|--------------|---------|
| **Informational** | Blog, guide, FAQ | "how to optimize sitemap" |
| **Navigational** | Brand page | "alignify login" |
| **Commercial** | Comparison, review | "SEO tools comparison" |
| **Transactional** | Product, pricing | "best SEO tool pricing" |

### Intent Identification

**Modifier words** (often signal intent):

| Intent | Modifiers |
|--------|-----------|
| Informational | "how," "what," "why," "guide," "tutorial" |
| Commercial | "best," "compare," "vs," "review," "top" |
| Transactional | "buy," "price," "cheap," "coupon," "free shipping" |
| Local | Location names |

**SERP check**: Search the term—knowledge cards/Wiki → informational; product lists/reviews → commercial; brand sites → navigational. Broader terms often show mixed SERP. See **serp-features** for feature types.

## Long-Tail Expansion

- **Google Autocomplete**: Alphabet method, position variants, question modifiers; see above. Primary source for long-tail.
- **Intent modifiers**: Core + "how," "best," "vs," "compare," "price"
- **Question words**: "how to," "what is," "why," "when"
- **Functional modifiers**: Core + "-er/-or" (e.g., "image optimizer" for tool-type queries); often higher conversion
- **Clustering**: Group by SERP overlap (same top pages), semantic similarity, or intent.

## Keyword Clustering & Topical Map

| Method | Use |
|--------|-----|
| **SERP overlap** | Keywords with overlapping top-ranking pages → same cluster |
| **Semantic** | Group by meaning, LSI, related concepts |
| **Intent-based** | Group by intent; separate pages if intent differs within cluster |

**Pillar–cluster** (map keywords to structure):
- **Pillar** (Hub): Broad topic page; links to clusters
- **Cluster** (Spoke): Focused subtopic; links back to pillar
- Target long-tail first; then pillar. Interlink clusters within topic.
- See **content-strategy** for full pillar-cluster planning and implementation.

## Evaluate & Screen

| Factor | Consider |
|--------|----------|
| **Search volume** | Monthly searches; ~100+/month typical floor; niche can relax |
| **Keyword difficulty (KD)** | New sites target lower KD |
| **CPC** | Higher CPC often = stronger commercial intent |
| **SERP features** | Featured Snippet, PAA, zero-click; SERP features can satisfy intent without click—affects real traffic; see **serp-features** (Zero-Click section), **featured-snippet** |
| **Screening order** | 1) Remove irrelevant 2) Filter very low volume 3) Assess achievability 4) Prioritize commercial/transactional |

## Product Positioning Test (SEO Fit)

Test if positioning is clear enough for search:

- **XXX + Function words**: Generator, Creator, Maker, Builder, Changer, Shortener, Scraper, Converter, Downloader, Translator, Extender, Summarizer, Resizer, Remover, Extractor, Recorder, Rewriter, Solver, Calculator; or Platform, Tool, Software, App, Provider, Assistant, Copilot
- **Input + to + Output**: e.g., "image to video," "text to speech"—clear input/output signals intent

**Agent/Copilot products**: Pure native Agent hard to grow via SEO; users rarely search "agent." Release related features first (e.g., CRM, sales bot for sales agent) to build traffic, then funnel to Agent product.

## Principles

- **Core rule**: Someone must search it—validate with tools; avoid inventing terms
- **Functional keywords**: Tool-type (-er/-or) often convert better; users are closer to action
- **Multi-language**: Re-research in target language; don't translate existing lists. See **translation** for translation workflow.

## SEO–PPC Keyword Synergy

Keyword research serves both SEO and Google Ads. Align both channels to avoid duplication, cannibalization, and wasted spend.

| Data flow | Use |
|-----------|-----|
| **keyword-research → google-ads** | Keyword list, clusters, intent; support terms (login, forum, pricing) → negative keywords for PPC |
| **google-ads → keyword-research** | PPC conversion rate, Search Terms report → SEO priority; high-converting PPC terms = worth ranking organically |
| **keyword-research → landing-page** | Clusters → dedicated LP per intent; PAA questions → FAQ sections |
| **GSC organic rank 4+** | If you rank well organically, consider reducing/pausing PPC on those terms to avoid cannibalization |

**PPC data for SEO priority**: `SEO ROI ≈ (Organic clicks × PPC conversion rate × Customer value) − SEO cost`. Use PPC conversion data to validate which keywords to pursue in organic.

**Reference**: [Backlinko – SEO and PPC: 8 Smart Ways to Align](https://backlinko.com/seo-and-ppc)

## Data Sources

| Source | Use |
|--------|-----|
| **Ahrefs** | Keywords Explorer, Site Explorer |
| **SEMrush** | Keyword Overview, Organic Research |
| **GSC** | Search queries, impressions, clicks |
| **GA** | Traffic by landing page |
| **PostHog** | Feature/search usage |

## Report Workflow

1. **Parse** — Read Excel/CSV, infer keyword, volume, KD, intent, etc. from headers
2. **Enrich** — Web search, visit competitor/product pages; read `project-context.md` if present
3. **Build** — Structure data for report
4. **Generate** — Output report in chosen format

## Output Format

- **Keyword list** with volume, KD, intent
- **Keyword mapping** to pages/content
- **Content gaps** (competitors rank, you don't)
- **Priority** ranking for implementation
- **Topical map** (cluster → pillar → page mapping)

### Report Structure Reference

| Section | Content |
|---------|---------|
| Executive Summary | Priorities (top 3) |
| Keyword Overview | Total keywords, primary intent, avg KD, content gaps count |
| Keyword List | Keyword, volume, KD, intent, priority, target page |
| Keyword Mapping | Page/URL, target keywords, status |
| Content Gaps | Keywords competitors rank for that you don't |
| Action Plan | Priority, action, impact, effort |
| Appendix | Search intent reference (Informational, Commercial, Transactional, Navigational) |

## Related Skills

- **seo-strategy**: SEO workflow, Product-Led SEO, audit approach; keyword research is Content phase
- **google-ads**: Keywords inform Search targeting; PPC data feeds back into SEO priority
- **paid-ads-strategy**: When to use paid vs organic; channel selection
- **content-strategy**: Keywords inform content plan; topic clusters
- **content-optimization**: Keyword placement, density vs stuffing, H2 keywords
- **title-tag, meta-description**: Keywords in title, description
- **heading-structure**: Keywords in H1, H2
- **link-building**: Keywords inform link targets
- **serp-features**: SERP features in keyword screening; PAA, Featured Snippet
- **featured-snippet**: Snippet-worthy query targeting
- **competitor-research**: Competitor keyword/topic analysis; reverse engineering
- **faq-page-generator**: PAA questions to FAQ sections; question-based keyword to FAQ content
