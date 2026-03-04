# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## Update Rules

- **Format**: `## [YYYY-MM-DD] <version>` — date first (release date), then version (e.g. v2.1.0) or `Initial` for first release.
- **Order**: Newest first. Unreleased at top; then by date descending.
- **When releasing**: Move Unreleased entries under a new `## [YYYY-MM-DD] vX.Y.Z` heading; clear Unreleased.
- **Date**: Use the actual release/commit date (YYYY-MM-DD). Check `git log --date=short` if unsure.

## [Unreleased]

### Added

- **template-page-generator** — Template aggregation + detail pages; users browse → use → customize; CMS, design, vibe coding; programmatic SEO.
- **gtm-strategy** — GTM: PLG/SLG/MLG modes; 90-day framework; ICP; new market entry; repositioning.
- **pmf-strategy** — Product-market fit; Sean Ellis 40% test; vitamin vs painkiller.
- **copywriting, video-marketing** — PAS/AIDA/BAB; headlines, CTAs; short-form, long-form scripts.
- **press-coverage-page-generator, press-coverage-page.md** — Third-party coverage; full page vs section; media kit distinction.
- **local-seo, pr-marketing** — GBP, NAP, citations; press release, media relations.
- **youtube-seo, pinterest-posts, medium-posts** — Platform skills.
- **youtube-ads, native-ads** — TrueView, Bumper, Discovery; Taboola, Outbrain.
- **conversion-optimization, product-launch, retention-strategy** — CRO, PIE; launch execution; churn prevention.

### Changed

- **parasite-seo, programmatic-seo** — Moved from strategies/ to seo/.
- **product-launch** — Focus on launch execution; GTM framework → gtm-strategy.
- **pmf-strategy, cold-start-strategy, rebranding-strategy, localization-strategy** — Added gtm-strategy.
- **landing-page-generator** — Programmatic LPs; programmatic-seo, template-page-generator.
- **programmatic-seo** — template-page-generator, landing-page-generator.
- **indie-hacker-strategy** — Pieter Levels playbook; First 100 users; Build in Public (40/30/20/10); Traction Triangle; removed China going-global.
- **cold-start-strategy, community-forum** — Indie content → indie-hacker-strategy; cross-refs.
- **7 skills** — Added indie-hacker-strategy to Related Skills (discount-marketing, directory-submission, integrated-marketing, pmf-strategy, product-launch, parasite-seo, reddit-posts).
- **seo-strategy** — Strategic Context (why SEO, when to invest, AI search era); Alignify ref.
- **template-page-generator** — Aggregation + detail; user-facing flow; CMS, design, vibe coding.
- **skills-list, README, page-taxonomy** — 143 skills; Pages 43.
- **content-marketing-strategy** — Video → video-marketing.
- **media-kit-page-generator** — Press-coverage distinction; Related Skill.
- **homepage-generator, trust-badges-generator, pr-marketing** — Press-coverage cross-refs.
- **indie-hacker-strategy, template-page, display-ads** — English-only triggers.
- **seo-strategy, domain-selection, indie-hacker-strategy** — Alignify link text in English.

## [2026-03-05] v2.2.0

### Added

- **where-to-use-skills.md, use-cases-and-roadmap.md** — Platform guide; use cases, roadmap.
- **paid-ads/** — google-ads, meta-ads, linkedin-ads, reddit-ads, tiktok-ads, app-ads, ctv-ads, display-ads, directory-listing-ads.
- **domain/** — domain-selection, domain-architecture, multi-domain-brand-seo.
- **tools-page-generator, file-naming.md** — Tools page; uppercase file naming.

### Changed

- **README** — 127 skills; Use Cases; where-to-use-skills.
- **Skills** — Platform ↔ paid-ads linkage; audit fixes.
- **Features vs Use cases vs Solutions** — Clearer differentiation; tools vs features.
- **Structure** — Removed empty slug/; 127 skills; CHANGELOG format unified.

### Removed

- **using-beyond-cursor.md, platforms-with-skills.md** — Merged into where-to-use-skills.md.

## [2026-03-01] v2.1.0

### Changed

- Description optimization (83 skills); page taxonomy merged into skills-list.

## [2026-03-01] v2.0.0

### Changed

- Skill naming v4 (83 skills); 18+ skill content updates.

### Added

- description-rules.md, docs/README.md.

## [2026-02-28] Initial

### Added

- CHANGELOG, skills-task-progress, using-beyond-cursor, platforms-grokipedia, channels-directories, components-breadcrumb, components-social-share, pages-article, seo-content-optimization.

### Changed

- seo-on-page split; product-marketing-context; pages-article, pages-blog, content-strategy.
