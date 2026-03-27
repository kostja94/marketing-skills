---
name: grid
description: When the user wants to design, optimize, or audit grid layouts for content display. Also use when the user mentions "grid layout," "grid design," "multi-column grid," "CSS grid," "responsive grid," "card grid," "product grid," or "feature grid." For cards layout, use card.
metadata:
  version: 1.0.1
---

# Components: Grid Layout

Guides grid layout design for equal-hierarchy, multi-column content display. Grids display multiple items with equal emphasis; space-efficient and scannable. Used for products, templates, tools, features, blog indexes, and galleries.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## When to Use Grid

| Use grid when | Use list when |
|---------------|---------------|
| Visual content (images, thumbnails) | Text-heavy; scan by title |
| Equal emphasis across items | Compact; many items; dense info |
| Products, templates, gallery, features | Blog index, docs, search results |
| Browsing, discovery | Reading, scanning |

See **list** for list layout; **card** for card structure within grid.

## Grid Structure

| Element | Purpose |
|---------|---------|
| **Columns** | 1–4+ columns; adapt to viewport |
| **Gap** | Consistent spacing between items |
| **Items** | Equal or proportional sizing |
| **Responsive** | 1 col mobile → 2–4 cols desktop |

## Implementation

- **CSS Grid**: `repeat(auto-fill, minmax(min, 1fr))` or `repeat(auto-fit, minmax())` for fluid columns
- **Breakpoints**: e.g., 1 col &lt;768px; 2 cols 768–1024px; 3–4 cols &gt;1024px
- **Consistency**: Same padding, aspect ratios across items; see **card** for card structure

## Best Practices

| Principle | Practice |
|-----------|----------|
| **Equal hierarchy** | Items compete equally; no single dominant item |
| **Consistent sizing** | Same card/item dimensions in grid |
| **Gap consistency** | Uniform gap (e.g., 16px, 24px) |
| **No layout shift** | Reserve space for images; avoid CLS |

## Responsive

- **Mobile**: Single column; full-width items
- **Tablet**: 2 columns; touch targets ≥44×44px
- **Desktop**: 3–4 columns; hover states OK

## Infinite Scroll

If using infinite scroll with grid: crawlers cannot access content loaded on scroll. Provide paginated component pages for SEO-critical content. See **site-crawlability** for search-friendly implementation.

## Related Skills

- **site-crawlability**: Infinite scroll SEO; paginated component pages
- **card**: Card structure within grid; product, template, tool cards
- **list**: List layout vs grid; when to use each
- **masonry**: Masonry for varying heights (Pinterest-style)
- **carousel**: Carousel for slides/rotation; when grid is too dense
- **hero-generator**: Hero above; grid below for content sections
- **products-page-generator**: Product grid
- **template-page-generator**: Template grid
- **features-page-generator**: Feature grid
