---
name: seo-content-keyword-research
description: When the user wants to research keywords, find target keywords, or analyze search intent. Also use when the user mentions "keyword research," "target keywords," "search volume," "search intent," or "keyword difficulty."
metadata:
  version: 1.0.0
---

# SEO Content: Keyword Research

Guides keyword research for SEO: finding target keywords, assessing difficulty, and understanding search intent.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product, audience, and positioning.

Identify:
1. **Product/service**: What you offer
2. **Audience**: Who searches for it
3. **Goals**: Traffic, conversions, brand
4. **Tool access**: Ahrefs, Semrush, Google Keyword Planner, or free tools

## Keyword Research Process

### 1. Seed Keywords

- Product names, category terms, pain points
- Customer language from product context
- Competitor keywords

### 2. Expand

- Keyword tools: related keywords, questions, suggestions
- Search suggestions (Google autocomplete)
- "People also ask" and "Related searches"
- Competitor analysis

### 3. Evaluate

| Factor | Consider |
|--------|----------|
| **Search volume** | Monthly searches; balance volume vs. competition |
| **Keyword difficulty (KD)** | Ease of ranking; new sites target lower KD |
| **Search intent** | Informational, navigational, transactional |
| **Commercial value** | High-intent keywords for conversion pages |

### 4. Categorize

- **Head terms**: High volume, high competition (e.g., "SEO")
- **Long-tail**: Lower volume, lower competition (e.g., "SEO for small business 2024")
- **Question keywords**: "how to," "what is," "why" (good for content)

## Search Intent

| Intent | Content type | Example |
|--------|--------------|---------|
| **Informational** | Blog, guide, FAQ | "how to optimize sitemap" |
| **Navigational** | Brand page | "alignify login" |
| **Transactional** | Product, pricing | "best SEO tool pricing" |
| **Commercial** | Comparison, review | "SEO tools comparison" |

## Output Format

- **Keyword list** with volume, KD, intent
- **Keyword mapping** to pages/content
- **Content gaps** (keywords competitors rank for, you don't)
- **Priority** ranking for implementation

## Related Skills

- **seo-content-content-strategy**: Keywords inform content plan
- **seo-on-page-metadata**: Keywords in title, description
- **seo-on-page-heading**: Keywords in H1, H2
- **seo-off-page-link-building**: Keywords inform link targets
