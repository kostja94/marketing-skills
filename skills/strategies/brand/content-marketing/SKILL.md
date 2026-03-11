---
name: content-marketing
description: When the user wants to plan content marketing across channels, define content types and formats, or create a content repurposing strategy. Also use when the user mentions "content marketing strategy," "content types," "content formats," "content repurposing," "content calendar," "content mix," "owned content," "content distribution," "content funnel," or "content planning across channels."
metadata:
  version: 1.2.0
---

# Strategies: Content Marketing

Guides content marketing strategy across channels: content types, formats, distribution, and repurposing. 62% of successful B2B have a documented strategy; content repurposing addresses the top challenge—consistently developing new content. Use this skill when planning content across blog, email, social, video, and pages.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Content types**: What you create (by purpose/theme)
- **Content formats**: How it's delivered (article, video, email, post)
- **Channels**: Where it's distributed (blog, email, X, LinkedIn, etc.)
- **Repurposing**: One core content → multiple formats → multiple channels
- **Funnel mapping**: Content by stage (awareness, consideration, decision)

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read Sections 3 (Value Proposition), 4 (Audience), 11 (Content Strategy).

Identify:
1. **Goals**: Traffic, conversions, brand, retention
2. **Existing content**: What already exists; audit gaps
3. **Capacity**: Resources, tools, cadence
4. **Channels**: Blog, email, social, video; which channels fit audience

## Content Types (What You Create)

| Type | Purpose | Funnel | Skills |
|------|---------|--------|--------|
| **How-to guides** | Educate; informational intent | Awareness, Consideration | content-strategy, article-content, article-page-generator |
| **Comparisons** | "X vs Y"; commercial intent | Consideration | content-strategy, alternatives-page-generator |
| **List posts** | "Top 10," "Best X" | Consideration | content-strategy, article-content, article-page-generator |
| **Case studies** | Proof; customer success | Consideration, Decision | customer-stories-page-generator |
| **Product updates** | Feature launches, release notes | Decision, Retention | changelog-page-generator |
| **News / Trending** | Industry news, hot topics | Awareness | article-content, article-page-generator |
| **Glossaries** | Definitions; internal link hub | Awareness | glossary-page-generator |
| **Tools / calculators** | Linkable assets; engagement | Consideration | — |
| **Funding / PR** | Funding, acquisitions | Brand | article-content, article-page-generator |
| **Onboarding** | Welcome, first-use guidance | Retention | email-marketing |
| **Campaign** | Promotions, limited-time | Decision | email-marketing |
| **Newsletter** | Curated insights; nurture | Retention | email-marketing |

### Product Marketing Content

| Type | Use | Format |
|------|-----|--------|
| **QA answers** | Internal reference or customer-facing; product questions | Docs, FAQ, KB |
| **Use guide** | How to use product; onboarding | Blog, docs, video |
| **Maintenance guide** | Care, upkeep, best practices | Docs, blog |
| **Troubleshooting** | Common issues, bugs, fixes | FAQ, docs, KB |

**Use**: Blog, docs, or in-product; supports activation and retention. See **faq-page-generator**, **docs-page-generator**.

## Content Formats (How It's Delivered)

| Format | Use | Skills |
|--------|-----|--------|
| **Pages** | Homepage, about, features, pricing, landing | homepage-generator, about-page-generator, landing-page-generator |
| **Articles** | Blog posts, guides, listicles | article-content, article-page-generator, blog-page-generator |
| **Email** | EDM, newsletter, sequences | email-marketing |
| **Social posts** | X, LinkedIn, Reddit, TikTok | twitter-x-posts, linkedin-posts, reddit-posts, tiktok-captions; **visual-content** for post images |
| **Video** | Short-form, long-form, webinar | video-marketing |
| **Infographics** | Visual summaries | **visual-content** |
| **Slides / PDF** | Decks, whitepapers, eBooks | — |
| **Podcast** | Audio episodes | — |

## Content Repurposing Matrix

**Principle**: One core content → multiple formats → multiple channels. Maximize ROI.

| Core Content | Formats | Channels |
|--------------|---------|----------|
| **Case study** | Article, video, infographic, slides | Blog, email, LinkedIn, YouTube, sales deck |
| **How-to guide** | Article, video, checklist, PDF | Blog, email, YouTube, docs |
| **Product update** | Article, email, post, video | Blog, email, X, LinkedIn, changelog |
| **Industry insight** | Article, podcast, post, newsletter | Blog, Spotify, X, email |

**Example**: One client success story → article (blog) + video (YouTube) + infographic (LinkedIn) + slides (sales) → 4 channels from 1 creation.

## Funnel Mapping

| Stage | Content Focus | Channels |
|-------|---------------|----------|
| **Awareness** | Education, thought leadership, glossary, how-tos | Blog, SEO, social, PR |
| **Consideration** | Comparisons, case studies, demos, features | Blog, email, landing, social |
| **Decision** | Pricing, testimonials, product pages, case studies | Website, email, sales |
| **Retention** | Onboarding, newsletter, product updates, changelog | Email, in-app, blog |

## Article Orientations

Article types by orientation—drives structure, SEO depth, and schema choice. See **article-page-generator** for page structure.

| Orientation | Examples | Primary Goal | SEO Priority |
|-------------|----------|--------------|--------------|
| **Funding / PR** | Funding rounds, acquisitions, executive hires | Brand awareness, press, investor relations | Low — thin content, few search queries |
| **Product updates** | Feature launches, release notes, changelogs | User education, product adoption | Low–medium — internal announcements rarely rank |
| **Guides / How-to** | Tutorials, step-by-step, best practices | Education, lead nurture, authority | High — matches search intent |
| **News / Trending** | Industry news, hot topics, seasonal | Engagement, social shares, topical relevance | Medium — quick traffic spikes, short shelf life |
| **Evergreen** | Pillar guides, glossaries, comparisons | Long-term traffic, backlinks, authority | High — compounds over time |

**SEO-driven vs non-SEO-driven**: SEO-driven (how-to, listicles, comparisons) → target keywords, full optimization. Non-SEO-driven (funding, product updates) → focus on clarity, shareability, internal linking to SEO content. Hybrid: product launch posts can include SEO-friendly sections (e.g., "How to use [feature]").

## Evergreen vs Timely Mix

| Mix | Ratio | Use |
|-----|-------|-----|
| **Evergreen** | 70–75% | Pillar guides, how-tos, comparisons, glossaries; long-term traffic; refresh 6–12 months |
| **Timely** | 25–30% | Seasonal, trending, news; quick spikes; link into evergreen pillars |

**Evergreen vs timely (article-level)**: Evergreen = year-round relevance; steady traffic; refresh every 6–12 months. Timely = weeks to months; spikes then decline; often one-and-done; use NewsArticle schema. Recommended mix: 70/30 or 60/40 evergreen-to-timely.

See **content-strategy** for SEO topic clusters and pillar-cluster structure.

## Content Calendar

- Map content types to topics and keywords
- Prioritize by opportunity (volume → intent → feasibility)
- Schedule by capacity; include update schedule for existing content
- Plan repurposing: which core pieces become formats for which channels
- **Visual-first**: Plan images in calendar from the start; see **visual-content** for specs and repurposing

## Output Format

- **Content types** plan (what to create)
- **Format × channel** matrix (how and where)
- **Repurposing** plan (one-to-many)
- **Funnel** mapping (awareness/consideration/decision)
- **Content calendar** (topics, keywords, deadlines, repurposing)

## Related Skills

- **content-strategy**: SEO topic clusters, pillar-cluster, editorial calendar; SEO content planning
- **integrated-marketing**: PESO model, channel mix; content as owned media
- **article-content**: Article body creation; word count by type; writing frameworks
- **article-page-generator**: Article page structure, orientations; blog content
- **email-marketing**: Email content types (onboarding, campaign, newsletter)
- **twitter-x-posts, linkedin-posts, reddit-posts, tiktok-captions**: Platform-specific post formats
- **visual-content**: Visual content planning; images for social, infographics, repurposing; cross-channel specs
- **landing-page-generator**: Landing page copy and structure
- **customer-stories-page-generator**: Case study content
- **branding**: Brand voice, storytelling; content consistency
- **translation**: Translation workflow for multilingual content; glossary, style guide
