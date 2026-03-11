---
name: carousel
description: When the user wants to design, optimize, or audit carousel/slider layouts for content display. Also use when the user mentions "carousel," "slider," "carousel layout," "testimonial carousel," "gallery carousel," "quote carousel," "image slider," or "carousel accessibility."
metadata:
  version: 1.0.0
---

# Components: Carousel Layout

Guides carousel (slider) layout design for sequential content display. Carousels show one or few items at a time; users swipe or click to advance. Best when space is limited and multiple items need rotation—testimonials, quotes, logos, gallery highlights.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## When to Use Carousel

| Use carousel when | Use grid/list when |
|-------------------|---------------------|
| **Limited space** | Full catalog visible |
| One focus at a time; rotation desired | Browse, compare many items |
| Testimonials, quotes, logos, featured gallery | Products, templates, blog index |
| Above fold; hero or section highlight | Full listing; discovery |

See **grid** for equal-hierarchy display; **list** for text-heavy scan; **masonry** for varying-height gallery.

## Carousel vs Grid vs List vs Masonry

| Layout | Structure | Best for |
|--------|-----------|----------|
| **Grid** | Equal rows and columns; all visible | Products, templates, features |
| **List** | Single column; stacked | Blog index, docs, search results |
| **Masonry** | Columns; varying heights | Pinterest-style gallery |
| **Carousel** | Slides; one/few visible; swipe/click | Testimonials, logos, featured items |

## Best Practices

### Accessibility

- **Keyboard navigation**: Arrow keys to move; Enter/Space to activate; focus visible
- **User control**: Don't auto-advance too fast; allow pause; avoid auto-advance if `prefers-reduced-motion` is set
- **Announcements**: Screen reader users need to know current slide and total (e.g., "Slide 2 of 5")
- **Touch targets**: ≥44×44px for prev/next buttons on mobile

### Performance

- **Lazy load**: Load off-screen slides on demand; avoid loading all images upfront
- **Reserve space**: Reserve space for slides to avoid layout shift (CLS)

### SEO

- **Content in DOM**: All carousel content must be in the initial HTML at page load. Google does not simulate clicks; content loaded via AJAX on slide change is not discoverable. Same as **tab-accordion**.
- **Recommendation**: Server-render all slides in HTML; use CSS/JS only to show/hide. See **rendering-strategies**.

## Use Cases

| Use case | Format | Page Skill |
|----------|--------|------------|
| **Testimonials** | Quote carousel; multiple testimonials | **testimonials-generator** |
| **Showcase / Gallery** | Featured items; rotation | **showcase-page-generator** |
| **Press logos** | "As Seen In" logo strip or quote carousel | **press-coverage-page-generator** |
| **Community** | Banner carousel below hero | **community-forum** |

## Related Skills

- **grid**: Grid for full catalog; when carousel is too restrictive
- **list**: List for text-heavy scan
- **masonry**: Masonry for varying-height gallery
- **card**: Card structure within carousel slides
- **testimonials-generator**: Testimonial carousel; testimonials as content
- **showcase-page-generator**: Gallery format options (grid, masonry, carousel)
- **tab-accordion**: Similar SEO requirement—content in DOM at load
- **rendering-strategies**: SSR, SSG; content in initial HTML for crawlers
