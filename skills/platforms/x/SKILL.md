---
name: twitter-x-posts
description: When the user wants to create X (Twitter) post copy, threads, or optimize for X platform. Also use when the user mentions "X post," "Twitter post," "tweet," "thread," "X marketing," or "post to X."
metadata:
  version: 1.0.0
---

# Platforms: X (Twitter)

Guides X post copy creation and optimization. Use for generating publish-ready posts, threads, and content that performs on X. Suitable for copy agents, design agents (image specs), and video agents (video post specs).

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Output: Publish-Ready Copy

This skill enables agents to generate X post copy that can be published directly. Output includes character-counted text, thread structure, and platform-compliant formatting.

## Character Limits

| Type | Limit | Notes |
|------|-------|-------|
| **Standard post** | 280 characters | Most users |
| **Premium** | 25,000 characters | X Premium subscribers |
| **URL** | Counts as 23 chars | t.co shortens all links |
| **Emoji** | ~2 chars each | Varies by emoji |

## Optimal Lengths (Engagement)

| Use Case | Characters | Purpose |
|----------|------------|---------|
| **General** | 71-100 | Sweet spot for engagement |
| **Promotional** | 120-130 | Product/offer posts |
| **Question** | 60-80 | Drive replies |
| **Retweet-friendly** | ~116 | Leaves room for "RT @user:" |

## Thread Format

- **Structure**: 3-5 connected posts; number as 1/5, 2/5, etc.
- **First post**: Strong hook; no "thread" in first line
- **Last post**: CTA, summary, or question
- **Each post**: ~80 chars; can stand alone

## Post Structure (Hook + Value + CTA)

| Part | Ratio | Guideline |
|------|-------|-----------|
| **Hook** | 10% | First 1-2 lines; question, fact, or emotion; ~50 chars |
| **Value** | 70% | Practical info; use thread for depth |
| **CTA** | 20% | Call for reply, question, or action |

End with open question to drive replies. Thread structure can extend impressions ~10x.

## Algorithm (Grok AI)

### Signal Weights

| Signal | Impact |
|--------|--------|
| **Replies** | Highest (~54-75x likes); quality > quantity |
| **Author replies** | Active reply chains ~75x visibility |
| **Bookmark** | 2026 signal; saves boost recommendation |
| **Media** | Images/video ~2x; video 2-4x exposure |
| **External links** | Reduce score ~50%; prefer internal refs |
| **Post limit** | 5-8/day; >10/day reduces later visibility ~80% |

**Content**: Open questions, controversial views, stories; avoid "RT if agree" bait.

### TweepCred

| Threshold | Effect |
|-----------|--------|
| **< 65** | Only last 3 posts enter For You |
| **New accounts** | Need +17 to appear in feed |
| **Blue V** | Auto 100 points |

Monitor account health; avoid spam, bulk ops, excessive links.

### Distribution

Posts tested in small group first; early interaction (first 30 min) decides reach. Niche consistency helps SimClusters match.

## Link Optimization

| Practice | Guideline |
|----------|-----------|
| **Penalty** | External links ~-50%; Regular accounts: link posts 0% engagement since 2025 |
| **Placement** | Put link in reply, not main post |
| **Ratio** | Max 1 link per 5 posts |
| **Premium** | Premium+ safest for links (~0.25-0.3% engagement) |
| **Preview** | Title <60 chars, description <100 chars; 1200x628 image |

## Premium Impact

| Tier | Reach | Link posts |
|------|-------|------------|
| **Regular** | <100/post | 0% engagement |
| **Premium ($8)** | ~600/post | ~0.25-0.3% |
| **Premium+ ($40)** | ~1550/post | Safest for links |

Premium ~10x reach vs Regular. If X is core channel, Premium helps.

## Video

- **Exposure**: 2-4x vs text
- **Length**: 8-30s short video preferred
- **VQV**: High video completion boosts score 2-3x

## Content Ratio

| Type | Share | Use |
|------|-------|-----|
| **Value** | 70% | Education, how-to, insights |
| **Interaction** | 20% | Polls, questions, AMA |
| **Promo** | 10% | Product, offers |

## Twitter Cards + SEO

Cards (og:image, title, description) boost CTR ~64%, engagement ~26%. Use for Social SEO and Programmatic SEO; X traffic can accelerate Google indexing.

## Image Specs (for Design Agents)

| Format | Dimensions | Use |
|-------|------------|-----|
| **Single image** | 1200×675 (16:9) | Best visibility; no crop |
| **Square** | 800×800 | Single image |
| **Profile** | 400×400 | Avatar |
| **Header** | 1500×500 (3:1) | Banner |
| **File** | ~5MB; JPG/PNG | Over 5MB may compress |

## Output Format

When generating X copy, provide:

1. **Post text** with character count
2. **Hashtags** (if used; 1-3 recommended)
3. **Thread structure** (if thread)
4. **Image specs** (if design agent needs dimensions)

## Related Skills

- **influencer-marketing**: X is key influencer platform
- **reddit-posts**: Alternative community channel
- **open-graph, twitter-cards**: OG and Twitter Card tags for X link previews
