---
name: seo-technical-indexing
description: When the user wants to fix indexing issues, use noindex, or understand Search Console indexing. Also use when the user mentions "indexing," "not indexed," "Crawled - currently not indexed," "noindex," "Google Indexing API," or "Search Console."
metadata:
  version: 1.0.0
---

# SEO Technical: Indexing

Guides indexing troubleshooting, noindex usage, and Search Console best practices.

## Scope (Technical SEO)

- **Indexing status**: Check GSC "Pages" report; fix noindex, robots.txt blocks, "Crawled - currently not indexed"
- **Noindex**: Use when excluding pages intentionally; avoid on important pages

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for site URL and indexing goals.

Identify:
1. **Tool**: Google Search Console access
2. **Issue type**: Not indexed, Crawled-not-indexed, Excluded, etc.
3. **Framework**: Next.js, Vercel, static, etc.

## Index Status Check

- **Tool**: Google Search Console → Pages report
- **States**: Indexed, Discovered-not-indexed, Excluded, etc.
- **Troubleshooting**: Remove accidental noindex, check robots.txt, fix duplicate content

## Crawled - Currently Not Indexed

| Cause | Action |
|-------|--------|
| Low quality, duplicate, off-topic | Improve content, fix duplicates, set correct canonical |
| Static assets (CSS/JS) | See below |
| Feed, share URLs with params | Usually OK to ignore; or noindex, canonical to main URL |
| Important content pages | Use URL Inspection, verify canonical/internal links/sitemap, Request indexing |

**Process**: GSC Coverage → click Issue → view sample URLs → identify pattern → fix.

### Static Assets (Next.js / Vercel)

Vercel adds unique `dpl=` params to static assets per deploy, creating many "Crawled - currently not indexed" URLs.

| Do | Don't |
|----|-------|
| Keep robots.txt allowing `/_next/` | Do not block `/_next/` (breaks CSS/JS loading) |
| Accept static assets in GSC as expected | Do not block `/_next/static/css/` or `?dpl=` |
| Use X-Robots-Tag for static assets | CSS/JS should not be indexed; no SEO impact |

Static assets in "Crawled - currently not indexed" is **normal and expected**.

### GSC Coverage Issue Types

| Issue | Meaning | Action |
|-------|---------|--------|
| Crawled - currently not indexed | Crawled but not indexed | See above |
| Excluded by «noindex» tag | Intentionally excluded | Ignore if expected |
| Redirect / 404 | Redirect or missing | Fix URL or redirect |
| Duplicate / Canonical | Duplicate content | Usually OK; keep canonical |

## Noindex Usage

- **When**: Login, admin, duplicate content, low-value pages
- **How**: `metadata.robots = { index: false }` or X-Robots-Tag
- **Caution**: Avoid noindex on important pages

## Google Indexing API

| Type | Typical use |
|------|-------------|
| JobPosting | Job boards |
| BroadcastEvent | Live platforms |

**Requirements**: Enable Indexing API, create service account, add owner in Search Console, request quota (default 200 URLs/day).

## Output Format

- **Diagnosis**: Likely cause from GSC data
- **Action items**: Prioritized fixes
- **References**: [Page indexing report](https://support.google.com/webmasters/answer/7440203)

## Related Skills

- **seo-technical-robots**: Ensure robots.txt does not block indexing
- **seo-technical-sitemap**: Submit and maintain sitemap
- **seo-technical-indexnow**: Faster indexing for Bing
- **seo-technical-canonical**: Resolve duplicate content
