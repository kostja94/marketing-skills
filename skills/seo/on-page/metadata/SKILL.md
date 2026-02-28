---
name: page-metadata
description: When the user wants to optimize meta tags other than title, description, Open Graph, or Twitter Cards. Also use when the user mentions "hreflang," "meta robots," "viewport," "charset," "canonical meta," or "other meta tags."
metadata:
  version: 1.0.0
---

# SEO On-Page: Metadata (Other Meta Tags)

Guides optimization of meta tags beyond title, description, Open Graph, and Twitter Cards. Covers hreflang, robots, viewport, charset, and metadata completeness.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (On-Page SEO)

- **Hreflang**: Language/region targeting for multilingual sites
- **Meta robots**: index/noindex, follow/nofollow (page-level)
- **Viewport**: Mobile responsiveness
- **Charset**: Character encoding
- **Metadata completeness**: All pages have title + meta description (see title-tag, meta-description)

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for language/locale and indexing goals.

Identify:
1. **Multi-language**: zh, en, x-default if applicable
2. **Indexing**: Full index, noindex for specific pages
3. **Tech stack**: Next.js, HTML, etc.

## hreflang (Multi-language)

- Use `alternates.languages` in Next.js metadata
- Include `x-default` for default language
- Each language version should reference all others
- **References**: [Google hreflang](https://developers.google.com/search/docs/specialty/international/localized-versions)

### Next.js (App Router)

```tsx
export const metadata = {
  alternates: {
    languages: {
      'en-US': '/en/page',
      'zh-CN': '/zh/page',
      'x-default': '/en/page',
    },
  },
};
```

### HTML (generic)

```html
<link rel="alternate" hreflang="en" href="https://example.com/en/page" />
<link rel="alternate" hreflang="zh" href="https://example.com/zh/page" />
<link rel="alternate" hreflang="x-default" href="https://example.com/en/page" />
```

## Meta Robots (Page-level)

For pages that should not be indexed:

```html
<meta name="robots" content="noindex, nofollow">
```

Or in Next.js: `metadata.robots = { index: false }`. See indexing for full indexing control.

## Viewport

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Required for mobile-friendly pages; affects Core Web Vitals and mobile search.

## Charset

```html
<meta charset="UTF-8">
```

Place in `<head>`; first child of `<head>` recommended.

## Output Format

- **hreflang** setup if multi-language
- **Meta robots** if noindex needed
- **Viewport** / **charset** if missing

## Related Skills

- **title-tag**: Title tag
- **meta-description**: Meta description
- **open-graph**: Open Graph for social sharing
- **twitter-cards**: Twitter Cards for X previews
- **canonical-tag**: Canonical + hreflang for multi-language
- **indexing**: noindex, Search Console
- **schema-markup**: Structured data complements metadata
- **heading-structure**: H1 should align with title
- **localization-strategy**: Hreflang implementation
