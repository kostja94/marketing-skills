---
name: indexing
description: When the user wants to fix indexing issues from Search Console, use noindex, or implement Google Indexing API. Also use when the user mentions "fix indexing," "not indexed," "Crawled - currently not indexed," "discovered - currently not indexed," "index coverage," "noindex," "noindex tag," "pages not indexed," "why not indexed," "request indexing," or "Google Indexing API." For sitemap, use xml-sitemap.
metadata:
  version: 1.0.1
---

# SEO Technical: Indexing

Guides indexing troubleshooting and fix actions. For how to find and diagnose issues in GSC, see **google-search-console**.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **Fix actions**: noindex, canonical, content quality, URL Inspection; verify robots.txt does not block (see **robots-txt**)
- **Noindex**: Page-level index control; which pages to exclude and how. Complements **robots-txt** (path-level crawl control) and **google-search-console** (Coverage diagnosis)

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for site URL and indexing goals.

Identify issue from GSC (see **google-search-console** for Coverage report, issue types, diagnosis workflow). Then apply fix below.

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
| Keep robots.txt allowing `/_next/` | Do not block `/_next/` (breaks CSS/JS loading). See **robots-txt** |
| Accept static assets in GSC as expected | Do not block `/_next/static/css/` or `?dpl=` |
| Use X-Robots-Tag for static assets | CSS/JS should not be indexed; no SEO impact |

Static assets in "Crawled - currently not indexed" is **normal and expected**.

## Other Issue Types (from GSC Coverage)

| Issue | Fix |
|-------|-----|
| Excluded by «noindex» tag | Remove noindex if accidental; keep if intentional |
| Blocked by robots.txt | See **robots-txt**; remove Disallow for important paths |
| Redirect / 404 | Fix URL or add redirect |
| Duplicate / Canonical | Set correct canonical; usually OK |
| **Soft-404** | Page returns 200 but content says "not found" or empty—Google may treat as 404. Fix: return 404 status for truly missing pages; or add real content for 200 pages |

### Soft-404

A soft-404 occurs when a page returns HTTP 200 but the content indicates the page doesn't exist (e.g. "Page not found" message, empty state). Google may treat it as 404 and exclude from index.

| Fix | When |
|-----|------|
| **Return 404** | Page truly doesn't exist; use proper 404 status |
| **Add content** | Page is intentional (e.g. empty search results); ensure substantive content or use noindex |
| **Redirect** | If URL moved, use 301 to correct destination |

## Noindex Usage

- **How**: `metadata.robots = { index: false }` or `<meta name="robots" content="noindex">` or X-Robots-Tag
- **Rationale**: Not all site content should be indexed; noindex is a valid choice for many pages
- **Caution**: Avoid noindex on important content pages
- **With robots.txt**: robots.txt = path-level crawl control; noindex = page-level index control. Do **not** block noindex pages in robots.txt—crawlers must access the page to read the directive. Use both: robots for /admin/, /api/; noindex for /login/, /thank-you/, etc. See **robots-txt** for when to use which.
- **nofollow ≠ noindex**: nofollow controls link equity only; it does **not** prevent indexing. To exclude from search, use noindex. See **page-metadata** for meta robots implementation.

### Page Types That Typically Need Noindex

| Category | Page Types | Typical Meta | Reason |
|----------|------------|--------------|--------|
| **Auth & Account** | Login, Signup, Password reset, Account dashboard | Login: `noindex,nofollow`; Signup: `noindex,follow` | No search value; login indexed = security risk; signup follow allows crawl of Privacy/Terms links |
| **Admin & Private** | Admin, Staging, Test pages, Internal tools | `noindex,nofollow` | Not for public; avoid discovery |
| **Conversion Endpoints** | Thank-you, Confirmation, Checkout success, Download gate | `noindex,follow` | Post-conversion; no SERP value; allow link equity |
| **System & Utility** | 404, Internal search results, Faceted/filter URLs | `noindex,follow` or `noindex,nofollow` | Thin/duplicate; 404 = error state |
| **Legal** | Privacy, Terms, Cookie Policy (optional) | Often `noindex,follow` | Low-value indexed; reduces clutter |
| **Duplicate & Thin** | Printer-friendly, Parameter URLs, Near-duplicate | `noindex,follow` or canonical | Duplicate content; canonical preferred when possible |
| **Low-Value** | Media kit, Feedback board (external), Thin press | `noindex` or index for brand queries | Case-by-case |

**noindex,follow vs noindex,nofollow**: Use `noindex,follow` for most cases—excludes from SERP but allows link equity. Use `noindex,nofollow` only for login (security), staging, or temporary test pages.

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

- **google-search-console**: Find and diagnose indexing issues in GSC
- **robots-txt**: Path-level crawl control; when to use robots.txt vs noindex; do not block /_next/ or noindex pages
- **page-metadata**: Meta robots implementation; noindex vs nofollow
- **xml-sitemap**: Submit and maintain sitemap
- **indexnow**: Faster indexing for Bing
- **canonical-tag**: Resolve duplicate content
