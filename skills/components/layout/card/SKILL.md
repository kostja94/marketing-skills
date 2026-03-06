---
name: card
description: When the user wants to design, optimize, or audit card layouts for content display. Also use when the user mentions "card layout," "card component," "card grid," "product cards," "template cards," "tool cards," "feature cards," "gallery cards," "integration cards," or "card design."
metadata:
  version: 1.1.0
---

# Components: Card Layout

Guides card layout design for scannable, responsive content display. Cards are self-contained containers that group related content; used in grids for blog posts, products, templates, tools, features, galleries, and integrations.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Card Anatomy

| Element | Purpose |
|---------|---------|
| **Container** | Border, background, shadow; consistent padding |
| **Image / Thumbnail** | Visual anchor; consistent aspect ratio (1:1, 4:3 common) |
| **Title** | Clear; keyword-rich where relevant |
| **Description / Metadata** | Supporting text; date, author, category |
| **CTA** | Action button or link; "View," "Use," "Connect," etc. |

**Principle**: One card = one topic. Keep each card focused for scannability.

## Card Types by Use Case

| Type | Typical Elements | Page Skill |
|------|------------------|------------|
| **Product card** | Image, name, price, CTA (Add to cart, View) | **products-page-generator** |
| **Template card** | Thumbnail, name, short description, "Use" or "Preview" CTA | **template-page-generator** |
| **Tool card** | Name, one-line benefit, CTA to tool page | **tools-page-generator** |
| **Feature card** | Name, benefit, optional screenshot | **features-page-generator** |
| **Gallery / Showcase item** | Thumbnail, title, creator, link | **showcase-page-generator** |
| **Integration card** | Logo, name, short description, "Connect" or "Install" | **integrations-page-generator** |
| **Blog / Article card** | Cover image, title, excerpt, date, author | **blog-page-generator**, **article-page-generator** |
| **Resource card** | Thumbnail, title, format (guide, webinar), CTA | **resources-page-generator** |

## Layout & Responsiveness

- **Grid**: CSS Grid `repeat(auto-fill, minmax())` or Flexbox; columns adapt to viewport
- **Mobile**: Single column on small screens; 2–4 columns on desktop
- **Consistency**: Same padding, spacing, and aspect ratios across cards
- **Hover**: Subtle elevation (shadow, translate-y); avoid scale that causes layout shift (CLS)

## Design Principles

| Principle | Practice |
|-----------|----------|
| **Visual hierarchy** | Title > description > CTA; clear flow |
| **Scannability** | Minimal text; benefit-led copy |
| **Consistency** | Same structure across all cards in a grid |
| **Action clarity** | One primary CTA per card; avoid choice overload |

## SEO & Schema

- **Cards themselves**: No specific schema; layout is UI
- **Content in cards**: Use appropriate schema for the page (Product, Article, ItemList, etc.); see **schema-markup**
- **Images**: Alt text on thumbnails; see **image-optimization**
- **Links**: Descriptive anchor text; internal linking; see **internal-links**

## Grid vs List vs Masonry vs Carousel

| Layout | Best for | Skill |
|--------|----------|-------|
| **Grid** | Visual content (products, templates, gallery); equal emphasis | **grid** |
| **List** | Text-heavy (blog index, docs); compact; scan by title | **list** |
| **Masonry** | Varying heights; image gallery, portfolio | **masonry** |
| **Carousel** | Limited space; testimonials, logos, featured rotation | **carousel** |

## Related Skills

- **products-page-generator**: Product cards, grid layout, category pages
- **template-page-generator**: Template cards, gallery structure
- **tools-page-generator**: Tool cards, toolkit hub
- **features-page-generator**: Feature grid/list
- **showcase-page-generator**: Gallery grid, per-item format
- **integrations-page-generator**: Catalog grid, integration cards
- **category-page-generator**: Product grid, consistent layout
- **grid**: Grid layout for card display; when to use grid
- **list**: List layout; cards in list format
- **masonry**: Masonry for varying-height cards (gallery)
- **carousel**: Carousel for card slides (testimonials, featured)
- **hero-generator**: Hero vs card—hero is single above-fold; cards are repeated units
- **brand-visual-generator**: Typography, spacing, visual consistency
- **image-optimization**: Card thumbnail optimization, alt text, LCP
