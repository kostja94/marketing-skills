# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## Update Rules

- **Format**: `## [YYYY-MM-DD] <version>` — date first, then version.
- **Order**: Newest first. Unreleased at top; then by date descending.

## [Unreleased]

_None._

## [2026-03-07] v2.3.11

### Added

- **education-program** — Student/education discount channel; verification (.edu, SheerID, UNiDAYS); placement priority (registration P0, pricing P1, homepage P1, standalone P2); discount structure (first-time vs renewal); page strategy (embed vs standalone).
- **SECURITY.md** — Security audit, prompt injection checks, verification steps; moved to docs/.
- **pricing-page-generator** — Pricing Visibility & Placement: public vs hidden pricing; marketing site vs in-app billing; Enterprise/Contact sales; API/usage pricing; Special programs; conversion psychology; placement for student discount (registration P0, pricing P1).
- **Competitor brand keyword ads** — google-ads: Competitor Brand Keywords section (LP not blog); alternatives-page-generator: LP preferred for paid ads; paid-ads-strategy: Competitor Brand Bidding; landing-page-generator: Comparison type for competitor ads.

### Changed

- **pricing-page-generator** — Expand structure (pricing model selector, Enterprise, API, Special programs); add Pricing Models, Enterprise & API Pricing, Conversion Psychology; expand Output Format and Related Skills.
- **startups-page-generator** — Add Placement (embed vs standalone vs registration); education-program in Related Skills.
- **discount-marketing-strategy** — education-program in Campaign Types and Related Skills.
- **website-structure** — Pricing placement principle; education-program in Growth Strategy; pricing visibility note in Page Priority.
- **README** — Security section; SECURITY in Project Docs; Channels 9→10 (education-program).
- **skills-list, skills-relationships** — education-program; Channels diagram.

## [2026-03-06] v2.3.10

### Added

- **layout/carousel** — Carousel/slider layout; when to use vs grid/list/masonry; testimonials, logos, featured rotation; accessibility (keyboard nav, user control); SEO (content in DOM at load).

### Changed

- **testimonials-generator** — Carousel design/accessibility moved to **carousel**; add carousel to Related Skills.
- **showcase-page-generator** — Add carousel to Related Skills (Format: grid, masonry, carousel).
- **masonry** — Add Carousel to Masonry vs Grid vs Bento table; add carousel to Related Skills.
- **grid, card, list** — Add carousel to Related Skills; card adds Carousel to Grid vs List vs Masonry table.
- **category-pages, integrations, template-page, products, features, tools, resources** — Add grid/list to Related Skills.
- **landing-page-generator** — Add grid, list to Components Related Skills.
- **brand-visual, article, url-slug, favicon, directories** — Remove year from Best Practices section titles.

## [2026-03-06] v2.3.9

### Added

- **site-crawlability** — Infinite scroll search-friendly: component pages, full URLs, pushState, no overlap, 404 for out-of-bounds. Reference: [Google infinite scroll](https://developers.google.com/search/blog/2014/02/infinite-scroll-search-friendly).
- **layout/card** — Card layout component; anatomy, use cases (product, template, tool, feature, gallery, integration), responsive grid, design principles. Page skills (products, template, tools, features, showcase, integrations, category, resources) reference card.
- **layout/grid** — Grid layout; equal-hierarchy, multi-column; when to use vs list.
- **layout/list** — List layout; linear, stacked; blog index, docs, F-pattern.
- **layout/masonry** — Masonry layout; varying heights; gallery, portfolio, Pinterest-style.

### Changed

- **site-crawlability** — Expand Pagination/Infinite scroll with Google recommendations; add triggers: infinite scroll, pagination, masonry SEO.
- **masonry** — Add SEO Considerations: masonry + infinite scroll = not crawlable; link to site-crawlability.
- **list** — Add Infinite Scroll section; link to site-crawlability.
- **grid** — Add Infinite Scroll section; link to site-crawlability.
- **hero-generator** — Add Layout Types (split 50/50, 75/25, 25/75, centered, full-width image), Alignment (horizontal, vertical), responsive behavior. Add triggers: split layout hero, centered hero, hero alignment.
- **components** — Restructure to nested folders: `navigation/` (nav, breadcrumb, footer, sidebar, toc), `conversion/` (cta, popup, newsletter-signup, trust-badges, testimonials), `branding/` (logo, favicon, brand-visual, hero), `content/` (tab-accordion), `layout/` (card, grid, list, masonry), `utility/` (top-banner, social-share, url-slug). Aligns with pages/, seo/, paid-ads/ structure. skills-list, skills-guide, skills-relationships updated.

## [2026-03-05] v2.3.8

### Changed

- **brand-protection** — Expand reporting channels: Google Trademark, Bing Content Removal, payment processors, social platforms; add Cloudflare-specific guidance, hosting detection, reporting best practices; add references.

## [2026-03-05] v2.3.7

### Changed

- **brand-protection** — Merge brand-impersonation-response-plan content (implementation checklist, references); remove standalone doc.
- **press-coverage** — Move press-coverage-page.md from docs/ to skills/pages/marketing/press-coverage/reference.md; add SKILL ref.

### Removed

- docs/brand-impersonation-response-plan.md
- docs/press-coverage-page.md

## [2026-03-05] v2.3.6

### Added

- **brand-protection** — Impersonation response: evidence, reporting, support template, traffic recovery, implementation checklist, references.

### Changed

- **domain-selection** — Impersonation variants; brand-protection ref.
- **trust-badges, about-page, homepage, rebranding** — brand-protection in Related Skills.

## [2026-03-05] v2.3.5

### Changed

- **README** — References: group by Specification & Ecosystem, Platform & Human Guides, Project Docs; add Agent Skills spec, Vercel skills CLI; simplify doc links.

## [2026-03-05] v2.3.4

### Changed

- **github-seo** — Add Repository Name, About & README section: name/About/topics best practices; README structure (TOC, installation, usage, screenshots, badges); GEO practices (answer-first, short paragraphs, question headings); 350-char About limit; 6–20 topics; checklist.

## [2026-03-05] v2.3.3

### Changed

- **title-tag, meta-description** — CJK: title 25–35 (was 25–30); meta description 75–100 (was 70–80). Add pixel-width note; recommend pixel-accurate checker for CJK (font/locale variance).

## [2026-03-05] v2.3.2

### Changed

- **analytics-tracking** — GA4 event name: 40 chars (hard limit), not 60.
- **linkedin-posts** — Fix typos: 100→00 → 100–200; 300→,200 → 300–1,200; 1,300→,600 → 1,300–1,600; →MB → ≤10 MB; →10 → ≤210.
- **directory-submission** — Short description: 150–300 chars (was 150–255 vs 150–300).
- **twitter-x-posts** — Link preview: title ≤70 chars, description ≤200 chars (was <60, <100).

## [2026-03-05] v2.3.1

### Changed

- **title-tag** — Length 50–60 chars (Latin); add Length by Language (CJK 25–30, Cyrillic 50–55, Arabic 30–40); pixel-width note.
- **meta-description** — Length 150–160 chars (Latin); add Length by Language (CJK 70–80, Cyrillic 140–155, Arabic 70–90); localization-strategy, translation refs.

## [2026-03-05] v2.3.0

### Added

- **distribution-channels** — Marketplace listing, channel mix, Pinterest Product Pins.
- **research-sources** — Information sources for content ideation, competitor/industry tracking; generic examples.
- **growth-funnel** — AARRR framework, tactics by stage, post-campaign analysis.
- **cold-start-strategy** — Finding Users: demand-signal outreach (social, Fiverr/Upwork, comment outreach).
- **community-forum** — Community invite, forum promotion, brand encyclopedia.
- **content-strategy** — Structure and content equally important.
- **content-marketing** — Product marketing content (QA, use guide, maintenance, troubleshooting).
- **website-structure** — Clear navigation principle.
- **integrated-marketing** — Customer journey by stage (Awareness → Advocacy).
- **discount-marketing** — Promotional materials (banner, brochure, stickers, website prep).
- **conversion-optimization, analytics-tracking** — Commercialization infrastructure (data warehouse, A/B test, attribution).
- **pmf-strategy** — Product research & SaaS context; enterprise challenges.
- **gtm-strategy** — Enterprise / high-ACV challenges.
- **retention-strategy** — User value & feedback.
- **creator-program** — Ecosystem operations.

### Changed

- **community-forum** — Removed China-specific content (Zhihu, Douban, Tieba, Baidu, etc.); generic regional wording.
- **skills-list, skills-task-progress** — Added distribution-channels, research-sources, growth-funnel.

## [2026-03-05] v2.2.0

### Added

- where-to-use-skills.md, use-cases-and-roadmap.md; paid-ads/ (9 skills); domain/ (3 skills); tools-page-generator, file-naming.md.

### Changed

- README, skills-list; Features vs Use cases vs Solutions; platform ↔ paid-ads linkage.

### Removed

- using-beyond-cursor.md, platforms-with-skills.md → merged into where-to-use-skills.md.

## [2026-03-01] v2.1.0

- Description optimization (83 skills); page taxonomy merged into skills-list.

## [2026-03-01] v2.0.0

- Skill naming v4; description-rules.md, docs/README.md.

## [2026-02-28] Initial

- CHANGELOG, skills-task-progress, core skills; seo-on-page split; product-marketing-context.
