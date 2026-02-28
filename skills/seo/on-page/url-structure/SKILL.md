---
name: url-structure
description: When the user wants to optimize URL structure, fix URL issues, or plan URL hierarchy. Also use when the user mentions "URL structure," "URL optimization," "slug," "clean URLs," "URL hierarchy," "URL path," "permalink structure," "URL best practices," "dynamic URLs," or "URL parameters."
metadata:
  version: 1.0.0
---

# SEO On-Page: URL Structure

Guides URL structure optimization for SEO: readability, hierarchy, and best practices.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (On-Page SEO)

- **URL hierarchy**: Path structure, categories, depth
- **URL format**: Static vs dynamic; omit file extensions
- **URL slug**: See **url-slug-generator** for slug creation (3–5 words, under 60 chars)
- **Duplicate variants**: See **canonical-tag** for HTTPS, www, trailing slash

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

### Static vs Dynamic vs Pseudo-Static URLs

| Type | Example | Use |
|------|---------|-----|
| **Static** | `/blog/seo-guide` | Direct file; best SEO; content stable |
| **Dynamic** | `/product?id=123` | Program-generated; avoid for indexable content |
| **Pseudo-static** | `/blog/seo-guide` (rewritten from `.php`) | Combines both; common in CMS |
| **Rule** | Prefer static or pseudo-static; if dynamic, keep params ≤2; use **canonical-tag** and **robots-txt** (Clean-param) |

### File Extensions

- **Omit** `.html`, `.php`, `.aspx` — keeps URLs technology-agnostic, shorter, easier to refactor
- **Example**: `/seo-guide` not `/seo-guide.html`

### URL Parameter Handling

| Scenario | Approach |
|----------|----------|
| **UTM / tracking** | Canonical to base URL; params in query string only |
| **Search results** | Canonical to search page; avoid indexing result URLs |
| **Filters / sort** | Canonical to base; or **robots-txt** Clean-param |
| **Session IDs** | Use cookies; never in indexable URLs |

### Use Cases

| Scenario | Focus |
|----------|-------|
| **New site** | Plan hierarchy upfront; avoid later restructuring |
| **Migration** | 301 mapping; canonical; see **canonical-tag** |
| **Large site** | Dynamic URLs, params, multi-language — canonical + robots |
| **SEO audit** | Check structure, params, canonical consistency |

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
- **References**: [Alignify URL optimization](https://alignify.co/zh/seo/url-optimization); [Google URL guidelines](https://developers.google.com/search/docs/crawling-indexing/url-structure)

## Related Skills

- **canonical-tag**: HTTPS, www, trailing slash — handles duplicate URL variants
- **url-slug-generator**: Slug creation for content pages; length, keywords, format
- **category-page-generator**: E-commerce category URL hierarchy, faceted URLs
- **products-page-generator**: Product URL hierarchy
- **services-page-generator**: Service URL hierarchy
- **robots-txt**: Clean-param for query params
- **internal-links**: URL structure affects link patterns
