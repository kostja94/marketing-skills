---
name: seo-content-content-strategy
description: When the user wants to plan content for SEO, create content calendar, or build topic clusters. Also use when the user mentions "content strategy," "content plan," "topic clusters," "pillar content," "pillar page," "cluster articles," or "editorial calendar."
metadata:
  version: 1.0.0
---

# SEO Content: Content Strategy

Guides content strategy for SEO: topic clusters, pillar pages, cluster articles, and editorial planning.

**When invoking**: On **first use**, if helpful, open with 1?2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product, audience, and proof points.

Identify:
1. **Keywords**: From keyword research
2. **Existing content**: What already exists
3. **Resources**: Content capacity, tools
4. **Goals**: Traffic, conversions, authority

## Topic Clusters

Topic clusters organize content by **topic** rather than isolated keywords. A **pillar page** covers a broad core topic; **cluster articles** cover subtopics; all connect via internal links. This signals topical authority to search engines and AI systems.

### Structure

```
Pillar page (broad topic, 2,000-5,000+ words)
    <-> internal links
Cluster 1 (subtopic, 800-2,500 words)
Cluster 2 (subtopic)
...
Cluster 6-12 (subtopics)
    <-> cluster to cluster links
```

### Pillar Page

| Attribute | Guideline |
|-----------|-----------|
| **Length** | 2,000-5,000+ words; comprehensive guide |
| **Keyword** | Broad head term with search volume |
| **Role** | Hub; links to all cluster articles; targets primary topic |
| **Conversion** | Link to product/feature pages where relevant |

### Cluster Articles

| Attribute | Guideline |
|-----------|-----------|
| **Count** | 6-12 articles per pillar (minimum 6 for authority) |
| **Length** | 800-2,500 words each; focused on one subtopic |
| **Keyword** | Long-tail, specific intent per article |
| **Links** | Each cluster links to pillar; pillar links back; related clusters link to each other |

### Internal Linking Model

| Link type | Purpose |
|-----------|---------|
| **Pillar to Cluster** | Hub distributes authority; users discover subtopics |
| **Cluster to Pillar** | Signals relationship; passes equity to hub |
| **Cluster to Cluster** | Related subtopics; strengthens topical coverage |

### Why Topic Clusters Work

- **Topical authority**: Rank for multiple variations; comprehensive coverage signals expertise
- **Avoid cannibalization**: One page per topic/keyword; no competing pages
- **Better internal linking**: Clear logic; crawlers understand structure
- **AI citations**: Clustered content gets ~42% more AI citations than standalone
- **Traffic**: ~30% more organic traffic; rankings hold ~2.5x longer

### Implementation Steps

1. **Choose 3-7 core topics** ? business relevance, search demand, competitive opportunity
2. **Map subtopics** ? People Also Ask, competitor analysis, keyword tools
3. **Content audit** ? Identify existing pages that can become pillar or cluster; find gaps
4. **Build clusters first** (optional) ? Cluster pages often rank first; add pillar after
5. **Create pillar** ? Comprehensive guide; link to all clusters
6. **Establish links** ? Pillar <-> cluster; cluster <-> cluster
7. **Update quarterly** ? Maintain freshness and authority

### Example

- **Pillar**: "SEO Guide" (targets "SEO")
- **Clusters**: "Technical SEO," "On-Page SEO," "Link Building," "Content SEO," "Local SEO," "E-E-A-T"

## Content Types

| Type | Use | SEO Fit |
|------|-----|---------|
| **How-to guides** | Informational intent; high share potential | High ? matches search intent |
| **Comparisons** | Commercial intent; "X vs Y" | High |
| **List posts** | "Top 10," "Best X" | High |
| **Glossaries** | Definition queries; internal link hub | High |
| **Tools/calculators** | Linkable assets; engagement | High |
| **Case studies** | Proof; conversion support | Medium ? supports conversion |
| **Funding / PR** | Funding rounds, acquisitions | Low ? brand/PR, not search-driven |
| **Product updates** | Feature launches, release notes | Low ? internal audience |
| **News / Trending** | Industry news, hot topics | Medium ? quick spikes, short shelf life |

### Evergreen vs Timely Content Mix

- **Evergreen** (70?75%): Pillar guides, how-tos, comparisons, glossaries. Drives long-term traffic, backlinks, authority. Refresh every 6?12 months.
- **Timely** (25?30%): Seasonal, trending, news. Generates quick traffic, shows topical relevance. Link timely pieces into evergreen pillars.
- **Balance**: Too much evergreen = blog feels stale; too much timely = irregular traffic, constant content churn.

## Editorial Calendar

- Map keywords to content pieces
- Prioritize by opportunity (volume ? intent ? feasibility)
- Schedule by capacity
- Include update schedule for existing content

## Output Format

- **Topic cluster** map (pillar + 6-12 clusters)
- **Content calendar** (topics, keywords, deadlines)
- **Internal linking** plan
- **Update plan** for existing content

## Related Skills

- **seo-content-keyword-research**: Keywords drive content plan
- **seo-content-optimization**: Word count, H2 keywords, keyword density, multimedia, lists ? on-page content optimization
- **seo-on-page-internal-links**: Clusters need internal linking
- **seo-off-page-link-building**: Content strategy creates linkable assets
- **seo-on-page-heading**: Content structure uses headings
