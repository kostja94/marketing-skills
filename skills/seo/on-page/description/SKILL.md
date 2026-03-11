---
name: meta-description
description: When the user wants to optimize the meta description or meta tag description. Also use when the user mentions "meta description," "meta desc," "page description," "SEO description," "search snippet," "SERP description," "description tag," "snippet for search," "meta description length," "rewrite meta description," or "description not showing."
metadata:
  version: 1.3.0
---

# SEO On-Page: Meta Description

Guides optimization of the meta description tag for search engines and SERP display.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (On-Page SEO)

- **Meta description**: CTA; unique value; target keyword; unique per page

## Length by Language

Google truncates by **pixel width** (~920px desktop, ~680px mobile), not character count. Character limits are approximate—CJK chars are wider (~2× Latin), so fewer fit in the same pixels.

| Script / Language | Meta description (chars) | Notes |
|-------------------|--------------------------|-------|
| **Latin** (English, Spanish, French, etc.) | 150–160 | Desktop ~158; mobile ~120 |
| **CJK** (Chinese, Japanese, Korean) | 75–100 | Full-width chars; 70–80 conservative; 90–100 on some locales/fonts; use pixel checker when available |
| **Cyrillic** (Russian, etc.) | 140–155 | Slightly wider than Latin |
| **Arabic, Hebrew** | 70–90 | RTL; variable width |

**Pixel tools**: Use a pixel-accurate meta tag checker for CJK—font and locale affect display; character counts vary by source (65–80 to 90–120 in practice).

**Multilingual**: Use locale-specific limits; localize, don't just translate. See **localization-strategy**, **translation**.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for brand voice and target keywords.

Identify:
1. **Page type**: Homepage, landing, blog, product, etc.
2. **Primary keyword**: Target search query
3. **Language / script**: Apply length rule above
4. **CTA**: Primary action (sign up, learn more, buy, etc.)

## Best Practices

| Item | Guideline |
|------|-----------|
| **Length** | Per language (see table above); ~150 chars sweet spot for Latin; truncates beyond pixel limit |
| **Unique** | One per page; no duplicate descriptions |
| **Intent** | Answer "why should I click?"; match search intent |
| **CTA** | Include clear call-to-action when relevant |
| **Keyword** | Naturally include target keyword |
| **Content** | Include author, date, price where relevant |
| **Impact** | Does not affect ranking; well-written descriptions improve CTR 5–10% |

## Output Format

- **Recommended meta description** (with character count for target language)
- **Alternatives** (if A/B testing)

## GSC-Driven Optimization

For pages with low CTR despite good position, use google-search-console to identify opportunities. Optimize meta description for pages with CTR gap.

## Related Skills

- **google-search-console**: CTR analysis, identify low-CTR pages for meta optimization
- **title-tag**: Title pairs with description in SERP
- **localization-strategy, translation**: Multilingual metadata; locale-specific length
- **serp-features**: SERP features; standard result appearance in context
- **heading-structure**: H1 should align with title; description summarizes content
- **open-graph**: og:description for social sharing (often mirrors or extends meta description)
- **keyword-research**: Keywords in content inform description
