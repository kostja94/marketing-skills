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
| robots.txt | seo-technical-robots | Pending | P0 | | |
| sitemap.xml | seo-technical-sitemap | Pending | P0 | | |
| Canonical URLs | seo-technical-canonical | Pending | P1 | | |
| Indexing (noindex, GSC) | seo-technical-indexing | Pending | P1 | | |
| IndexNow (Bing) | seo-technical-indexnow | Pending | P2 | | |
| Crawlability (redirects, links, orphans) | seo-technical-crawlability | Pending | P0 | | |

---

## 2. On-Page SEO

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Meta tags (title, description, hreflang) | seo-on-page-metadata | Pending | P1 | | |
| Schema / structured data | seo-on-page-schema | Pending | P1 | | |
| Internal linking | seo-on-page-internal-links | Pending | P1 | | |
| URL structure | seo-on-page-url-structure | Pending | P2 | | |
| Heading structure (H1–H6) | seo-on-page-heading | Pending | P1 | | |

---

## 3. Content SEO

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Keyword research | seo-content-keyword-research | Pending | P1 | | |
| Content strategy (clusters, pillar) | seo-content-content-strategy | Pending | P2 | | |

---

## 4. Off-Page SEO

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Link building | seo-off-page-link-building | Pending | P2 | | |
| Backlink analysis | seo-off-page-backlink-analysis | Pending | P2 | | |

---

## 5. Pages

Add rows for pages that exist or need creation. See [page-types-taxonomy](https://github.com/kostja94/marketing-skills/blob/main/docs/page-types-taxonomy.md) for full taxonomy.

| Page | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Homepage | pages-home | Pending | P1 | | |
| Pricing | pages-pricing | Pending | P1 | | |
| Features | pages-features | Pending | P1 | | |
| Blog | pages-blog | Pending | P2 | | |
| FAQ | pages-faq | Pending | P2 | | |
| About | pages-about | Pending | P2 | | |
| Contact | pages-contact | Pending | P2 | | |
| Privacy / Terms / Legal | pages-privacy, pages-terms | Pending | P1 | | |
| *[Add more as needed]* | | | | | |

---

## 6. Components

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Navigation | components-navigation-menu | Pending | P1 | | |
| Footer | components-footer | Pending | P1 | | |
| Hero | components-hero | Pending | P1 | | |
| CTAs | components-cta | Pending | P1 | | |
| Trust badges / Testimonials | components-trust-badges, components-testimonials | Pending | P2 | | |
| Newsletter signup | components-newsletter-signup | Pending | P2 | | |

---

## 7. Channels & Platforms

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| Directory submission (Taaft, Product Hunt) | channels-directories | Pending | P2 | | |
| Affiliate / Influencer / Referral | channels-affiliate, etc. | Pending | P2 | | |
| X / LinkedIn / Reddit / TikTok | platforms-* | Pending | P2 | | |
| Grokipedia / GEO (AI search) | platforms-grokipedia, strategies-geo | Pending | P2 | | |

---

## 8. Analytics

| Task | Skill | Status | Priority | Notes | Updated |
|------|-------|--------|----------|-------|---------|
| GA4 / event tracking | analytics-tracking | Pending | P1 | | |
| Search Console setup | analytics-google-search-console | Pending | P1 | | |
| AI traffic tracking | analytics-ai-traffic | Pending | P2 | | |

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
