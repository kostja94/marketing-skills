---
name: seo-audit
description: When the user wants to run an SEO audit, technical SEO audit, or site health check. Also use when the user mentions "SEO audit," "technical audit," "site audit," "crawl audit," "indexing audit," "SEO health," or "fix SEO issues." For prioritization and organic strategy, use seo-strategy. For GSC data analysis, use google-search-console.
metadata:
  version: 1.1.0
---

# Strategies: SEO Audit

Guides end-to-end SEO audit: technical foundation, on-page, content, and off-page. Execute in order—technical blockers prevent indexing; on-page limits rankings; content and off-page build authority. Use when auditing an existing site or planning fixes.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Audit Order

| Phase | Focus | Skills |
|-------|-------|--------|
| **1. Technical** | Crawl, index, sitemap | robots-txt, xml-sitemap, canonical-tag, indexing, site-crawlability |
| **2. On-Page** | Metadata, structure, schema | title-tag, meta-description, page-metadata, schema-markup, internal-links, heading-structure |
| **3. Content** | Gaps, intent, optimization | keyword-research, content-strategy, content-optimization |
| **4. Off-Page** | Backlinks, authority | link-building, backlink-analysis |

**Principle**: Fix foundation before optimizing pages. See **seo-strategy** for workflow and prioritization.

## Technical Checklist

| Item | Check | Skill |
|------|-------|-------|
| **robots.txt** | Syntax; not blocking important pages | robots-txt |
| **Sitemap** | Submitted to GSC; indexable pages only; ≤50K URLs per sitemap | xml-sitemap |
| **HTTPS** | Sitewide; valid certificate | canonical-tag |
| **404/5xx** | Proper status codes; fix or redirect | site-crawlability |
| **noindex** | No accidental noindex on key pages | indexing |
| **Canonical** | Correct; no conflicts | canonical-tag |
| **Core Web Vitals** | LCP ≤2.5s, INP ≤200ms, CLS <0.1 | core-web-vitals |
| **Mobile** | Mobile-first; content parity; no intrusive interstitials | mobile-friendly |
| **Crawlability** | Redirect chains, broken links, orphan pages | site-crawlability |

## On-Page Checklist

| Item | Check | Skill |
|------|-------|-------|
| **Title** | Unique; 50–60 chars; keyword in first 10 words | title-tag |
| **Meta description** | 150–160 chars; CTA | meta-description |
| **Headings** | One H1; H1→H2→H3 hierarchy | heading-structure |
| **Images** | Alt text; no decorative alt for decorative images | image-optimization |
| **Schema** | Valid; Rich Results Test | schema-markup |
| **Internal links** | From strong pages; descriptive anchors | internal-links |
| **Duplicate content** | Canonical; consolidate or differentiate | canonical-tag |

## Content & Off-Page

| Phase | Focus | Skill |
|-------|-------|-------|
| **Content gap** | Missing topics vs competitors | content-strategy, competitor-research |
| **Intent match** | Content matches search intent | content-optimization |
| **Backlinks** | Toxic links; link gap vs competitors | backlink-analysis, link-building |

## Frequency

| Cadence | Use |
|---------|-----|
| **Full audit** | Quarterly |
| **Check-ins** | Monthly (GSC, indexing, Core Web Vitals) |

## Output Format

- **Phase 1–4 findings** (technical → on-page → content → off-page)
- **Priority list** (P0 blocker → P1 core → P2 important)
- **Skill mapping** (which skill for each fix)
- **Timeline** (immediate vs short-term vs ongoing)

## Related Skills

- **seo-strategy**: Workflow order, prioritization, when to invest in SEO
- **google-search-console**: Performance, indexing, Core Web Vitals data
- **site-crawlability**: Redirect chains, broken links, crawl budget
- **indexing**: Indexing issues, noindex, Search Console
- **core-web-vitals**: LCP, INP, CLS optimization
