---
name: seo-on-page-url-structure
description: When the user wants to optimize URL structure, fix URL issues, or plan URL hierarchy. Also use when the user mentions "URL structure," "URL optimization," "slug," "clean URLs," or "URL hierarchy."
metadata:
  version: 1.0.0
---

# SEO On-Page: URL Structure

Guides URL structure optimization for SEO: readability, hierarchy, and best practices.

**When invoking**: On **first use**, if helpful, open with 1â€? sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (On-Page SEO)

- **URL slug**: Short; descriptive; hyphens; primary keyword; no dates; avoid special characters

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for site structure.

Identify:
1. **Site structure**: Categories, subcategories, content types
2. **Current URLs**: Existing patterns and issues
3. **Multi-language**: URL structure for zh/en (e.g., /zh/, /en/ or subdomains)

## Best Practices

### URL Guidelines

| Principle | Guideline |
|-----------|-----------|
| **Readable** | Use words, not IDs; `/blog/seo-guide` not `/p/12345` |
| **Short** | Shorter is generally better; avoid unnecessary depth |
| **Keyword** | Include target keyword when natural |
| **Lowercase** | Use lowercase; avoid mixed case |
| **Hyphens** | Use hyphens to separate words: `seo-guide` |
| **Avoid** | Special chars, query params for core content, session IDs |

### Hierarchy

| Pattern | Example | Use |
|---------|---------|-----|
| **Flat** | `/page-name` | Simple sites |
| **Category** | `/blog/post-name`, `/tools/tool-name` | Content sites |
| **Nested** | `/category/subcategory/page` | Deep hierarchies (keep shallow) |

### Multi-language

| Pattern | Example |
|---------|---------|
| **Path prefix** | `/zh/page`, `/en/page` |
| **Subdomain** | `zh.example.com`, `en.example.com` |
| **ccTLD** | `example.cn`, `example.com` |

## Common Issues

| Issue | Fix |
|-------|-----|
| Long URLs | Shorten; remove redundant words |
| Dynamic params | Use canonical; clean params in robots (Yandex Clean-param) |
| Mixed case | Redirect to lowercase |
| Changed URLs | 301 redirect old to new |

## Output Format

- **URL structure** recommendation
- **Slug** conventions
- **Hierarchy** for key content types
- **Redirect** plan if changing URLs
- **References**: [Google URL guidelines](https://developers.google.com/search/docs/crawling-indexing/url-structure)

## Related Skills

- **seo-technical-canonical**: Canonical for duplicate URLs
- **seo-technical-robots**: Clean-param for query params
- **seo-on-page-internal-links**: URL structure affects link patterns
