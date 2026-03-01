# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added

- **download-page-generator** — Download page for desktop and mobile app: value proposition, platform selection (OS detection, App Store/Play Store), trust signals, CTA; optimization best practices (performance, conversion, trust) in skill.
- **page-taxonomy** — Page purpose reference: 品牌 (Brand), 营销-SEO/SEM, 功能使用 (Functional: Dashboard, SPA), 引导下载 (Download); SEM, Functional, Download dimensions; Download page in Marketing mapping.
- **docs-page-generator** — Documentation site structure (docs.* subdomain): Getting Started, guides, tutorials, API Reference (endpoint docs), knowledge base; sidebar, search, versioning.
- **changelog-page-generator** — Changelog/release notes: version history, updates; changelog.* or /changelog; trust, support reduction, feature adoption.
- **status-page-generator** — Status page for service health, uptime, incidents; status.* subdomain; reduces support during outages.
- **use-cases-page-generator** — Use case pages: bridge features → real problems; by ICP, industry, role; BOFU for SaaS/B2B.
- **solutions-page-generator** — Solutions pages: outcome-focused; "how does this solve my problem?"; by industry, team, outcome.
- **page-taxonomy** — Website-type dimension: Product/SaaS, B2B, E-commerce, Portfolio, Forum, Directory; page applicability matrix; subdomain conventions (docs, changelog, status, developer); Core vs Extended distinction.
- **website-structure** — Plan which pages to build, page priority (Must Have/Great to Have/Optional), generic template, growth→structure mapping; Alignify website structure guide.
- **github-seo** — GitHub for parasite SEO, GEO, and curated lists: repos, README, GitHub Pages, gists; Awesome-style navigation lists (awesome-*); Tier 2 technical authority; very high AI citation.
- **parasite-seo** — Parasite SEO strategy: high-authority platforms (Medium, Reddit, LinkedIn, Grokipedia); platform tiers; Site Reputation Abuse compliance. Moved parasite SEO content from grokipedia and geo. **Optimized**: barnacle SEO alias; tiered platform framework (Tier 1–6); keyword targeting, on-page optimization; tier-2 backlinks; content clustering; YouTube, Quora, Google Sites; common mistakes.
- **programmatic-seo** — Programmatic SEO strategy: template + data pages at scale; use cases (location, comparison, integration); pitfalls (thin content, index bloat); 300+ words, internal linking. **Optimized**: template structure (Intro, Evidence, Decision, FAQ, CTA); evidence block; data freshness rules, provenance; selective indexation; step-by-step workflow; best practices; common pitfalls.
- **cold-start-strategy** — Cold start strategy for first users: Product Hunt, AppSumo, Reddit, Indie Hackers, directories; multi-channel launch; pre-launch validation. Moved cold-start content from directory-submission and community-forum.
- **landing-page-generator** — Generic landing page structure (5-step flow), CTA, conversion; Landing Page ↔ Page Types mapping (content pull, CTA destination, internal linking); expanded Related Skills across pages.

### Removed

- **api-reference-generator** — API Reference is a section within docs, not a standalone page type; merged into docs-page-generator.

### Changed

- **docs-page-generator** — API Reference (endpoint docs) is now part of docs; no separate api-reference skill.
- **docs/** — Skills count 83→88 in docs/README, SKILLS_GUIDE; reference-rules §7+§8 merged into "Validation Checklist & Migration"; reference-rules Quick reference added; Contributor Docs usage hints.
- **Root/templates/tools** — page-types-taxonomy moved to docs/page-taxonomy.md (resolves duplication with skills-list); templates/README added; tools/README product refs simplified; README Project Structure updated; CONTRIBUTING links to description-rules.
- **README** — Hero merged to 2 paragraphs; Linking + Project Context merged; deduplication (88, generic, workflow); Using Beyond Cursor compressed; Tips simplified; References table consolidated; ASCII diagram rebuilt for clarity.
- **Product/website references** — Per reference-rules §6: reduced product examples to essential only; added no-endorsement disclosure where 3+ examples; prefer generic terms (e.g. "SEO tools", "affiliate tracking platforms"); affiliate, creator-program, directories, geo, grokipedia, keyword-research, parasite-seo, logo, programmatic-seo, seo-monitoring, article, localization, backlink-analysis, affiliate-program.
- **affiliate-marketing** — Pitfalls (fraud, brand bidding), recruitment strategies, implementation flow; tools simplified to generic (affiliate tracking platforms).
- **affiliate-page-generator** — Landing page best practices, post-launch (Affiliate.Watch), cross-reference landing-page-generator.
- **keyword-research** — Intent identification (modifiers, SERP), discovery methods (base + incremental), long-tail expansion, clustering (SERP/semantic/intent), pillar–cluster, screening order, principles. Product positioning test (XXX + function words, Input + to + Output); Agent/Copilot products. Multi-platform search: English platforms (Reddit, Quora, X, Hacker News).
- **localization-strategy** — Subdirectories over subdomains for i18n; multilingual risks (batch publishing, de-index). i18n SEO principles, URL structure options, hreflang checklist.
- **content-strategy** — On-page SEO essence; Product-Led SEO; products suited for SEO (tool, content, e-commerce, service).
- **integrated-marketing** — Growth metrics by stage; growth as means, monetization as goal.
- **traffic-analysis** — Branded vs non-branded organic traffic; bot traffic.
- **landing-page-generator** — Comparison, Use cases/Solutions page types for integrated products.
- **homepage-generator** — Positioning clarity; avoid vague brand-speak.
- **community-forum** — Examples: English platforms; cold-start reference. Cold-start strategy moved to cold-start-strategy.
- **directory-submission** — Cold-start framing moved to cold-start-strategy; added cold-start-strategy reference.
- **grokipedia-recommendations** — Parasite SEO content moved to parasite-seo; added parasite-seo reference.
- **generative-engine-optimization** — Parasite SEO section moved to parasite-seo; added parasite-seo reference.
- **reddit-posts** — Added parasite-seo to Related Skills.
- **twitter-x-posts** — Programmatic SEO mention clarified; added programmatic-seo reference.
- **category-page-generator** — Added programmatic-seo to Related Skills.
- **parasite-seo** — Added GitHub to platform notes; added github-seo reference.
- **generative-engine-optimization** — Added GitHub and github-seo reference.
- **directory-submission** — Awesome lists reference github-seo; added github-seo to Related Skills.
- **heading-structure** — Added page-metadata to Related Skills.
- **reddit-posts** — Added cold-start-strategy to Related Skills.
- **schema-markup** — Compressed GEO section; added generative-engine-optimization reference.
- **localization-strategy** — Added url-structure, content-strategy to Related Skills.
- **content-optimization** — GEO section simplified; TL;DR/QAE moved to article-page-generator; added references.
- **keyword-research** — Pillar-cluster references content-strategy for full planning.
- **article-page-generator** — Research Phase clarified as lightweight; references keyword-research, content-strategy for deep research.
- **internal-links** — Orphan pages reference site-crawlability for technical detection.
- **site-crawlability** — Orphan pages reference internal-links for link strategy.
- **content-strategy** — Initial Assessment references keyword-research for discovery.
- **creator-program, influencer-marketing** — Rebuilt from scratch to fix encoding (1â2 → 1–2, etc.).
- **docs/reference-rules.md** — Reference standardization: internal (**skill-name**), external (descriptive link text), References section, Alignify/Google conventions; **§6 Product and Website Examples**: quantity limit (≤5 per category), no-promotional-intent disclosure, neutral language.
- **brand-visual-generator** — Two-font system, industry color mapping, anti-patterns, accessibility checklist.
- **hero-generator** — Four essentials, 3-second rule, emotional intent.
- **logo-generator** — Brand guidelines linkage, clear space, responsive breakpoints.
- **page-metadata** — hreflang rules (self-reference, symmetric, x-default), common mistakes.
- **xml-sitemap** — Multi-language sitemap with hreflang per URL.
- **schema-markup** — inLanguage for multilingual sites.

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
