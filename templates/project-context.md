# Project Context

> Copy to `.cursor/project-context.md` or `.claude/project-context.md`. Fill in sections that apply — the agent reads this to deliver accurate, tailored results. **Without context, AI outputs stay generic.**

**Last updated**: [YYYY-MM-DD] — Keep fresh; stale context degrades output quality.

---

## Document System (Optional)

When using multiple context documents, define roles and cross-references. Each document owns its domain; avoid duplication.

| Document | Role | References |
|----------|------|------------|
| **project-context.md** (this file) | Product overview, positioning, ICP, brand, keyword summary, competitor summary | Details in sub-documents |
| **[project]-features.md** | Feature pages, page structure, capability mapping, Title/Meta/content summary | Keywords, use cases, competitors |
| **[project]-keywords.md** | Keyword-to-page mapping, search intent, URL patterns | Feature URLs |
| **[project]-use-cases.md** | Personas, scenarios, Use Case page content | Feature internal links |
| **[project]-competitors.md** | Competitor analysis, differentiation, competitor keywords | Feature structure |
| **[project]-task-tracker.md** | Project tasks, SEO/marketing backlog, progress | Features, keywords |

**Principle**: One document per domain; cross-reference instead of duplicating. This file is the entry point; sub-documents hold specifics.

---

## Language Strategy (Optional)

Define language usage per context. Adjust to your team's needs.

| Context | Language | Notes |
|---------|----------|-------|
| **Website content** | [Primary locale] | Main site, landing pages, product copy |
| **Documents / reports** | [Your preferred language] | Strategy, analysis, tasks, insights — for internal use |
| **Product copy** | [Product language] | Positioning, slogan, key messages — keep original for reference |
| **Technical / SEO** | [Site language] | URLs, keywords, platform names — match the website |

**Rule**: Product names, feature names, URLs, keywords use site language; strategy, tasks, insights use your document language.

---

## Project Overview

| Field | Content |
|-------|---------|
| **Industry** | [e.g. B2B SaaS, e-commerce, AI tools] |
| **Website** | [e.g. https://example.com] |
| **Stage** | [Pre-launch / Beta / Growth / Mature] |
| **Core product** | [One-line summary] |
| **Slogan** | [Optional — product tagline] |
| **Metrics** | [Optional — users, conversion rate, etc.] |
| **Company** | [Optional — legal name, region] |

**Product form**:
- **Platforms**: [e.g. Web only / Web + iOS + Android / Web + desktop app / Hardware]
- **Entry points**: [e.g. Get Started, Book a Demo, Download, Subscribe]
- **Data scale** (optional): [e.g. user count, sessions analyzed, funding round]

---

## 1. Product Overview

**One-line description**:
```
[Example: A SaaS tool that helps small businesses automate audits and reporting.]
```

**Category**: [e.g. SEO software, HRIS, e-commerce platform]  
**Business model**: [e.g. B2B SaaS, B2C subscription, marketplace]  
**Pricing**: [e.g. Freemium, subscription tiers, Enterprise custom]

**Core product lines** (if multiple):

| Product / Feature | Description |
|-------------------|-------------|
| [Name] | [What it does] |
| [Name] | [What it does] |

**Differentiation**: [2–3 bullets — why choose you over alternatives]

---

## 2. Positioning Statement

Use this format (Geoffrey Moore / Crossing the Chasm):

> **For** [target customer] **who** [need/job-to-be-done], **our** [product] **is a** [category] **that** [primary benefit]. **Unlike** [alternative/competitor], **we** [differentiator] **because** [reasons to believe].

---

## 3. Value Proposition & Key Messages

- **Primary value prop**: [One sentence — what's in it for the customer]
- **Key messages**: [3–5 bullets; use verbatim customer language when possible]
- **Proof points**: [e.g. "X+ businesses", "Y% improvement", case study links]

---

## 4. Target Audience / ICP

**Primary ICP**:
- **Who**: [e.g. Marketing managers at companies with 50–500 employees]
- **Industry**: [e.g. B2B SaaS, manufacturing, e-commerce]
- **Jobs to be done**: [What progress are they trying to make?]
- **Pain points**: [Specific, not generic]
- **Buying triggers**: [e.g. New CMO, compliance audit, competitor launched feature]

**Secondary ICP**: [If different from primary]

**Language / locale**: [e.g. en-US, zh-CN, multi-language]

---

## 5. Existing Website

- **URL**: [e.g. https://example.com]
- **Tech stack**: [e.g. Next.js, WordPress, Webflow]
- **Current state**: [New site / Redesign / Migration / Iterating]
- **Product entry points**: [e.g. Web only / Web + mobile app / Web + download page]

**Navigation structure**:
- [Main nav items — e.g. Features, Pricing, Resources]
- [Secondary — e.g. Blog, FAQ, About]

**URL hierarchy** (key patterns):

| Path pattern | Example | Purpose |
|--------------|---------|---------|
| / | Homepage | — |
| /features, /pricing | Core marketing | — |
| /blog, /resources | Content | — |
| /[category], /[product] | Detail pages | — |

**Subdomains** (if any): [e.g. app.example.com, docs.example.com — note indexing strategy]

---

## 6. Keywords

| Type | Examples |
|------|----------|
| **Primary** | [Core category terms] |
| **Secondary** | [Supporting terms] |
| **Long-tail** | [Specific queries] |
| **Competitor / brand** | [e.g. "X alternative", "X vs Y"] |
| **Target intent** | [Informational / Commercial / Transactional] |

**Programmatic SEO** (if applicable): [e.g. template pages, directory — list target patterns and keywords]

---

## 7. Competitors

- **Direct**: [Competitor 1, Competitor 2]
- **Alternatives**: [Status quo, substitutes — e.g. "Manual spreadsheets", "Hiring agencies"]
- **Differentiation**: [e.g. We focus on SMBs; they target enterprises]
- **Gaps to exploit**: [e.g. Competitors lack AI-powered insights]
- **Comparison pages to create**: [e.g. "Us vs Competitor A", "Us vs Competitor B"]

---

## 8. Brand & Voice

Voice and tone for copy across touchpoints. See **branding** for full brand strategy.

- **Voice**: [e.g. Professional / Friendly / Technical / Bold]
- **Tone**: [e.g. Confident but not arrogant, helpful, concise]
- **Avoid**: [Buzzwords to never use]
- **Preferred terms**: [e.g. "audit" not "analysis", "customer" not "user"]

---

## 9. Product Documentation

- **Path or link**: [e.g. docs/, Notion URL, help center]
- **Key features**: [List main capabilities; link to detailed docs if available]

---

## 10. Other Context

- **Strategy**: [Current priorities, market focus]
- **Timeline**: [e.g. Launch in Q2, new feature release]
- **Constraints**: [e.g. No claims about pricing; avoid mentioning unlaunched features]

---

## 11. Content / Blog / Article Strategy

Articles must connect to the product and be keyword-driven. See **content-marketing** for content types, formats, and repurposing.

**Optimization foundation** (article-page-generator): **Product** + **Keywords** + **Article intent** + **Competitor articles** — these four inputs drive tailored analysis and recommendations.

**Article orientations** (not all articles are SEO-driven):
- **SEO-driven**: How-to guides, comparisons, pillar content — target keywords, optimize for search
- **Non-SEO-driven**: Funding announcements, product updates, company news — brand/PR focus, don't expect rankings
- **Evergreen vs timely**: Evergreen (70–75%) for long-term traffic; timely (25–30%) for trends, news, seasonal

**Product connection**:
- **How articles support product**: [e.g. Educate on problem product solves; introduce features; nurture leads]
- **Natural product mentions**: [Where to link — e.g. CTA in conclusion, in-paragraph when relevant]
- **Avoid**: [e.g. Purely generic content with no product tie-in]

**Keyword basis**: Use Section 6 for article topics; run keyword research (keyword-research) before drafting; map primary/secondary/long-tail to pillar vs cluster.

**Competitor articles**: Paste 3–5 high-ranking competitor URLs for a target keyword, or ask the agent to search and analyze. Output: content gaps, structure, length, H2s, keywords, CTA placement.

---

## 12. Features vs Use Cases vs Solutions

Differentiate by content angle to avoid overlap and cannibalization:

| Type | Focus | Example page |
|------|-------|--------------|
| **Features** | What the product does (capabilities) | /features, /features/[capability] |
| **Use cases** | Who uses it, in what scenario | /use-cases, /for-[persona] |
| **Solutions** | Outcome by industry / company size | /solutions, /for-[industry] |

---

## 13. Optimization Priorities (Optional)

| Priority | SEO | GEO (AI search) | Content |
|----------|-----|-----------------|---------|
| **P0** | [e.g. Fix crawlability, sitemap] | [e.g. FAQ structured for AI citation] | [e.g. Core pillar pages] |
| **P1** | [e.g. Title/meta per page type] | [e.g. Clear Q&A format] | [e.g. Comparison pages] |
| **P2** | [e.g. Internal links, schema] | — | [e.g. Long-tail articles] |

---

## 14. Visual Identity (Optional)

Use when components-brand-visual, components-logo, or pages-media-kit need visual specs.

**Colors**: Primary, secondary, backgrounds  
**Typography**: Headings, body, sizes  
**Spacing**: Margins, padding  
**Layout**: [e.g. viewport, top bar, footer]

---

## Quick Reference

| Section | Used by |
|---------|---------|
| Overview, 1–4 | All skills: SEO, pages, components, channels |
| 5 | Technical SEO, sitemap, crawlability; directory submission |
| 6 | On-page SEO, metadata, keyword research |
| 7 | Competitive positioning, content strategy |
| 8 | Copy, tone, testimonials, CTAs; see **branding** |
| 9–10 | Features, content strategy; directory features, pros/cons |
| 11 | Article creation, optimization; see **content-marketing** |
| 12 | Page taxonomy; avoid Features/Use Cases/Solutions overlap |
| 13 | Prioritization; agent suggests next steps |
| 14 | Logo, favicon, brand visual, media kit |

**Sub-document pattern**: Use `[project]-features.md`, `[project]-keywords.md`, `[project]-use-cases.md`, `[project]-competitors.md` for details. This file stays as the entry point.

**Cold start** (cold-start-strategy): Fill Overview, 1–4, 5, 6, 8, 9 for Product Hunt, directories, etc.

**Directory submission** (directory-submission): Fill Overview, 1–4, 5, 6, 8, 9 for Taaft, Product Hunt, etc.

**Tip**: Start with Overview and 1–4, 8. Add 5–7 as you have them. Update regularly — context degrades when stale.
