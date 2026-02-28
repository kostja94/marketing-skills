---
name: localization-strategy
description: When the user wants to plan or implement localization strategy for multilingual and global growth. Also use when the user mentions "localization," "multilingual," "i18n," "global expansion," or "market entry."
metadata:
  version: 1.0.0
---

# Strategies: Localization

Guides localization strategy for AI/SaaS products expanding into global markets. Covers i18n implementation, translation, pricing, and marketing adaptation--not just text translation.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product, target markets, and brand.

Identify:
1. **Target markets**: Priority languages/regions
2. **Product type**: SaaS, AI tool, content
3. **Technical stack**: Next.js, React, etc.

## Localization vs. Translation

Localization includes:
- **Product**: Features, UI/UX, cultural adaptation
- **Pricing**: True localization (adjust by market) vs. cosmetic (currency only)
- **Marketing**: Channels, content, user personas
- **Compliance**: GDPR, local regulations

## Technical (i18n)

### URL Structure

- **Subdirectories**: `/zh`, `/de`, `/es`, `/ru`
- **Default**: Root path for English; prefix for others
- **Hreflang**: Add to all multilingual pages

### Common Issues (Next.js + next-intl)

| Issue | Solution |
|-------|----------|
| Route conflict | `generateStaticParams()`; validate locale |
| Auto redirect | `localeDetection: false` |
| Middleware | Apply only to prefixed paths (e.g. `/zh`) |
| URL duplication | Manual switcher; `getLocalizedHref()` |

### SEO

- **Hreflang** on all language versions
- **Language switcher**: Use `<a>` not `<button>`; links in initial HTML
- **Canonical**: Handle multi-domain if using local TLDs

## Keyword Research by Market

| Market | Tool |
|--------|------|
| **Russia** | Yandex Wordstat |
| **Korea** | Naver DataLab |
| **Global** | Google Keyword Planner, Semrush |

Consider: Cultural expressions, search habits, competition, long-tail in small markets.

## Terminology

- **AIGC vs. GenAI**: Use "AIGC" for China; "Generative AI" for English markets
- **KOL vs. Influencer**: "Influencer" in English; "KOL" in Chinese
- **Avoid machine translation** for product/marketing: Terminology, culture, SEO quality

## Pricing Strategies

| Strategy | Use |
|----------|-----|
| **True localization** | Adjust price by purchasing power |
| **Cosmetic** | Display currency only; same price |
| **Tools** | Parity Deals, Chargebee |

## Output Format

- **Market** priority
- **i18n** approach
- **Keyword** strategy per market
- **Pricing** recommendation
- **Technical** checklist

## Related Skills

- **page-metadata**: Hreflang implementation
- **navigation-menu-generator**: Language switcher SEO
- **affiliate-marketing**: Local affiliates for target markets
