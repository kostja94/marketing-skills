---
name: seo-technical-indexing
description: When the user wants to fix indexing issues from Search Console, use noindex, or implement Google Indexing API. Also use when the user mentions "fix indexing," "not indexed," "Crawled - currently not indexed," "noindex," or "Google Indexing API."
metadata:
  version: 1.0.0
---

# SEO Technical: Indexing

Guides indexing troubleshooting and fix actions. For how to find and diagnose issues in GSC, see analytics-google-search-console.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **Fix actions**: noindex, robots.txt, canonical, content quality, URL Inspection
- **Noindex**: Use when excluding pages intentionally; not all content needs indexing. Complements robots.txt (crawl control) and analytics-google-search-console (Coverage interpretation)

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for site URL and indexing goals.

Identify issue from GSC (see analytics-google-search-console for Coverage report, issue types, diagnosis workflow). Then apply fix below.

## Crawled - Currently Not Indexed

| Cause | Action |
|-------|--------|
| Low quality, duplicate, off-topic | Improve content, fix duplicates, set correct canonical |
| Static assets (CSS/JS) | See below |
| Feed, share URLs with params | Usually OK to ignore; or noindex, canonical to main URL |
| Important content pages | Use URL Inspection, verify canonical/internal links/sitemap, Request indexing |

### Static Assets (Next.js / Vercel)

Vercel adds unique `dpl=` params to static assets per deploy, creating many "Crawled - currently not indexed" URLs.

| Do | Don't |
|----|-------|
| Keep robots.txt allowing `/_next/` | Do not block `/_next/` (breaks CSS/JS loading) |
| Accept static assets in GSC as expected | Do not block `/_next/static/css/` or `?dpl=` |
| Use X-Robots-Tag for static assets | CSS/JS should not be indexed; no SEO impact |

Static assets in "Crawled - currently not indexed" is **normal and expected**.

## Other Issue Types (from GSC Coverage)

| Issue | Fix |
|-------|-----|
| Excluded by «noindex» tag | Remove noindex if accidental; keep if intentional |
| Redirect / 404 | Fix URL or add redirect |
| Duplicate / Canonical | Set correct canonical; usually OK |

## Noindex Usage

- **When**: Login, admin, duplicate content, low-value pages, legal boilerplate, thank-you pages
- **How**: `metadata.robots = { index: false }` or X-Robots-Tag
- **Rationale**: Not all site content should be indexed; noindex is a valid choice for many pages
- **Caution**: Avoid noindex on important content pages
- **With robots.txt**: robots.txt controls crawl access; noindex controls indexing. Use both: robots for paths (e.g. /admin/), noindex for specific pages. See seo-technical-robots

## Google Indexing API

| Type | Typical use |
|------|-------------|
| JobPosting | Job boards |
| BroadcastEvent | Live platforms |

**Requirements**: Enable Indexing API, create service account, add owner in Search Console, request quota (default 200 URLs/day).

## Output Format

- **Action items**: Prioritized fixes
- **References**: [Page indexing report](https://support.google.com/webmasters/answer/7440203)

## Related Skills

- **analytics-google-search-console**: Find and diagnose indexing issues in GSC
- **seo-technical-robots**: Ensure robots.txt does not block indexing
- **seo-technical-sitemap**: Submit and maintain sitemap
- **seo-technical-indexnow**: Faster indexing for Bing
- **seo-technical-canonical**: Resolve duplicate content
