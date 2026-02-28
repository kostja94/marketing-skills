# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [2.0.0] - 2025-02-28

### Changed

- **Skill naming optimization (v4)** — All 83 skills renamed for discoverability and consistency. SEO: `seo-*` → industry terms (e.g. `schema-markup`, `title-tag`, `link-building`). Pages: `pages-*` → `[type]-page-generator`. Components: `components-*` → `[component]-generator`. Channels: `channels-*` → descriptive names (e.g. `affiliate-marketing`, `directory-submission`). Platforms: added suffix (e.g. `twitter-x-posts`, `reddit-posts`). Strategies: full names (e.g. `generative-engine-optimization`). See `docs/naming-rules.md`.
- **Related Skills** — All skill references updated to new names across 83 skills.
- **Documentation** — SKILLS_GUIDE, docs/page-types-taxonomy, templates, docs/using-beyond-cursor, README updated to new skill names.
- **platforms-x** — Post structure (hook/value/CTA); TweepCred; link optimization; Premium impact; Bookmark; video; content ratio; Twitter Cards + SEO.
- **channels-email-marketing** — EDM vs Newsletter; five content types; deliverability (SPF/DKIM/DMARC); article delivery (Retention, ToFu, MoFu) + SEO synergy.
- **channels-referral** — Mechanism types (link/code/social); tracking and attribution; fraud prevention; design framework; implementation (dashboard vs landing page, self-build vs third-party); Referral vs affiliate.
- **channels-community-forum** — Forum promotion (Indie Hacker, HN, Hackernoon); community invitation (welcome email, CTA, banner, EDM, Discord); vertical communities; brand basics (encyclopedia, Q&A).
- **analytics-seo-monitoring** — SEO data analysis system: indexing, traffic, keywords, backlinks; benchmark; article database; tool selection; penalty recovery; work document management.
- **analytics-traffic** — Traffic diversification (search <75%), natural traffic benchmark.
- **analytics-tracking** — User ID, CTA attribution for article ROI.
- **channels-egc** — Employee-generated content, employee advocacy; 8x engagement, LinkedIn 561% reach.
- **strategies-integrated-marketing** — IMC, PESO model, program vs channel vs campaign, channel evaluation.
- **components-top-banner** — Announcement bar, sticky banner; lead capture, promo, urgency; 3-second rule.
- **components-sidebar** — Sidebar for blogs/docs; nav, CTA, related content; conversion data (prefer in-content).
- **components-popup** — Popup/modal; timing, triggers; mobile/SEO considerations; easy-exit pattern.
- **components-favicon** — Favicon, app icons, PWA; sizes 16-512px; SVG/PNG/ICO.
- **components-brand-visual** — Visual identity: typography, colors, spacing; Section 12 template.
- **pages-media-kit** — Brand guidelines, logo assets, usage rules; Related Skills: logo, favicon, brand-visual.
- **pages-article** — Optimization Foundation: Product + Keywords + Article intent + Competitor articles (four inputs).
- **seo-content-content-strategy** — Content types + SEO fit; evergreen vs timely mix (70–75% / 25–30%).
- **product-marketing-context** — Section 11: article orientations; Section 12: Visual Identity (colors, typography, spacing).

### Added

- **docs/description-rules.md** — Description optimization guidelines.
- **docs/description-optimization-suggestions.md** — Optimization suggestions per skill.
- **docs/compliance-audit-report.md** — Compliance audit report.

### Fixed

- **integrated-marketing** — Replaced Chinese in description with English.
- **Related Skills** — Fixed 22 incorrect references (category-page-generator, google-search-console, etc.).
- **components-logo, components-hero, pages-404** — Encoding fix; Related Skills: media-kit, favicon, brand-visual.
- **SKILLS_GUIDE.md** — Updated skill count (70 → 83).
- **strategies-integrated-marketing** — Added channels-community-forum to Related Skills.
- **analytics-google-search-console** — Fixed shorthand reference (backlink-analysis → seo-off-page-backlink-analysis).
- **channels-directories** — Fixed shorthand reference (link-building → seo-off-page-link-building).

### Removed

- **Temporary docs** — Deleted skill-naming-optimization-plan (v1–v4), skill-naming-compliance-audit. Kept naming-rules.md.

## [2025-02-28]

### Fixed

- **Encoding** — Replaced corrupted Unicode (en-dash, arrows, symbols) with ASCII in 12 skills: content-strategy, toc, navigation-menu, footer, category-pages, features, resources, customer-stories, products, glossary, blog, heading. Prevents future mojibake.

### Changed

- **seo-on-page-metadata** — Split into title, description, open-graph, twitter-cards; metadata now hreflang, robots, viewport only
- **seo-on-page-schema** — Schema mapping by product type; GEO; Recipe; validation workflow
- **product-marketing-context** — Section 11: content strategy (product connection, keywords, competitor URLs)
- **pages-article** — Product connection; competitor analysis; featured image guidelines
- **pages-blog** — Subdomain vs subdirectory; content strategy; TOC, CTA, related posts
- **seo-content-content-strategy** — Topic clusters (pillar + 6–12 clusters); internal linking; English only

### Added

- **CHANGELOG.md**
- **Creator greeting** — Intro on first use; contact info
- **skills-task-progress.md** — Task tracking template
- **platforms-grokipedia** — Grokipedia, parasite SEO, GEO
- **channels-directories** — Directory submission (Taaft, Product Hunt)
- **docs/using-beyond-cursor.md** — Use skills in Lovable, Bolt, v0, ChatGPT, Gemini
- **components-breadcrumb** — BreadcrumbList schema; types; multi-path
- **pages-article** — Article page structure; SEO; schema; GEO; internal linking
- **components-social-share** — Share buttons; intent URLs; platform sizes
- **seo-content-optimization** — Word count; H2 keywords; density; tables; lists
