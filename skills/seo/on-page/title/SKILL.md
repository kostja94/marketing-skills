---
name: title-tag
description: When the user wants to optimize the title tag, page title, or SERP title. Also use when the user mentions "title tag," "meta title," "page title," "SEO title," "SERP title," "browser tab title," "title optimization," "headline for search," "title too long," "title tag length," "duplicate title tags," or "optimize title for CTR." For meta description, use meta-description. For structured data, use schema-markup.
metadata:
  version: 1.4.0
---

# SEO On-Page: Title Tag

Guides optimization of the HTML title tag for search engines and SERP display.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (On-Page SEO)

- **Title tag**: Primary search snippet; primary keyword near start; unique per page

## Length by Language

Google truncates by **pixel width** (~580–600px desktop), not character count. Character limits are approximate—CJK chars are wider (~2× Latin), so fewer fit in the same pixels.

| Script / Language | Title (chars) | Notes |
|-------------------|---------------|-------|
| **Latin** (English, Spanish, French, etc.) | 50–60 | ~55 recommended |
| **CJK** (Chinese, Japanese, Korean) | 25–35 | Full-width chars; 25–30 desktop; 20–28 mobile; use pixel checker when available |
| **Cyrillic** (Russian, etc.) | 50–55 | Slightly wider than Latin |
| **Arabic, Hebrew** | 30–40 | RTL; variable width |

**Pixel tools**: Use a pixel-accurate checker for CJK—font and locale affect display.

**Multilingual**: Use locale-specific limits; don't translate then truncate. See **localization-strategy**, **translation**.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for brand voice and target keywords.

Identify:
1. **Page type**: Homepage, landing, blog, product, etc.
2. **Primary keyword**: Target search query
3. **Language / script**: Apply length rule above
4. **Brand**: Optional brand append at end

## Best Practices

| Item | Guideline |
|------|-----------|
| **Length** | Per language (see table above); Google truncates beyond ~600px |
| **Front-load** | Main phrase first; branding at end |
| **Keyword** | Include primary keyword near the start |
| **Unique** | One unique title per page |
| **Clarity** | Match search intent; avoid keyword stuffing |
| **Engagement** | Numbers, power words, questions can boost CTR ~36% |
| **H1 alignment** | H1 should align with title; Google may rewrite titles if they mismatch content or intent |

**Example**: Bad: "SEO Tips for Small Business" → Better: "11 SEO Tips That Actually Work (2026)"

## Output Format

- **Recommended title** (with character count for target language)
- **Alternatives** (if A/B testing)

## GSC-Driven Optimization

For pages with low CTR despite good position, use google-search-console to identify opportunities. Compare actual CTR vs expected by position; optimize title for pages with CTR gap.

## Related Skills

- **google-search-console**: CTR analysis, identify low-CTR pages for title optimization
- **meta-description**: Meta description pairs with title in SERP
- **localization-strategy, translation**: Multilingual metadata; locale-specific length
- **serp-features**: SERP features; standard result appearance in context
- **heading-structure**: H1 should align with title tag
- **open-graph**: og:title for social sharing (often mirrors title)
- **schema-markup**: Structured data complements metadata
