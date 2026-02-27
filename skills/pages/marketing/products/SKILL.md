---
name: pages-products
description: When the user wants to create, optimize, or audit a product listing or category page. Also use when the user mentions "product page," "product listing," "shop," or "e-commerce products."
metadata:
  version: 1.0.0
---

# Pages: Products

Guides product listing and category page content for e-commerce. For individual product detail pages, structure varies by platform.

**When invoking**: On **first use**, if helpful, open with 1?2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product catalog and positioning.

Identify:
1. **Page type**: Category, collection, or product grid
2. **Products**: Count, filters, sorting
3. **Audience**: Browsers, researchers, buyers

## Best Practices

### Category/Listing Page

| Element | Purpose |
|---------|---------|
| **Category title** | Clear H1; target keyword |
| **Description** | SEO copy; benefits of category |
| **Filters** | Price, size, brand, etc. |
| **Product cards** | Image, name, price, CTA |
| **Pagination** | Crawlable; rel prev/next |

### Product Card

- **Image**: Alt text; multiple angles
- **Name**: Descriptive; keyword
- **Price**: Clear; sale/compare-at
- **CTA**: Add to cart, view details

### SEO

- **Category pages**: Unique titles, descriptions
- **Schema**: ItemList, Product
- **Internal links**: Cross-category; breadcrumbs

## Output Format

- **Structure** for listing page
- **Product card** elements
- **Filter/sort** approach
- **SEO** metadata and schema

## Related Skills

- **pages-features**: For SaaS feature pages
- **seo-on-page-schema**: Product, ItemList schema
- **seo-on-page-internal-links**: Category linking
