---
name: site-crawlability
description: When the user wants to improve crawlability, fix orphan pages, or optimize site structure for search engines. Also use when the user mentions "crawlability," "crawl budget," "orphan pages," "internal links," "site structure," "site crawlability," "infinite scroll," "pagination," "masonry SEO," or "content not indexed."
metadata:
  version: 1.1.0
---

# SEO Technical: Crawlability

Guides crawlability improvements: robots, X-Robots-Tag, site structure, and internal linking.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **Redirect chains & loops**: Fix multi-hop redirects; point directly to final URL
- **Broken links (4xx)**: Fix broken internal/external links; 301 or remove
- **Site architecture**: Logical hierarchy; pages within 3–4 clicks from homepage
- **Orphan pages**: Add internal links to pages with no incoming links
- **Pagination**: Prefer pagination over infinite scroll for crawlability

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for site structure.

Identify:
1. **Site structure**: Flat vs. deep hierarchy
2. **Framework**: Next.js, static, SPA, etc.
3. **Key paths**: Sitemap, robots.txt, API, static assets

## Best Practices

### Redirect Chains & Loops

- Fix multi-hop redirects; point directly to final URL
- Loops: URLs redirecting back to themselves; break the cycle

### Broken Links (4xx)

- Fix broken internal/external links; 301 or remove
- Audit regularly; update or remove broken links

### Site Architecture

| Principle | Guideline |
|-----------|-----------|
| **Depth** | Important pages within 3–4 clicks from homepage |
| **Orphan pages** | Add internal links to pages with no incoming links; see **internal-links** for link strategy |
| **Hierarchy** | Logical structure; hub pages link to content |

### Pagination vs Infinite Scroll

**Problem**: With infinite scroll, crawlers cannot emulate user behavior (scroll, click "Load more"); content loaded after initial page load is not discoverable. Same applies to masonry + infinite scroll, lazy-loaded lists, and similar patterns.

**Solution**: Prefer pagination for key content. If keeping infinite scroll, make it search-friendly per [Google's recommendations](https://developers.google.com/search/blog/2014/02/infinite-scroll-search-friendly):

| Requirement | Practice |
|-------------|----------|
| **Component pages** | Chunk content into paginated pages accessible without JavaScript |
| **Full URLs** | Each page has unique URL (e.g. `?page=1`, `?lastid=567`); avoid `#1` |
| **No overlap** | Each item listed once in series; no duplication across pages |
| **Direct access** | URL works in new tab; no cookie/history dependency |
| **pushState/replaceState** | Update URL as user scrolls; enables back/forward, shareable links |
| **404 for out-of-bounds** | `?page=999` returns 404 when only 998 pages exist |

**Reference**: [Infinite scroll search-friendly recommendations](https://developers.google.com/search/blog/2014/02/infinite-scroll-search-friendly) (Google Search Central, 2014)

### Pagination (Traditional)

- Reference links to next/previous pages; `rel="prev"` / `rel="next"` where applicable
- Avoid dynamic-only loading; ensure links in HTML

## Common Issues

| Issue | Check |
|-------|-------|
| Redirect chains | Update links to point directly to final URL |
| Broken links | 301 or remove; audit internal and external |
| Orphan pages | Add internal links from hub or navigation; see **internal-links** for strategy |
| Infinite scroll | Provide paginated component pages; or replace with pagination for key content; see above |

## Output Format

- **Redirect audit**: Chains and loops to fix
- **Broken link audit**: 4xx links to fix
- **Site structure**: Orphan pages, hierarchy
- **Pagination**: Implementation for crawlable content

## Related Skills

- **seo-strategy**: SEO workflow; crawlability is Technical phase (P0)
- **website-structure**: Plan which pages to build, page priority, structure planning; use before or alongside crawlability audit
- **robots-txt**: robots.txt configuration
- **xml-sitemap**: URL discovery
- **google-search-console**: Index status, Coverage report
- **indexing**: Fix indexing issues
- **internal-links**: Internal linking best practices
- **masonry**: Masonry + infinite scroll has same crawl issue; layout skill references this for SEO
