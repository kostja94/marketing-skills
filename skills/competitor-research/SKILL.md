---
name: competitor-research
description: When the user wants to find competitors for a product or website, assess substitutes, or analyze competition for content, search visibility, backlinks or positioning. Also use when the user mentions "competitor analysis," "competitor research," "competitor keywords," "competitor backlinks," "link gap," "content gap," "competitor content," "competitive analysis," or "competitor comparison." For content roadmap, use content-strategy.
metadata:
  version: 2.0.0
---

# Competitor Research

Guides competitor research for SEO, content, backlinks, and positioning. Use when planning content, auditing articles, building links, or evaluating market position.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

For marketing engagements, lead with the content and distribution view. Use product comparisons to identify meaningful differences and claims the client can support. For a positioning or replacement question, lead with the product view. Use [research workflow](references/research-workflow.md) to select the evidence, follow discoveries and assemble the final report. The SEO and backlink methods below are optional modules selected by scope.

## Discover competitors and classify relationships

Start with the reference product or URL, market and user task. Inspect the product page to establish the input, outcome and intended user. Set the comparison unit (company, product, capability or feature). For an unknown site or ambiguous brand, verify identity before adding candidates.

Choose a product view for user choice, replacement and switching costs; choose a marketing/content view for who attracts the same audience or answers the same question. For a baseline study, maintain one register and derive both views.

1. Start with known products, manual alternatives and adjacent steps in the user workflow. Inspect navigation, templates, integrations, comparison, alternatives, migration and support pages. Identify unexpected pages and examine the action a user can take there.
2. For a promising finding, record the actual URL and what it demonstrates. Search the specific feature, user problem or output in the target market, then inspect at least one new candidate when attainable. Trace the chain from original page through query to new evidence. Stop at the agreed boundary or when new sources repeat existing tasks and relationships.
3. For each material candidate record the comparison unit and task, relationship (direct, indirect, manual substitute, upstream, downstream or platform), coverage (whole or partial, with scope), surface (product, search, community or other evidenced channel), source URL, date and confidence. Leave uncertain relationships pending. Vendor mentions establish leads; check the other product or independent task evidence before claiming substitutability. An import list establishes supported sources, not parity or market share.
4. Deliver the register, strongest discovery trail and open checks. Offer comparison pages for substantiated evaluation needs, alternatives pages for supported replacement tasks and migration pages for executable transfer paths. Hand keyword-research the source URL, observed action, inferred need and concrete seed when a finding warrants query validation.

### Search from a known brand and from a user task

- Search "[brand] alternatives". Capture the publisher, the reference product, named replacements and the job each claims to replace. Check both vendor comparison pages and third-party lists. Follow promising names to their official product or feature pages.
- Search the competitor brand and relevant branded variants in the target market. Inspect placements explicitly labeled as ads. Record query, locale, date, advertiser, visible destination and promoted benefit. An ad impression supports competition for that search opportunity; the advertiser's selected keyword, match type and spend remain unknown. If ads cannot be inspected, mark coverage pending. If an ad promises a different workflow, investigate that relationship separately.
- Search "best [specific feature or job]" and "best [tool] for [audience or constraint]". Extract products and the reasons for inclusion, then check the claimed capability at the source. Use the new feature or use case as the next query to discover specialist providers beyond familiar brands.

Keep the discovery surface distinct from the competitive relationship. Deduplicate products across ads, lists and alternative pages while retaining each independent source and what it establishes.

### Discover products through their distribution channels

Map the task to the device or host where the user performs it. For each relevant environment, inspect the native marketplace or in-product add-on catalog: mobile app stores, browser extensions, collaboration or CRM marketplaces, integration directories and connector/template galleries. Start with categories, collections, related apps, publisher portfolios and host recommendations as well as native search. Follow the tools and endpoints named by a connector into their own listings. For private or login-only catalogs use available authorized access or request a listing/export when needed; mark unchecked surfaces explicitly.

Record the store and locale, host, listing URL or stable ID, publisher, workflow step, inputs and outputs. Distinguish first-party features, standalone apps, extensions of known products, third-party connectors and recipes. Group multiple distribution listings under the same product while preserving channel-specific capabilities. A listing supports availability and stated scope; user reviews provide leads for use cases to verify. Record whether discovery used the native catalog or only a publicly indexed listing.

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

1. **Obtain URLs**: From the user, relevant Contextus competitor or content modules, or web search for `"[target keyword]"` to find top-ranking pages
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
2. **Enrich** — Web search, visit competitor sites; read root `{project}.md` if present
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
