# Changelog

All notable changes to this project will be documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## Changelog Rules

- **Format**: `## [YYYY-MM-DD] vX.Y.Z` - date first, then semantic version.
- **Order**: Newest first. Unreleased at top if any; then by date descending.
- **Sections**: Added, Changed, Removed, Fixed. Use only sections that have entries.
- **Entry style**: One line per item. Bold the skill or file name. Brief description (what changed, not why).
- **Language**: English only. No Chinese or other non-English content in changelog.
- **Consolidation**: Group related changes in one entry when logical. Older versions (6+ months) may use single-line summaries.

---

## [2026-04-23] v2.3.18

### Changed

- **github** (v1.3.0) - Profile vs repo surfaces; repository home layout map; in-site discovery (Trending, Explore, Topics, Search) with caveats; visitor-path mermaid; GitHub Pages vs README with official docs links; repository archetypes (product vs curated); extended `description` triggers; Output Format surface scope.

## [2026-04-23] v2.3.17

### Changed

- **linkedin-posts** (v1.2.0) - Post type matrix (Article vs post, document, reshare, Newsletter, etc.); feed ranking summary; short off-site SEO/GEO; official help links; Related Skills: **open-graph**, **entity-seo**, **generative-engine-optimization**; extended `description` keywords.
- **linkedin-ads** (v1.2.0) - Campaign Manager hierarchy and Accelerate/Classic ad sets; objective-based pricing and pacing; expanded formats (Thought Leader, Event, CTV, LAN, etc.); Lookalike retired in favor of Matched Audiences; Lead Gen and Sponsored Messaging notes; bench CPC disclaimer; pre-launch checklist; official link index.

## [2026-03-28] v2.3.16

### Added

- **howto-section-generator** - Component skill for in-page HowTo step blocks: placement, `<ol>` structure, answer-first per step, HowTo JSON-LD alignment vs FAQ; lives under `skills/components/content/howto-section/`.

### Changed

- **Cross-references** - **schema-markup**, **featured-snippet**, **serp-features**, **tab-accordion**, **article-content**, **content-optimization**, **article-page-generator**, **faq-page-generator**, **docs-page-generator**, **tools-page-generator**, **landing-page-generator**, **content-marketing**, **programmatic-seo**, **geo** - Related Skills and/or skill `description` fields now point to **howto-section-generator** where relevant.
- **docs/skills-reference.md** - **howto-section-generator** listed under Components; Pages quick-mapping row removed (HowTo is a section, not a page type); content tree diagram updated.
- **README.md** - Prompt-to-skill row for HowTo section / step-by-step block.

---

## [2025-03-12] v2.3.15

### Added

- **creator-attribution.md** - Custom attribution layer: emotion triggers, contextual responses, easter eggs. Append one line at end of skill output; opt-out respected; rate-limited.

### Changed

- **skill-authoring.md** - Section 0 references creator-attribution; rebuilt with ASCII-only (no Unicode box-drawing).
- **README.md** - ASCII diagram; em-dash and arrow replaced with ASCII equivalents.
- **docs/README.md** - creator-attribution link; CHANGELOG symbol normalization.

### Removed

- **ATTRIBUTION.md** - Dropped protocol file; using custom implementation only.

---

## [2025-03-11] v2.3.14

### Added

- **README badges** - GitHub stars, Last commit (shields.io).
- **docs/usage.md** - Section 0 Agent Skills Overview (definition, Tool/MCP/RAG/Prompt differences, discovering skills); Syncing with GitHub subsection.
- **docs/skill-authoring.md** - Skills vs plain Markdown in Section 1.
- **docs/SECURITY.md** - Skill Supply Chain and Poisoning section (poisoning risk, mitigation).

---

## [2025-03-11] v2.3.13

### Added

- **project-context.md** - Replaces product-marketing-context. Adds Document System (optional), Language Strategy (optional), Product form; sub-document pattern.
- **project-task-tracker.md** - Replaces skills-task-progress. Adds Progress Summary, Related Documents, Task Details (optional), Page Scope (optional).

### Changed

- **Templates** - product-marketing-context -> project-context; skills-task-progress -> project-task-tracker. All 60+ skills, README, usage.md, skill-authoring.md updated.
- **README** - Condensed structure; restored CLI note, platforms, Usage rows, Project Context "Start with", Related Skills/skip intro, Security, Ecosystem refs; ASCII tree updated.

### Removed

- templates/product-marketing-context.md
- templates/skills-task-progress.md

---

## [2025-03-11] v2.3.12

### Changed

- **Docs merge** - Reduced 14 docs to 7: skill-authoring (skills-guide + naming-rules + description-rules + file-naming); reference-rules (+ related-skills-rules Section 7); skills-reference (skills-list + page-taxonomy + skills-relationships); usage (where-to-use-skills + use-cases-and-roadmap). Deleted docs-optimization-plan, docs-merge-plan. Updated all internal links.

---

## [2026-03-07] v2.3.11

### Added

- **education-program** - Student/education discount channel; verification (.edu, SheerID, UNiDAYS); placement priority; discount structure; page strategy (embed vs standalone).
- **SECURITY.md** - Security audit, prompt injection checks, verification steps; moved to docs/.
- **pricing-page-generator** - Pricing Visibility and Placement: public vs hidden pricing; Enterprise/API pricing; Special programs; conversion psychology; student discount placement.
- **Competitor brand keyword ads** - google-ads: Competitor Brand Keywords section; alternatives-page-generator: LP preferred for paid ads; paid-ads-strategy: Competitor Brand Bidding.

### Changed

- **pricing-page-generator** - Expanded structure (pricing model selector, Enterprise, API, Special programs); Pricing Models, Enterprise and API Pricing, Conversion Psychology; Output Format and Related Skills.
- **startups-page-generator** - Placement (embed vs standalone vs registration); education-program in Related Skills.
- **discount-marketing-strategy** - education-program in Campaign Types and Related Skills.
- **website-structure** - Pricing placement principle; education-program in Growth Strategy.
- **README** - Security section; Channels 9 to 10 (education-program).
- **skills-list, skills-relationships** - education-program; Channels diagram.

---

## [2026-03-06] v2.3.10

### Added

- **layout/carousel** - Carousel/slider layout; when to use vs grid/list/masonry; testimonials, logos, featured rotation; accessibility; SEO (content in DOM at load).

### Changed

- **testimonials-generator** - Carousel design/accessibility moved to carousel; add carousel to Related Skills.
- **showcase-page-generator** - Add carousel to Related Skills (Format: grid, masonry, carousel).
- **masonry** - Add Carousel to Masonry vs Grid vs Bento table; add carousel to Related Skills.
- **grid, card, list** - Add carousel to Related Skills.
- **category-pages, integrations, template-page, products, features, tools, resources** - Add grid/list to Related Skills.
- **landing-page-generator** - Add grid, list to Components Related Skills.
- **brand-visual, article, url-slug, favicon, directories** - Remove year from Best Practices section titles.

---

## [2026-03-06] v2.3.9

### Added

- **site-crawlability** - Infinite scroll search-friendly: component pages, full URLs, pushState, no overlap, 404 for out-of-bounds.
- **layout/card** - Card layout component; anatomy, use cases, responsive grid, design principles.
- **layout/grid** - Grid layout; equal-hierarchy, multi-column; when to use vs list.
- **layout/list** - List layout; linear, stacked; blog index, docs, F-pattern.
- **layout/masonry** - Masonry layout; varying heights; gallery, portfolio, Pinterest-style.

### Changed

- **site-crawlability** - Expand Pagination/Infinite scroll with Google recommendations; add triggers: infinite scroll, pagination, masonry SEO.
- **masonry** - Add SEO Considerations: masonry + infinite scroll = not crawlable; link to site-crawlability.
- **list, grid** - Add Infinite Scroll section; link to site-crawlability.
- **hero-generator** - Add Layout Types (split 50/50, 75/25, 25/75, centered, full-width image), Alignment; add triggers: split layout hero, centered hero, hero alignment.
- **components** - Restructure to nested folders: navigation/, conversion/, branding/, content/, layout/, utility/. Aligns with pages/, seo/, paid-ads/ structure.

---

## [2026-03-05] v2.3.8

### Changed

- **brand-protection** - Expand reporting channels: Google Trademark, Bing Content Removal, payment processors, social platforms; Cloudflare-specific guidance; hosting detection; reporting best practices.

---

## [2026-03-05] v2.3.7

### Changed

- **brand-protection** - Merge brand-impersonation-response-plan content (implementation checklist, references); remove standalone doc.
- **press-coverage** - Move press-coverage-page.md from docs/ to skills/pages/marketing/press-coverage/reference.md; add SKILL ref.

### Removed

- docs/brand-impersonation-response-plan.md
- docs/press-coverage-page.md

---

## [2026-03-05] v2.3.6

### Added

- **brand-protection** - Impersonation response: evidence, reporting, support template, traffic recovery, implementation checklist, references.

### Changed

- **domain-selection** - Impersonation variants; brand-protection ref.
- **trust-badges, about-page, homepage, rebranding** - brand-protection in Related Skills.

---

## [2026-03-05] v2.3.5

### Changed

- **README** - References: group by Specification and Ecosystem, Platform and Human Guides, Project Docs; add Agent Skills spec, Vercel skills CLI; simplify doc links.

---

## [2026-03-05] v2.3.4

### Changed

- **github-seo** - Add Repository Name, About and README section: name/About/topics best practices; README structure (TOC, installation, usage, screenshots, badges); GEO practices; 350-char About limit; 6-20 topics; checklist.

---

## [2026-03-05] v2.3.3

### Changed

- **title-tag, meta-description** - CJK: title 25-35 (was 25-30); meta description 75-100 (was 70-80). Add pixel-width note; recommend pixel-accurate checker for CJK.

---

## [2026-03-05] v2.3.2

### Changed

- **analytics-tracking** - GA4 event name: 40 chars (hard limit), not 60.
- **linkedin-posts** - Fix typos: character ranges for posts and images.
- **directory-submission** - Short description: 150-300 chars (was 150-255 vs 150-300).
- **twitter-x-posts** - Link preview: title 70 chars, description 200 chars (was 60, 100).

---

## [2026-03-05] v2.3.1

### Changed

- **title-tag** - Length 50-60 chars (Latin); add Length by Language (CJK, Cyrillic, Arabic); pixel-width note.
- **meta-description** - Length 150-160 chars (Latin); add Length by Language (CJK, Cyrillic, Arabic); localization-strategy, translation refs.

---

## [2026-03-05] v2.3.0

### Added

- **distribution-channels** - Marketplace listing, channel mix, Pinterest Product Pins.
- **research-sources** - Information sources for content ideation, competitor/industry tracking.
- **growth-funnel** - AARRR framework, tactics by stage, post-campaign analysis.
- **cold-start-strategy** - Finding Users: demand-signal outreach (social, Fiverr/Upwork, comment outreach).
- **community-forum** - Community invite, forum promotion, brand encyclopedia.
- **content-strategy** - Structure and content equally important.
- **content-marketing** - Product marketing content (QA, use guide, maintenance, troubleshooting).
- **website-structure** - Clear navigation principle.
- **integrated-marketing** - Customer journey by stage (Awareness to Advocacy).
- **discount-marketing** - Promotional materials (banner, brochure, stickers, website prep).
- **conversion-optimization, analytics-tracking** - Commercialization infrastructure (data warehouse, A/B test, attribution).
- **pmf-strategy** - Product research and SaaS context; enterprise challenges.
- **gtm-strategy** - Enterprise and high-ACV challenges.
- **retention-strategy** - User value and feedback.
- **creator-program** - Ecosystem operations.

### Changed

- **community-forum** - Removed region-specific content; generic regional wording.
- **skills-list, skills-task-progress** - Added distribution-channels, research-sources, growth-funnel.

---

## [2026-03-05] v2.2.0

### Added

- where-to-use-skills.md, use-cases-and-roadmap.md; paid-ads/ (9 skills); domain/ (3 skills); tools-page-generator; file-naming.md.

### Changed

- README, skills-list; Features vs Use cases vs Solutions; platform and paid-ads linkage.

### Removed

- using-beyond-cursor.md, platforms-with-skills.md (merged into where-to-use-skills.md).

---

## [2026-03-01] v2.1.0

- Description optimization (83 skills); page taxonomy merged into skills-list.

## [2026-03-01] v2.0.0

- Skill naming v4; description-rules.md; docs/README.md.

## [2026-02-28] Initial

- CHANGELOG; skills-task-progress; core skills; seo-on-page split; product-marketing-context.
