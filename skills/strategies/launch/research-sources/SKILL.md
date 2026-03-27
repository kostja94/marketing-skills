---
name: research-sources
description: When the user wants to find information sources for content ideation, competitor monitoring, or industry tracking. Also use when the user mentions "research sources," "information sources," "content ideation," "industry monitoring," "competitor monitoring," "market intelligence," "content research," or "topic research." For keywords, use keyword-research.
metadata:
  version: 1.1.1
---

# Strategies: Research Sources

Guides selecting and organizing information sources for marketing research: content ideation, competitor monitoring, and industry tracking. Use this skill when planning where to gather signals for content, competitive intelligence, or market trends.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Use Cases

| Use case | Purpose |
|----------|---------|
| **Content ideation** | Topic ideas, trends, gaps for blog, newsletter, social |
| **Competitor monitoring** | Product updates, positioning, pricing, reviews |
| **Industry tracking** | Market shifts, funding, layoffs, regulatory changes |

## Source Categories

| Category | Format | Use |
|----------|--------|-----|
| **News** | Real-time, daily | Breaking news, announcements |
| **Blogs** | Company, analyst | Deep dives, product updates |
| **Newsletters** | Curated, weekly/daily | Trends, summaries; low effort |
| **Events** | Conferences, webinars | Industry pulse, networking |
| **Data** | Layoffs, market cap, funding | Quantitative signals |
| **Community** | Forums, Q&A | Real questions, pain points |
| **Archives** | Wayback, Internet Archive | Historical content, competitor changes |

**Selection criteria**: Authority, freshness, coverage, language/locale. Prefer 10–15 high-quality sources over 50+ low-signal ones.

## Example Sources (Generic)

| Category | Examples |
|----------|----------|
| **News** | TechCrunch, VentureBeat, MIT Technology Review |
| **Blogs** | Google AI Blog, OpenAI Blog, company blogs |
| **Newsletters** | TLDR AI, Ben's Bites, The Batch (DeepLearning.AI) |
| **Data** | Layoffs.fyi, Crunchbase, Companies Market Cap |
| **Archives** | Internet Archive, Wayback Machine |
| **Community** | Reddit, Quora, Stack Overflow; regional (e.g. Qiita for Japan) |

**Note**: Add locale-specific sources via **localization-strategy**; avoid long URL lists.

## By Use Case

| Use case | Source types |
|----------|--------------|
| **Content ideation** | News, blogs, newsletters, community (Reddit, Quora, Stack Overflow) |
| **Competitor monitoring** | Competitor blogs, review sites, social, funding databases |
| **Industry tracking** | News, newsletters, events, layoff/funding data |

**Avoid**: Long URL lists that go stale. Use category framework + a few examples; update periodically.

## Integration with Skills

| Skill | How research sources feed in |
|-------|------------------------------|
| **keyword-research** | Newsletters, community for long-tail and question keywords |
| **competitor-research** | Competitor blogs, review platforms, funding data |
| **content-marketing** | News, blogs for topic ideas; events for timely content |
| **content-strategy** | Industry trends for pillar/cluster planning |

## Output Format

- **Use case** (ideation, competitor, industry)
- **Category** selection (news, blogs, newsletters, etc.)
- **Source** shortlist (5–15; name + purpose)
- **Cadence** (daily scan, weekly digest, event calendar)

## Related Skills

- **keyword-research**: Keyword discovery; research sources inform topics
- **competitor-research**: Competitor analysis; sources for monitoring
- **content-marketing**: Content planning; sources for ideation
- **content-strategy**: Topic clusters; industry signals for pillars
