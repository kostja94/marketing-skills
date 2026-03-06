---
name: list
description: When the user wants to design, optimize, or audit list layouts for content display. Also use when the user mentions "list layout," "list design," "vertical list," "stacked list," "blog list," "article list," "documentation list," "search results layout," or "infinite scroll list."
metadata:
  version: 1.1.0
---

# Components: List Layout

Guides list layout design for linear, stacked content display. Lists are compact, text-heavy; users scan by title or metadata. Used for blog indexes, documentation, search results, and dense content.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## When to Use List

| Use list when | Use grid when |
|---------------|---------------|
| Text-heavy; scan by title | Visual content; equal emphasis |
| Many items; compact display | Fewer items; browsing |
| Blog index, docs, search results | Products, templates, gallery |
| F-pattern reading (top-left, left column) | Discovery, exploration |

See **grid** for grid layout; **card** for card structure.

## List Structure

| Element | Purpose |
|---------|---------|
| **Items** | Single column; stacked vertically |
| **Per item** | Title, optional metadata (date, author), excerpt, link |
| **Spacing** | Consistent gaps; dividers or alternating background |
| **Density** | Compact (docs) vs relaxed (blog) |

## List Variants

| Variant | Use |
|---------|-----|
| **Simple list** | Title + link; minimal (nav, TOC) |
| **Rich list** | Title, excerpt, date, author | Blog index |
| **Table-like** | Columns for metadata (date, status) | Docs, admin |
| **With thumbnail** | Small image + text | Blog with thumbnails |

## Best Practices

| Principle | Practice |
|-----------|----------|
| **Scannable** | Clear titles; consistent hierarchy |
| **Compact** | Less vertical space than grid |
| **Link area** | Full row or title clickable |
| **Metadata** | Date, author, category; secondary styling |

## F-Pattern

Users read top-left first, then scan left column. Place primary content (titles) left-aligned; metadata secondary.

## Infinite Scroll

If using infinite scroll for list (e.g., blog index, search results): crawlers cannot access content loaded on scroll. Provide paginated component pages or use traditional pagination for SEO-critical content. See **site-crawlability** for search-friendly infinite scroll implementation.

## Responsive

- **Mobile**: Single column; full-width items
- **Touch targets**: ≥44×44px for touchable rows
- **Truncation**: Long titles; ellipsis or wrap by design

## Related Skills

- **site-crawlability**: Infinite scroll SEO; paginated component pages; search-friendly implementation
- **grid**: Grid vs list; when to use each
- **carousel**: Carousel for slides; when list is too long for space
- **card**: Card in list (e.g., blog with thumbnail)
- **toc-generator**: TOC as list; jump links
- **blog-page-generator**: Blog index list
- **article-page-generator**: Article list format
- **docs-page-generator**: Documentation list
