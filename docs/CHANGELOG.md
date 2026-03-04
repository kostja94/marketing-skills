# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added

- **where-to-use-skills.md** — Platform guide: native (Cursor, Claude Code, Codex, OpenCode, Gemini CLI, GitHub Copilot, Windsurf, Cline, Base44, Trae), AGENTS.md (Lovable, Replit), paste (v0, Bolt, Medo, ChatGPT, Gemini), CLI (AMP, KiloCode, Roo, Goose, Kiro, OpenClaw). Official docs links, path reference.
- **use-cases-and-roadmap.md** — Use cases (personal site, product website, vibe coding, fork & adapt, partnership), content roadmap, non-website agent future.
- **README** — Use Cases section; logical reorder (Installation → Where to Use → Structure → Usage → Context → Skills → Workflow); 40+ agents.
- **CONTRIBUTING** — Fork & adapt guidance for building your own skills.

### Changed

- **README** — Replaced using-beyond-cursor with where-to-use-skills; skills.sh 20+ → 40+ agents; Medo (replaces Miaoda).
- **docs/README** — Added use-cases-and-roadmap, where-to-use-skills.
- **Skills** — Cross-references: branding, content-marketing-strategy, eeat-signals, competitor-research; page taxonomy updates.
- **solutions-page-generator, use-cases-page-generator** — Clearer distinction: Solutions = industry-first (by industry, company size, team); Use cases = scenario-first (by scenario, persona, business goal). Common industries, company size segments, decision table. Use cases as sub-pages under solutions.
- **features-page-generator** (v1.1.0), **use-cases-page-generator** (v1.2.0) — Features vs Use cases differentiation: avoid overlap and content cannibalization. Features = What (capability-first, no scenario narratives); Use cases = When/How (scenario-first, link to features, don't duplicate). Organization: features by capability (not by use case); use cases: Content Differentiation section.
- **page-taxonomy, skills-list** — Features vs Use cases vs Solutions triad; content angle differentiation to avoid cannibalization.
- **website-structure** — Structure Principles: Features vs Use cases linking and content division.
- **tools-page-generator** (new) — Free tools pages: lead gen, not primary monetization; same ICP; toolkit hub; programmatic SEO; Tools vs Features distinction. Tool types (calculators, checkers, converters, generators); gate strategy; SPA-friendly.
- **page-taxonomy, skills-list** — Tools page; Tools vs Features; Product/SaaS extended pages.
- **programmatic-seo** — Free tools as use case; Semrush/Ahrefs examples.
- **website-structure, landing-page, resources-page-generator, features-page-generator** — Tools integration.
- **domain-architecture** (new) — Subfolder vs subdomain vs independent domain; brand architecture (Branded House / House of Brands); Hub-Spoke principles.
- **rebranding-strategy** (new) — Rebranding: domain change, 301 redirects, migration checklist, social media announcement, internal communication.
- **multi-domain-brand-seo** (new) — Multi-domain brand search: Hub ranks first for brand queries; Hub-Spoke differentiation; Schema Organization subOrganization.
- **skills-list** — Added domain-architecture, rebranding-strategy, multi-domain-brand-seo.
- **seo-strategy** — Alternative SEO Strategies: multi-domain-brand-seo; Related Skills: domain-architecture, rebranding-strategy, multi-domain-brand-seo.
- **website-structure** — Domain structure section; cross-ref to domain-architecture.
- **branding** — Related Skills: domain-architecture, rebranding-strategy.
- **domain-selection** (new) — Initial domain choice: Brand vs PMD vs EMD, TLD (.ai, .com, .io), length, readability, history check, defensive registration; .ai domain natural backlinks. Reference: [Alignify 域名SEO](https://alignify.co/zh/seo/domain).
- **skills-list** — Added domain-selection.
- **seo-strategy** — New site workflow: domain-selection → website-structure; Related Skills: domain-selection.
- **website-structure** — Domain structure section: cross-ref to domain-selection; Related Skills: domain-selection.
- **domain-architecture** — Related Skills: domain-selection; intro cross-ref to domain-selection.
- **rebranding-strategy** — Related Skills: domain-selection; intro cross-ref to domain-selection.
- **alternatives-page-generator** (v1.1.0) — Purpose, keywords, competitor types (Direct/Bundlers/Indirect); URL structure; problem-focused intro; HTML table for AEO/GEO; brand keyword ads + PPC landing page; programmatic SEO; measurement metrics.
- **strategies/** — Reorganized by theme: `domain/` (domain-selection, domain-architecture, multi-domain-brand-seo), `pricing/` (pricing-strategy, discount-marketing). Improves granularity consistency.
- **skills-list, CONTRIBUTING, skills-guide, skills-relationships** — Updated paths for strategies/domain/* and strategies/pricing/*.
- **SKILLS_GUIDE.md** → **skills-guide.md** — Lowercase for cross-platform compatibility; docs use lowercase per [Google style](https://developers.google.com/style/filenames).
- **file-naming.md** (new) — Documents why README, CONTRIBUTING, CHANGELOG, SKILL, LICENSE use uppercase (tool/spec conventions).

### Removed

- **using-beyond-cursor.md**, **platforms-with-skills.md** — Merged into where-to-use-skills.md.

## [2.1.0] - 2025-02-28

### Changed

- Description optimization (83 skills); page taxonomy merged into skills-list.

## [2.0.0] - 2025-02-28

### Changed

- Skill naming v4 (83 skills); 18+ skill content updates.

### Added

- description-rules.md, docs/README.md.

## [2025-02-28]

### Added

- CHANGELOG, skills-task-progress, using-beyond-cursor, platforms-grokipedia, channels-directories, components-breadcrumb, components-social-share, pages-article, seo-content-optimization.

### Changed

- seo-on-page split; product-marketing-context; pages-article, pages-blog, content-strategy.
