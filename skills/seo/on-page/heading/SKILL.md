---
name: heading-structure
description: When the user wants to write or optimize H1-H6, fix heading hierarchy, improve content structure, rewrite an H1, or align headings with page intent. This skill owns actual heading changes; page-metadata may only check and report metadata-to-heading alignment.
metadata:
  version: 2.1.0
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

### Clarity, Consistency and Specificity

- Optimize first for a reader who scans the headings: each heading should make the section's subject immediately clear. SEO phrasing supports that purpose.
- Reuse structural headings across the same page family when they describe equivalent sections. Consistency is useful; repeated wording alone is not a defect.
- Keep concise labels such as `FAQ` and `Related Investors` when they are sufficient. Do not expand a label merely to add words or manufacture uniqueness.
- Add the entity and relevant topic when they improve identification: `Sequoia Capital’s AI Portfolio`, `Sequoia Capital’s Investment Philosophy`, or `Mistral AI’s Company History`. These are examples, not required sections or universal templates.
- Front-load the entity or primary search concept when the result reads naturally. Skip keyword insertion when it adds repetition, awkwardness or an unsupported promise. Do not impose a heading word-count target.
- Distinguish reusable structure from content-specific meaning. Specific analytical subsections should name their actual subject; do not rotate synonyms just to pass a swap test.
- Match the body’s scope: a selected portfolio must not imply a complete portfolio; a short company introduction must not be relabeled as a company history or investment philosophy without that content.
- When headings are generated from shared components, keep reusable phrasing in one maintained configuration and interpolate canonical entity names. Use editorial overrides only for a real difference in content, not cosmetic variation.

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
| Vague content headings | Name the actual subject; preserve useful structural labels such as "FAQ" rather than expanding them mechanically |
| Keyword stuffing | Natural language; avoid forced keywords |

## Output Format

- **H1** recommendation (with the primary concept when natural)
- **H2-H6** outline for content
- **Hierarchy** check
- **Reuse and specificity**: identify shared page-family headings and content-specific overrides; flag only misleading repetition or unsupported claims
- **References**: [Google headings](https://developers.google.com/search/docs/appearance/title-link)

## Related Skills

- **featured-snippet**: H2/H3 for snippet extraction; semantic HTML for list/table snippets
- **page-metadata**: Checks and reports title/H1/body alignment; routes actual heading edits here
- **content-optimization**: H2 keyword placement, quantity, tables, lists; complements heading structure
- **article-page-generator**: Article page H1-H3 structure, intro/body/conclusion
- **title-tag**: H1 and title share page intent but may use different natural variants
- **schema-markup**: Article schema uses headline (often H1)
- **content-strategy**: Content outline informs headings
