---
name: analytics-google-search-console
description: When the user wants to analyze Google Search Console data, use GSC API, or interpret search performance. Also use when the user mentions "GSC," "Search Console," "indexing report," "Core Web Vitals," "Enhancements," "Insights report," "search performance," "impressions," "CTR," "average position," "index coverage," "title tag," "meta description," or "searchanalytics.query."
metadata:
  version: 1.2.0
---

# Analytics: Google Search Console

Guides analysis of Google Search Console (GSC) data: performance metrics, indexing, sitemaps, Core Web Vitals, and rich results. Covers best practices for monthly monitoring and actionable insights.

**When invoking**: On **first use**, if helpful, open with 1?2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Performance**: Clicks, impressions, CTR, average position; API for export
- **Insights**: Simplified overview; top/trending content and queries
- **Indexing**: Pages indexed, pages not indexed, reasons (Coverage)
- **Technical**: Sitemaps, Core Web Vitals, Enhancements
- **API**: searchanalytics.query for programmatic access
- **Methodology**: How to read charts, avoid common mistakes, correlate with releases

## Analysis Best Practices

### Chart Reading

| Practice | Why |
|----------|-----|
| **Focus one metric at a time** | Stacked bar charts hide fluctuations; toggle off other metrics to see each clearly |
| **Don't compare just two points** | End-of-month vs prior month misses mid-month drama; examine full trend |
| **Check beyond top 10** | Many reports default to top 10; scroll or paginate for more rows |
| **Screenshot charts** | GSC retains limited history; save images for future reference |
| **Record in spreadsheet** | Export at month-end; use formulas to track correlations over time |
| **Track release dates** | Join dev standups, read release notes; correlate GSC shifts with deployments |

### Investigation Workflow

1. **Pinpoint date**: When did the metric change?
2. **Correlate**: Any releases, CMS changes, server maintenance, third-party code?
3. **Decide**: Investigate, correct, overlook, or monitor closely
4. **Loop in**: Product or dev team for root cause

## Key Reports & Metrics

### 1. Performance (Search Results)

**Location**: Performance ??Search results

| Metric | Use |
|--------|-----|
| **Clicks** | Traffic from Google Search |
| **Impressions** | How often site appeared in results |
| **CTR** | Whether users think page answers query |
| **Average position** | Ranking trend |

**Dimensions**: Query, page, country, device, date. Filter by search type: web, image, video, news. Use to find low-CTR high-impression pages (title/meta optimization opportunities).

**Search appearance**: AMP, blue link, rich results (filterable in UI and API).

#### CTR Benchmarks by Position

Use to compare actual CTR vs expected. Benchmarks vary by SERP features (AI Overviews, featured snippets); clean SERPs:

| Position | Expected CTR (baseline) | With AI Overviews (lower) |
|----------|-------------------------|---------------------------|
| 1 | 25??5% | ~19% |
| 2 | 12??8% | ~12% |
| 3 | 8??2% | ~7% |
| 4?? | 5??% | ~5% |
| 6??0 | 2??% | 2??% |

**Interpretation**: If actual CTR is below expected for your position, prioritize title/meta optimization. Over 90% of first-page results have CTR below 10%; significant upside exists.

#### Low CTR, High Impressions: Optimization Workflow

1. **Identify**: Sort by impressions; filter positions 1??0; 1,000+ monthly impressions
2. **Compare**: Actual CTR vs expected for position (see table above)
3. **Gap**: e.g., position 4 at 2% CTR vs expected 5??% ??~3??% uplift potential
4. **Action**: Optimize title and meta (see below); add schema for rich results (+10??0% clicks)

#### Title Tag Best Practices

| Aspect | Guideline |
|--------|-----------|
| **Length** | 50??0 chars to avoid truncation; Google reads full tag, weights beginning |
| **Front-load** | Main phrase first; branding at end |
| **Clarity** | Match search intent; avoid keyword stuffing |
| **Engagement** | Numbers, power words, questions can boost CTR ~36% |
| **Example** | Bad: "SEO Tips for Small Business" ??Better: "11 SEO Tips That Actually Work (2026)" |

Google may rewrite titles if they mismatch content or intent. H1 should align with title.

#### Meta Description Best Practices

| Aspect | Guideline |
|--------|-----------|
| **Length** | 120??58 chars (~150 sweet spot); ~920px desktop, ~680px mobile |
| **Unique** | One per page; no duplicate descriptions |
| **Intent** | Answer "why should I click?"; match search intent |
| **Content** | Include author, date, price where relevant |
| **Impact** | Does not affect ranking; well-written descriptions improve CTR 5??0% |

#### Rich Results & CTR

Pages with review stars, FAQ schema, or other rich snippets see 10??0% more clicks. See seo-on-page-schema.

### 2. Insights Report

**Location**: Performance ??Insights (or Overview)

Simplified overview; replaces standalone Search Console Insights. Data from GSC only (no GA since Dec 2024).

| Card | Use |
|------|-----|
| **Clicks and impressions** | Site visibility and click effectiveness |
| **Your content** | Top, trending up, trending down pages |
| **Queries leading to your site** | Top, trending up, trending down queries |
| **Top countries** | Geographic audience |
| **Branded vs non-branded** | Brand recognition (AI-labeled; may mislabel) |
| **Additional traffic sources** | Image, Video, News search, Discover |

**Trending**: Based on click change vs previous period. Click items to jump to Performance report filtered to that item.

**Query groups**: Similar queries grouped; group name = best-performing query. Not available for sub-properties or low-impression sites.

### 3. Page Indexing (Coverage)

**Location**: Indexing ??Page indexing

**Status grouping** (updated): Valid + Valid with warning ??**Indexed**. Error + Excluded ??**Not indexed**.

**Indexed vs Not indexed are complementary**: Not all site content should be indexed. Login, admin, duplicate content, legal boilerplate, and low-value pages often intentionally use noindex. Indexed and non-indexed pages can reference each other (e.g., sitemap includes indexable URLs; noindex pages still exist and link internally). Non-indexed is not inherently a problem?investigate only when important pages are excluded. See seo-technical-indexing (noindex usage) and seo-technical-robots (crawl control) for when to exclude.

| Metric | Action |
|--------|--------|
| **Pages indexed** | Turn off "Pages not indexed" to view alone; watch for drops |
| **Pages not indexed** | Turn off "Pages indexed" to view alone; watch for spikes. Distinguish intentional (noindex, robots) from accidental |

**Filter**: All submitted pages / Unsubmitted pages only (dropdown near top).

**Source column**: Indicates whether issue is caused by website or Google.

**Why pages are not indexed**: Drill into reasons and example URLs. Common culprits:

- Duplicate content
- Noindex tags
- Redirect errors
- 5xx errors
- 404 errors
- Blocked by robots.txt
- Discovered ??currently not indexed
- Crawled ??currently not indexed

**Quick check**: If trend line is stable, spend ~3 seconds; move on. Investigate if fourth column (trend) shifts.

**Diagnosis workflow**: GSC Coverage ??click Issue ??view sample URLs ??identify pattern ??fix (see seo-technical-indexing for fix actions).

**Coverage issue types**:

| Issue | Meaning | Next step |
|-------|---------|-----------|
| Crawled - currently not indexed | Crawled but not indexed | See seo-technical-indexing |
| Excluded by «noindex» tag | Intentionally excluded; often valid (login, admin, legal, etc.) | Ignore if expected; verify important pages not accidentally noindexed |
| Blocked by robots.txt | Crawl blocked | See seo-technical-robots; may be intentional |
| Redirect / 404 | Redirect or missing | Fix URL or redirect |
| Duplicate / Canonical | Duplicate content | Usually OK; keep canonical |

**URL Inspection**: Verdicts: "URL is on Google," "URL is on Google, but has issues," "URL is not on Google." Use for important pages; verify canonical, internal links, sitemap; Request indexing if needed.

### 4. Video Indexing (If Applicable)

**Location**: Indexing ??Video indexing

- **Videos indexed** / **Videos not indexed**: Toggle off the other for clear view
- **Why videos are not indexed**: Thumbnail blocked, invalid size/format, not in main content, etc.

Skip if video SEO is not in roadmap.

### 5. XML Sitemaps

**Location**: Indexing ??Sitemaps

| Check | Action |
|------|--------|
| Status | Confirm each sitemap says "Success" |
| URLs indexed | Click sitemap ??see indexed count; drops indicate indexing issues |
| Bellwether sitemaps | For large sites, monitor templated sitemaps (by country, language, division) |

Enterprise: Glitches can block new URL crawling, cause hreflang confusion, delay fresh content discovery.

### 6. Core Web Vitals

**Location**: Experience ??Core Web Vitals

**Priority**: Mobile first (Google's higher expectations for mobile).

| Metric | Mobile | Desktop |
|--------|-------|---------|
| **Good URLs** | Target | Secondary |
| **Needs improvement** | Fix | Monitor |
| **Poor URLs** | Fix | Monitor |

**Why URLs don't have good score**: Click "Open report" ??grouped example URLs by issue type.

| Issue | Threshold (mobile) |
|-------|--------------------|
| LCP | > 2.5s (good), > 4s (poor) |
| INP | > 200ms (good), > 500ms (poor) |
| CLS | > 0.1 (needs improvement), > 0.25 (poor) |

**Tip**: Historical chart is short; export to spreadsheet for longer trends. Share with dev team regularly; correlate dates with releases.

**Layout** (updated): Two tables?Poor or Need improvement; Good (click "View data about usable pages").

### 7. Enhancements (Rich Results)

**Location**: Experience ??Enhancements (Product snippets, Merchant listings under Shopping)

**Status** (updated): Two-tier??*invalid** (critical issues, may not appear) vs **valid** (no critical issues; may still have warnings). Warnings no longer top-level.

| Type | Examples |
|------|----------|
| Content | Breadcrumbs, FAQ, Events, Videos, Job postings, Review snippets, Q&A, Discussion forums |
| Shopping | Product snippets, Merchant listings |
| Other | Recipes, Datasets, Hotels, Vacation rentals, Profile pages, Practice problems, Math solvers, Image metadata |

**Note**: Reports show sample items, not full list. Use URL Inspection for unlisted URLs.

### 8. AI Overviews (GSC Limitation)

- **GSC**: AI Overviews clicks/impressions are not separated from organic in Performance report.
- **Workaround**: Filter queries that tend to trigger AI Overviews to estimate AI-driven visibility:

```
(?i)^(who|what|where|when|why|how|which|is|are|can|does|should)|\b(vs|versus|compare|difference|pros and cons|guide|tutorial|best|top|list)\b
```

For GA4 AI traffic tracking, see analytics-ai-traffic.

### 9. Links & Disavow

**Location**: Links (inbound links), Security & Manual Actions

- **Links report**: View links to site and pages; anchor text distribution.
- **Disavow file**: Submit via GSC when necessary (manual penalty, toxic links). Use sparingly; over-disavowing can harm. See seo-off-page-backlink-analysis for when to disavow.

## Search Console API

**Method**: `searchanalytics.query()` ??exposes all Performance report data.

### Metrics

Clicks, Impressions, CTR, Position.

### Dimensions

date, query, page, country, device. Search appearance (AMP, blue link, rich results). Filter by search type: web, image, video, news.

### Limits

| Limit | Value |
|-------|-------|
| Rows per day per search type per property | 50,000 |
| Rows per response | 25,000 (use pagination: startRow, rowLimit) |
| Data availability | 2?? days after |

**Tip**: Run daily queries for one day of data to avoid quota. Verify data presence first (dimensions: date only, no filters).

**Optimization**: Gzip compression; `fields` parameter for partial responses; pagination for large datasets.

**References**: [Search Console API](https://developers.google.com/webmaster-tools/about), [searchanalytics.query](https://developers.google.com/webmaster-tools/v1/how-tos/search_analytics)

## Monthly Audit Checklist

- [ ] Performance: Clicks, impressions, CTR, position trends
- [ ] Insights: Top/trending content and queries (if available)
- [ ] Page indexing: Indexed vs not indexed (isolated views)
- [ ] Why not indexed: Trend lines for key reasons
- [ ] Sitemaps: All "Success"; indexed URL counts stable
- [ ] Core Web Vitals: Mobile good/needs improvement/poor
- [ ] Enhancements: No new invalid items (critical issues)
- [ ] Links: No manual actions; disavow only if needed (see backlink-analysis)
- [ ] Data exported to spreadsheet (month-end snapshot)
- [ ] Charts screenshotted for history
- [ ] Release notes reviewed for correlation

## Output Format

- **Summary**: Key findings, trends, anomalies
- **Metrics**: Specific numbers and date ranges
- **CTR analysis**: Actual vs expected by position; low-CTR high-impression pages
- **Title/meta opportunities**: Pages with CTR gap; specific optimization suggestions
- **Action items**: Prioritized fixes (indexing, CWV, sitemaps, enhancements, title/meta)
- **Correlation**: Suspected causes (releases, config changes)
- **Next steps**: Monitoring plan, dev handoff

## Related Skills

- **seo-on-page-metadata**: Title, meta description, hreflang implementation
- **seo-technical-sitemap**: Fix sitemap errors
- **seo-technical-indexing**: Resolve indexing issues (fix actions)
- **seo-on-page-schema**: Fix structured data / rich results
- **seo-off-page-backlink-analysis**: When to disavow; backlink audit
- **analytics-traffic**: Traffic sources, attribution
- **analytics-tracking**: GA4 events (correlate with GSC)
- **analytics-ai-traffic**: GA4 AI traffic tracking
