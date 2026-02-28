---
name: seo-on-page-description
description: When the user wants to optimize the meta description or meta tag description. Also use when the user mentions "meta description," "page description," "SEO description," or "snippet for search."
metadata:
  version: 1.0.0
---

# SEO On-Page: Meta Description

Guides optimization of the meta description tag for search engines and SERP display.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (On-Page SEO)

- **Meta description**: ~105 chars; CTA; unique value; target keyword; unique per page

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for brand voice and target keywords.

Identify:
1. **Page type**: Homepage, landing, blog, product, etc.
2. **Primary keyword**: Target search query
3. **CTA**: Primary action (sign up, learn more, buy, etc.)

## Best Practices

| Item | Guideline |
|------|-----------|
| **Length** | ~105 characters (truncates on mobile/desktop beyond that) |
| **Unique** | One per page |
| **CTA** | Include clear call-to-action when relevant |
| **Keyword** | Naturally include target keyword |
| **Compelling** | Encourage click; differentiate from competitors |

## Output Format

- **Recommended meta description** (with character count)
- **Alternatives** (if A/B testing)

## GSC-Driven Optimization

For pages with low CTR despite good position, use analytics-google-search-console to identify opportunities. Optimize meta description for pages with CTR gap.

## Related Skills

- **analytics-google-search-console**: CTR analysis, identify low-CTR pages for meta optimization
- **seo-on-page-title**: Title pairs with description in SERP
- **seo-on-page-heading**: H1 should align with title; description summarizes content
- **seo-on-page-open-graph**: og:description for social sharing (often mirrors or extends meta description)
- **seo-content-keyword-research**: Keywords in content inform description
