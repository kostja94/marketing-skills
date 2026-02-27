---
name: seo-technical-crawlability
description: When the user wants to improve crawlability, fix orphan pages, or optimize site structure for search engines. Also use when the user mentions "crawlability," "crawl budget," "orphan pages," "internal links," or "site structure."
metadata:
  version: 1.0.0
---

# SEO Technical: Crawlability

Guides crawlability improvements: robots, X-Robots-Tag, site structure, and internal linking.

**When invoking**: On **first use**, if helpful, open with 1â€? sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **Redirect chains & loops**: Fix multi-hop redirects; point directly to final URL
- **Broken links (4xx)**: Fix broken internal/external links; 301 or remove
- **Site architecture**: Logical hierarchy; pages within 3â€? clicks from homepage
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
| **Depth** | Important pages within 3â€? clicks from homepage |
| **Orphan pages** | Add internal links to pages with no incoming links |
| **Hierarchy** | Logical structure; hub pages link to content |

### Pagination

- Prefer pagination over infinite scroll for crawlability
- Reference links to next/previous pages; avoid dynamic-only loading

## Common Issues

| Issue | Check |
|-------|-------|
| Redirect chains | Update links to point directly to final URL |
| Broken links | 301 or remove; audit internal and external |
| Orphan pages | Add internal links from hub or navigation |
| Infinite scroll | Replace with pagination for key content |

## Output Format

- **Redirect audit**: Chains and loops to fix
- **Broken link audit**: 4xx links to fix
- **Site structure**: Orphan pages, hierarchy
- **Pagination**: Implementation for crawlable content

## Related Skills

- **seo-technical-robots**: robots.txt configuration
- **seo-technical-sitemap**: URL discovery
- **analytics-google-search-console**: Index status, Coverage report
- **seo-technical-indexing**: Fix indexing issues
- **seo-on-page-internal-links**: Internal linking best practices
