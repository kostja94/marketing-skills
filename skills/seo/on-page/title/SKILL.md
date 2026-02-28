---
name: seo-on-page-title
description: When the user wants to optimize the title tag, page title, or SEO title. Also use when the user mentions "title tag," "page title," "SEO title," "title optimization," or "headline for search."
metadata:
  version: 1.0.0
---

# SEO On-Page: Title Tag

Guides optimization of the HTML title tag for search engines and SERP display.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (On-Page SEO)

- **Title tag**: Primary search snippet; ~55 chars; primary keyword near start; unique per page

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for brand voice and target keywords.

Identify:
1. **Page type**: Homepage, landing, blog, product, etc.
2. **Primary keyword**: Target search query
3. **Brand**: Optional brand append at end

## Best Practices

| Item | Guideline |
|------|-----------|
| **Length** | ~55 characters (Google truncates beyond that) |
| **Keyword** | Include primary keyword near the start |
| **Unique** | One unique title per page |
| **Brand** | Optional: append brand at end |
| **Clear** | Compelling; clearly describe page content |

## Output Format

- **Recommended title** (with character count)
- **Alternatives** (if A/B testing)

## GSC-Driven Optimization

For pages with low CTR despite good position, use analytics-google-search-console to identify opportunities. Compare actual CTR vs expected by position; optimize title for pages with CTR gap.

## Related Skills

- **analytics-google-search-console**: CTR analysis, identify low-CTR pages for title optimization
- **seo-on-page-description**: Meta description pairs with title in SERP
- **seo-on-page-heading**: H1 should align with title tag
- **seo-on-page-open-graph**: og:title for social sharing (often mirrors title)
- **seo-on-page-schema**: Structured data complements metadata
