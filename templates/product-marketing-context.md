# Product Marketing Context

> Copy to `.cursor/product-marketing-context.md` or `.claude/product-marketing-context.md`. Fill in sections that apply — the agent reads this to deliver accurate, tailored results. **Without context, AI outputs stay generic.**

**Last updated**: [YYYY-MM-DD] — Keep fresh; stale context degrades output quality.

---

## 1. Product Overview

**One-line description**:
```
Example: A SaaS tool that helps small businesses automate SEO audits and reporting.
```

**Category**: [e.g. SEO software, HRIS, e-commerce platform]  
**Business model**: [e.g. B2B SaaS, B2C subscription, marketplace]  
**Pricing**: [e.g. Freemium, $29–199/mo, Enterprise custom]

---

## 2. Positioning Statement

Use this format (Geoffrey Moore / Crossing the Chasm):

> **For** [target customer] **who** [need/job-to-be-done], **our** [product] **is a** [category] **that** [primary benefit]. **Unlike** [alternative/competitor], **we** [differentiator] **because** [reasons to believe].

```
Example: For marketing managers at SMBs who need to run SEO audits without hiring an agency, our product is an SEO platform that automates audits and reporting. Unlike enterprise tools like SEMrush, we focus on simplicity and affordability because we're built for teams under 50 people and priced at $29/mo.
```

---

## 3. Value Proposition & Key Messages

- **Primary value prop**: [One sentence — what's in it for the customer]
- **Key messages**: [3–5 bullets; use verbatim customer language when possible]
- **Proof points**: [e.g. "10,000+ businesses", "64% reduction in X", case study links]

---

## 4. Target Audience / ICP

**Primary ICP**:
- **Who**: [e.g. Marketing managers at companies with 50–500 employees]
- **Industry**: [e.g. B2B SaaS, manufacturing, e-commerce]
- **Jobs to be done**: [What progress are they trying to make?]
- **Pain points**: [Specific, not generic — e.g. "Manual audits take 8+ hours weekly"]
- **Buying triggers**: [e.g. New CMO, compliance audit, competitor launched feature]

**Secondary ICP**: [If different from primary]

**Language / locale**: [e.g. en-US, zh-CN, multi-language]

---

## 5. Existing Website

- **URL**: [e.g. https://example.com]
- **Tech stack**: [e.g. Next.js, WordPress, Webflow]
- **Current state**: [New site / Redesign / Migration / Iterating]
- **Key pages**: [e.g. /pricing, /features, /blog, /about]

---

## 6. Keywords

| Type | Examples |
|------|----------|
| **Primary** | [e.g. SEO audit tool, keyword research]
| **Secondary** | [e.g. small business SEO, automated reporting]
| **Long-tail** | [e.g. SEO audit tool for startups]
| **Target intent** | [Informational / Commercial / Transactional]

---

## 7. Competitors

- **Direct**: [Competitor 1, Competitor 2]
- **Alternatives**: [Status quo, substitutes — e.g. "Manual spreadsheets", "Hiring agencies"]
- **Differentiation**: [e.g. We focus on SMBs; they target enterprises]
- **Gaps to exploit**: [e.g. Competitors lack AI-powered insights]

---

## 8. Brand & Voice

- **Voice**: [e.g. Professional / Friendly / Technical / Bold]
- **Tone**: [e.g. Confident but not arrogant, helpful, concise]
- **Avoid**: [Buzzwords to never use — e.g. "streamline", "revolutionize", "synergy"]
- **Preferred terms**: [e.g. "audit" not "analysis", "customer" not "user"]

---

## 9. Product Documentation

- **Path or link**: [e.g. docs/product.md, Notion URL, help center]
- **Key features**: [List main capabilities; link to detailed docs if available]

---

## 10. Other Context

- **Strategy**: [Current priorities, market focus]
- **Timeline**: [e.g. Launch in Q2, new feature release]
- **Constraints**: [e.g. No claims about pricing; avoid mentioning unlaunched features]

---

## 11. Content / Blog / Article Strategy

Articles must connect to the product and be keyword-driven. Use this section so the agent can create or optimize content that supports conversion.

**Optimization foundation** (pages-article): **Product** + **Keywords** + **Article intent** + **Competitor articles** — these four inputs drive tailored analysis and recommendations.

**Article orientations** (not all articles are SEO-driven):
- **SEO-driven**: How-to guides, comparisons, pillar content — target keywords, optimize for search
- **Non-SEO-driven**: Funding announcements, product updates, company news — brand/PR focus, don't expect rankings
- **Evergreen vs timely**: Evergreen (70–75%) for long-term traffic; timely (25–30%) for trends, news, seasonal — see pages-article for mix and structure

**Product connection**:
- **How articles support product**: [e.g. Educate on problem product solves; introduce features; nurture leads]
- **Natural product mentions**: [Where to link — e.g. CTA in conclusion, in-paragraph when relevant]
- **Avoid**: [e.g. Purely generic content with no product tie-in]

**Keyword basis**:
- Use **Section 6 (Keywords)** for article topics and target terms
- Run keyword research (seo-content-keyword-research) before drafting
- Map primary/secondary/long-tail to article types (pillar vs cluster)

**Competitor articles for optimization**:
- **URLs to analyze**: [Optional — paste 3–5 high-ranking competitor URLs for a target keyword]
- **Or**: Ask the agent to search for top-ranking articles for a keyword; agent fetches and analyzes them
- **Output**: Optimization suggestions (content gaps, structure, length, H2s, keywords, CTA placement)

```
Example URLs to analyze (for "SEO audit tool"):
- https://competitor1.com/best-seo-audit-tools
- https://competitor2.com/seo-audit-guide
- https://competitor3.com/how-to-audit-website-seo
```

---

## 12. Visual Identity (Optional)

Use when components-brand-visual, components-logo, or pages-media-kit need visual specs. Document colors, typography, spacing so the agent can apply consistent branding.

**Colors**:
- Primary: [e.g. #4D46FE]
- Secondary/accent: [e.g. #8F6CFF, #B592FF]
- Backgrounds: [e.g. #F4F5F7, #191919; gradients with opacity]

**Typography**:
- Headings: [font, weight, color — e.g. Barlow Condensed Semi Bold #191919]
- Body: [font, weight, color — e.g. Poppins Regular #666666]
- Sizes: [e.g. Hero 120pt, section 60pt, sub 28pt, body 16pt]

**Spacing**: [e.g. 120px horizontal margin; 120px section padding]

**Layout** (if fixed): [e.g. viewport 1440x900; top bar 72px; footer 620px]

---

## Quick Reference

| Section | Used by |
|---------|---------|
| 1-4 | All skills: SEO, pages, components, channels |
| 5 | Technical SEO, sitemap, crawlability; directory submission (URL) |
| 6 | On-page SEO, metadata, keyword research; directory tags, Primary Task |
| 7 | Competitive positioning, content strategy |
| 8 | Copy, tone, testimonials, CTAs; directory descriptions |
| 9-10 | Features, API docs, content strategy; directory features, pros/cons |
| 11 | Article creation, optimization; competitor analysis; product-linked content |
| 12 | Logo, favicon, brand visual, media kit; typography, colors, spacing |

**Directory submission** (channels-directories): When submitting to Taaft, Product Hunt, etc., the agent reads this file and generates ready-to-paste content (tagline, description, pros/cons, tags) per platform. Fill 1–4, 5, 6, 8, 9 for best results.

**Tip**: Start with 1–4 and 8. Add 5–7 as you have them. Update regularly — context degrades when stale.
