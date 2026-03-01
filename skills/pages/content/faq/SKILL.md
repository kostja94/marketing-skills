---
name: faq-page-generator
description: When the user wants to create, optimize, or audit FAQ page content. Also use when the user mentions "FAQ page," "frequently asked questions," "help page," "Q&A page," "FAQ schema," "FAQ section," "common questions," "FAQ SEO," or "accordion FAQ."
metadata:
  version: 1.0.0
---

# Pages: FAQ

Guides FAQ page content, structure, and optimization for SEO and conversion.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for objections, product details, and customer language.

Identify:
1. **Source of questions**: Support tickets, sales, chat, surveys
2. **Conversion focus**: Objection-handling, decision-support
3. **Placement**: Dedicated page, in-page sections, or both

## Best Practices

### Word Count & Answer Length

| Context | Recommended | Notes |
|---------|-------------|-------|
| **Featured Snippet (paragraph)** | 40–60 words | 45 words most common; ~70% of snippets are paragraphs; see **featured-snippet** |
| **First sentence** | 40–50 words | Answer immediately; Google pulls from first lines |
| **Full answer** | 40–100 words | GEO: keep under 100 words per answer for AI citation |
| **Complex questions** | Flexible | Prioritize clarity over rigid count; some need more |

**Principle**: Start with direct answer in 40–60 words; add brief context. Quality and completeness matter more than strict length.

### Number of Questions

| Placement | Count | Notes |
|-----------|-------|-------|
| **FAQ section** (in-page) | 3–8 | Small set; directly related to page topic; catches long-tail |
| **Dedicated FAQ page** | 5–30 | 10–30 genuine questions; group by category |
| **Schema minimum** | 2+ | Single Q&A technically valid but rarely shown |
| **Schema per page** | 5–8 optimal | Balance value vs. dilution; quality over quantity |
| **Google display** | Max 2 per result | Google shows max 2 FAQ dropdowns per SERP snippet (since 2021); see **serp-features** |

**Note**: FAQ rich results are now restricted to well-known government/health sites in many regions. Schema still helps AI Overviews, PAA, and voice search.

### Question Best Practices

- **Source**: Support tickets, chat logs, sales objections, PAA, AnswerThePublic, Semrush
- **Phrasing**: Match how users ask—"How do I return an item?" not "Return Policy"
- **Intent**: Target "how," "what," "why" queries; align with search intent
- **Structure**: Use H2/H3 for each question; helps extraction
- **Avoid**: Promotional, irrelevant, or invented questions
- **Conversion**: Address objections; move toward purchase or next step

### Answer Best Practices

- **Answer-first**: Place direct answer in first 1–2 sentences (40–60 words)
- **Format**: Paragraph (70%), list (19%), table (6%)—choose by content type
- **Scannable**: Bullets, numbered lists, bold for key terms
- **Self-contained**: Each answer readable alone (GEO: AI cites discrete blocks)
- **Conversational**: Human-friendly; no jargon
- **Complete**: No need for follow-up to understand
- **Entity signals**: Clear brand/product names for GEO citation

### Organization

- **Categories**: Group by topic (Billing, Features, Support, Compliance)
- **Hierarchy**: Clear sections, logical order
- **Navigation**: Table of contents, accordions, jump links, search bar
- **Maintenance**: Audit quarterly; rewrite underperforming answers

### SEO & GEO

- **Keywords**: Natural inclusion in Q&A
- **Title/meta**: Optimized for FAQ queries
- **Schema**: FAQPage JSON-LD; validate with Rich Results Test
- **Schema = visible**: Markup must match on-page content exactly
- **GEO**: Atomic answer blocks; definitions, lists, stats; under 100 words per answer

### Why It Matters

- Reduces support load
- Targets long-tail and voice search
- Can convert 2×+ higher than standard content
- Builds trust; creates featured snippet opportunities; see **featured-snippet**, **serp-features**
- FAQ schema supports AI Overviews, PAA, voice search even when rich results don't display (20–30% CTR lift when they do)

## Output Format

- **Question list** (from research)
- **Category** structure
- **Answer** format and tone
- **Schema** (FAQPage)
- **SEO** metadata

## Related Skills

- **landing-page-generator**: FAQ section for LP objection handling (step 4); reuse conversion Q&A
- **pricing-page-generator**: FAQ often addresses pricing objections
- **contact-page-generator**: FAQ reduces contact form volume
- **schema-markup**: FAQPage schema
- **title-tag, meta-description, page-metadata**: FAQ page metadata
- **generative-engine-optimization**: GEO for AI citation; FAQ content structure for ChatGPT, Perplexity, AI Overviews
- **featured-snippet**: Featured Snippet optimization; answer length, formats
- **serp-features**: SERP features; PAA, FAQ display limits
