---
name: pages-article
description: When the user wants to create, optimize, or audit a single article/post page (not the blog index). Also use when the user mentions "article page," "blog post page," "single post," "post template," "individual article," "competitor article analysis," "optimize based on top-ranking articles," or "analyze ranking articles."
metadata:
  version: 1.0.0
---

# Pages: Article (Single Post)

Guides structure, SEO, and UX for **individual article pages** — one blog post, one guide, one piece of long-form content. Distinct from **pages-blog**, which covers the blog index/listing page.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

**Output workflow**: Always output in order: **1. Intent Analysis** → **2. Content Analysis** → **3. Recommendations**. Do not skip steps.

## Optimization Foundation: Four Inputs

Article analysis and creation rest on **four inputs**. Gather or infer them before outputting recommendations:

| Input | Purpose | Source |
|-------|---------|--------|
| **Product** | Product connection, features, use cases, CTA placement | product-marketing-context (Sections 1–4, 9–11); article content; web search |
| **Keywords** | Target keyword, primary/secondary placement | product-marketing-context Section 6; seo-content-keyword-research; article |
| **Article intent** | Informational, commercial, transactional, navigational; drives structure, CTA, SEO depth | product-marketing-context Section 6 (target intent); article orientation; content type |
| **Competitor articles** | Structure to adopt, content gaps, length target, keyword opportunities | User-provided URLs; product-marketing-context Section 11; web search |

**When any input is missing**: Proactively ask or search. For competitors, ask: *"Do you have competitor article URLs? If not, I can search for top-ranking articles for [target keyword]."* For product/keywords/intent, infer from article or prompt user to add product-marketing-context.

## Before Analysis: Gather Context

**1. Competitor articles**

- **If user provides URLs**: Use them for competitor analysis.
- **If user does not provide URLs**: Proactively ask: *"Do you have competitor article URLs to analyze? If not, I can search for top-ranking articles for [target keyword from article]."*
- **If user agrees or asks to search**: Search the web for top-ranking pages (e.g. `"[target keyword]"` or `"[keyword] site:competitor.com"`), fetch 2–3 articles via mcp_web_fetch or WebSearch, then include competitor analysis in Recommendations.

**2. Product / company context**

Use available context to give **tailored** analysis:

| Source | Use for |
|--------|---------|
| **product-marketing-context.md** | Keywords (Section 6), competitors (Section 7), content strategy (Section 11), product connection |
| **Article content** | Extract product name, features, URLs; infer target keyword and audience |
| **Web search** | When analyzing a known brand (e.g. Lessie AI): search for "[product] features", "[product] vs competitors", company positioning — use to validate product connection, suggest missing features/use cases, and improve competitor gap analysis |

If no product-marketing-context exists, infer from the article and optionally search for company/product info to enrich recommendations.

## Scope

- **Single article page**: One post, one URL (e.g. `/blog/how-to-optimize-seo`)
- **Not** the blog index, category pages, or archive pages — see **pages-blog** for those

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for topics, audience, keywords, and Section 11 (Content/Blog/Article Strategy).

Identify:
1. **Product connection**: How does this article support the product? (educate on problem, introduce features, nurture leads)
2. **Keyword basis**: Target keyword from product context or keyword research — see **seo-content-keyword-research**
3. **Content type**: Blog post, guide, tutorial, news, evergreen
4. **Length**: Short (<1,000 words), medium (1,000–2,500), long (2,500+)
5. **Intent**: Informational, commercial, problem-aware

**Product-linked content**: Articles should tie to the product (problem it solves, features, use cases). Avoid purely generic content with no product relevance. Link to product/feature pages naturally in conclusion or when context fits.

## Article Orientations

Not all articles share the same goal. Choose structure, SEO depth, and schema based on **orientation** and **primary objective**.

### Article Types by Orientation

| Orientation | Examples | Primary Goal | SEO Priority |
|-------------|----------|--------------|--------------|
| **Funding / PR** | Funding rounds, acquisitions, executive hires | Brand awareness, press, investor relations | Low — thin content, few search queries |
| **Product updates** | Feature launches, release notes, changelogs | User education, product adoption | Low–medium — internal announcements rarely rank |
| **Guides / How-to** | Tutorials, step-by-step, best practices | Education, lead nurture, authority | High — matches search intent |
| **News / Trending** | Industry news, hot topics, seasonal | Engagement, social shares, topical relevance | Medium — quick traffic spikes, short shelf life |
| **Evergreen** | Pillar guides, glossaries, comparisons | Long-term traffic, backlinks, authority | High — compounds over time |

### SEO-Driven vs Non-SEO-Driven

- **SEO-driven**: How-to guides, listicles, comparisons, pillar content. Target keywords, optimize structure, invest in GEO. Goal: organic traffic.
- **Non-SEO-driven**: Funding announcements, product updates, company news. Goal: brand, PR, existing audience. Don't expect rankings; focus on clarity, shareability, and internal linking to SEO content.
- **Hybrid**: Product launch posts can include SEO-friendly sections (e.g., "How to use [feature]" with keyword targeting) while the main goal remains announcement.

### Evergreen vs Timely Content

| Attribute | Evergreen | Timely |
|-----------|-----------|--------|
| **Relevance** | Year-round; foundational topics | Weeks to months; trends, news, seasonal |
| **Traffic** | Steady, compounds over time | Spikes then decline |
| **Examples** | "How to write a business plan," "Best SEO strategies" | Holiday guides, trending microtrends, breaking news |
| **Maintenance** | Refresh every 6–12 months; update stats | Often one-and-done; may archive or redirect |
| **Schema** | `Article` or `BlogPosting` | `NewsArticle` for time-sensitive news |

**Recommended mix**: 70/30 or 60/40 **evergreen-to-timely**. Too much evergreen = blog feels outdated; too much timely = irregular traffic, constant churn. Use timely content to link into evergreen pillar articles.

**Date display**: For timely content, `datePublished` matters more; for evergreen, prefer `dateModified` when visible (see Date Display below).

## Competitor Article Analysis

Triggered when user provides URLs or agrees to search (see **Before Analysis** above):

1. **Obtain articles**: URLs from user or product context (Section 11), or search web for `"[keyword]"` to find top-ranking pages
2. **Fetch content**: mcp_web_fetch, WebSearch, or user-provided text
3. **Analyze**: Content Analysis dimensions + word count, H2 structure, keyword placement, content gaps, CTA, schema
4. **Output**: Add to Recommendations — structure to adopt, sections to add, length target, keyword opportunities, content gaps to fill

## Article Page Structure

| Section | Purpose |
|---------|---------|
| **Hero/Header** | Title (H1), author, **single date** (see Date Display below), **reading time** (word count ÷ 200; round up), featured image, **share buttons** |
| **TL;DR or Key Takeaways** | Choose one: **TL;DR** = 50–100 word bold summary paragraph; **Key Takeaways** = 5–7 bullet points; placed after intro; supports GEO/AI citation |
| **Introduction** | 40–120 words; hook in first 1–2 sentences (pain point, stat, or question); primary keyword in first 100 words; readers decide in ~8 seconds |
| **Body** | H2–H3 hierarchy; QAE pattern (see GEO below); scannable (lists, short paragraphs 40–80 words, visuals) |
| **Conclusion** | Summary, CTA (newsletter, related content, **product** — link to product/feature when relevant) |
| **Related posts** | 3–6 contextual links; end-of-article recommendations |
| **Author bio** | E-E-A-T; credentials, photo, link to author page |

### Featured Image

The hero image displayed at the top of the article. Same image typically used for Schema, Open Graph, and Twitter Cards.

| Attribute | Guideline |
|-----------|-----------|
| **Dimensions** | 1200–1600px wide; proportional height; 1200×630px for social (og:image) |
| **File size** | Under 200 KB; compress (WebP preferred) |
| **Format** | WebP, JPEG, PNG; avoid oversized originals |
| **Alt text** | Descriptive; include keyword when natural; accessibility + Google Images |
| **File name** | Descriptive (e.g. `seo-checklist-2025.webp`); keyword when natural |
| **Relevance** | Must align with article topic; articles with relevant images get ~94% more views |
| **LCP** | Set `width` and `height` attributes to prevent CLS; use `srcset`/`sizes` for responsive |

Schema and Open Graph require the same image (min 1200px wide, absolute URL). See **seo-on-page-open-graph**, **seo-on-page-twitter-cards**.

### Social Sharing

- Add **share buttons** (X, LinkedIn, Facebook, etc.) — see **components-social-share**
- Place after intro and/or end of article; sticky sidebar for long-form
- Requires **Open Graph** and **Twitter Cards** for rich previews when shared

### GEO / AI Optimization (Generative Engine Optimization)

Optimize for AI citation (ChatGPT, Perplexity, Google AI Overviews). Content structured for GEO is cited ~35% more frequently.

| Element | Guideline |
|---------|-----------|
| **TL;DR or Key Takeaways** | Choose one: **TL;DR** = 50–100 word summary paragraph; **Key Takeaways** = 5–7 bullet points; placed after intro; supports GEO |
| **QAE pattern** | Question (H2) → Answer (2 sentences) → Evidence (data, examples, lists) |
| **Answer-first** | Direct answer in first 40–60 words after each H2 |
| **Answer blocks** | 100–200 words per section; direct answer + context + evidence + nuance |
| **Structured formats** | Lists, tables, numbered steps increase citation rate |

See **strategies-geo** for full GEO strategy.

### Paragraph Length & Content

| Element | Guideline |
|---------|-----------|
| **Paragraph length** | 2–4 sentences; 40–80 words per paragraph; avoid walls of text |
| **Break long blocks** | Use lists, subheadings (H3), images, callout boxes every 2–3 paragraphs |
| **Answer blocks** | 100–200 words per H2 section; direct answer + context + evidence |
| **Scannability** | Short sentences; one idea per paragraph; **front-load** key info (F-pattern: readers scan top, then left); **bold** key phrases for Featured Snippets |

### Long-Form (1,000+ words)

- Add **table of contents** (TOC) after intro — see **components-toc**
- Use jump links for major sections
- Break text with images, lists, definition boxes, mini-FAQs

## SEO Best Practices (2025)

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

- **Readability**: Grade 8–10 (Flesch-Kincaid); short sentences, clear language
- **Depth**: 2,500+ words for pillar content; 1,000+ for cluster articles
- **Originality**: Unique angle, data, examples; avoid thin or rehashed content
- **E-E-A-T**: Author bio, citations, changelog, expert quotes; **Experience** (first-hand, case studies, original research) strengthens trust; **YMYL** (health, finance, legal) requires higher E-E-A-T

### Common Mistakes to Avoid

- Multiple H1s; skipping heading levels (H2→H4); keyword stuffing in headings
- Neglecting conclusion or CTA; no internal links to related content
- Walls of text; generic "click here" anchors

### URL

- Clean slug: 3–5 words; primary keyword; lowercase, hyphens
- Example: `/blog/seo-checklist-2025` not `/blog/post-12345`
- Avoid date in path: `/blog/article-title` not `/blog/2025/01/15/article-title`

### Date Display (Critical for CTR)

**Google recommends**: Minimize the presence of other dates on the page. If both `datePublished` and `dateModified` are shown, Google may pick the wrong date for SERP display.

- **Search Engine Land case**: A site showing both dates saw **22% CTR drop** — Google chose the outdated date.
- **Best practice**: Show **only one date** on the page — prefer `dateModified` if it exists, otherwise `datePublished`.
- **Schema**: Keep both `datePublished` and `dateModified` in JSON-LD; the rule applies to **visible** date only.

## Schema (Article / BlogPosting / NewsArticle)

Choose the **most specific** type that matches content:

| Type | Use case |
|------|----------|
| **BlogPosting** | Informal blog posts; individual authors; regularly updated |
| **Article** | Formal, evergreen content; tool intros; encyclopedic |
| **NewsArticle** | Time-sensitive news; recognized publishers |

### Required Properties

- **headline** (max 110 chars; often = H1)
- **image** (min 1200px wide; absolute URL)
- **datePublished** (ISO 8601)
- **author** (Person or Organization)
- **publisher** (Organization with logo)

### Recommended Properties

- **dateModified** — signals freshness
- **description** — brief summary
- **mainEntityOfPage** — canonical URL

### JSON-LD Example

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "The Ultimate SEO Checklist for 2025",
  "description": "A complete guide to optimizing blog posts for search and AI.",
  "image": "https://example.com/image.jpg",
  "datePublished": "2025-01-15T09:00:00Z",
  "dateModified": "2025-02-01T14:30:00Z",
  "author": { "@type": "Person", "name": "Jane Doe", "url": "https://example.com/author/jane" },
  "publisher": { "@type": "Organization", "name": "Example", "logo": { "@type": "ImageObject", "url": "https://example.com/logo.png" } }
}
```

Place in `<head>` via `<script type="application/ld+json">`. Validate with [Rich Results Test](https://search.google.com/test/rich-results).

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
| **Anchor text** | Descriptive (e.g. "Google's Search Quality Guidelines", "Semrush study"); link to source |
| **Same URL** | Counts once per page for link equity; no need to repeat |
| **E-E-A-T** | External links to reputable sources signal trust; avoid linking to low-quality sites |

## References / Citations

| Scenario | Recommendation |
|----------|----------------|
| **Data or statistics** | Cite source inline (e.g. "According to [Semrush](url), 72% of…") or in a References section |
| **Expert quotes** | Attribute; link to source or profile |
| **Reference section** | For pillar/evergreen content with 5+ citations; list at end before Related posts |
| **Format** | Inline links preferred; numbered refs (e.g. [1], [2]) for academic-style pieces |
| **When to include** | Any claim that benefits from authority (stats, studies, definitions); strengthens E-E-A-T |

## AI-Assisted Content

When content is AI-assisted: **human review** before publish; **verify facts** and add citations; **original insights** or data; avoid generic phrasing. Google may label AI content; transparency and human refinement support E-E-A-T.

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

When auditing or optimizing an article, analyze content (beyond structure):

| Dimension | What to check |
|-----------|---------------|
| **Hook** | Intro opens with pain point, stat, or question? |
| **Keyword in first 100 words** | Primary keyword present? |
| **QAE pattern** | H2s as questions? Answer-first (40–60 words) in each section? |
| **Word count** | Matches type? (300–600 news, 1,000–2,500 cluster, 2,500+ pillar) |
| **Paragraph length** | 40–80 words per paragraph? No walls of text? |
| **Multimedia** | Images, tables, lists, stats; alt text; scannability |
| **Product connection** | Ties to product? Natural links to features/pricing? |
| **CTA** | Placement (conclusion, mid-article); clarity; product link |
| **Internal links** | 3–5 in body + 3–6 Related? Descriptive anchor text? No "click here"? |
| **Outbound links** | 2–5 external links? Authoritative sources? Descriptive anchors? |
| **References** | Data/stats cited? Reference section for 5+ citations? E-E-A-T signal? |
| **Data/evidence** | Original data, citations, examples; avoid thin content |
| **Gaps** | What do top-ranking articles cover that this misses? |

## Output Format

### 1. Intent Analysis (output first)

Before any recommendations, output a brief analysis:

| Dimension | Output |
|-----------|--------|
| **Orientation** | Funding/PR, Product update, Guide, News, Evergreen |
| **Primary goal** | Brand, PR, education, product adoption, organic traffic, … |
| **SEO vs non-SEO** | SEO-driven / Non-SEO-driven / Hybrid |
| **Evergreen vs timely** | Evergreen / Timely |
| **Implications** | 1–2 sentences: e.g. "Low SEO priority → focus on clarity, shareability" or "SEO-driven → full keyword + GEO optimization" |

### 2. Content Analysis (output second)

Apply the Content Analysis table above. Output a brief assessment per dimension (✅ / ⚠️ / ❌ + one-line note).

### 3. Recommendations (output third, tailored to intent)

Assign **priority** to each item: **P0** (critical), **P1** (high), **P2** (medium), **P3** (nice-to-have). Output as table or list with priority prefix.

| Priority | Use when |
|----------|----------|
| **P0** | Blocks GEO/SEO; missing core element (TL;DR or Key Takeaways, keyword in first 100 words, schema) |
| **P1** | Significant impact on traffic, CTR, or conversion (title length, share buttons, CTA) |
| **P2** | Improves UX or authority (related posts, author bio, internal links) |
| **P3** | Polish (image optimization, readability tweaks) |

Example: `[P0] Add TL;DR or Key Takeaways — GEO, AI citation`

- **Product connection** (how article supports product; where to link)
- **Keyword** (target from product context or keyword research)
- **Structure** for article template (hero, TL;DR or Key Takeaways, intro, body, conclusion, related, author)
- **Paragraph length** (40–80 words; break with lists, H3s; 100–200 words per H2 section)
- **Featured image** (dimensions, alt, file size, og:image alignment)
- **GEO** elements (TL;DR or Key Takeaways, QAE pattern) — *skip or minimal for non-SEO-driven*
- **SEO** checklist (title, meta, H1, keyword placement) — *skip or minimal for non-SEO-driven*
- **Schema** type and JSON-LD
- **Internal links** (3–5 in body + 3–6 Related; anchor text suggestions; avoid "click here")
- **Outbound links** (2–5 external; cite stats, research; anchor text for each)
- **References** (inline citations vs Reference section; when to add for E-E-A-T)
- **Competitor analysis** (when URLs provided or searched): content gaps vs top rankers, structure to adopt, length target, keyword opportunities — see **Before Analysis** to prompt user or search

## Related Skills

- **pages-blog**: Blog index/listing page; article pages live within blog
- **seo-content-keyword-research**: Keyword basis for articles; run before drafting
- **seo-on-page-title, seo-on-page-description**: Article metadata
- **seo-on-page-schema**: Article/BlogPosting/NewsArticle schema
- **seo-on-page-heading**: H1–H6 structure for article body
- **seo-content-optimization**: Word count, H2 keywords, keyword density, tables, lists, multimedia
- **seo-on-page-internal-links**: Related posts, contextual links
- **seo-on-page-open-graph, seo-on-page-twitter-cards**: Social previews for articles (required for share previews)
- **components-social-share**: Share buttons placement, platforms, intent URLs
- **components-toc**: Table of contents for long articles
- **components-breadcrumb**: Breadcrumb (e.g. Home > Blog > Category > Post)
- **strategies-geo**: GEO strategy; AI citation optimization
