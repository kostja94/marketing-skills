---
name: content-decay-analysis
description: Diagnoses declining organic search traffic and rankings on existing pages, prioritizes refresh candidates, and defines recovery actions. Use when users ask to find decaying content, audit traffic drops on older articles, prioritize content updates, or recover lost rankings. Differs from content-strategy (which plans new topical hubs) and keyword-research (which discovers new terms).
metadata:
  version: 1.0.0
---

# Content Decay Analysis

## Scope

Identifies existing pages losing organic search impressions, clicks, or rankings over time, categorizes the root causes of decay (SERP shifts, intent drift, competitor freshness, or technical regressions), and produces a prioritized content refresh roadmap. Works with standard Google Search Console (GSC) exports, analytics CSVs, or project context documents without requiring proprietary connectors.

## Required Inputs & Missing Information Checks

- **Minimum required:** Page-level organic performance data across two comparable periods (e.g., last 90 days vs. previous 90 days, or year-over-year) showing URLs, clicks, impressions, CTR, and average position.
- **Helpful context:** Read `{project}.md` (if present) to verify core commercial pages, target audience, and product positioning before recommending rewrites.
- **If data is missing:** Ask the user for a GSC or analytics export comparing two time periods before diagnosing specific URLs.

## Instructions

1. **Filter Meaningful Pages:** Exclude brand-new URLs (published < 90 days ago) and low-volume noise (e.g., pages with fewer than 50 baseline clicks or 1,000 baseline impressions) unless they are high-intent commercial pages.
2. **Calculate Decay Severity:** Compare Period A (baseline) vs. Period B (current) for each URL:
   - **Absolute Click Loss:** `Clicks_B - Clicks_A`
   - **Relative Click Change (%):** `((Clicks_B - Clicks_A) / Clicks_A) * 100`
   - **Impression vs. CTR Split:** Determine whether traffic fell due to lost impressions/rankings or stable impressions with dropping CTR.
3. **Classify Root Cause per URL:**
   - **Ranking Erosion (Impressions & Position Down):** Competitors published fresher/deeper content, or search intent shifted.
   - **SERP Feature / AI Overview Squeeze (Impressions Stable, CTR Down):** Title/meta snippet lost appeal, or zero-click SERP elements absorbed clicks.
   - **Technical / Canonical Regression (Sudden Drop to Zero):** Accidental `noindex`, broken redirects, canonical changes, or internal link removal.
4. **Prioritize Refresh Queue:** Score and rank pages into three tiers:
   - **Tier 1 (Immediate Refresh):** High historical conversions or top-20% click loss where position is still #4–#15 (striking distance).
   - **Tier 2 (Structural Rewrite):** Significant intent shift or position drop beyond #15 requiring new sections, updated data, and stronger internal linking.
   - **Tier 3 (Consolidate or Prune):** Thin/outdated posts with overlapping keywords that should be 301-redirected into a stronger pillar page.
5. **Define Actionable Refresh Briefs:** For each Tier 1 and Tier 2 URL, specify concrete updates (outdated stats to replace, missing subtopics, title/meta CTR improvements, and internal links to add).

## Output Format

### 1. Executive Summary
- Total decaying URLs identified, total net clicks lost, and top 3 priority refresh targets.

### 2. Prioritized Content Decay Table

| URL | Baseline Clicks | Current Clicks | Change (%) | Avg. Position Shift | Primary Decay Cause | Priority Tier |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `/blog/example-guide` | 2,400 | 1,150 | -52.1% | 3.2 → 8.4 | Ranking Erosion / Outdated Data | Tier 1 |

### 3. Page-by-Page Refresh Action Plan
For each Tier 1 & Tier 2 page:
- **Target URL & Query Focus**
- **Diagnosis:** Why performance dropped
- **Specific Actions:** Exact sections to update, snippet/title adjustments, and internal links needed

## Related Skills

- `content-strategy` — Use when planning net-new content pillars rather than refreshing existing declining pages.
- `keyword-opportunity` — Use when expanding a refreshed page with new secondary keywords.
- `page-metadata` — Use when a decaying page has stable rankings but needs title tag and meta description optimization to recover CTR.
- `internal-links` — Use when reinforcing refreshed pages with internal link equity.