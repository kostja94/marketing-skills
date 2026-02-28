---
name: breadcrumb-generator
description: When the user wants to add, optimize, or audit breadcrumb navigation. Also use when the user mentions "breadcrumbs," "breadcrumb trail," "path navigation," "BreadcrumbList schema," "location-based breadcrumb," "attribute-based breadcrumb," or "site hierarchy display."
metadata:
  version: 1.0.0
---

# Components: Breadcrumb Navigation

Guides breadcrumb implementation for SEO, UX, and GEO. Breadcrumbs show users their location in the site hierarchy and help search engines understand content taxonomy. Well-implemented breadcrumbs can increase CTR by 20–30%, reduce bounce rates by up to 30%, and strengthen internal linking.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Breadcrumb UI**: Visual trail (Home > Category > Page)
- **BreadcrumbList schema**: JSON-LD structured data for rich results
- **Placement**: Typically below header, above main content

## Breadcrumb Types

| Type | Use case | Recommendation |
|------|----------|----------------|
| **Location-based** | Reflects site hierarchy (Home > Blog > SEO > Page) | **Recommended** — most SEO-friendly; clear structure |
| **Attribute-based** | Shows product attributes (Home > Electronics > Phone > iPhone 15) | E-commerce; product classification |
| **Path-based** | Shows user's browsing path | **Avoid** — different users, different paths; can cause confusion |

**Default**: Use location-based for most sites. Use attribute-based for e-commerce product pages.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for site structure and key pages.

Identify:
1. **Site structure**: Hierarchy depth (e.g., Home > Category > Subcategory > Product)
2. **Page types**: Blog, e-commerce, docs, etc.
3. **Multi-category**: Products in multiple categories—need canonical path

## Best Practices

### Structure & Hierarchy

| Practice | Guideline |
|----------|-----------|
| **Depth** | 3–5 levels optimal; avoid very long trails |
| **Anchor text** | Keyword-rich, human-readable; descriptive |
| **Consistency** | Same pattern across all pages (blog, category, product) |
| **Canonical path** | For items in multiple categories, define one canonical breadcrumb to avoid diluted link equity |

### Schema (BreadcrumbList)

| Requirement | Guideline |
|--------------|-----------|
| **Format** | JSON-LD in `<script type="application/ld+json">` |
| **URLs** | Absolute URLs with https:// for each item |
| **Position** | Sequential integers starting from 1 |
| **Match** | Schema must match visible breadcrumbs exactly |
| **Order** | ItemListOrderAscending (position 1 first) |

### Placement & Design

| Practice | Guideline |
|----------|-----------|
| **Position** | Below nav bar or above page title; top of content area |
| **Visual** | Smaller font, lighter color; avoid competing with main content |
| **Separator** | Clear separator (>, /, ›); consistent across site |
| **Naming** | Match page title or nav menu; concise, descriptive |

### UX & Accessibility

| Practice | Guideline |
|----------|-----------|
| **Mobile** | Tappable; short, readable text; high contrast |
| **Long trails** | Horizontal scroll container rather than truncating |
| **Current page** | Last item non-linked; use `aria-current="page"` |
| **Screen readers** | `nav` with `aria-label="Breadcrumb"`; proper landmark |

### SEO Impact

- **Internal linking**: Breadcrumbs distribute link equity
- **Crawlability**: Helps crawlers understand taxonomy
- **GEO**: BreadcrumbList appears frequently on pages cited by Google AI Mode
- **Note**: Google removed visual breadcrumbs from mobile SERPs (Jan 2025) to save space, but schema and algorithmic value remain important for crawlers and AI

## Implementation

### Semantic HTML

```html
<nav aria-label="Breadcrumb">
  <ol itemscope itemtype="https://schema.org/BreadcrumbList">
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="https://example.com/"><span itemprop="name">Home</span></a>
      <meta itemprop="position" content="1" />
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="https://example.com/category/"><span itemprop="name">Category</span></a>
      <meta itemprop="position" content="2" />
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" aria-current="page">
      <span itemprop="name">Current Page</span>
      <meta itemprop="position" content="3" />
    </li>
  </ol>
</nav>
```

### BreadcrumbList JSON-LD

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Category",
      "item": "https://example.com/category/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Current Page",
      "item": "https://example.com/category/current-page/"
    }
  ]
}
</script>
```

### Next.js (dynamic)

Generate BreadcrumbList from route segments or page metadata. Ensure `item` URLs are absolute. Use `next-seo` BreadcrumbJsonLd or custom component.

### Multiple Breadcrumb Paths

When a page is reachable via multiple paths (e.g., product in multiple categories), Google supports **multiple BreadcrumbList** on the same page. Use an array of BreadcrumbList objects; define a canonical path to avoid diluted link equity when possible.

```html
<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [ /* path A */ ]
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [ /* path B */ ]
  }
]
</script>
```

## When to Use Breadcrumbs

| Site type | Use case |
|-----------|----------|
| **E-commerce** | Category > Subcategory > Product |
| **Blog** | Home > Blog > Category > Post (see **article-page-generator** for article page structure) |
| **Docs** | Home > Docs > Section > Page |
| **Large sites** | Any site with 3+ level hierarchy |

**Skip** on flat sites (e.g., single-page, 1–2 level depth).

**Deep pages**: For 6+ levels, consider omitting middle levels; show only the most important categories to avoid clutter.

## Platform Notes

| Platform | Options |
|----------|---------|
| **WordPress** | Yoast SEO, Rank Math, Breadcrumb NavXT |
| **Next.js** | next-seo BreadcrumbJsonLd, custom from route segments |
| **Shopify, Drupal, Joomla** | Built-in or plugin support |

## Common Errors

| Error | Fix |
|-------|-----|
| Relative URLs in schema | Use absolute URLs (https://) |
| Schema doesn't match visible trail | Keep schema and UI in sync |
| Missing position | Include sequential position (1, 2, 3…) |
| Last item linked | Current page typically not a link |
| Too many levels | Limit to 5–7; omit middle levels for deep paths |
| Inaccurate path | Breadcrumb must reflect actual site structure |
| No schema | Add BreadcrumbList; otherwise no SERP breadcrumbs |

## Output Format

- **Structure** recommendation (levels, labels)
- **BreadcrumbList** JSON-LD (with absolute URLs)
- **HTML** structure (semantic, accessible)
- **Placement** (below header, above main)
- **Validation**: [Rich Results Test](https://search.google.com/test/rich-results), [Schema Markup Validator](https://validator.schema.org/), Search Console enhanced report

## Related Skills

- **article-page-generator**: Article pages use breadcrumbs (Home > Blog > Category > Post)
- **schema-markup**: BreadcrumbList is a core schema type
- **navigation-menu-generator**: Header nav; breadcrumbs complement primary nav
- **internal-links**: Breadcrumbs are internal links; distribute link equity
- **site-crawlability**: Breadcrumbs help crawlers understand structure
- **category-page-generator**: Category hierarchy in breadcrumbs
- **products-page-generator**: Product pages often need breadcrumbs (Category > Product)
