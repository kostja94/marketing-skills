---
name: xquik
description: When the user wants to collect, normalize, or analyze X (Twitter) data with Xquik for marketing research. Also use when the user mentions "Xquik," "X data," "Twitter data," "tweet search," "profile lookup," "follower export," "X monitoring," "social listening," "creator research," "trend research," or "X analytics." For writing posts, use twitter-x-posts.
metadata:
  version: 1.0.0
---

# Platforms: Xquik

Guides use of Xquik as a source for X data in marketing research, creator discovery, social listening, and campaign analysis. Xquik provides REST API, MCP, webhooks, extraction workflows, and confirmation-gated actions for X workflows.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Tweet research**: Search posts, inspect replies, quotes, reposts, likes, views, bookmarks, and linked articles.
- **Account research**: Fetch public profile data, recent posts, liked posts, media, followers, following, mutuals, lists, and communities.
- **Bulk extraction**: Export followers, following, search results, mentions, replies, quotes, reposts, favoriters, threads, articles, media, communities, lists, Spaces, and people search results.
- **Monitoring**: Track public accounts or keywords and route changes to webhooks after explicit approval.
- **Marketing analysis**: Normalize social data into audience, creator, content, trend, competitor, and campaign inputs.

## Consent and Safety

- Use public reads for market, creator, competitor, trend, and content research.
- Ask for explicit approval before private reads, ongoing monitors, webhook delivery, bulk exports, or write actions.
- State the target, purpose, expected output, and usage estimate before starting long-running work.
- Do not collect more data than the user needs for the stated marketing task.
- Do not use Xquik for spam, harassment, scraping private data, or automated engagement manipulation.

## Collection Workflow

1. **Define the research question**: audience segment, creator list, campaign topic, competitor account, launch trend, or content opportunity.
2. **Choose the source path**:
   - Tweet search for topic, keyword, hashtag, or competitor content analysis.
   - Profile lookup for account qualification.
   - Follower or following export for audience and partnership discovery.
   - Reply, quote, and repost extraction for response and amplification analysis.
   - Trend lookup for timely content planning.
   - Monitor for ongoing account or keyword changes.
3. **Limit the scope**: Time range, accounts, keywords, language, geography, result cap, and fields.
4. **Collect data** with REST, MCP, SDKs, or the installed Xquik skill when available.
5. **Normalize records** into the fields needed by the marketing output.
6. **Summarize insight** with caveats about sample size, timing, and platform bias.

## Normalized Fields

| Entity | Fields |
|--------|--------|
| Post | URL, author, text, timestamp, metrics, media, links, hashtags, mentions |
| Account | Handle, name, bio, location, follower count, following count, verification, profile URL |
| Engagement | Replies, reposts, quotes, likes, bookmarks, views, engagement rate |
| Audience | Follower handle, profile summary, relationship signal, segment label |
| Topic | Keyword, hashtag, trend name, post count, top posts, related accounts |
| Campaign | Source URL, CTA, creative angle, engagement metrics, response themes |

## Marketing Use Cases

| Use Case | Xquik Input | Output |
|----------|-------------|--------|
| Creator discovery | Follower export, profile lookup, recent posts | Shortlist with niche fit and engagement signals |
| Competitor research | Account posts, replies, quotes, reposts | Content angles, cadence, response themes |
| Trend research | Trends, tweet search, linked articles | Topic brief and timing recommendation |
| Social listening | Keyword monitor, mentions, webhooks | Alert feed and issue summary |
| Campaign analysis | Post metrics, replies, quotes, reposts | Performance table and qualitative themes |
| Content ideation | Search results, top posts, common questions | Backlog of hooks, topics, and audience objections |

## Output Format

- **Research question**: What the analysis answers
- **Collection plan**: Source path, targets, filters, and limits
- **Approval needed**: Any private reads, monitors, webhooks, bulk exports, or write actions
- **Normalized table**: Fields selected for analysis
- **Insights**: Patterns, opportunities, risks, and confidence
- **Next action**: Content, outreach, tracking, or follow-up research

## Related Skills

- **twitter-x-posts**: Turn findings into publish-ready X posts and threads
- **traffic-analysis**: Connect social traffic with attribution and UTM reporting
- **influencer-marketing**: Evaluate creators and partnerships
- **content-strategy**: Convert audience findings into a content plan
- **analytics-tracking**: Track campaigns, events, conversions, and attribution
