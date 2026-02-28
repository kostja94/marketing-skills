---
name: seo-on-page-heading
description: When the user wants to optimize heading structure (H1-H6), fix heading hierarchy, or improve content structure. Also use when the user mentions "H1," "heading," "heading hierarchy," or "content structure."
metadata:
  version: 1.0.0
---

# SEO On-Page: Heading Structure

Guides heading (H1-H6) optimization for SEO and content structure.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (On-Page SEO)

- **H1 tag**: One per page; clear headline; matches content; primary keyword near start
- **Header tags (H1-H6)**: Logical hierarchy; keyword in headers; one idea per heading

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for target keywords.

Identify:
1. **Page type**: Homepage, article, product, etc.
2. **Primary keyword**: Target search query
3. **Content outline**: Main sections and subsections

## Best Practices

### H1

| Principle | Guideline |
|-----------|-----------|
| **One per page** | Single H1 per page |
| **Primary keyword** | Include target keyword naturally |
| **Descriptive** | Clearly describe page content |
| **Match intent** | Align with title tag and user intent |

### H2-H6 Hierarchy

| Principle | Guideline |
|-----------|-----------|
| **Logical order** | H1 ? H2 ? H3; don't skip levels |
| **One idea per heading** | Each heading = one topic |
| **Scannable** | Headings should summarize section content |
| **Keyword variation** | Use related keywords in subheadings |

### Structure

```
H1 (page title)
? H2 (section 1)
   ? H3 (subsection)
   ? H3
? H2 (section 2)
   ? H3
? H2 (section 3)
```

## Common Issues

| Issue | Fix |
|-------|-----|
| Multiple H1s | Use single H1; use H2 for other sections |
| Skipped levels | Use H2 after H1, H3 after H2 |
| Generic headings | Make descriptive; avoid "Introduction," "Conclusion" |
| Keyword stuffing | Natural language; avoid forced keywords |

## Output Format

- **H1** recommendation (with keyword)
- **H2-H6** outline for content
- **Hierarchy** check
- **References**: [Google headings](https://developers.google.com/search/docs/appearance/title-link)

## Related Skills

- **seo-content-optimization**: H2 keyword placement, quantity, tables, lists; complements heading structure
- **pages-article**: Article page H1?H3 structure, intro/body/conclusion
- **seo-on-page-title**: H1 should align with title tag
- **seo-on-page-schema**: Article schema uses headline (often H1)
- **seo-content-content-strategy**: Content outline informs headings
