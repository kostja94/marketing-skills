---
name: linkedin-posts
description: When the user wants to create LinkedIn post copy or optimize for LinkedIn. Also use when the user mentions "LinkedIn post," "LinkedIn article," "professional post," "post to LinkedIn," "LinkedIn content," "LinkedIn copy," "B2B LinkedIn," "LinkedIn engagement," "LinkedIn feed," "share box," "document post," "poll," "Newsletter," "reshare," or "LinkedIn marketing." For LinkedIn ads, use linkedin-ads.
metadata:
  version: 1.2.0
---

# Platforms: LinkedIn

Guides LinkedIn post copy creation and optimization. Use for generating publish-ready professional content. Suitable for copy agents and design agents (image specs).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Output: Publish-Ready Copy

This skill enables agents to generate LinkedIn post copy optimized for engagement. Output includes character-counted text and structure for the "See more" threshold.

## Post Types and Entry Points (organic)

| Kind | What to know |
|------|----------------|
| **Start a post** | Short update; can include **link preview** if you paste a URL. Same feed format as other updates. |
| **Photo** | Single or multiple images (carousel in feed). |
| **Video** | Uploaded file (distinct from **LinkedIn Live**, which is live streaming and has separate gating). |
| **Write article** | **Article** = long-form editor, **separate** from the short post box; long URL, better for depth and some **off-site** discoverability. |
| **Document** | PDF / PPT / DOC (slides in feed). Official limits (check current help): on the order of **~100MB / ~300 pages** per file—verify when publishing. |
| **Poll** | Engagement driver; keep question and options scannable. |
| **More** (menu) | Often includes **celebrations**, **hiring**-style share, **Find an expert**, etc. (varies by product/region). |
| **Reshare** | Reshare or **quote** another member’s post with your take—adds context; avoid empty reshares. |
| **Newsletter** | **Series** subscription; not the same as a one-off post but compound reach over time. |
| **Event** | Create/promote events via a dedicated flow, not the same as a plain text post. |

**Product detail**: [Get started with posting on LinkedIn](https://www.linkedin.com/help/linkedin/answer/a518996) · [Upload and share documents](https://www.linkedin.com/help/linkedin/answer/a518909)

**Why it matters for copy**: Match CTA and length to the **form** (e.g. a document deck vs a 5-line hot take). Do not treat a **short post** and an **Article** as interchangeable.

## How the Feed Ranks (what to write for)

- The feed is **not** a pure reverse-chronological friend list. It blends **1st-degree connections, follows, company/topic interest, and recommended “out of network”** content from the **Economic Graph**, plus ads. [How the Feed ranks content](https://www.linkedin.com/help/linkedin/answer/a9554004)
- Relevance uses **context** of the post, **profile and network signals**, and **behavior** (read, react, comment, share, **dwell**). Demographics like age or gender are **not** used to rank feed visibility (per public help guidance).
- Platform direction in recent public communications: more **LLM/semantic** understanding, less **inauthentic engagement** and **engagement-bait** / low-quality repetition; favor **real expertise** and **meaningful** discussion. [Background on feed engineering (blog)](https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed)

**Writing implications**: Strong **first line** and **on-topic depth**; comments that add substance; avoid templates that look automated or “pod” coordinated.

## Off-Site SEO and GEO (brief)

- **Short feed posts** are often **login-gated** for crawlers; do **not** assume every post is indexed on Google like a blog post.
- **Public profile, Company Page, and Articles** (where public) are stronger for **name/company/role** style queries. Align **headline, about, and entity names** with your site and other public bios for **E-E-A-T**-style consistency.
- **GEO** (AI/search answers): one clear, quotable line **who you help** + links to **evidence** (site, case study, talk) in profile or long-form, not only in DMs or groups.
- For **link previews** on social: **open-graph**; for people/org **entities**: **entity-seo**; for **generative/AI search** strategy: **generative-engine-optimization**.

## Character Limits

| Type | Limit | Notes |
|------|-------|-------|
| **Post** | 3,000 characters | Optimal: 1,300–1,600 |
| **First line (critical)** | 210–235 chars | Visible before "See more"; 60–80% decide here |
| **Short posts** | 100–200 chars | Polls, announcements, quotes |

## Optimal Length by Content Type

| Type | Characters | Use |
|------|------------|-----|
| **Short** | 100–200 | Polls, announcements, quotes |
| **Medium** | 300–1,200 | Case studies, tips, BTS |
| **Long** | 1,200–2,000 | Thought leadership, analysis |
| **Sweet spot** | 1,300–1,600 | Highest engagement |
| **Avoid** | >2,000 | ~35% engagement drop |

## First Line (Hook)

- **Place key message in first 140 chars**
- **Strong openings**: Specific results, pain points, bold claims, surprising stats
- **Avoid**: Vague teases, hashtag-first, generic greetings

## Image Specs (for Design Agents)

| Format | Dimensions | Use |
|--------|------------|-----|
| **Single image** | 1200×627 (1.91:1) | Feed; link previews |
| **Square** | 1200×1200 | Single image |
| **Carousel (organic)** | Up to 20 images | Multi-image post |
| **File** | ≤10 MB; JPG/PNG | Native uploads perform better |
| **Vertical** | Preferred | 88% browse on mobile |

## Best Practices

- **Mobile-first**: 88% users on mobile
- **Polls and document (PDF) posts**: Often strong for reach; pair with a clear takeaway
- **Post frequency**: Weekly minimum is a common bar for company pages; individuals often **several times per week** if sustainable
- **Alt text**: Add for accessibility
- **B2B tone**: Professional and constructive; see **influencer-marketing** and **about-page-generator** for voice alignment with profile/brand

## Output Format

When generating LinkedIn copy, provide:

1. **First line** (≤210 chars; hook)
2. **Full post** with character count
3. **Hashtags** (a few, relevant; end of post)
4. **Image specs** (if design agent needs dimensions)
5. **Form note** if not a plain post (e.g. “pair with a 5-slide document” or “use Article for 1,200+ words”)

## Related Skills

- **linkedin-ads**: Paid promotion; same professional tone as organic
- **open-graph**: Link share previews (Facebook, LinkedIn, etc.)
- **entity-seo**: People/org **sameAs** and entity consistency
- **generative-engine-optimization**: AI search / answer visibility (cross-platform; not only LinkedIn)
- **influencer-marketing**: LinkedIn influencers for B2B
- **about-page-generator**: Professional brand alignment
- **visual-content**: Cross-channel visual planning; LinkedIn image specs in context

## Official references (index)

- [Get started with posting](https://www.linkedin.com/help/linkedin/answer/a518996) · [Feed ranking (help)](https://www.linkedin.com/help/linkedin/answer/a9554004) · [Share photos](https://www.linkedin.com/help/linkedin/answer/a527229) · [Share videos](https://www.linkedin.com/help/linkedin/answer/a7174587)
