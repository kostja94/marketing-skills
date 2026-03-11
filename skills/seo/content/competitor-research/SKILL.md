---
name: competitor-research
description: When the user wants to analyze competitors for SEO, content, backlinks, or positioning. Also use when the user mentions "competitor analysis," "competitor research," "competitor keywords," "competitor backlinks," "link gap," "content gap," "competitor content," "competitive analysis," or "competitor comparison."
metadata:
  version: 1.2.0
---

# SEO Content: Competitor Research

Guides competitor research for SEO, content, backlinks, and positioning. Use when planning content, auditing articles, building links, or evaluating market position.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Research Types

| Type | Purpose | Output |
|------|---------|--------|
| **Keyword/topic** | Topics competitors rank for; gaps | Keyword opportunities; content ideas |
| **Content** | Structure, length, gaps vs top rankers | Length target; H2 structure; content gaps |
| **Backlink** | Link profile; sites linking to competitors | Link gap; outreach targets |
| **Pricing** | Competitor pricing, positioning | Pricing context; differentiation |
| **SEO metrics** | Organic traffic, rankings vs competitors | Benchmark; opportunity areas |

## Competitor Keyword / Topic Analysis

| Method | Practice |
|--------|----------|
| **Reverse engineering** | Analyze competitor titles, H1, URL; identify topics they rank for |
| **SERP overlap** | Keywords with overlapping top-ranking pages → same cluster; #4–10 = opportunity |
| **site: operator** | `site:competitor.com` to see indexed pages |
| **Tool** | Ahrefs, Semrush—competitor keyword overlap, gap analysis |

**Output**: Keyword opportunities; topics competitors cover that you don't.

## Competitor Content Analysis

| Element | Check |
|---------|-------|
| **Word count** | Top 10 average; length target for your content |
| **H2 structure** | Topics covered; structure to adopt |
| **Content gaps** | What top rankers cover that you miss |
| **Keyword placement** | Primary keyword in title, H1, first 100 words |
| **Format** | Lists, tables, FAQ; match or improve |

**Use when**: Auditing or creating articles; see **article-page-generator** for Research Phase integration.

### Competitor Article Fetch Workflow (for Article Analysis)

When analyzing or auditing a single article, use this lightweight workflow to obtain competitor articles:

1. **Obtain URLs**: From user, project-context Section 11, or web search for `"[target keyword]"` to find top-ranking pages
2. **Fetch content**: Use mcp_web_fetch or WebSearch to fetch 2–3 top-ranking pages
3. **Analyze**: Word count, H2 structure, keyword placement, content gaps, CTA, schema
4. **Output**: Competitor URLs, brief structure comparison, content gaps, length target, keyword opportunities

**Output format**: Competitor URLs; word count and H2 structure per URL; content gaps vs your article; recommended length target; keyword opportunities (terms top rankers use that your article misses).

## Competitor Backlink Analysis

| Action | Purpose |
|--------|---------|
| **Compare profiles** | Your backlinks vs competitors |
| **Link gap** | Sites linking to competitors but not you |
| **Opportunity** | Outreach to those sites; content they might link to |

**Tools**: Ahrefs, Semrush—Link Intersect, competitor backlink reports. See **backlink-analysis**.

## Competitor Pricing

| Use | Practice |
|-----|----------|
| **Positioning** | Where you sit vs competitors |
| **Differentiation** | Value prop when price differs |
| **Alternatives pages** | Who to include; how to position |

See **pricing-strategy**, **alternatives-page-generator**.

## Data Sources

| Source | Use |
|--------|-----|
| **SimilarWeb** | Traffic, engagement, traffic sources by domain |
| **Ahrefs** | Competitor domains, backlinks, DR |
| **SEMrush** | Organic competitors, traffic share |
| **GA** | Referral traffic, acquisition by source |
| **PostHog** | Competitor feature usage (if tracked) |

## Report Workflow

1. **Parse** — Read Excel/CSV, infer domain, visits, traffic sources, etc. from headers
2. **Enrich** — Web search, visit competitor sites; read `project-context.md` if present
3. **Build** — Structure data for report
4. **Generate** — Output report in chosen format

## Output Format

- **Competitors** identified
- **Research type** (keyword, content, backlink, pricing)
- **Findings** (gaps, opportunities, benchmarks)
- **Recommendations** (content to create, links to pursue, positioning)

### Report Structure Reference

| Section | Content |
|---------|---------|
| Executive Summary | Key findings (top 3), top 3 recommendations |
| Competitor Overview | Competitor, category, market position, key strength |
| Product Comparison | Feature/capability vs Us vs Competitors |
| SWOT Analysis | Our strengths/weaknesses/opportunities/threats; competitor deep dives |
| Marketing & Messaging | Value prop, target audience, key channels |
| Gaps & Opportunities | Gap, opportunity, priority |
| Prioritized Recommendations | Recommendation, impact, effort, owner |

## Related Skills

- **keyword-research**: Competitor reverse; keyword discovery
- **article-page-generator**: Competitor article analysis in Research Phase
- **content-strategy**: Competitor analysis for topic mapping
- **content-optimization**: Competitor length and structure as reference
- **backlink-analysis**: Competitor backlink comparison; link gap
- **seo-monitoring**: Competitive comparison; organic vs competitors
- **alternatives-page-generator**: Competitor selection; comparison framing
- **migration-page-generator**: Competitor migration paths
- **pricing-strategy**: Competitor pricing context
- **affiliate-marketing**: Find affiliates promoting competitors
- **directories**: Competitor info for directory submissions
