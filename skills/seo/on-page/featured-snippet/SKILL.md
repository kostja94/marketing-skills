---
name: featured-snippet
description: When the user wants to optimize for Featured Snippets, Position Zero, or snippet extraction. Also use when the user mentions "featured snippet," "position zero," "snippet optimization," "answer box," "definition box," "list snippet," "table snippet," "paragraph snippet," "PAA optimization," or "win position zero."
metadata:
  version: 1.0.0
---

# SEO On-Page: Featured Snippet

Guides optimization for Featured Snippets (Position Zero)—direct answers displayed above organic results. Featured snippets appear on ~19% of queries; by 2025, AI Overviews replaced many, but snippet optimization still supports AI citation and PAA. See **serp-features** for full SERP context.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Featured Snippet formats**: Paragraph, list, table
- **Content structure**: Answer-first, H2/H3, semantic HTML
- **Query targeting**: How, what, why; positions 2–5 opportunity
- **AI Overviews**: Layered content for both snippets and AI citation

## Current Landscape (2025–2026)

- Featured snippets appear on ~19% of search queries
- AI Overviews replaced 83%+ of featured snippets in many regions; appear in ~47% of US searches
- When AI Overviews show, 83% of searches may end without clicks (**zero-click**)—goal shifts to **citation** as well as CTR. Featured Snippets also cause zero-click when the answer suffices. See **serp-features** for zero-click by feature.
- Position zero still captures ~35% of clicks when snippets appear; pages with snippets see ~8% higher organic CTR
- Optimize for **both** traditional snippets and AI Overviews

### Featured Snippet vs AI Overview

**Not the same.** Featured snippets pull a direct passage from a single webpage. AI Overviews generate multi-source summaries using AI. When both appear, featured snippets still occupy a highly visible spot. Not every query triggers AI Overview—snippet optimization remains valuable. [Semrush](https://www.semrush.com/blog/featured-snippets/)

## Snippet Formats & Share

| Format | Share | Use | Optimization |
|--------|-------|-----|---------------|
| **Paragraph** | ~70% | Definition, "what is," "why" | 40–60 words; direct answer after H2 |
| **List** | ~19% | How-to, steps, options | `<ol>` or `<ul>`; semantic HTML |
| **Table** | ~6% | Comparisons, stats, specs | Clear headers; target keywords in column/row headers |
| **Video** | Rare | Visual how-to | Video schema; timestamps/chapters; see **video-optimization** |

**45 words** is the most common paragraph length. Answer-first format is critical. On mobile, featured snippets can occupy ~50% of the screen, pushing competitors below the fold. [Semrush](https://www.semrush.com/blog/featured-snippets/)

## Content Structure

### Answer-First Approach

- **Place direct answer** in first 1–2 sentences (40–60 words) before any other content
- **H2/H3**: Use clear headings; Google extracts from content under headings
- **Semantic HTML**: `<ol>`, `<ul>`, `<table>`, `<p>`—avoid divs styled as lists
- **Inverted pyramid**: Answer immediately (for snippet/AI), then add nuance/data that earns clicks
- **Objective tone**: Write like a dictionary entry—avoid personal opinions and emotional language; supports E-A-T

### HTML Structure

| Element | Use |
|---------|-----|
| **H2/H3** | Question or topic; Google recognizes and extracts; **list snippets can be compiled from headings** across the page—Google pulls H2s and converts to list items |
| **`<ol>`** | Steps, rankings, sequences; list snippets |
| **`<ul>`** | Non-sequential items; bullet snippets |
| **`<table>`** | Comparisons, specs; table snippets; clean rows/columns; H2/H3 intro; target keywords in heading and surrounding content; ensure data is relevant and scannable |
| **First paragraph** | 40–60 words; direct answer |

**Annotations matter**: Search engines use semantic labeling to identify relevant blocks ("Fraggles") and extract passages. Structure pages clearly—headings, lists, tables—so crawlers can annotate and pull the right content. Annotations can suggest relationships between blocks, enabling engines to stitch text from multiple parts. [SEJ / Bing](https://www.searchenginejournal.com/how-bing-q-and-a-featured-snippet-algorithm-works/362716/)

### Visual Elements

- Optimized images near answers can **double CTR** by capturing thumbnail slots
- **Alt text, captions, file names** support Image Pack and snippet thumbnails. See **image-optimization** for captions and full image SEO; **serp-features** for Image Pack context.

## Query Targeting

| Factor | Guidance |
|--------|-----------|
| **Query types** | "How," "what," "why" questions; definitional queries |
| **Long-tail** | Featured snippets typically appear for long-tail (specific) queries; short-tail is broad and less likely |
| **Ranking position** | Target positions 2–5; snippet ownership often comes from these (not always #1). **Prerequisite**: Must rank in top ~20 blue links to be considered; Q&A runs through top organic results |
| **Q&A memory** | Bing (and likely Google) memorize results; you may retain snippet even if blue link ranking drops—once earned, you don't necessarily need to maintain position |
| **Intent** | Informational; match user intent precisely |
| **Tools** | PAA (excellent for low-volume, snippet-triggering queries), AnswerThePublic, AlsoAsked, Semrush Keyword Magic Tool (SERP features filter: "Featured snippet") |

### How the Algorithm Works (Bing/Google)

- **Foundation**: Core algorithm ranks blue links; Q&A/Featured Snippet is a modular layer on top—same ranking foundation
- **Process**: 1) Take top blue link results; 2) Extract or create summary; 3) Identify implicit question each document answers; 4) Match user's question to best implicit question; 5) Feature that answer
- **E-A-T**: Snippets are E-A-T–based (Bing: "Relevancy" = accuracy/expertise). Correctness first—conforms to accepted opinion, document quality. Then authority and trust (document, author, publisher). See **eeat-signals** for E-E-A-T implementation.
- **Meta descriptions**: Do not affect ranking; engines generate descriptions on the fly. Over-optimized or missing meta descriptions lead engines to extract their own—structure helps them choose well. [SEJ](https://www.searchenginejournal.com/how-bing-q-and-a-featured-snippet-algorithm-works/362716/)

## GEO / AI Overviews

- **Layered content**: Clear definitions, lists, steps—AI can cite and summarize
- **Self-contained blocks**: Each answer readable alone; supports AI extraction
- **Schema**: FAQPage, HowTo, Article—helps machines understand structure
- See **generative-engine-optimization** for full GEO strategy

## Finding Opportunities

- **Manual**: Search target keyword; note if snippet appears and format (paragraph/list/table/video)
- **PAA**: People Also Ask questions often trigger snippets; use as H2 or dedicated page
- **Tools**: Semrush Keyword Magic Tool—filter by "Featured snippet" in SERP features; "Open SERP" to view current snippet
- **Best opportunities**: Keywords where you already rank on page 1 (positions 1–10)

## Monitoring

- **Google Search Console**: Identify snippet opportunities; track performance
- **Position Tracking** (e.g. Semrush): "Featured Snippets" tab—"Already featured" vs "Opportunities"
- **Rich Results Test**: Validate schema; ensure extraction eligibility
- **CTR benchmarks**: Snippets ~114% CTR increase vs position #1; adjust expectations when AI Overviews dominate

## Output Format

- **Target queries** (snippet-worthy)
- **Format** (paragraph/list/table) per query
- **Content structure** (H2, answer length, semantic HTML)
- **Schema** if applicable (FAQ, HowTo)

## Related Skills

- **serp-features**: SERP features overview; Featured Snippet in context
- **content-optimization**: H2 keywords, tables, lists; defers snippet-specific structure to this skill
- **faq-page-generator**: FAQ format and answer length; FAQ schema for PAA
- **schema-markup**: FAQPage, HowTo for rich results
- **heading-structure**: H2–H3 hierarchy
- **generative-engine-optimization**: AI citation; GEO strategy
- **eeat-signals**: E-E-A-T implementation; authority, trust, author
- **image-optimization**: Image SEO for snippet thumbnails; alt, captions, file names; captions support snippet context
- **video-optimization**: Video snippet format; VideoObject; timestamps/chapters

## References

- [How the Bing Q&A / Featured Snippet Algorithm Works](https://www.searchenginejournal.com/how-bing-q-and-a-featured-snippet-algorithm-works/362716/) (SEJ)—Bing algorithm, annotations, E-A-T, Q&A memory
- [Featured Snippets: What They Are & How to Earn Them](https://www.semrush.com/blog/featured-snippets/) (Semrush)—formats, optimization, PAA, tools
