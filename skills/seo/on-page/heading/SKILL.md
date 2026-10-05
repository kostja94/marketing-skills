---
name: heading-structure
description: When the user wants to write or optimize H1-H6, fix heading hierarchy, improve content structure, rewrite an H1, or align headings with page intent. This skill owns actual heading changes; page-metadata may only check and report metadata-to-heading alignment.
metadata:
  version: 2.0.0
---

# SEO On-Page: Heading Structure

Guides heading (H1-H6) optimization for SEO and content structure.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (On-Page SEO)

- **H1 tag**: Clear visible page headline that confirms the user's task and value
- **Header tags (H1-H6)**: Logical content hierarchy and one coherent section per heading

## Initial Assessment

**Project context:** Read root `contextus.md` when present and load only the modules relevant to this task. Without Contextus, use available project material or user-provided facts and ask for missing information; do not create a parallel context system.

Identify:
1. **Page type**: Homepage, article, product, etc.
2. **Primary keyword**: Target search query
3. **Content outline**: Main sections and subsections

## Best Practices

### H1

| Principle | Guideline |
|-----------|-----------|
| **Primary page heading** | Prefer one clear H1 that identifies the page; audit accessibility and template semantics before treating an extra H1 as a ranking emergency |
| **Search language** | Include the primary concept naturally when useful; do not force exact-match phrasing |
| **Descriptive** | Clearly describe page content |
| **Match intent** | Serve the same page intent and promise as the title tag without requiring identical wording |

### H2-H6 Hierarchy

| Principle | Guideline |
|-----------|-----------|
| **Logical order** | Use heading levels to express document structure; do not choose a level for visual size alone |
| **One idea per heading** | Each heading = one topic |
| **Scannable** | Headings should summarize section content |
| **Keyword variation** | Use related keywords in subheadings |

### Structure

```
H1 (page title)
-> H2 (section 1)
   -> H3 (subsection)
   -> H3
-> H2 (section 2)
   -> H3
-> H2 (section 3)
```

## Common Issues

| Issue | Fix |
|-------|-----|
| Multiple H1s | Confirm the template and accessibility semantics; prefer one clear primary H1, but do not present extra H1s as an automatic ranking failure |
| Visual styling encoded as hierarchy | Keep semantic level based on structure and style it separately |
| Generic headings | Make descriptive; avoid "Introduction," "Conclusion" |
| Keyword stuffing | Natural language; avoid forced keywords |

## Output Format

- **H1** recommendation (with keyword)
- **H2-H6** outline for content
- **Hierarchy** check
- **References**: [Google headings](https://developers.google.com/search/docs/appearance/title-link)

## Related Skills

- **featured-snippet**: H2/H3 for snippet extraction; semantic HTML for list/table snippets
- **page-metadata**: Checks and reports title/H1/body alignment; routes actual heading edits here
- **content-optimization**: H2 keyword placement, quantity, tables, lists; complements heading structure
- **article-page-generator**: Article page H1-H3 structure, intro/body/conclusion
- **title-tag**: H1 and title share page intent but may use different natural variants
- **schema-markup**: Article schema uses headline (often H1)
- **content-strategy**: Content outline informs headings
