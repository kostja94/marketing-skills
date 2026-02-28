# Skills Task Progress

> Copy to `.cursor/skills-task-progress.md` or `.claude/skills-task-progress.md`. Track marketing & SEO tasks when skills are installed in your project. The agent reads this to understand what's done and what's next.

**Last updated**: [YYYY-MM-DD] — Update after each task; stale progress misguides the agent.

---

## Legend

| Status | Meaning |
|--------|---------|
| **Pending** | Not started; needs work |
| **In Progress** | Currently working on it |
| **Done** | Completed |

| Priority | Meaning |
|----------|---------|
| **P0** | Blocker — fix first (e.g. crawlability, indexing) |
| **P1** | High — core SEO/marketing; do soon |
| **P2** | Medium — important but not urgent |
| **P3** | Low — nice to have |

**Workflow order**: Technical SEO → On-Page → Content → Off-Page. Fix foundation before optimizing pages.

---

## 1. Technical SEO (Foundation)

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| robots.txt | robots-txt | Pending | P0 | | |
| sitemap.xml | xml-sitemap | Pending | P0 | | |
| Canonical URLs | canonical-tag | Pending | P1 | | |
| Indexing (noindex, GSC) | indexing | Pending | P1 | | |
| IndexNow (Bing) | indexnow | Pending | P2 | | |
| Crawlability (redirects, links, orphans) | site-crawlability | Pending | P0 | | |

---

## 2. On-Page SEO

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Title tag | title-tag | Pending | P1 | | |
| Meta description | meta-description | Pending | P1 | | |
| Hreflang, meta robots, viewport | page-metadata | Pending | P1 | | |
| Open Graph | open-graph | Pending | P2 | | |
| Twitter Cards | twitter-cards | Pending | P2 | | |
| Schema / structured data | schema-markup | Pending | P1 | | |
| Internal linking | internal-links | Pending | P1 | | |
| URL structure | url-structure | Pending | P2 | | |
| Heading structure (H1–H6) | heading-structure | Pending | P1 | | |

---

## 3. Content SEO

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Keyword research | keyword-research | Pending | P1 | | |
| Content strategy (clusters, pillar) | content-strategy | Pending | P2 | | |

---

## 4. Off-Page SEO

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Link building | link-building | Pending | P2 | | |
| Backlink analysis | backlink-analysis | Pending | P2 | | |

---

## 5. Pages

Add rows for pages that exist or need creation. See [page-types-taxonomy](https://github.com/kostja94/marketing-skills/blob/main/docs/page-types-taxonomy.md) for full taxonomy.

| Page | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Homepage | homepage-generator | Pending | P1 | | |
| Pricing | pricing-page-generator | Pending | P1 | | |
| Features | features-page-generator | Pending | P1 | | |
| Blog | blog-page-generator | Pending | P2 | | |
| FAQ | faq-page-generator | Pending | P2 | | |
| About | about-page-generator | Pending | P2 | | |
| Contact | contact-page-generator | Pending | P2 | | |
| Privacy / Terms / Legal | privacy-page-generator, terms-page-generator | Pending | P1 | | |
| *[Add more as needed]* | | | | | |

---

## 6. Components

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Navigation | navigation-menu-generator | Pending | P1 | | |
| Breadcrumbs | breadcrumb-generator | Pending | P1 | | |
| Footer | footer-generator | Pending | P1 | | |
| Hero | hero-generator | Pending | P1 | | |
| CTAs | cta-generator | Pending | P1 | | |
| Trust badges / Testimonials | trust-badges-generator, testimonials-generator | Pending | P2 | | |
| Newsletter signup | newsletter-signup-generator | Pending | P2 | | |

---

## 7. Channels & Platforms

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Directory submission (Taaft, Product Hunt) | directory-submission | Pending | P2 | | |
| Affiliate / Influencer / Referral | affiliate-marketing, etc. | Pending | P2 | | |
| X / LinkedIn / Reddit / TikTok | twitter-x-posts, linkedin-posts, etc. | Pending | P2 | | |
| Grokipedia / GEO (AI search) | grokipedia-recommendations, generative-engine-optimization | Pending | P2 | | |

---

## 8. Analytics

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| GA4 / event tracking | analytics-tracking | Pending | P1 | | |
| Search Console setup | google-search-console | Pending | P1 | | |
| AI traffic tracking | ai-traffic-tracking | Pending | P2 | | |

---

## Optional: ICE Score (Advanced)

For nuanced prioritization, use **Impact (1–10) × Confidence (1–10) × Ease (1–10)**. Higher = do first.

| Task | Impact | Confidence | Ease | ICE | Notes |
|------|--------|------------|------|-----|-------|
| *Example* | 8 | 7 | 9 | 504 | High impact, easy win |
| | | | | | |

---

## Quick Reference

| Section | When to tackle |
|---------|----------------|
| 1. Technical SEO | First — fix crawlability, indexing, sitemap |
| 2–4. On-Page, Content, Off-Page | After technical foundation |
| 5. Pages | Per page type; prioritize high-traffic pages |
| 6. Components | With page work |
| 7. Channels | When ready for distribution |
| 8. Analytics | Early — need data to measure |

**Tip**: Delete rows for skills you didn't install. Add custom tasks (e.g. "Migrate to new CMS") as needed. The agent uses this file to avoid redundant work and suggest next steps.
