---
name: seo-on-page-schema
description: When the user wants to add or optimize structured data (Schema.org, JSON-LD). Also use when the user mentions "schema," "structured data," "JSON-LD," "rich snippets," or "FAQ schema."
metadata:
  version: 1.0.0
---

# SEO On-Page: Schema / Structured Data

Guides implementation of Schema.org structured data (JSON-LD) for rich snippets and enhanced search results.

## Scope (On-Page SEO)

- **Schema markup**: Schema.org types (Recipe, Product, Article, Event, LocalBusiness, etc.) for rich results

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product type and content.

Identify:
1. **Page type**: Article, Product, FAQ, Organization, etc.
2. **Content**: What entities to describe
3. **Goal**: Rich snippets, Knowledge Panel, etc.

## Common Schema Types

| Type | Use case |
|------|----------|
| **Organization** | Site-wide, company info |
| **WebSite** | Site-wide, search action |
| **Article** | Blog posts, news |
| **Product** | E-commerce product pages |
| **FAQPage** | FAQ sections |
| **BreadcrumbList** | Breadcrumb navigation |
| **LocalBusiness** | Local business pages |

## Best Practices

| Principle | Guideline |
|-----------|-----------|
| **Accuracy** | Data must match visible page content |
| **Completeness** | Include all required properties |
| **JSON-LD** | Preferred format; place in `<script type="application/ld+json">` |
| **Validation** | Test with [Rich Results Test](https://search.google.com/test/rich-results) |

## Implementation

### Next.js (metadata)

```tsx
export const metadata = {
  other: {
    'script:ld+json': JSON.stringify({
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "...",
      "author": { "@type": "Person", "name": "..." },
      "datePublished": "2024-01-01"
    }),
  },
};
```

### HTML (generic)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "..."
}
</script>
```

## Output Format

- **Schema type** recommendation
- **JSON-LD** structure
- **Required vs. optional** properties
- **Validation** steps
- **References**: [Schema.org](https://schema.org/), [Google Structured Data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)

## Related Skills

- **seo-on-page-metadata**: Metadata complements schema
- **seo-technical-indexing**: Google Indexing API for JobPosting, BroadcastEvent
