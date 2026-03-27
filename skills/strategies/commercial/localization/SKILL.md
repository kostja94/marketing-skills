---
name: localization-strategy
description: When the user wants to plan or implement localization strategy for multilingual and global growth. Also use when the user mentions "localization," "multilingual," "i18n," "global expansion," "market entry," "localization strategy," "hreflang," "multi-language SEO," or "international SEO." For translation workflow, glossary, and style guide, use translation.
metadata:
  version: 1.1.0
---

# Strategies: Localization

Guides localization strategy for AI/SaaS products expanding into global markets. Covers i18n implementation, translation, pricing, and marketing adaptation--not just text translation.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, target markets, and brand.

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

Choose one; be consistent:

| Option | Example | Pros / Cons |
|--------|---------|-------------|
| **Subdirectories** | `/en/`, `/de/`, `/zh/` | Recommended; maintains domain authority |
| **Subdomains** | `de.example.com` | Separate hosting; less authority transfer |
| **ccTLD** | `example.de` | Strongest geo signal; costly |

- **Use subdirectories, not subdomains** for i18n; subdomains transfer less authority.
- **Default locale**: Root path for default (e.g. `/` for English); prefix for others (`/zh/`, `/de/`).
- **IETF BCP 47**: Use valid codes (`en`, `en-US`, `zh-CN`, `pt-BR`). Same language, different country (e.g. `de-DE` vs `de-AT`) needs ≥20% content difference for Google to differentiate.

### i18n SEO Principles

- **No hardcoded strings**: All user-facing text via translation dictionary.
- **Symmetric alternates**: Every locale page lists ALL other versions (including self-reference). ~75% of international sites have hreflang errors; missing reciprocal links is the most common.
- **x-default**: Always include for fallback when user language/location doesn't match any version.
- **Canonical alignment**: Canonical must match the same regional version hreflang refers to; misalignment causes Google to ignore hreflang.
- **Full SEO coverage**: Metadata, OpenGraph, JSON-LD (`inLanguage`), and sitemap all locale-aware.

### Common Issues (Next.js + next-intl)

| Issue | Solution |
|-------|----------|
| Route conflict | `generateStaticParams()`; validate locale |
| Auto redirect | `localeDetection: false` |
| Middleware | Apply only to prefixed paths (e.g. `/zh`) |
| URL duplication | Manual switcher; `getLocalizedHref()` |

### SEO

- **Hreflang** on all language versions; self-reference + symmetric annotations.
- **Language switcher**: Use `<a>` not `<button>`; links in initial HTML.
- **Canonical**: Handle multi-domain if using local TLDs; align with hreflang.
- **SPAs**: Use sitemap-based hreflang as backup when HTML head is JS-rendered. See **rendering-strategies**.

## Keyword Research by Market

| Market | Tool |
|--------|------|
| **Russia** | Yandex Wordstat |
| **Korea** | Naver DataLab |
| **Global** | Google Keyword Planner, SEO tools |

Consider: Cultural expressions, search habits, competition, long-tail in small markets.

## Terminology & Translation

- **Translation workflow, glossary, style guide**: See **translation** for full workflow
- **Avoid machine translation** for product/marketing: See **translation** (Human vs MT)

## Pricing Strategies

| Strategy | Use |
|----------|-----|
| **True localization** | Adjust price by purchasing power |
| **Cosmetic** | Display currency only; same price |
| **Tools** | Parity Deals, Chargebee |

## i18n SEO Checklist (New Feature / New Locale)

### New feature with i18n

1. Add translation keys to all locale JSON files. Use **translation** for glossary, style guide, and translation workflow.
2. Add `generateMetadata()` with alternates (hreflang) per page.
3. Add JSON-LD with `inLanguage` and translated fields.
4. Add page to sitemap with hreflang annotations.
5. Set `lang` attribute on `<html>`; UTF-8 encoding.

### New locale

1. Add locale code to config; create `{code}.json` dictionary.
2. Register in sitemap locale list; regenerate.
3. Add OpenGraph `locale` and `alternateLocale`.
4. Ensure all alternates are symmetric (every page lists all versions).

### Multilingual Risks

- **Batch publishing**: Too many translated pages at once can trigger de-indexing or thin-content penalties.
- **Mitigation**: Roll out slowly; ensure content is product/industry relevant; avoid Wikipedia-like breadth; monitor indexing in GSC.

### Avoid

- IP-based redirects that override user preferences.
- Machine translation without localization for product/marketing (see **translation**).
- Missing reciprocal hreflang between language versions.
- Canonical tags that conflict with hreflang.

## Output Format

- **Market** priority
- **i18n** approach
- **Keyword** strategy per market
- **Pricing** recommendation
- **Technical** checklist
- **i18n SEO** checklist (if applicable)

## Related Skills

- **pricing-strategy**: Base price structure; localization-strategy covers pricing by market
- **page-metadata**: Hreflang implementation
- **url-structure**: URL hierarchy for i18n (subdirectories, subdomains)
- **content-strategy**: Multilingual content planning; avoid thin translations
- **translation**: Translation workflow, glossary, style guide, human vs MT; produces content for localized pages
- **navigation-menu-generator**: Language switcher SEO
- **affiliate-marketing**: Local affiliates for target markets
- **gtm-strategy**: New market entry; localization as GTM for new geography
