---
name: faq-page-generator
description: When the user wants to create, optimize, or audit FAQ page content. Also use when the user mentions "FAQ page," "frequently asked questions," "help page," "Q&A page," "FAQ schema," "FAQ section," "common questions," "FAQ SEO," "accordion FAQ," "People Also Ask," "PAA," "People Also Search For," "PASF," or "FAQ rich results." For FAQ structured data markup, use schema-markup. For AI search visibility strategy, use generative-engine-optimization.
metadata:
  version: 1.2.0
---

# Pages: FAQ

Guides FAQ page content, structure, and optimization for SEO, conversion, and rich results (PAA, Featured Snippet, GEO, PASF). FAQ content from real user questions and rich-result targeting.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## FAQ and Rich Results

| Feature | Relationship | Optimization |
|---------|--------------|---------------|
| **People Also Ask (PAA)** | FAQ schema triggers PAA-style dropdowns; PAA questions = FAQ source | FAQPage schema; match question phrasing; "how/what/why" format. PAA ~51% of searches. See **serp-features** |
| **Featured Snippet** | Answers extracted for position zero | 40-60 words; answer-first; H2/H3; paragraph (70%), list (19%), table (6%). See **featured-snippet** |
| **GEO / AI Overviews** | AI cites FAQ blocks; FAQ most cited content type (3-7x more citations) | Self-contained; 40-80 words; entity signals; content in initial HTML. See **geo** |
| **People Also Search For (PASF)** | Appears when user bounces; comprehensive FAQ reduces bounce | Match intent; cover related questions. PASF shows 6-8 related queries. |
| **FAQ rich result** | FAQPage schema; max 2 dropdowns per SERP | Restricted to government/health in many regions; schema still helps PAA, voice, AI |

**PAA vs PASF**: PAA = expandable question boxes (same SERP). PASF = related queries after bounce. Both benefit from comprehensive, intent-matching content.

## Content Sources

**Real user**: Support tickets, chat logs, sales objections, surveys, reviews.

**Rich-result purpose**: PAA (search keyword, extract questions), AnswerThePublic, AlsoAsked, Featured Snippet queries, competitor FAQ, keyword research, GEO citation data.

**Reverse flow**: Use PAA, Featured Snippet, GSC Search queries to find questions you rank for but don't answer.

## Content Structure

| Approach | When | Example |
|----------|------|---------|
| **Page topic** | In-page section | 3-8 questions about that page |
| **Theme** | Dedicated page | Group by Billing, Features, Support, Compliance |
| **Logical flow** | Decision funnel | Awareness -> Consideration -> Purchase -> Support |
| **Objection handling** | Conversion | "Is it worth it?" "Can I cancel?" |

**Page-specific**: LP (objection handling); pricing (billing, plans, enterprise); alternatives (migration, comparison); category (materials, recommendations); tools (what is X, how calculated). See **landing-page-generator**, **pricing-page-generator**, **alternatives-page-generator**, **category-pages**, **tools-page-generator**.

## Dedicated FAQ Page vs In-Page FAQ Section

| Dimension | Dedicated Page | In-Page Section |
|-----------|----------------|-----------------|
| **Placement** | /faq, /help, standalone URL | Within LP, pricing, blog, product page |
| **Count** | 5-30 (5-10 optimal) | 3-8 |
| **Structure** | Categories, TOC, navigation | Inline; after main content |
| **Schema** | One FAQPage per page | Same; schema matches visible Q&A |
| **When to use** | Many questions; support/help hub; central FAQ | Objection handling; page-specific long-tail; conversion |
| **Related pages** | contact-page, docs-page, website-structure | landing-page, pricing-page, blog, alternatives, category-pages, tools-page |

**Shared rules**: Word count, content rules, format, and schema apply to both. Choose placement based on question volume and page purpose.

## Accordion: Crawlable?

**Yes.** Google indexes accordion content fully; hidden content receives full weight.

**Requirements**: Content in DOM at load (no AJAX on click); use `<details>`/`<summary>` or server-rendered HTML; first item expanded. Avoid `display: none` for primary content. See **tab-accordion**, **rendering-strategies**.

**Nuance**: Some tests suggest visible content outperforms hidden. Use accordion for secondary FAQ; keep primary Q&A visible.

## Best Practices

### Word Count

| Element | Range | Notes |
|---------|-------|------|
| **Answer** | 40-80 words | Sweet spot for AI; under 40 = incomplete; over 80 = cut off |
| **Featured Snippet** | 40-60 words | 45 words most common |
| **First sentence** | 40-50 words | Answer immediately |
| **Sentences** | 2-4 | Standalone, comprehensive |

### Content Rules

- **Genuine questions**: PAA, AnswerThePublic, support; no invented marketing questions
- **Standalone answers**: Each answer makes sense alone; AI extracts individual pairs
- **Content parity**: Schema must exactly match visible content; hidden schema = violation
- **No duplicates**: Each Q&A on one page; choose most authoritative
- **Topical focus**: FAQs match page topic
- **Inverted pyramid**: Most important first; data, numbers, actionable advice
- **Keywords**: 1-2 times naturally; no stuffing
- **Quality over quantity**: 5-10 excellent beat 50 thin
- **Update quarterly**: Add questions from emerging trends

### Format

- **Schema**: JSON-LD; one FAQPage per page
- **Answer HTML** (in schema `text`): `<a>`, `<strong>`, `<em>`, `<p>`, `<br>`, `<ol>`; use sparingly
- **Structure**: H2/H3 per question; semantic HTML; answer-first under heading
- **Validation**: Google Rich Results Test, Schema.org Validator, GSC

### Number of Questions

| Placement | Count | Notes |
|-----------|-------|------|
| **In-page section** | 3-8 | Directly related to page |
| **Dedicated page** | 5-10 optimal | 10-30 if well-crafted; quality over quantity |
| **Schema minimum** | 2+ | Single Q&A rarely shown |
| **Google display** | Max 2 per result | See **serp-features** |

### Question and Answer

**Question**: Match how users ask ("How do I return?" not "Return Policy"); target "how/what/why"; H2/H3; avoid promotional or invented.

**Answer**: Answer-first in 40-60 words; paragraph, list, or table by content type; scannable (bullets, bold); self-contained; entity signals. See **entity-seo**.

### Organization

Group by topic; clear hierarchy; TOC, accordions, jump links; audit quarterly.

## Initial Assessment

**Check project context** (`.cursor/project-context.md` or `.claude/project-context.md`) for objections, product details, customer language.

Identify: (1) Source of questions (2) Conversion focus (3) Placement (dedicated vs in-page).

## Why It Matters

- Reduces support load
- Long-tail and voice search
- Category pages: +157% conversion when FAQ used
- 20-30% CTR lift when rich results display
- 3-7x more AI citations with optimized FAQ

## Output Format

- Question list (from research)
- Category structure
- Answer format and tone
- Schema (FAQPage)
- SEO metadata

## Related Skills

- **howto-section-generator**: Step-by-step HowTo sections; not FAQ—use HowTo schema, not FAQPage
- **tab-accordion**: Accordion implementation; details/summary
- **serp-features**: PAA, Featured Snippet, PASF, FAQ limits
- **featured-snippet**: Answer length, position zero
- **geo**: GEO strategy; citable blocks; AI crawlers
- **schema-markup**: FAQPage implementation
- **keyword-research**: PAA to FAQ; question keywords
- **landing-page-generator**, **pricing-page-generator**, **alternatives-page-generator**, **category-pages**, **tools-page-generator**: In-page FAQ section
- **contact-page-generator**, **docs-page-generator**, **website-structure**: Dedicated FAQ page; FAQ reduces contact form volume
- **title-tag, meta-description, page-metadata**: Metadata
- **entity-seo**: Entity signals for GEO
- **rendering-strategies**: Content in initial HTML
