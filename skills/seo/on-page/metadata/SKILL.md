---
name: page-metadata
description: When the user wants to optimize meta tags other than title, description, Open Graph, or Twitter Cards. Also use when the user mentions "hreflang," "meta robots," "viewport," "charset," "canonical meta," "other meta tags," "meta robots noindex," "meta robots nofollow," "hreflang tags," "viewport meta," or "meta charset."
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
- **Metadata completeness**: All pages have title + meta description (see **title-tag**, **meta-description**)

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for language/locale and indexing goals.

Identify:
1. **Multi-language**: zh, en, x-default if applicable
2. **Indexing**: Full index, noindex for specific pages
3. **Tech stack**: Next.js, HTML, etc.

## hreflang (Multi-language)

**Three non-negotiables**: (1) Self-referencing tags (each page links to itself), (2) Symmetric annotations (every version lists ALL others), (3) Valid ISO 639-1 or language-region codes (`en`, `en-US`, `zh-CN`).

**Implementation methods**: HTML `<link>` in head, XML sitemap (`xhtml:link`), or HTTP headers. For SPAs/JS-rendered pages, use sitemap-based hreflang as backup. See **rendering-strategies** for SSR/SSG/CSR.

**Canonical alignment**: Canonical URL must match the same regional version hreflang refers to. Misalignment causes Google to ignore hreflang.

**x-default**: Fallback for users whose language/location doesn't match any version. Point to default locale or language-selector page.

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

### Common Mistakes (Avoid)

- Missing reciprocal references between language versions.
- Canonical tag conflicting with hreflang.
- Relying solely on machine translation without localization (see **translation**).
- Ignoring mobile—hreflang must appear on both desktop and mobile.
- Forgetting to update hreflang when page structure changes.

## Meta Robots (Page-level)

Page-level control for indexing and link following. See **indexing** for which page types typically need noindex.

| Directive | Effect |
|-----------|--------|
| `noindex` | Exclude page from search results |
| `nofollow` | Do not pass link equity through links on the page; **does NOT prevent indexing** |
| `noindex,follow` | Exclude from SERP; allow crawlers to follow links (most common for thank-you, signup, legal) |
| `noindex,nofollow` | Exclude + block link flow (login, staging, test pages) |

**Crawl vs index vs link equity**: robots.txt = crawl control; noindex = index control; nofollow = link equity only. See **robots-txt**, **indexing**.

```html
<meta name="robots" content="noindex, follow">
```

Next.js: `metadata.robots = { index: false, follow: true }`. Default is `index: true, follow: true`.

## Viewport

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Required for mobile-friendly pages; affects Core Web Vitals and mobile search. For full mobile-first indexing and mobile usability requirements, see **mobile-friendly**.

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

- **title-tag, meta-description**: Title and meta description
- **open-graph, twitter-cards**: Social sharing; link previews
- **canonical-tag**: Canonical + hreflang for multi-language
- **indexing**: noindex page-type list; noindex vs nofollow
- **robots-txt**: Crawl vs index; robots.txt vs noindex
- **mobile-friendly**: Mobile-first indexing; viewport required
- **rendering-strategies**: SSR, SSG, CSR; SPAs need sitemap-based hreflang
