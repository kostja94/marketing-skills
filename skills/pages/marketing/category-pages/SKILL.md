---
name: pages-category-pages
description: When the user wants to create, optimize, or audit e-commerce category pages or listing pages. Also use when the user mentions "category page," "product category," "faceted navigation," "filter URLs," or "e-commerce listing."
metadata:
  version: 1.0.0
---

# Pages: Category Pages

Guides e-commerce category page structure, content, and SEO optimization. Category pages organize products by attributes and drive 3x more organic revenue than product pages by ranking for broad, high-volume keywords.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product catalog and site structure.

Identify:
1. **Catalog**: Product count, categories, subcategories
2. **Facets**: Filters (size, color, price, brand, etc.)
3. **URL structure**: Current hierarchy, parameter handling

## Category Structure

### Hierarchy

| Principle | Practice |
|-----------|----------|
| **Logical grouping** | General -> specific (e.g., Furniture -> Bedroom furniture -> Beds) |
| **User search intent** | Match how users search (e.g., "bedroom furniture" vs "furniture") |
| **Crawl depth** | <=4 clicks from homepage; shorter paths improve indexing |
| **Long-tail categories** | Niche categories convert better (36% vs 11.5% for broad) |

### URL Structure

- **Subfolders**: `example.com/shoes/sneakers`, `example.com/shoes/outdoor-shoes`
- **Slugs**: Descriptive, keyword-rich; lowercase; no stop words
- **Avoid**: Dates, timestamps, `/category/` prefix
- **Breadcrumbs**: Show path; help users and crawlers

## Faceted Navigation (Filters)

Filters create many URL combinations (size + color + price). Manage to avoid duplicate content and crawl waste:

| Strategy | Use |
|----------|-----|
| **Canonical** | Point all faceted URLs to base category URL |
| **robots.txt** | Block faceted URLs from indexing if needed |
| **nofollow** | Add to internal links to faceted URLs |
| **JavaScript** | Keep filters client-side; single URL for category |

## On-Page Content

### Content Requirements

- **150-300 words** unique copy; pages with this rank ~2.7x higher than product-only grids
- **Placement**: After hero/H1; FAQ block at bottom
- **Purpose**: Help users decide; answer curation, materials, recommendations
- **Avoid**: Manufacturer copy; crowding product grid

### SEO Elements

| Element | Practice |
|---------|----------|
| **H1** | One per page; primary keyword; clear purpose |
| **Title tag** | 50-60 chars; keyword; compelling for CTR |
| **Meta description** | 150-160 chars; value props (free shipping, returns) |
| **Schema** | ItemList, Product; AggregateRating if reviews; FAQ if applicable |

### Trust & Conversion

- **Reviews**: Star ratings in SERPs; 99.9% of users read reviews
- **FAQ**: Answer materials, quality, recommendations; +157% conversion when used
- **Guides**: Link to product guides; internal linking for SEO

## Technical

- **Consistent layout**: Same template across categories; predictable UX
- **Mobile**: Responsive; touch targets >=44x44px
- **Redirects**: 301 to category when product pages move; avoid breaking hierarchy

## Output Format

- **Structure** (hierarchy, URL paths)
- **Facet strategy** (canonical, nofollow, robots)
- **Content** (H1, intro copy, FAQ)
- **SEO** (metadata, schema)
- **Checklist** for audit

## Related Skills

- **pages-products**: Product cards, grid layout
- **seo-technical-canonical**: Faceted URL canonicalization
- **seo-on-page-schema**: ItemList, Product, FAQ schema
- **seo-on-page-internal-links**: Category linking
- **components-breadcrumb**: Breadcrumb trail for category hierarchy
- **seo-on-page-url-structure**: URL hierarchy
