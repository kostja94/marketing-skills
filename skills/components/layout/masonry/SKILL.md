---
name: masonry
description: When the user wants to design, optimize, or audit masonry (Pinterest-style) layouts for content display. Also use when the user mentions "masonry layout," "masonry grid," "Pinterest layout," "waterfall layout," "brick layout," "varying height grid," "gallery layout," or "masonry SEO."
metadata:
  version: 1.1.0
---

# Components: Masonry Layout

Guides masonry layout design for content with varying heights. Masonry stacks items in columns without distinct rows; items fill gaps like a brick wall. Best for image galleries, portfolios, and discovery-focused platforms.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## When to Use Masonry

| Use masonry when | Use grid when |
|------------------|---------------|
| **Varying heights** | Equal-height items |
| Image-heavy; varied aspect ratios | Products, templates (consistent) |
| Gallery, portfolio, showcase | Card grid |
| Discovery, browsing; visual-first | Structured browsing |

See **grid** for equal-height grid; **card** for card structure.

## Masonry vs Grid vs Bento vs Carousel

| Layout | Structure | Best for |
|--------|-----------|----------|
| **Grid** | Equal rows and columns; uniform items | Products, templates, features |
| **Masonry** | Columns; items stack without rows; gaps filled | Pinterest, Behance; varied content |
| **Bento** | Intentional sections; predefined sizes | Homepage, dashboard; Apple-style |
| **Carousel** | Slides; one/few visible; swipe/click | Testimonials, logos, featured items; see **carousel** |

## Masonry Structure

| Element | Purpose |
|---------|---------|
| **Columns** | 2–4 columns; fluid or fixed |
| **Items** | Varying heights; natural aspect ratio |
| **Gap** | Consistent horizontal and vertical spacing |
| **Order** | Top-to-bottom fill within columns |

## Implementation

- **CSS columns**: `column-count`; simple, no JS; but items flow top-to-bottom then next column
- **Masonry.js / libraries**: True masonry (left-to-right fill); may need JS
- **CSS Grid + `grid-auto-flow: dense`**: Approximate; no JS; see **grid** for dense grid

**Note**: Pure masonry can create accessibility challenges (screen reader order); ensure logical DOM order.

## SEO Considerations

**Masonry + infinite scroll = content not crawlable.** Masonry galleries often use infinite scroll or lazy load; crawlers cannot emulate scroll or "Load more" clicks, so content beyond the initial view is not discoverable.

| If you use | Then |
|------------|------|
| **Infinite scroll** | Provide paginated component pages with full URLs; implement pushState; see **site-crawlability** for search-friendly infinite scroll |
| **Lazy load** | Ensure content exists in HTML or is reachable via crawlable links |
| **Pagination** | Prefer for SEO-critical content; crawlers can follow next/prev links |

**Reference**: [Google – Infinite scroll search-friendly recommendations](https://developers.google.com/search/blog/2014/02/infinite-scroll-search-friendly)

## Best Practices

| Principle | Practice |
|-----------|----------|
| **Visual-first** | Thumbnails; minimal text |
| **Aspect ratio** | Preserve original; avoid forced cropping |
| **Lazy load** | Many images; load on scroll |
| **Performance** | Masonry can be heavy; consider grid for simpler cases |

## Use Cases

| Use case | Format | Page Skill |
|----------|--------|------------|
| **Showcase / Gallery** | User work; varied sizes | **showcase-page-generator** |
| **Portfolio** | Projects; mixed media | — |
| **Pinterest-style** | Pins; discovery | — |
| **Image-heavy blog** | Blog with varied images | **blog-page-generator** |

## Related Skills

- **site-crawlability**: Infinite scroll SEO; paginated component pages; search-friendly implementation
- **grid**: Equal-height grid; when masonry is overkill
- **carousel**: Carousel for slides/rotation; when masonry is overkill
- **card**: Card structure; masonry often uses cards
- **showcase-page-generator**: Gallery masonry
- **image-optimization**: Lazy load, aspect ratio, LCP
