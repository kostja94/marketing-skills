---
name: site-crawlability
description: When the user wants to improve crawlability, fix orphan pages, or optimize site structure for search engines. Also use when the user mentions "crawlability," "crawl budget," "orphan pages," "internal links," "site structure," "site crawlability," "infinite scroll," "pagination," "masonry SEO," "AI crawler optimization," "GPTBot crawlability," "ClaudeBot crawlability," or "content not indexed." For internal links, use internal-links.
metadata:
  version: 1.2.1
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
- **Crawl budget**: Reduce waste on duplicates, redirects, low-value URLs (see below)
- **AI crawler optimization**: SSR for critical content; URL management; reduce 404/redirect waste (see below)

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for site structure.

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

### Crawl Budget

Crawl budget is the number of URLs Googlebot will crawl on your site in a given period. Large sites (10,000+ pages) may waste up to 30% of crawl budget on duplicates, redirects, and low-value URLs.

| Waste source | Fix |
|--------------|-----|
| **Duplicate URLs** | Canonical; consolidate; 301 to preferred |
| **Redirect chains** | Point directly to final URL |
| **Parameter proliferation** | Use `rel="canonical"`; consider `Clean-param` (Yandex) |
| **Low-value pages** | noindex for thin/duplicate; see **indexing** |
| **Crawl traps** | Avoid infinite URL generation (e.g. faceted filters) |

**Sitemap**: Include only indexable, canonical URLs. See **xml-sitemap**, **canonical-tag**.

### AI Crawler Optimization

AI crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.) now represent ~28% of Googlebot's crawl volume. Their behavior differs from search engines—optimizing for both improves GEO (AI search visibility). See **generative-engine-optimization** for GEO strategy. [Vercel/MERJ study](https://vercel.com/blog/the-rise-of-the-ai-crawler) (Dec 2024):

| Factor | AI Crawlers (GPTBot, Claude) | Googlebot |
|--------|------------------------------|-----------|
| **JavaScript** | Do not execute JS; cannot read client-side rendered content | Full JS rendering |
| **404 rate** | ~34% of fetches hit 404s | ~8% |
| **Redirects** | ~14% of fetches follow redirects | ~1.5% |
| **Content in initial HTML** | JSON, RSC in initial response can be indexed | Same |

**Recommendations for AI crawlability:**

| Practice | Action |
|----------|--------|
| **Server-side rendering** | Critical content in initial HTML. Use SSR, ISR, or SSG. See **rendering-strategies** for full guide. |
| **URL management** | Keep sitemaps updated; use consistent URL patterns; avoid outdated /static/ assets that cause 404s. AI crawlers frequently hit outdated URLs. |
| **Redirects** | Fix redirect chains; point directly to final URL. AI crawlers waste ~14% of fetches on redirects. |
| **404 handling** | Fix broken links; remove or redirect outdated URLs. High 404 rates suggest AI crawlers may use stale URL lists. |

**Reference**: [The rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler) (Vercel, 2024)

## Common Issues

| Issue | Check |
|-------|-------|
| Redirect chains | Update links to point directly to final URL |
| Broken links | 301 or remove; audit internal and external |
| Orphan pages | Add internal links from hub or navigation; see **internal-links** for strategy |
| Infinite scroll | Provide paginated component pages; or replace with pagination for key content; see above |
| AI crawlers missing content | Ensure critical content in initial HTML; see **rendering-strategies** |

## Output Format

- **Redirect audit**: Chains and loops to fix
- **Broken link audit**: 4xx links to fix
- **Site structure**: Orphan pages, hierarchy
- **Pagination**: Implementation for crawlable content
- **AI crawler**: SSR/URL/redirect checks if GEO or AI visibility is a goal

## Related Skills

- **seo-strategy**: SEO workflow; crawlability is Technical phase (P0)
- **website-structure**: Plan which pages to build, page priority, structure planning; use before or alongside crawlability audit
- **robots-txt**: robots.txt configuration; AI crawler allow/block (GPTBot, ClaudeBot)
- **xml-sitemap**: URL discovery; keep updated to reduce AI crawler 404s
- **google-search-console**: Index status, Coverage report
- **indexing**: Fix indexing issues
- **internal-links**: Internal linking best practices
- **masonry**: Masonry + infinite scroll has same crawl issue; layout skill references this for SEO
- **generative-engine-optimization**: GEO strategy; AI search visibility; crawlability enables AI citation
- **canonical-tag**: Canonical reduces crawl budget waste on duplicates
- **rendering-strategies**: SSR, SSG, CSR; content in initial HTML; crawler visibility
