---
name: article-page-generator
description: When the user wants to create, optimize, or audit a single article/post page (not the blog index). Also use when the user mentions "article page," "blog post page," "single post," "post template," "article structure," "post optimization," "competitor article analysis," "optimize based on top-ranking articles," "analyze ranking articles," "optimize article for SEO," or "article schema." For writing article body content (intro, body, conclusion), use article-content.
metadata:
  version: 1.2.0
---

# Pages: Article (Single Post)

Guides **structure, SEO, and UX** for individual article pages — layout, metadata, schema, technical. For **article body content** (intro, body, conclusion, writing), see **article-content**. Distinct from **blog-page-generator**, which covers the blog index/listing page.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

**Output workflow**: Always output in order: **0. Research Phase** (keywords, search intent, competitors) → **1. Intent Analysis** → **2. Content Analysis** → **3. Recommendations**. Do not skip steps. When Research Phase was performed via web search, show the search results and findings.

## Optimization Foundation: Four Inputs

Article analysis and creation rest on **four inputs**. Gather or infer them before outputting recommendations:

| Input | Purpose | Source |
|-------|---------|--------|
| **Product** | Product connection, features, use cases, CTA placement | project-context (Sections 1–4, 9–11); article content; web search |
| **Keywords** | Target keyword, primary/secondary placement | project-context Section 6; keyword-research; article |
| **Article intent** | Informational, commercial, transactional, navigational; drives structure, CTA, SEO depth | project-context Section 6 (target intent); article orientation; content type |
| **Competitor articles** | Structure to adopt, content gaps, length target, keyword opportunities | User-provided URLs; project-context Section 11; web search |

**When any input is missing**: Proactively ask or search. For article analysis: perform **Research Phase** (keyword search, search intent, competitor articles) by default — see Research Phase section. For product/keywords/intent, infer from article or prompt user to add project-context.

## Before Analysis: Gather Context

**1. Product / company context**

Use available context to give **tailored** analysis:

| Source | Use for |
|--------|---------|
| **project-context.md** | Keywords (Section 6), competitors (Section 7), content strategy (Section 11), product connection |
| **Article content** | Extract product name, features, URLs; infer target keyword and audience |
| **Web search** | When analyzing a known brand: search for "[product] features", "[product] vs competitors", company positioning — use to validate product connection, suggest missing features/use cases, and improve competitor gap analysis |

If no project-context exists, infer from the article and optionally search for company/product info to enrich recommendations.

## Research Phase: Keyword, Search Intent, Competitor (Required for Article Analysis)

**Lightweight** research for article analysis. When **analyzing or auditing** an article, perform searches and **output the results** in Section 0. Skip only if user explicitly asks to skip (e.g. "skip search").

- **Keyword**: Extract from article (title, H1, H2s, first 100 words); search for opportunities — see **keyword-research** (extract from article method)
- **Search intent**: Informational / Commercial / Transactional / Navigational — see **keyword-research** Search Intent
- **Competitor articles**: Fetch 2–3 top-ranking pages; analyze structure, gaps, length target — see **competitor-research** (Competitor Article Fetch Workflow)

**Output format**: See Output Format Section 0 below.

## Scope

- **Single article page**: One post, one URL (e.g. `/blog/how-to-optimize-seo`)
- **Not** the blog index, category pages, or archive pages — see **blog-page-generator** for those

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for topics, audience, keywords, and Section 11 (Content/Blog/Article Strategy).

Identify:
1. **Product connection**: How does this article support the product? (educate on problem, introduce features, nurture leads)
2. **Keyword basis**: Target keyword from product context or keyword research — see **keyword-research**
3. **Content type**: Blog post, guide, tutorial, news, evergreen
4. **Length**: Short (<1,000 words), medium (1,000–2,500), long (2,500+)
5. **Intent**: Informational, commercial, problem-aware

**Product-linked content**: Articles should tie to the product (problem it solves, features, use cases). Avoid purely generic content with no product relevance. Link to product/feature pages naturally in conclusion or when context fits.

## Article Orientations

Choose structure, SEO depth, and schema based on **orientation**. See **content-marketing** for full Article Orientations (Funding/PR, Product update, Guide, News, Evergreen), SEO-driven vs non-SEO-driven, Evergreen vs Timely.

**Intent Analysis output**: Orientation, primary goal, SEO vs non-SEO, Evergreen vs timely — see Output Format Section 1.

## Article Page Structure

| Section | Purpose |
|---------|---------|
| **Hero/Header** | Title (H1), author, **single date** (see **schema-markup** Date display for CTR), **reading time** (word count ÷ 200; round up), featured image, **share buttons** |
| **TL;DR or Key Takeaways** | See **article-content** for content; placed after intro; supports GEO/AI citation |
| **Introduction** | See **article-content** for hook, length, keyword placement |
| **Body** | See **article-content** for QAE, paragraph length, scannability |
| **Conclusion** | See **article-content** for summary, CTA, product connection |
| **Related posts** | 3–6 contextual links; end-of-article recommendations |
| **Author bio** | E-E-A-T; credentials, photo, link to author page — see **eeat-signals** |

### Featured Image

See **image-optimization** (Article / Blog hero). Same image for Schema, Open Graph, Twitter Cards; min 1200px wide, absolute URL. See **open-graph**, **twitter-cards**.

### Social Sharing

- Add **share buttons** (X, LinkedIn, Facebook, etc.) — see **social-share-generator**
- Place after intro and/or end of article; sticky sidebar for long-form
- Requires **Open Graph** and **Twitter Cards** for rich previews when shared

### GEO / AI Optimization

See **article-content** for TL;DR, Key Takeaways, QAE pattern, answer-first; **generative-engine-optimization** for full GEO strategy.

### Long-Form (1,000+ words)

- Add **table of contents** (TOC) after intro — see **toc-generator**
- Use jump links for major sections
- Break text with images, lists, definition boxes, mini-FAQs

## SEO Best Practices

### Title & Meta

| Element | Guideline |
|---------|-----------|
| **Title** | 55 chars; primary keyword near start; power words |
| **Meta description** | 150–160 chars; CTA; primary keyword |
| **H1** | One per page; matches title; primary keyword naturally |

### Keyword Placement

- **Title**: 1× primary keyword
- **First 100 words**: 1× primary keyword
- **Body**: 2–3× naturally; avoid stuffing
- **At least one H2**: Include primary or related keyword

### Content Quality

See **article-content** for readability, depth, originality, word count by type. **E-E-A-T**: Author bio, citations, changelog, expert quotes — see **eeat-signals**.

### Common Mistakes to Avoid

- Multiple H1s; skipping heading levels (H2→H4); keyword stuffing in headings
- Neglecting conclusion or CTA; no internal links to related content
- Walls of text; generic "click here" anchors

### URL

Use **url-slug-generator** for slug creation. Key rules:

- **Slug**: 3–5 words; under 60 chars; primary keyword; lowercase, hyphens
- **Example**: `/blog/ai-people-search` not `/blog/ai-search-engine-finding-people-speed-discovery-outreach`
- **Avoid**: Date in path (`/blog/2025/01/15/article-title`); copy-pasting full title

### Date Display

See **schema-markup** (Date display for CTR): show only one visible date; prefer dateModified.

## Schema & Open Graph

See **schema-markup** for Article/BlogPosting/NewsArticle type selection, required properties, JSON-LD example, and date display. Validate with [Rich Results Test](https://search.google.com/test/rich-results).

## Open Graph for Articles

Use `og:type: article` for article pages (not `website`):

```html
<meta property="og:type" content="article">
<meta property="og:article:published_time" content="2025-01-15T09:00:00Z">
<meta property="og:article:modified_time" content="2025-02-01T14:30:00Z">
<meta property="og:article:author" content="https://example.com/author/jane">
```

## Internal Linking

| Element | Guideline |
|---------|-----------|
| **Volume** | 3–5 contextual links in body + 3–6 in Related posts = 6–11 total per article |
| **First paragraph** | 1 link to pillar or key related content |
| **Body** | 2–4 contextual links; one per major section when relevant |
| **Related posts** | 3–6 end-of-article links; same topic cluster |
| **Anchor text** | Descriptive (e.g. "SEO checklist for 2025", "how to optimize meta tags"); avoid "click here", "learn more", "read more" |
| **Variation** | Mix exact-match, partial-match, branded anchors; avoid over-optimization |
| **Orphan prevention** | Every article has ≥1 internal link from hub/pillar or nav |

## Outbound Links (External)

| Element | Guideline |
|---------|-----------|
| **Volume** | 2–5 external links per article; cite authoritative sources |
| **When to use** | Statistics, research, definitions, tool comparisons, expert quotes |
| **Anchor text** | Descriptive (e.g. "Google's Search Quality Guidelines", "SEO study"); link to source |
| **Same URL** | Counts once per page for link equity; no need to repeat |
| **E-E-A-T** | External links to reputable sources signal trust — see **eeat-signals** |

## References / Citations

See **article-content** for citation format; **eeat-signals** for E-E-A-T and when to include.

## AI-Assisted Content

See **article-content** for AI-assisted content guidance; **eeat-signals** for E-E-A-T.

## Technical

- **Core Web Vitals**: LCP < 1.0s on mobile
- **Images**: WebP, compressed; descriptive alt text; keyword in filename when natural
- **IndexNow**: For fast indexing of new posts
- **Canonical**: Self-referencing canonical on article page

## Post-Publication

- **Refresh**: Update every 6–12 months; refresh stats, add insights
- **Internal links**: Add links from older posts to new articles
- **Monitor**: GSC indexing, rankings, Core Web Vitals

## Content Analysis

When auditing or optimizing an article, apply the Content Audit Checklist. See **article-content** for full dimensions.

## Output Format

### 0. Research Phase (output first, when analysis/audit is performed)

When analyzing or auditing an article, output this section **before** Intent Analysis. Include search sources and findings. If user asked to skip search, note that and infer from article only.

| Section | Output |
|--------|--------|
| **Keyword Search** | Primary keyword (from article or search), secondary keywords, keyword opportunities (from SERP/competitor analysis). If search was performed: query used, top results observed. |
| **Search Intent** | Intent for primary keyword (Informational/Commercial/Transactional/Navigational), intent for 2–3 secondary keywords, whether article content matches intent. If search was performed: SERP snippet types observed. |
| **Competitor Articles** | If searched: 2–3 URLs, brief structure (word count, H2s), content gaps, length target. If user provided URLs: same. See **competitor-research** for full methodology. If skipped: "Competitor analysis skipped." |

### 1. Intent Analysis (output second)

Before any recommendations, output a brief analysis:

| Dimension | Output |
|-----------|--------|
| **Orientation** | Funding/PR, Product update, Guide, News, Evergreen |
| **Primary goal** | Brand, PR, education, product adoption, organic traffic, … |
| **SEO vs non-SEO** | SEO-driven / Non-SEO-driven / Hybrid |
| **Evergreen vs timely** | Evergreen / Timely |
| **Implications** | 1–2 sentences: e.g. "Low SEO priority → focus on clarity, shareability" or "SEO-driven → full keyword + GEO optimization" |

### 2. Content Analysis (output third)

Apply the Content Analysis table above. Output a brief assessment per dimension (✅ / ⚠️ / ❌ + one-line note).

### 3. Recommendations (output fourth, tailored to intent)

Assign **priority** to each item: **P0** (critical), **P1** (high), **P2** (medium), **P3** (nice-to-have). Output as table or list with priority prefix.

| Priority | Use when |
|----------|----------|
| **P0** | Blocks GEO/SEO; missing core element (TL;DR or Key Takeaways, keyword in first 100 words, schema) |
| **P1** | Significant impact on traffic, CTR, or conversion (title length, share buttons, CTA) |
| **P2** | Improves UX or authority (related posts, author bio, internal links) |
| **P3** | Polish (image optimization, readability tweaks) |

Example: `[P0] Add TL;DR or Key Takeaways — GEO, AI citation`

- **Product connection** (how article supports product; where to link) — see **article-content**
- **Keyword** (target from product context or keyword research)
- **Structure** for article template (hero, TL;DR or Key Takeaways, intro, body, conclusion, related, author) — content creation: **article-content**
- **Featured image** (dimensions, alt, file size, og:image alignment)
- **GEO** elements (TL;DR or Key Takeaways, QAE pattern) — *skip or minimal for non-SEO-driven*
- **SEO** checklist (title, meta, H1, keyword placement) — *skip or minimal for non-SEO-driven*
- **Schema** type and JSON-LD
- **Internal links** (3–5 in body + 3–6 Related; anchor text suggestions; avoid "click here")
- **Outbound links** (2–5 external; cite stats, research; anchor text for each)
- **References** (inline citations vs Reference section; when to add for E-E-A-T)
- **Competitor analysis** (when URLs provided or searched): content gaps vs top rankers, structure to adopt, length target, keyword opportunities — see **competitor-research** for methodology; **Before Analysis** to prompt user or search

## Related Skills

- **article-content**: Article body creation; intro, body, conclusion; writing frameworks; Content Audit Checklist
- **eeat-signals**: E-E-A-T; author bio, citations, YMYL
- **competitor-research**: Content gaps, structure, length target
- **blog-page-generator**: Blog index/listing; article pages live within blog
- **keyword-research**: Keyword basis for articles
- **schema-markup**: Article/BlogPosting/NewsArticle schema
- **heading-structure**: H1–H6 structure for article body
- **content-optimization**: H2 keywords, tables, lists, multimedia; word count for articles → **article-content**
- **image-optimization**: Article hero/featured image specs
- **internal-links**: Related posts, contextual links
- **open-graph, twitter-cards**: Social previews for articles
- **generative-engine-optimization**: GEO strategy; AI citation optimization
