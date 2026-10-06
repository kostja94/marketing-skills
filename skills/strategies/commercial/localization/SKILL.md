---
name: localization-strategy
description: Plan, audit, implement, migrate, or validate localization for multilingual products and websites, including locale scope, market readiness, URL architecture, content coverage, hreflang coordination, rollout, and production verification. Use translation for the actual translation, glossary, and language review work.
metadata:
  version: 2.0.0
---

# Localization Strategy

Own the end-to-end localization decision and delivery lifecycle. Do not treat localization as a request to translate every source page or to create locale routes before the content is ready.

## Boundaries

- This skill owns market and locale selection, scope, technical architecture, rollout, migration, release gates, and measurement.
- **translation** owns translated copy, terminology, style, review, and source-change updates.
- **keyword-research** owns target-market query research; do not translate a source keyword list.
- **page-metadata**, **canonical-tag**, and **url-structure** own their specialist implementation details. Coordinate them here without duplicating their full rules.
- Preserve project-specific product facts, route inventories, and terminology in the project context or implementation repository. Do not turn them into universal rules.

## Establish the Current State

Read root `contextus.md` when present. Build the evidence set from the production site, route or CMS inventory, navigation and internal links, sitemap, source repository, analytics, and search data as available. A sitemap alone is not a complete page inventory.

Confirm:

- target markets, languages, and actual locale distinctions;
- current and proposed public URL patterns;
- default locale and whether it is prefixed;
- which page types are localized, source-only, or market-specific;
- content owner, glossary, review capacity, and update cadence;
- current route, canonical, hreflang, sitemap, language-switcher, and fallback behavior;
- existing indexed URLs that require redirects or compatibility handling.

When a site has thousands of same-template pages, inventory page types and representative examples rather than listing every URL.

## Decide Whether a Locale Should Launch

Prioritize a locale using evidence such as existing demand, search opportunity, conversion or revenue potential, competitive depth, payment and support readiness, compliance, and the team's ability to keep content current.

Separate these decisions:

1. **Language support**: the interface or content is available in a language.
2. **Locale support**: spelling, formats, currency, terminology, or product behavior differs.
3. **Market entry**: pricing, payments, channels, proof, support, and compliance are ready for a geography.

Do not create country-specific copies only because the countries differ. A new locale needs a maintained user or market distinction.

## Define the Coverage Model

Create a page-type or route-family matrix with one state per locale:

| State | Meaning | Public behavior |
|---|---|---|
| `source-current` | Source-language page is current | Source URL is public |
| `translation-draft` | Work exists but is not approved | Preview or noindex only |
| `localized-ready` | Content, terminology, facts, and metadata passed review | Locale URL may be indexed |
| `outdated` | Source changed after localized approval | Keep, warn internally, and queue review according to risk |
| `not-applicable` | Product or content does not apply to the market | Do not manufacture an alternate |

Core product, pricing, checkout, legal, and high-intent pages require a stricter release gate than low-risk support or user-generated content. Do not publish a locale URL whose language shell hides source-language body content.

## Choose URL and Routing Architecture

Use stable, crawlable URLs for public localized pages. Subdirectories are often operationally simple, but subdomains or ccTLDs can be valid when hosting, ownership, regulation, or market operations justify them. Do not claim one structure is universally superior.

Key invariants:

- each indexable locale page has one stable public URL;
- the URL, rendered language, `<html lang>`, navigation, metadata, and structured data describe the same locale;
- a language switcher uses discoverable links and, when an equivalent exists, preserves the current page context;
- user preferences may improve return visits but do not replace public locale URLs;
- missing translations do not silently render source-language content under a localized URL;
- canonical, hreflang, sitemap, internal links, and redirects agree on the public URL form.

Use BCP 47 language or locale identifiers appropriate to the real distinction. Do not invent regional variants merely for SEO.

## Coordinate Content Production

For each approved locale:

1. Lock the source version and record page type, audience, intent, claims, constraints, and owner.
2. Use **keyword-research** for the target market rather than translating source queries.
3. Use **translation** to produce copy, glossary decisions, style guidance, and review evidence.
4. Adapt examples, proof, pricing, payments, dates, units, imagery, and compliance only when verified for that market.
5. Keep feature availability and legal statements tied to the actual locale or market.
6. Mark the locale `localized-ready` only after content and implementation gates pass.

Legal or regulated content requires subject-matter review. Translation must preserve parties, numbers, obligations, rights, jurisdiction, version precedence, and section correspondence unless authorized counsel changes them.

## Migrate Existing Locale URLs

When replacing query parameters, cookies, old prefixes, domains, or routing systems:

1. Capture the current URL and behavior inventory, including indexed and externally linked variants.
2. Freeze the target public URL policy and locale mapping.
3. Map old URLs to the most equivalent new locale URLs.
4. Add permanent redirects where the old public URL is being replaced; preserve relevant path and query state when safe.
5. Update internal links, language switching, canonicals, hreflang, sitemaps, structured data, and analytics segmentation.
6. Keep compatibility redirects until logs and search data show they are no longer needed; do not use an arbitrary universal retention period.
7. Define rollback triggers and verify that rollback will not restore conflicting index signals.

Framework examples may be useful, but public URL and content-state invariants take precedence over a particular Next.js or i18n library configuration.

## Release Verification

Verify observable production behavior, not only configuration files:

- representative URLs for every page type and locale return the intended status;
- initial HTML contains the correct language, title, description, canonical, and locale-aware structured data;
- hreflang is reciprocal only among genuinely equivalent, published pages;
- language switching reaches the corresponding page or clearly explains that no equivalent exists;
- no locale URL renders mixed-language or source-language fallback as if localized;
- sitemaps include only canonical, indexable, published locale URLs;
- redirects are finite, preserve the intended destination, and do not expose duplicate public forms;
- internal links remain inside the current locale where an equivalent target exists;
- build, lint, route generation, and project-specific tests pass.

Use representative samples for very large route sets and add automated checks for route families.

## Monitor and Expand

Measure by locale and market rather than only global totals: crawl/index coverage, impressions, clicks, conversions, activation, revenue, support load, and stale-content rate. Report cannibalization, wrong-locale ranking, or indexing conflicts; do not automatically restructure pages without authorization.

Expand after the first locale demonstrates maintainable publishing and source-change synchronization. Volume alone is not success.

## Output

Provide only the artifacts the request needs, such as:

- locale and market decision;
- current-state findings;
- coverage matrix and ownership;
- URL or migration map;
- phased implementation plan;
- release and production-verification results;
- unresolved product, legal, or market decisions.

Do not create a new planning document when an existing project SSOT or implementation Skill can be updated.

## Related Skills

- **translation**: copy production, glossary, style, language review, and update workflow
- **keyword-research**: target-market search language and intent
- **page-metadata**, **canonical-tag**, **url-structure**: specialist SEO and URL implementation
- **pricing-strategy**, **gtm-strategy**: market economics and entry planning
- **navigation-menu-generator**: language switcher and discoverable navigation
