---
name: seo-technical-sitemap
description: When the user wants to create, audit, or optimize sitemap.xml. Also use when the user mentions "sitemap," "sitemap.xml," "lastmod," "changefreq," "priority," "URL discovery for search engines," "single source of truth," "URL config," "unify sitemap IndexNow," or "reduce duplicate maintenance."
metadata:
  version: 1.0.0
---

# SEO Technical: Sitemap

Guides sitemap creation, auditing, and optimization for search engine discovery.

**When invoking**: On **first use**, if helpful, open with 1â€? sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **Sitemap**: Create XML sitemap; submit to Google Search Console
- **URL discovery**: Help search engines find pages; especially important for large sites or poor internal linking

## Task

Generate an XML Sitemap that complies with the sitemaps.org protocol from the project's page list, and declare it in robots.txt.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for site URL and page structure.

Identify:
1. **Site URL**: Base domain (e.g., `https://example.com`)
2. **URL count**: Total indexable pages (single sitemap vs. sitemap index)
3. **Data source**: Static config, CMS, file system, or hybrid

## 1. Protocol Essentials

| Item | Spec |
|------|------|
| Single sitemap limit | â‰?0,000 URLs, â‰?0MB (uncompressed) |
| Sitemap index | When exceeding limit, split and have main index reference sub-sitemaps |
| Encoding | UTF-8 |
| URL format | Full URL, same host, include `https://` |
| Required tags | `<loc>` |
| Optional tags | `<lastmod>`, `<changefreq>`, `<priority>` |

## 2. Field Requirements

| Field | Description | Recommendation |
|-------|--------------|---------------|
| url | Full URL | `https://example.com/path` |
| lastModified | Page last modified time | Use page metadata, ISO 8601; use `YYYY-MM-DD` or omit when no data |
| changeFrequency | Update frequency | Home `daily`, list pages `weekly`, content pages `monthly` |
| priority | Relative importance | Home 1.0, aggregate pages 0.9, content pages 0.7â€?.8, others 0.5â€?.6 |

### lastmod (Critical)

- **Must be accurate**: Reflect actual page modification time, not sitemap generation time. Google requires verifiability; Bing reports ~18% of sitemaps ignored due to lastmod errors.
- **Format**: W3C Datetime (`YYYY-MM-DD` or `YYYY-MM-DDTHH:MM:SS+TZD`), e.g. `2025-01-15`, `2025-01-15T14:30:00+08:00`.
- **Avoid**: Using `new Date()` for lastmodâ€”causes all URLs to share the same timestamp; search engines may ignore.
- **Apply when**: Content updates, structured data changes, or important link changes.

### changefreq / priority

- **changefreq**: Hints only; does not directly determine crawl frequency. Values: `always`, `hourly`, `daily`, `weekly`, `monthly`, `yearly`, `never`.
- **priority**: 0.0â€?.0; **does not affect ranking**; set higher for important pages; avoid identical values for all.

## 3. Architecture & Split

### Single Sitemap

- When URLs â‰?0,000, generate `/sitemap.xml` directly.

### Sitemap Index (Multiple Sub-sitemaps)

- When exceeding limit, split by type or language; main index references sub-sitemaps.
- Example splits: `/sitemap/posts.xml`, `/sitemap/pages.xml`, `/sitemap/zh.xml`, `/sitemap/en.xml`.
- Main index outputs `/sitemap.xml` or `/sitemap-index.xml`, each entry as `<sitemap><loc>...</loc></sitemap>`.

### Multilingual Sites

- Split by locale: `/sitemap/zh.xml`, `/sitemap/en.xml`.
- Or by content type + language: `/sitemap/zh-posts.xml`, `/sitemap/en-posts.xml`.

## 4. Implementation

| Tech Stack | Implementation |
|------------|-----------------|
| Next.js App Router | `app/sitemap.ts` export `MetadataRoute.Sitemap` or `generateSitemaps` |
| Next.js Pages Router | `pages/sitemap.xml.ts` or `getServerSideProps` return XML |
| Astro | `src/pages/sitemap-index.xml.ts` or `@astrojs/sitemap` |
| Vite / Static build | Build script generates `public/sitemap.xml` |
| Other | Generate static `/sitemap.xml` or return dynamically via API |

### Route Exclusion

- If the project has i18n / middleware redirects, exclude sitemap paths to avoid redirect.
- Example (Next.js matcher): `'/((?!api|_next|sitemap|sitemap-index|.*\\..*).*)'`.

## 5. Page Scope

### Include

- Home: `/`
- Locale/region home pages (e.g. `/zh`, `/en`)
- All indexable content pages, list pages, category pages

### Exclude

- `/api/*`, `/admin/*`, `/_next/*`
- Static assets (images, JS, CSS, etc.)
- Login, admin, drafts, and other pages not intended for indexing

## 6. Data Source & Maintenance (Single Source of Truth)

- **Single source of truth**: Read URL list from config, CMS, or metadata; avoid hardcoding in sitemap.
- **Multiple page types**: Tools, blog, marketing pages can be merged into one array for unified generation.
- **New pages**: Add only to data source; sitemap updates automatically; avoid maintaining multiple places.

### Central Config (Recommended)

Create a config (e.g., `site-pages-config.ts`) that exports:
- Page slugs/paths by section (tools, blog, marketing, etc.)
- Optional: `modifiedDate` per page for accurate lastmod
- Function: `getAllPageUrls(baseUrl)` for sitemap and IndexNow

**Why**: Sitemap, IndexNow, and feed can all import from the same configâ€”no duplicate URL maintenance. IndexNow should use the same URL list; avoid separate hardcoded lists.

## 7. robots.txt

Add to robots.txt:

```
Sitemap: https://example.com/sitemap.xml
```

With multiple sitemaps, only declare the main index.

## 8. Output Format

### Single Sitemap Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2025-01-15</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://example.com/page</loc>
    <lastmod>2025-01-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

### Sitemap Index Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://example.com/sitemap/pages.xml</loc>
    <lastmod>2025-01-15</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap/posts.xml</loc>
    <lastmod>2025-01-14</lastmod>
  </sitemap>
</sitemapindex>
```

## 9. Common Issues

| Issue | Cause / Fix |
|-------|-------------|
| Sitemap 404 | Build failure, wrong path, incorrect export; check routes and deployment |
| Missing pages | URLs not in data source, filtered or excluded |
| lastmod anomaly | Avoid `new Date()`; use `modifiedDate` from page metadata |
| Google not indexing | Submit sitemap in GSC; check Coverage (analytics-google-search-console) and robots |
| EN/ZH URL mismatch | Use unified data source; share same list when generating by locale |

## References

- [sitemaps.org](https://www.sitemaps.org/protocol.html)
- [Google Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)

## Related Skills

- **analytics-google-search-console**: Sitemap status, indexed URL count, Coverage
- **seo-technical-robots**: Reference sitemap in robots.txt
- **seo-technical-indexnow**: Share same URL list from config
