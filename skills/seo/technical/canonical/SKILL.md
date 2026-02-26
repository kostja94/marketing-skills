---
name: seo-technical-canonical
description: When the user wants to configure canonical URLs, fix duplicate content, or consolidate URL signals. Also use when the user mentions "canonical," "duplicate content," "preferred URL," or "URL consolidation."
metadata:
  version: 1.0.0
---

# SEO Technical: Canonical

Guides canonical tag configuration to consolidate duplicate content and declare preferred URLs.

## Scope (Technical SEO)

- **Duplicate site versions**: Ensure only one URL version (HTTPS, www vs non-www); 301 redirect others
- **Duplicate content**: Canonical tags; consolidate and 301 to preferred URL

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for site URL and language structure.

Identify:
1. **Site URL**: Base domain
2. **Duplicate scenarios**: Multi-language, query params, pagination, alternate URLs
3. **Framework**: Next.js, React, static, etc.

## When to Use Canonical

- **Multi-language**: Each language version has its own canonical
- **Same content, multiple URLs**: Params, pagination, tracking params, www vs non-www
- **Self-referencing**: Canonical should point to self or the preferred version
- **Avoid chain canonical**: A→B→C is invalid

## Rules

| Rule | Note |
|------|------|
| **Absolute URL** | Include `https://` |
| **Consistency** | Must match current page URL or the chosen preferred version |
| **No chains** | A→B→C is invalid |

## Implementation Patterns

### Next.js (metadata)

```tsx
export const metadata = {
  alternates: {
    canonical: "https://example.com/page-slug",
    languages: {
      zh: "https://example.com/zh/page-slug",
      en: "https://example.com/page-slug",
      "x-default": "https://example.com/page-slug",
    },
  },
};
```

### HTML (generic)

```html
<link rel="canonical" href="https://example.com/page-slug" />
```

## Relationship to Other Technical SEO

- **Sitemap**: URLs in sitemap should match canonical
- **IndexNow**: Submit canonical URLs

## Output Format

- **Canonical URL** for each page type
- **Implementation** (metadata or HTML)
- **Multi-language** setup if applicable
- **References**: [Google Canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)

## Related Skills

- **seo-technical-sitemap**: Sitemap URLs should match canonical
- **seo-technical-indexnow**: Submit canonical URLs
- **seo-technical-indexing**: Resolve duplicate content in GSC
