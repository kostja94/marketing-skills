---
name: page-metadata
description: When the user wants a full-page metadata audit or implementation across discovery, search intent, title, description, canonical, robots, hreflang, Open Graph, Twitter Cards, code or CMS changes, build validation, rendered HTML, production verification, localization, or post-release observation. Also use for "metadata audit," "sitewide meta optimization," "metadata implementation," "meta robots," "hreflang," "viewport," or "charset." For an isolated title, description, heading, Open Graph, or Twitter Card task, use its specialist skill directly.
metadata:
  version: 2.0.0
---

# SEO On-Page: Page Metadata

Orchestrates the complete metadata lifecycle. It owns scope, routing, implementation, validation, and delivery; specialist skills own their individual writing and tag rules.

**When invoking**: On first use, briefly state the scope and which specialist skills are needed. Then work from current production evidence and the real source of truth rather than producing a detached copy sheet.

## Ownership and boundaries

| Concern | Owner |
|---|---|
| Lifecycle, page inventory, implementation, validation, delivery | **page-metadata** |
| `<title>` writing and review | **title-tag** |
| Meta description writing and review | **meta-description** |
| H1-H6 writing and hierarchy | **heading-structure** |
| Open Graph | **open-graph** |
| X/Twitter Cards | **twitter-cards** |
| Canonical URL | **canonical-tag** |
| Localization | **localization-strategy**, **translation** |
| Post-release query and CTR observation | **google-search-console** |

This skill may check H1 and body coverage to confirm that metadata promises are fulfilled. It must not rewrite H1-H6; route that work to **heading-structure**. It may report keyword cannibalization, but must not merge pages, change page roles, delete URLs, or redistribute target keywords.

## Required inputs and evidence

Read root `contextus.md` when present and load only relevant modules. Otherwise use project documentation and verified product facts. Establish:

1. Target site, locales, environment, and release scope.
2. Page inventory from production navigation, footer, contextual links, index or hub pages, robots.txt, sitemap, production URLs, and application routes. A sitemap is evidence, not a complete inventory guarantee. For very large generated page families, inspect the template and representative examples instead of enumerating every URL.
3. Page type, unique job, primary search intent, target query evidence, audience, and page-specific facts.
4. Current production output: title, description, H1, canonical, robots, hreflang, OG, Twitter Cards, HTTP status, and server-returned HTML.
5. Actual maintenance source: framework metadata API, layout template, route module, static HTML, JSON/YAML, CMS fields, server injection, or proxy layer.

Never infer current production metadata from source code alone. Deployment and production may differ in either direction.

## Lifecycle

### 1. Discover and classify pages

- Build a URL-to-page-type map and select representative samples for repeated page families.
- Identify missing, duplicate, stale, inherited, fallback, or cross-locale metadata.
- Detect template-generated brand suffixes before writing titles so the suffix is not duplicated.
- Flag old brand names, parent-product language, obsolete features, or copied sibling-page claims.

### 2. Establish intent and page identity

- Confirm what the page alone can promise and prove.
- Use verified product facts and current page content; do not invent differentiators.
- Apply the **Swap Test**: if a title or description could be moved unchanged to a sibling page, it lacks page-specific information.
- Report potential cannibalization with affected URLs, overlapping intent, and evidence. Stop at reporting.

### 3. Route specialist work

- Use **title-tag** for title decisions and **meta-description** for descriptions.
- Use **heading-structure** only when headings need actual edits; otherwise check semantic alignment.
- Use **open-graph** and **twitter-cards** for social metadata. Social copy may differ from SEO copy, but page identity and claims must remain consistent.
- Use **canonical-tag**, **localization-strategy**, and **translation** when applicable.

### 4. Localize by market

- Research query language and intent for each locale; do not translate and truncate source metadata.
- Preserve product and brand terminology intentionally through a terminology source when one exists.
- Confirm each locale URL, canonical, hreflang set, and `og:locale` relationship.
- Treat missing or materially non-equivalent locale pages as an implementation issue rather than fabricating parity.

### 5. Implement at the source of truth

- Edit canonical code or CMS fields, not generated output.
- Preserve URL and page identity unless a separate migration task changes them.
- Account for layout inheritance, route precedence, template interpolation, CMS fallbacks, and automatic brand suffixes.
- Keep title, description, social metadata, canonical, robots, and hreflang internally consistent without forcing identical strings.

### 6. Validate before release

Run relevant lint, typecheck, tests, and production build. Then start or preview the built application when practical and inspect the initial server response HTML for representative URLs and locales. A browser DOM snapshot alone is insufficient when crawlers may receive different HTML.

Check:

- exactly one effective title and one intended description;
- no empty, placeholder, duplicate, or doubly suffixed output;
- title and H1 serve the same page intent without needing identical wording;
- H2/body content substantiate the metadata promise;
- canonical, robots, hreflang, OG, and Twitter tags resolve to intended absolute URLs;
- HTML escaping, locale output, images, and status codes are correct.

### 7. Verify production and observe

- Recheck representative production URLs after deployment using raw response HTML.
- Use platform preview/debug tools where available for social tags; cached previews may require refresh.
- Use **google-search-console** after recrawl to observe query mix, impressions, title/snippet behavior, and CTR. Do not promise a ranking or CTR lift.

## Other technical metadata

- `robots` controls page-level indexing/snippet behavior; robots.txt controls crawling. Use **indexing** and **robots-txt** for strategy.
- `viewport` normally uses `width=device-width, initial-scale=1`.
- Declare UTF-8 early in the document head.
- Hreflang annotations must use valid language or language-region codes, include self and reciprocal references, and align each locale with its own canonical URL. Use HTML, sitemap, or HTTP headers consistently.

## Deliverable

Provide scope and evidence, affected URLs or families, their true maintenance source, before/after metadata where useful, unresolved blockers, any cannibalization report, build/HTML/locale/production verification, and a post-release observation plan.

## Primary references

- [Google: title links](https://developers.google.com/search/docs/appearance/title-link)
- [Google: snippets and meta descriptions](https://developers.google.com/search/docs/appearance/snippet)
- [Google: localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions)

## Related Skills

- **title-tag**, **meta-description**, **heading-structure**
- **open-graph**, **twitter-cards**, **canonical-tag**
- **localization-strategy**, **translation**
- **indexing**, **robots-txt**, **google-search-console**
