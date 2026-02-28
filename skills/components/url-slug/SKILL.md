---
name: url-slug-generator
description: When the user wants to create, optimize, or validate URL slugs for content pages. Also use when the user mentions "URL slug," "blog URL," "article URL," "short URL," "clean slug," or "SEO-friendly URL."
metadata:
  version: 1.0.0
---

# Components: URL Slug

Guides creation of SEO-friendly URL slugs for blog posts, articles, and content pages. Research on 11.8M Google results shows shorter URLs tend to rank higher; position #1 URLs average 50–60 characters.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **URL slug**: The path segment after the base (e.g., `ai-people-search` in `/blog/ai-people-search`)
- **Applies to**: Blog posts, articles, guides, category pages, product pages

## Best Practices (2025)

### Length

| Guideline | Target |
|-----------|--------|
| **Slug length** | Under 60 characters total (including path prefix) |
| **Word count** | 3–5 words |
| **Principle** | Shorter = easier to read, share, remember; less truncation in SERPs |

**Example**: "The Complete Guide to AI Search Engine for Finding People" → `ai-people-search` (3 words) or `ai-search-finding-people` (4 words), not `ai-search-engine-finding-people-speed-discovery-outreach` (9 words, 51 chars).

### Format

| Rule | Do | Avoid |
|------|-----|-------|
| **Separators** | Hyphens (`-`) | Underscores (`_`), spaces, periods |
| **Case** | Lowercase only | Mixed case (causes duplicate content) |
| **Characters** | Letters (a-z), numbers (0-9), hyphens | Special chars |
| **Stop words** | Remove when possible: the, a, and, or, to | Keep when needed: "how-to" |

### Content

| Rule | Guideline |
|------|-----------|
| **Primary keyword** | Include near start; one focus per URL |
| **Descriptive** | Clear what page is about from slug alone |
| **No keyword stuffing** | One keyword mention is enough |
| **No dates** | Omit unless time-specific (news, annual roundups) |

### Non-ASCII Characters

| Scenario | Rule |
|----------|------|
| **Accented letters** | Convert to ASCII: é→e, ü→u, ñ→n, ç→c |
| **Non-Latin scripts** | Use UTF-8 percent-encoding if required; prefer ASCII for compatibility |
| **Example** | `jalapeno` not `jalapeño`; `cafe` not `café` |

### Common Mistakes

- **Copy-pasting full title**: Summarize instead — long title → short slug
- **Auto-generated IDs**: `/post/12847` — always customize
- **Tracking params in slug**: UTM, session IDs — use query params separately
- **Changing without redirect**: Always 301 from old to new slug

## Slug Generation Workflow

1. **Extract primary keyword** from title or target keyword
2. **Summarize** in 3–5 words (don't copy full title)
3. **Remove stop words** (the, a, and, or) unless needed for readability
4. **Lowercase, hyphenate**, validate length < 60 chars
5. **Check uniqueness** — no duplicate slugs site-wide

## Examples

| Title / Topic | ❌ Too long | ✅ Recommended |
|---------------|-------------|-----------------|
| AI Search Engine for Finding People: Speed vs. Discovery | `ai-search-engine-finding-people-speed-discovery-outreach` | `ai-people-search` or `ai-search-finding-people` |
| The Ultimate SEO Checklist for 2025 | `the-ultimate-seo-checklist-for-2025` | `seo-checklist-2025` |
| How to Increase Website Traffic | `how-to-increase-the-traffic-to-your-website` | `increase-website-traffic` |
| Best Running Shoes for Marathon Training | `best-running-shoes-for-marathon-training-in-2025` | `best-running-shoes-2025` |

## Output Format

When creating or auditing a slug:

- **Recommended slug** (3–5 words)
- **Character count** (slug only)
- **Primary keyword** included
- **Alternatives** if multiple valid options

- **Reference**: [Alignify URL optimization](https://alignify.co/zh/seo/url-optimization)

## Related Skills

- **url-structure**: URL hierarchy, site structure; references this skill for slug conventions
- **canonical-tag**: When changing slugs, set up 301 redirects
- **article-page-generator**: Article URL slugs
- **blog-page-generator**: Blog post URL slugs
- **glossary-page-generator**: Glossary term slugs
- **products-page-generator**: Product page slugs
- **customer-stories-page-generator**: Case study page slugs
- **resources-page-generator**: Resource page slugs
- **features-page-generator**: Per-feature page slugs
