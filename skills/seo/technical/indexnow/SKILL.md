---
name: seo-technical-indexnow
description: When the user wants to implement IndexNow, notify search engines of new/updated URLs, or speed up Bing indexing. Also use when the user mentions "IndexNow," "Bing indexing," "URL notification," "instant indexing," "sitemap IndexNow sync," or "share URL list with sitemap."
metadata:
  version: 1.0.0
---

# SEO Technical: IndexNow

Guides IndexNow protocol integration for faster search engine indexing (primarily Bing).

**When invoking**: On **first use**, if helpful, open with 1â€? sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **IndexNow**: Submit URLs to Bing/Yandex for faster indexing
- **URL notification**: Notify search engines of new or updated URLs

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for site URL.

Identify:
1. **Site URL**: Base domain
2. **URL source**: Config file, sitemap, CMS, etc.
3. **Deployment**: CI/CD, manual, or both

## Overview

IndexNow notifies search engines (mainly Bing) of new or updated URLs to speed up indexing.

## Implementation Steps

### 1. API Key and Verification

- Generate API key (e.g., UUID)
- Create verification file: `https://example.com/{key}.txt`
- File content: the API key string
- Configure key and URL in your IndexNow client

### 2. Submission Methods

| Method | When to use |
|--------|-------------|
| **Single URL** | New or updated page |
| **Batch** | Many URLs at once (e.g., after deploy) |
| **Relative paths** | Convert to full URLs before submitting |

### 3. Best Practices

| Practice | Note |
|----------|------|
| **When to submit** | New pages, major content updates, meta changes |
| **When not to** | Minor edits; let natural crawling handle |
| **Frequency** | Once per deploy; avoid excessive submissions |
| **Priority** | Submit high-value commercial pages first |

### 4. CI/CD Integration

```bash
npm run build
npm run indexnow:all
```

### 5. Single Source of Truth (URL List)

- **Use same config as sitemap**: Import URL list from central config (e.g., `site-pages-config.ts`) or sitemap generation logic.
- **Avoid**: Separate hardcoded URL lists for IndexNowâ€”leads to inconsistency and missed URLs.
- **Feed**: If you have RSS/feed, it can also consume from the same config to stay in sync.

## Supported Search Engines

- **Bing**: Primary support
- **Yandex**: Supports IndexNow
- **Google**: Does not use IndexNow; use Sitemap + Search Console

## Verification

- Check [Bing Webmaster Tools](https://www.bing.com/webmasters/indexnow) for indexing status
- Monitor submission logs for errors

## Common Issues

| Issue | Fix |
|-------|-----|
| Domain verification fails | Ensure URL uses correct domain |
| API key error | Verify key and verification file match |
| Network errors | Retry; API can be intermittent |

## Output Format

- **Setup steps**: Key generation, verification file
- **Submission flow**: Single vs. batch
- **Integration**: CI/CD or manual script
- **References**: [IndexNow docs](https://www.bing.com/indexnow/getstarted)

## Related Skills

- **seo-technical-sitemap**: Share same URL list from central config
- **seo-technical-indexing**: Broader indexing strategy
