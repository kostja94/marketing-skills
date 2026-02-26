---
name: seo-on-page-metadata
description: When the user wants to optimize meta tags, title, description, or hreflang. Also use when the user mentions "meta tags," "title tag," "meta description," or "hreflang."
metadata:
  version: 1.0.0
---

# SEO On-Page: Metadata

Guides optimization of meta tags, title, description, hreflang, Open Graph, and Twitter Card.

## Scope (On-Page SEO)

- **Title tag**: ~55 chars; primary keyword near start; clear, compelling
- **Meta description**: ~105 chars; CTA; unique value; target keyword
- **Hreflang**: Language/region targeting for multilingual sites
- **Metadata completeness**: All pages have title + meta description

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for brand voice and target keywords.

Identify:
1. **Page type**: Homepage, landing, blog, product, etc.
2. **Primary keyword**: Target search query
3. **Multi-language**: zh, en, x-default if applicable

## Best Practices

### Title Tag

| Item | Guideline |
|------|-----------|
| **Length** | ~55 characters (Google truncates beyond that) |
| **Keyword** | Include primary keyword near the start |
| **Unique** | One unique title per page |
| **Brand** | Optional: append brand at end |

### Meta Description

| Item | Guideline |
|------|-----------|
| **Length** | ~105 characters (truncates on mobile/desktop beyond that) |
| **Unique** | One per page |
| **CTA** | Include clear call-to-action when relevant |
| **Keyword** | Naturally include target keyword |

### hreflang (Multi-language)

- Use `alternates.languages` in Next.js metadata
- Include `x-default` for default language
- Each language version should reference all others
- **References**: [Google hreflang](https://developers.google.com/search/docs/specialty/international/localized-versions)

## Output Format

- **Recommended title** (with character count)
- **Recommended meta description** (with character count)
- **hreflang** setup if multi-language

## Related Skills

- **seo-technical-canonical**: Canonical + hreflang for multi-language
- **seo-on-page-schema**: Structured data complements metadata
- **seo-on-page-heading**: H1 should align with title
