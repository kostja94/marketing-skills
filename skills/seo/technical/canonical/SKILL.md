---
name: canonical-tag
description: When the user wants to configure canonical URLs, fix duplicate content, or consolidate URL signals. Also use when the user mentions "canonical," "canonical URL," "duplicate content," "duplicate content fix," "preferred URL," or "URL consolidation." For GSC duplicates, use google-search-console.
metadata:
  version: 1.0.1
---

# SEO Technical: Canonical

Guides canonical tag configuration to consolidate duplicate content and declare preferred URLs.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **Duplicate site versions**: HTTPS vs HTTP; www vs non-www; trailing slash (/page vs /page/) — choose one, 301 redirect others
- **Duplicate content**: Canonical tags; consolidate and 301 to preferred URL
- **HTTPS**: SSL/TLS; secure connection; ranking signal since 2014

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for site URL and language structure.

Identify:
1. **Site URL**: Base domain
2. **Duplicate scenarios**: Multi-language, query params, pagination, alternate URLs
3. **Framework**: Next.js, React, static, etc.

## Canonicalization Methods (Choose by Scenario)

| Method | When | Strength |
|--------|------|----------|
| **301 redirect** | Preferred; server can redirect | Strongest — permanent redirect |
| **Canonical tag** | Cannot redirect (e.g. params, pagination) | Strong — HTML signal |
| **robots.txt** | Block non-canonical paths | Weak — advisory only |

Use 301 for HTTP→HTTPS, www variants, trailing slash. Use canonical for params, pagination, UTM.

## HTTPS & Security

HTTPS is a ranking signal ([Google, 2014](https://developers.google.com/search/blog/2014/08/https-as-ranking-signal)). Users and crawlers should access only the HTTPS version.

| Requirement | Action |
|-------------|--------|
| **SSL/TLS certificate** | Install valid certificate; use Let's Encrypt for free |
| **301 redirect** | HTTP → HTTPS; all HTTP requests redirect to HTTPS |
| **Mixed content** | No HTTP resources on HTTPS pages; fix mixed content warnings |
| **HSTS** | Optional; `Strict-Transport-Security` header for repeat visitors |

**WWW vs non-WWW**: Choose one preferred version; 301 redirect the other. See canonical rules above.

## When to Use Canonical

- **Multi-language**: Each language version has its own canonical; use **hreflang** with canonical
- **Same content, multiple URLs**: Params, pagination, tracking params, www vs non-www, trailing slash (/page vs /page/)
- **Self-referencing**: Canonical should point to self or the preferred version
- **Avoid chain canonical**: A→B→C is invalid

## Rules

| Rule | Note |
|------|------|
| **Absolute URL** | Include `https://` |
| **Consistency** | Must match current page URL or the chosen preferred version |
| **No chains** | A→B→C is invalid |

## Implementation Patterns

### Next.js (metadata)

```tsx
export const metadata = {
  alternates: {
    canonical: "https://example.com/page-slug",
    languages: {
      zh: "https://example.com/zh/page-slug",
      en: "https://example.com/page-slug",
      "x-default": "https://example.com/page-slug",
    },
  },
};
```

### HTML (generic)

```html
<link rel="canonical" href="https://example.com/page-slug" />
```

### Server Redirects (301)

**Apache (.htaccess)**:
```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

**Nginx**:
```nginx
return 301 https://$host$request_uri;
```

## Relationship to Other Technical SEO

- **Sitemap**: URLs in sitemap should match canonical
- **IndexNow**: Submit canonical URLs

## Output Format

- **Canonical URL** for each page type
- **Implementation** (metadata or HTML)
- **Multi-language** setup if applicable
- **References**: [Alignify URL optimization](https://alignify.co/zh/seo/url-optimization); [Google Canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)

## Related Skills

- **url-structure**: URL hierarchy and format; canonical handles duplicate variants (HTTPS, www, trailing slash)
- **localization-strategy**: hreflang + canonical for multi-language
- **xml-sitemap**: Sitemap URLs should match canonical
- **indexnow**: Submit canonical URLs
- **google-search-console**: Find duplicate content in Coverage report
- **indexing**: Resolve indexing issues
- **site-crawlability**: Crawl budget; redirect chains; canonical reduces duplicate crawl waste
