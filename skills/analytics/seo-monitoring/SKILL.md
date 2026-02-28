---
name: analytics-seo-monitoring
description: When the user wants to build an SEO data analysis system, monitor indexing/traffic/keywords/backlinks, or set up benchmarks. Also use when the user mentions "SEO data analysis," "SEO monitoring," "article database," "traffic benchmark," "penalty recovery," or "SEO work document."
metadata:
  version: 1.0.0
---

# Analytics: SEO Monitoring

Guides building a holistic SEO data analysis system. Covers four core metrics (indexing, traffic, keywords, backlinks), benchmark setup, article database, tool selection, traffic diversification, penalty recovery, and work document management.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Core metrics**: Indexing, traffic, keywords, backlinks
- **Benchmark**: Natural traffic baseline; trend comparison
- **Article database**: Per-article performance tracking
- **Tool selection**: GA4, GSC, Semrush, Umami, PostHog, etc.
- **Traffic diversification**: Healthy source mix
- **Penalty recovery**: Algorithm impact, fix workflow
- **Work documents**: Monthly records, responsibility tracking

## Four Core Metrics

### 1. Indexing

| Metric | Purpose | Data Source |
|--------|---------|-------------|
| **Pages indexed / not indexed** | Coverage; early focus: all target pages indexed | GSC, site: command, Semrush (Organic Research > Pages) |
| **Keyword count per page** | More keywords = more potential traffic | Semrush |
| **Index coverage** | Target pages indexed; functional pages findable | GSC, site: command |

**Early priority**: Ensure all pages that need to rank are indexed.

### 2. Traffic

| Metric | Purpose | Data Source |
|--------|---------|-------------|
| **Total traffic** | Growth; keyword relevance (irrelevant traffic has little value) | GA4, Semrush |
| **Subdirectory traffic** | Per-section performance; concentration vs dispersion | Semrush, GA4 |
| **Competitive comparison** | Organic, keyword traffic, total clicks vs competitors | Semrush, Similarweb |
| **Organic by page / country** | Granular breakdown | GA4, GSC |

### 3. Keywords

| Metric | Purpose | Data Source |
|--------|---------|-------------|
| **Rank changes** | Target keyword movement | GSC, Semrush |
| **Keyword count** | New gains / losses per page | Semrush, GSC |

### 4. Backlinks

| Metric | Purpose | Data Source |
|--------|---------|-------------|
| **Referring domains vs backlinks** | Ratio; directory links can be high volume but low value | Semrush, Ahrefs, Moz |
| **Backlink quality** | Do links drive traffic? Low ROI = deprioritize | Semrush, GA4 (referral) |

## Natural Traffic Benchmark

**Location**: GA4 > Reports > Acquisition > Traffic acquisition

1. Review organic traffic trend
2. Record baseline (e.g., monthly total)
3. Compare periodically to detect growth or decline

**Tip**: Add CTA events on key articles to track content ROI (see analytics-tracking).

## Article Database

Track per-article performance to find high/low patterns:

| Field | Use |
|-------|-----|
| **URL, publish date, target keywords** | Content metadata |
| **Index status, rank, traffic, backlinks** | Performance |
| **vs benchmark or competitors** | Context |

Use to guide topic selection, optimization, and resource allocation.

## Tool Selection

| Use | Tools |
|-----|-------|
| **Precise attribution** | GA4, GSC, Bing Webmaster, Yandex Webmaster |
| **Visit analytics** | Umami, Plausible, Clarity (Microsoft), Superset |
| **Third-party estimates** | Semrush, Similarweb |
| **Open-source GA alternative** | PostHog |
| **SEO data** | Semrush, Ahrefs, Moz |

**Attribution config**:
- **User ID**: Cross-device, cross-session identification; send to GA4
- **GSC API**: Index, clicks, impressions, coverage for automation, dashboards

Choose by privacy, cost, and team workflow.

## Traffic Diversification

| Principle | Guideline |
|-----------|-----------|
| **Search share** | Keep organic search below ~75% of total |
| **Health** | Higher direct + referral share = healthier |
| **Brand sites** | Diversified traffic is common for strong brands |
| **Non-brand** | Possible without brand (e.g., tool sites) |
| **Reputation** | Site/brand reputation matters; Google assessors evaluate it |
| **Engagement** | Content, email, social, free tools drive return visits |

## Penalty Recovery

| Step | Action |
|------|--------|
| **Identify** | Which algorithm update caused the impact |
| **Analyze** | Site issues; draft fix plan |
| **Assess cost** | Decide if fixes are worth it; sometimes abandoning is best |
| **Execute** | Implement changes; wait at least 3 months until next major update |
| **Parallel** | Use other channels for quality traffic; improve engagement data for Google |
| **Data window** | Google typically uses ~6 months of data for site quality |
| **Recovery** | Outcome is uncertain; do what you can, then wait |

## Monitoring Metrics Table

### Traffic

| Metric | Source | Notes |
|--------|--------|-------|
| Total sessions | GA4 | |
| Channel share | GA4 | |
| Channel absolute | GA4 | |
| Country % and absolute | GA4 | |
| Top pages | Semrush | Compare with competitors |
| Key page traffic | GA4 | Define "key pages" first |

### Engagement

| Metric | Source | Notes |
|--------|--------|------|
| Pages per session | GA4 | Use GA for own site; third-party for competitors |
| Avg session duration | GA4 | |
| Bounce rate | GA4 | |

### Backlinks

| Metric | Source | Notes |
|--------|--------|------|
| Domain authority | Semrush, Moz, Ahrefs | |
| Backlinks, referring domains | Semrush | |
| Top referring domains by authority | Semrush | |
| Important links | Manual log | Track loss |
| Link graph | Semrush | Health check |
| New quality links (self + competitors) | Semrush | Outreach |
| Indexed pages | Semrush | High-authority pages; internal linking |
| Outbound domains | Semrush | Partnership opportunities |

### Keywords

| Metric | Source | Notes |
|--------|--------|------|
| Keyword count | Semrush | How many keywords rank |

### Content Output

| Metric | Source | Notes |
|--------|--------|------|
| Articles published | Manual | Weekly count |
| Published vs indexed | GSC | New content indexing |
| New page traffic | GA4 | Fresh content performance |

## Monthly Record Template

| Category | Metric | Source | Notes | Month 1 | Month 2 |
|----------|--------|--------|-------|---------|--------|
| Traffic | Total sessions | GA4 | | | |
| Traffic | Channel share | GA4 | | | |
| Engagement | Pages per session | GA4 | | | |
| Backlinks | Referring domains | Semrush | | | |
| Content | Articles published | Manual | | | |

Adjust rows as needed.

## Work Document Management

- **Structure**: Metrics, sources, notes, monthly values
- **Benefits**: Regular review, month-over-month trends, clear ownership
- **Format**: Spreadsheet or doc; assign owners per metric

## Output Format

- **Core metrics** summary (indexing, traffic, keywords, backlinks)
- **Benchmark** and trend
- **Article database** structure (if applicable)
- **Tool** recommendations
- **Monitoring table** (customized)
- **Action items** and owners

## Related Skills

- **analytics-traffic**: Traffic sources, attribution, diversification
- **analytics-tracking**: GA4, events, CTA attribution, User ID
- **analytics-google-search-console**: GSC reports, indexing, API
- **analytics-ai-traffic**: AI search traffic
- **seo-off-page-backlink-analysis**: Backlink audit, toxic links
- **seo-technical-indexing**: Fix indexing issues
