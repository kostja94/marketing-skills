---
name: content-optimization
description: When the user wants to optimize content for SEO—word count, H2 keywords, keyword density, multimedia, tables, lists. Also use when the user mentions "content length," "word count," "keyword stuffing," "H2 keywords," "keyword density," "tables," "bullet points," or "content structure."
metadata:
  version: 1.2.0
---

# SEO Content: Content Optimization

Guides on-page content optimization: word count, heading keywords, keyword density vs stuffing, multimedia, tables, and lists. Complements **heading-structure** (structure) and **content-strategy** (planning).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Word count**: For articles, see **article-content** (word count by type). This skill covers generic content length strategy.
- **H2 keywords**: Placement, quantity, variation
- **Keyword density vs stuffing**: Natural use; avoid manipulation
- **Multimedia**: Images, tables, lists, video for structure and Featured Snippets. See **featured-snippet** for snippet-specific optimization; **video-optimization** for video SEO.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for target keywords and content type.

Identify:
1. **Content type**: Article, guide, listicle, pillar, news
2. **Target keyword**: Primary and secondary
3. **Competitors**: Top 10 average length and structure — see **competitor-research**

---

## Word Count

**Google does not rank by word count.** Length should match search intent and topic depth. A 1,000-word post that satisfies intent can outrank a 3,000-word thin piece.

### Reference Ranges by Content Type

For **article** word count by type (news, how-to, listicle, pillar, etc.), see **article-content**. Generic ranges:

| Content type | Word count | Notes |
|--------------|-------------|-------|
| **News / announcements** | 300–600 | Time-sensitive; concise |
| **Standard articles / how-tos** | 1,000–1,500 | Single topic; actionable |
| **Listicles / guides** | 1,200–2,000 | "Top 10," "Best X" |
| **Pillar / cornerstone** | 2,000–3,500+ | Comprehensive; cluster hub |

### Strategy

1. **Analyze top 10** for target keyword — average length and depth
2. **Match intent** — informational often needs ~40% longer than transactional
3. **Value over padding** — each section must add genuine value; avoid fluff
4. **Comprehensive coverage** — answer the query and related questions

---

## H2 Heading Keywords

### Placement

- **Primary keyword**: Include naturally in at least one H2 when relevant
- **Related keywords**: Use LSI and long-tail in other H2s for topical coverage
- **Avoid stuffing**: Headings must stay clear and readable; organic placement only

### Quantity

- **No strict limit** — one H2 per major section; structure follows content
- **Typical article**: 4–8 H2s; pillar: 8–15+ H2s
- **Hierarchy**: H1 → H2 (major sections) → H3 (subsections); don't skip levels

### Best Practices

| Practice | Purpose |
|----------|---------|
| **Descriptive H2s** | Search engines understand context; users scan |
| **Answer-first** | Place direct answer in first 40–50 words after H2 for Featured Snippets; see **featured-snippet** |
| **Keyword variation** | Use related terms; avoid repeating exact phrase in every H2 |
| **Logical flow** | H2s outline the article; support topical authority |

---

## Keyword Density vs Keyword Stuffing

### Definitions

| Term | Meaning |
|------|---------|
| **Keyword density** | (Keyword count / Total words) × 100; a metric, not a ranking factor |
| **Keyword stuffing** | Excessive, unnatural repetition to manipulate rankings; black-hat |

### Current Guidance

- **Keyword density is not a direct ranking factor** — Google has stated since 2011 that repetition alone doesn't improve rankings
- **Reference range**: 0.5%–1.5% for most content; some sources cite up to 2.5%
- **Use density mainly to avoid stuffing** — if density exceeds ~2–3% and reads unnaturally, reduce
- **Prioritize natural placement**: title, H1, first 100 words, 1–2 H2s, body; avoid forced repetition

### How to Avoid Stuffing

- Write for users first; keywords should fit naturally
- Use synonyms, related terms, and question phrasing
- If a sentence sounds awkward with the keyword, rewrite
- Monitor: if every paragraph repeats the exact phrase, simplify

---

## Multimedia: Images, Tables, Lists

### Images

| Practice | Purpose |
|----------|---------|
| **Alt, file names, captions** | See **image-optimization** for full image SEO (alt, format, responsive, lazy loading, image sitemap, LCP, captions for Featured Snippets) |
| **Original over stock** | Unique images signal E-E-A-T — see **eeat-signals** |

**Content placement**: Put images near relevant text; captions support snippet thumbnails. See **image-optimization** for captions; **featured-snippet** for snippet context.

### Video

| Practice | Purpose |
|----------|---------|
| **Embed + metadata** | VideoObject schema, video sitemap, thumbnail; see **video-optimization** |
| **YouTube** | Google prioritizes YouTube in search; GEO citation; see **youtube-seo**, **generative-engine-optimization** |
| **Featured Snippet (video)** | Video schema; timestamps/chapters; see **featured-snippet** |

### Tables

- **Use for**: Comparisons, stats, specs, "X vs Y"
- **Semantic HTML**: `<table>`, `<thead>`, `<tbody>`, clear column headers
- **Featured Snippets**: ~6% of snippets are tables; optimize headers with target keywords. See **featured-snippet**
- **Mobile**: Responsive; avoid horizontal scroll when possible
- **Data quality**: No empty cells; consistent units; accurate, current data

### Lists: Ordered vs Unordered

| Type | Use case | SEO / Snippet |
|------|----------|---------------|
| **Ordered (`<ol>`)** | Steps, rankings, sequences, "Top 10" | List snippets (~19% of Featured Snippets); how-to; see **featured-snippet** |
| **Unordered (`<ul>`)** | Non-sequential items, features, options | Bullet snippets; definitions, options |

**Best practices**:
- Use semantic `<ol>` and `<ul>`; avoid divs styled as lists
- **Answer-first**: For snippet targets, put the direct answer in the first 40–50 words after the heading
- **Concise items**: List items should be scannable; expand in body if needed
- **Logical order**: Ordered lists = sequence matters; unordered = no sequence

### GEO / AI Citation

**Answer-first** (direct answer in first 40–60 words after H2) supports both Featured Snippets and GEO. For article-level GEO (TL;DR, Key Takeaways, QAE pattern), see **article-content** and **generative-engine-optimization**. For Featured Snippet formats and optimization, see **featured-snippet**.

---

## Content Audit Checklist

For **article** content audit (hook, QAE, product connection, CTA, references, gaps), see **article-content**. This skill covers generic content optimization (H2 keywords, multimedia, keyword density).

---

## Output Format

- **Word count** recommendation by content type
- **H2 outline** with keyword placement
- **Keyword density** check (avoid stuffing)
- **Structure** (tables, lists) for Featured Snippet opportunity; see **featured-snippet**
- **Multimedia** checklist (images per **image-optimization**; tables, lists)

## Related Skills

- **heading-structure**: H1–H6 hierarchy; H2 keyword placement
- **content-strategy**: Topic clusters, pillar + cluster
- **keyword-research**: Target keywords inform placement
- **featured-snippet**: Snippet formats, structure; answer-first
- **eeat-signals**: E-E-A-T; original images, trust
- **image-optimization**: Alt, captions, format, LCP, responsive, image sitemap
- **video-optimization**: Video SEO; VideoObject; video sitemap
- **competitor-research**: Competitor length and structure as reference
- **article-content**: Article word count by type; Content Audit Checklist; article body creation
