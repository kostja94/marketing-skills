---
name: seo-strategy
description: When the user wants to plan SEO strategy, prioritize SEO work, or understand the SEO workflow. Also use when the user mentions "SEO strategy," "SEO plan," "SEO roadmap," "SEO priority," "SEO audit," "SEO workflow," "where to start SEO," "SEO approach," "organic growth strategy," or "search strategy."
metadata:
  version: 1.0.0
---

# Strategies: SEO

Guides SEO strategy: workflow order, prioritization, Product-Led SEO, and when to use which skills. Use this skill when planning SEO from scratch, auditing an existing site, or deciding what to do next.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Workflow Order

**Fix foundation before optimizing pages.** Execute in this order:

| Phase | Focus | Skills |
|-------|-------|--------|
| **1. Technical** | Crawlability, indexing, sitemap | robots-txt, xml-sitemap, canonical-tag, indexing, indexnow, site-crawlability |
| **2. On-Page** | Metadata, structure, schema | title-tag, meta-description, page-metadata, schema-markup, internal-links, url-structure, heading-structure |
| **3. Content** | Keywords, clusters, optimization | keyword-research, content-strategy, content-optimization |
| **4. Off-Page** | Backlinks, authority | link-building, backlink-analysis |

Technical issues block indexing and crawl; on-page issues limit how well content ranks; content and off-page build authority over time.

## Product-Led SEO

SEO leverages content you already have—brand, features, scenarios, input, output, prompt, processes, knowledge—published in a structured way. Even without SEO, you'd showcase product features; SEO makes that content benefit you in traffic.

**Principle**: Do SEO around product/users, not around industry/search engines.

### Products Suited for SEO

| Type | Suited because |
|------|----------------|
| **Tool** | Users have clear use cases and needs |
| **Content** | Users have clear information needs |
| **E-commerce** | Users have clear purchase needs |
| **Service** | Users have clear service needs |

**Agent/Copilot products**: Pure native Agent hard to grow via SEO; users rarely search "agent." Release related features first (e.g., CRM, sales bot for sales agent) to build traffic, then funnel to Agent product. See **keyword-research** for product positioning test.

## SEO Audit Approach

| Scenario | Order | Focus |
|----------|-------|-------|
| **New site** | website-structure → Technical → On-Page → Content | Plan pages first; build foundation; add content |
| **Existing site** | Technical audit → On-Page audit → Content gap → Off-Page | Fix crawl/index first; then metadata, schema; then content gaps; then links |
| **Low traffic** | keyword-research → content-strategy → content-optimization | Often content or intent mismatch |
| **Not indexing** | indexing, robots-txt, site-crawlability | Technical blockers |

## SEO Roadmap Priorities

| Priority | Meaning | Examples |
|----------|---------|----------|
| **P0** | Blocker—fix first | Crawlability, indexing, robots blocking |
| **P1** | Core—do soon | Title, meta, schema, sitemap, internal links |
| **P2** | Important—not urgent | Open Graph, Twitter Cards, IndexNow |
| **P3** | Nice to have | Rich results, sitelinks optimization |

## Alternative SEO Strategies

| Strategy | When | Skill |
|----------|------|-------|
| **Programmatic SEO** | Scale pages with template + data | programmatic-seo |
| **Parasite SEO** | Leverage high-authority platforms | parasite-seo |
| **GEO** | AI search visibility, citations | generative-engine-optimization |
| **Localization** | Multi-language, international | localization-strategy |
| **Multi-domain brand SEO** | Multiple domains; brand query control | multi-domain-brand-seo |

## Output Format

- **Workflow phase** (where you are; what's next)
- **Priority list** (P0–P3 tasks)
- **Skill mapping** (which skill for each task)
- **Recommendation** (start with X; then Y)

## Related Skills

- **website-structure**: Plan which pages to build; do before or alongside Technical phase
- **keyword-research**: Discovery; informs content-strategy and content-optimization
- **content-strategy**: Topic clusters, pillar pages; content planning
- **programmatic-seo**: Template-based scale; alternative to manual content
- **parasite-seo**: High-authority platforms; alternative to owned-site SEO
- **generative-engine-optimization**: AI search visibility; complements traditional SEO
- **localization-strategy**: Multi-language SEO
- **domain-architecture**: Domain structure (subfolder/subdomain/independent); do before or with website-structure when multiple products
- **rebranding-strategy**: Domain change, 301 redirects; use when rebranding
- **multi-domain-brand-seo**: Brand search control when Hub and Spoke domains coexist
- **skills-task-progress**: Task tracking template; references this workflow
