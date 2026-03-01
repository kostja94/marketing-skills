# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Changed

- **about-page-generator** — Brand story, mission, values now reference branding.
- **homepage-generator** — Value prop, differentiation now reference branding.
- **logo-generator** — Brand guidelines source now references branding.
- **brand-visual-generator** — Visual identity strategy now references branding.
- **directory-submission** — Section 8 Brand & Voice now references branding.
- **product-marketing-context** — Section 8 and Quick Reference now reference branding.
- **content-strategy** — Now references content-marketing-strategy for cross-channel content planning.
- **integrated-marketing** — Content marketing now references content-marketing-strategy.
- **email-marketing** — Now references content-marketing-strategy for content types and formats.
- **article-page-generator** — Now references content-marketing-strategy; E-E-A-T and competitor analysis reference eeat-signals and competitor-research.
- **product-marketing-context** — Section 11 now references content-marketing-strategy.
- **link-building** — E-E-A-T now references eeat-signals.
- **content-optimization** — Competitors and E-E-A-T now reference competitor-research and eeat-signals.
- **keyword-research** — Competitor reverse now references competitor-research.
- **backlink-analysis** — Competitive comparison now references competitor-research.
- **featured-snippet** — E-A-T now references eeat-signals.
- **docs/** — SKILLS_GUIDE.md and CHANGELOG.md moved from root to docs/; all references updated.
- **alternatives-page-generator** — Content format: standalone page or blog listicle; quick verdict, comparison table, pros/cons; article-page-generator reference.
- **landing-page-generator** — Primary use for paid ads (PPC/SEM); LP requirements condensed; ad-to-page alignment moved to paid-ads-strategy.
- **page-taxonomy** — Added Alternatives, Integrations, Migration, Showcase, Contest, Startups (Marketing); Feedback, Disclosure (Utility).
- **website-structure** — Growth mapping updated with new page skills.

### Added

- **branding** — Brand strategy: purpose, values, positioning, storytelling (origin story, hero's journey, archetypes), voice & tone, visual identity strategy; consolidated from about, homepage, directories, product-marketing-context; logo and brand-visual remain as implementation components.
- **content-marketing-strategy** — Content types, formats, channels, repurposing matrix; funnel mapping; blog, email, social, video; consolidated from content-strategy, integrated-marketing, email-marketing, article; content-strategy remains SEO-focused.
- **eeat-signals** — E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness); author bio, citations, references, YMYL, AI content; consolidated from article, link-building, featured-snippet, content-optimization.
- **competitor-research** — Competitor analysis for SEO, content, backlinks, pricing; keyword/topic reverse, content gaps, link gap; consolidated from article, keyword-research, content-strategy, backlink-analysis, alternatives, migration, pricing-strategy, seo-monitoring.
- **seo-strategy** — SEO workflow order (Technical → On-Page → Content → Off-Page), Product-Led SEO, audit approach, prioritization; migrated Product-Led SEO and Products Suited for SEO from content-strategy.
- **paid-ads-strategy** — Paid ads (Google, Meta, LinkedIn); when to use/not use; ROAS; ad-to-page alignment; channel selection; migrated from cold-start (when NOT to use), landing-page (ad-to-page principles).
- **discount-marketing-strategy** — Discount structures (annual, volume, first-time, LTD); LTD/AppSumo; redeem code/coupon; BFCM; migrated from cold-start (LTD), referral, top-banner, contest, community-forum, affiliate.
- **pricing-strategy** — Pricing model, tier design, anchoring; base price structure; cross-references discount-marketing-strategy.
- **alternatives-page-generator** — Alternatives/comparison pages; "X alternatives," "X vs Y"; high SEO for SaaS.
- **integrations-page-generator** — Integrations, plugins, extensions; connect with Slack, Notion, etc.
- **migration-page-generator** — Migration guides; switch from competitor; step-by-step.
- **feedback-page-generator** — Feedback and roadmap pages; Canny, FeatureBase.
- **showcase-page-generator** — UGC gallery; "made with [product]"; creator community.
- **contest-page-generator** — Giveaway, contest, sweepstakes; Gleam, Woobox.
- **disclosure-page-generator** — Affiliate/sponsor disclosure; FTC compliance.
- **startups-page-generator** — Startups/education program; special pricing.
- **download-page-generator** — Download page for desktop/mobile app; platform selection, trust signals, CTA.
- **page-taxonomy** — Page purpose reference (Brand, SEO, SEM, Functional, Download); website-type dimension; page applicability matrix; subdomain conventions.
- **docs-page-generator** — Documentation site (docs.*): Getting Started, guides, API Reference, troubleshooting.
- **changelog-page-generator** — Changelog/release notes; changelog.* or /changelog.
- **status-page-generator** — Status page for service health; status.* subdomain.
- **use-cases-page-generator** — Use case pages; bridge features → real problems; BOFU for SaaS/B2B.
- **solutions-page-generator** — Solutions pages; outcome-focused; by industry, team, outcome.
- **website-structure** — Plan pages to build; Must Have/Great to Have/Optional; growth→structure mapping.
- **github-seo** — GitHub for parasite SEO, GEO; repos, README, Pages, awesome lists.
- **parasite-seo** — Parasite SEO; platform tiers; barnacle SEO; tiered framework.
- **programmatic-seo** — Template + data pages at scale; Intro, Evidence, Decision, FAQ, CTA.
- **cold-start-strategy** — First users; Product Hunt, AppSumo, Reddit, directories.
- **landing-page-generator** — 5-step flow; LP ↔ Page Types mapping; Related Skills.

### Removed

- **api-reference-generator** — API Reference is a section within docs, not a standalone page type; merged into docs-page-generator.

### Changed

- **docs-page-generator** — API Reference now part of docs.
- **docs/** — Skills count 83→88; reference-rules merged.
- **Root/templates/tools** — page-taxonomy moved to docs/; templates/README.
- **README** — Hero merged to 2 paragraphs; Linking + Product Context merged; deduplication (88, generic, workflow); Using Beyond Cursor compressed; Tips simplified; References table consolidated; ASCII diagram rebuilt for clarity.
- **Product/website references** — Reduced examples; no-endorsement disclosure.
- **affiliate-marketing** — Pitfalls, recruitment; tools simplified.
- **affiliate-page-generator** — LP best practices; landing-page-generator reference.
- **keyword-research** — Intent, discovery, clustering; pillar–cluster.
- **localization-strategy** — Subdirectories for i18n; hreflang.
- **content-strategy** — Product-Led SEO; products suited for SEO.
- **integrated-marketing** — Growth metrics by stage.
- **traffic-analysis** — Branded vs non-branded; bot traffic.
- **landing-page-generator** — Comparison, Use cases/Solutions types.
- **homepage-generator** — Positioning clarity.
- **community-forum, directory-submission** — Cold-start reference.
- **grokipedia-recommendations, generative-engine-optimization** — Parasite SEO moved.
- **reddit-posts, twitter-x-posts, category-page-generator** — Related Skills.
- **parasite-seo, generative-engine-optimization, directory-submission** — GitHub reference.
- **heading-structure** — page-metadata reference.
- **schema-markup** — GEO compressed; inLanguage.
- **creator-program, influencer-marketing** — Encoding fix.
- **docs/reference-rules.md** — §6 Product Examples; internal/external refs.
- **brand-visual-generator, hero-generator, logo-generator** — Design guidelines.
- **page-metadata, xml-sitemap** — hreflang rules.

## [2.1.0] - 2025-02-28

### Changed

- **Description optimization** — 83 skills: expanded keywords for discoverability.
- **docs/skills-list.md** — Page taxonomy (classification, intent, best practices) merged in.

## [2.0.0] - 2025-02-28

### Changed

- **Skill naming (v4)** — 83 skills renamed. SEO: industry terms; Pages: `[type]-page-generator`; Components: `[component]-generator`. See `docs/naming-rules.md`.
- **Content updates** — 18+ skills (platforms, channels, analytics, components, pages).

### Added

- **docs/description-rules.md** — Description guidelines for contributors.
- **docs/README.md** — Documentation index.

### Fixed

- **integrated-marketing** — Description language correction.

## [2025-02-28]

### Added

- CHANGELOG, Creator greeting, skills-task-progress, using-beyond-cursor, platforms-grokipedia, channels-directories, components-breadcrumb, components-social-share, pages-article, seo-content-optimization.

### Changed

- seo-on-page-metadata split; seo-on-page-schema; product-marketing-context; pages-article; pages-blog; seo-content-content-strategy.
