---
name: components-toc
description: When the user wants to add, optimize, or audit table of contents (TOC) for long-form content. Also use when the user mentions "TOC," "table of contents," "jump links," "content outline," or "article navigation."
metadata:
  version: 1.0.0
---

# Components: Table of Contents (TOC)

Guides TOC implementation for long-form articles, guides, and whitepapers. TOCs improve UX and SEO by enabling quick navigation and reducing bounce rates.

**When invoking**: On **first use**, if helpful, open with 1?2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for content structure.

Identify:
1. **Content type**: Blog article, guide, whitepaper, documentation
2. **Length**: TOC most valuable for 1000+ word content
3. **Platform**: Web, mobile, both

## Placement Strategies

| Placement | Best For | Pros | Cons |
|-----------|----------|------|------|
| **After intro** | Most articles | Natural flow; visible early | Can scroll out of view |
| **Floating sidebar** | Very long content | Always visible | More complex; mobile challenges |
| **Collapsible** | Long articles | Less intrusive | May be overlooked |
| **Top of article** | Mobile-first | Accessible on all devices | Takes space |

## Technical Implementation

### Heading Structure

- One `<h1>` per page
- `<h2>` for major sections
- `<h3>` for subsections; avoid skipping levels
- Headings ??0 characters for SEO

### Jump Links

- Assign unique IDs to headings (e.g., `id="keyword-optimization"`)
- Use kebab-case for IDs
- Link TOC entries via anchor tags (`#section-id`)
- Descriptive anchor text; include target keywords naturally

### Semantic HTML

```html
<nav aria-label="Table of contents">
  <ol>
    <li><a href="#section-1">Section Title</a></li>
  </ol>
</nav>
```

## SEO Best Practices

| Practice | Purpose |
|----------|---------|
| **Schema.org TableOfContents** | Help search engines understand structure |
| **Keywords in headings** | Natural integration; avoid stuffing |
| **Jump links in SERP** | Google may feature TOC links; increases CTR |

## UX Guidelines

### Visibility & Interaction

- Clear visual hierarchy; indent nested items
- Highlight current section when scrolling (optional)
- Smooth scroll behavior for jump links

### Mobile

- Minimum 16px font size
- Touch targets ??4×44px
- Responsive layout; consider collapsible on small screens

### Accessibility

| Requirement | Practice |
|-------------|----------|
| **ARIA** | `aria-label="Table of contents"` on nav |
| **Keyboard** | All links keyboard-accessible |
| **Screen readers** | Proper heading structure; TOC aids skimming |

## Output Format

- **TOC structure** (sections, nesting)
- **Heading/ID mapping** suggestions
- **HTML/ARIA** notes
- **SEO** checklist

## Related Skills

- **seo-on-page-heading**: TOC built from heading structure
- **pages-blog**: TOC common in long-form blog posts
