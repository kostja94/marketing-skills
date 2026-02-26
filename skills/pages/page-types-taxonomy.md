# Page Types Taxonomy

> A website page classification framework based on industry best practices. Use for navigation design, sitemaps, content strategy, and SEO optimization.

## Classification Dimensions

### 1. By Purpose

| Purpose | Goal | Key Metrics |
|---------|------|-------------|
| **Brand** | Build awareness, trust, identity | Brand search, dwell time, trust signals |
| **SEO** | Organic traffic, educate users, topical authority | Organic rankings, traffic, backlinks |
| **Marketing** | Conversion, acquisition, partnership recruitment | Conversion rate, CAC, signups/purchases |
| **Legal** | Compliance, transparency, risk control | Compliance, accessibility |
| **Utility** | Navigation support, UX, system functions | Usability, error recovery |

### 2. By Search Intent

| Intent | User Stage | Typical Pages |
|--------|------------|---------------|
| **Navigational** | Finding brand/website | Homepage, brand pages |
| **Informational** | Learning, understanding | Blog, guides, glossary, FAQ |
| **Commercial** | Comparing, evaluating | Features, pricing, services, case studies |
| **Transactional** | Buying, signing up, taking action | Product pages, pricing, landing pages |

### 3. By Funnel Stage

| Stage | Goal | Conversion Strength |
|-------|------|---------------------|
| **Awareness** | Attract, educate | Low |
| **Consideration** | Compare, evaluate | Medium |
| **Decision** | Convert, purchase | High |
| **Support** | Trust, compliance, post-sale | Indirect |

---

## Page Classification Mapping

### Brand

Build brand identity, trust, and E-E-A-T signals. Core goal: help users and search engines understand "who you are."

| Page | Skill | Intent | Funnel | Notes |
|------|-------|--------|--------|-------|
| **Home** | pages-home | Navigational | Awareness | Brand hub, internal link anchor, authority distribution |
| **About** | pages-about | Navigational | Awareness | Company story, team, trust, E-E-A-T |
| **Contact** | pages-contact | Navigational | Support | Accessibility, local SEO, trust signals |

---

### SEO / Content (Informational)

Focused on organic traffic, educating users, and topical authority. Goals: long-tail keywords, featured snippets, AI answer citations.

| Page | Skill | Intent | Funnel | Notes |
|------|-------|--------|--------|-------|
| **Features** | pages-features | Commercial | Consideration | Product value, benefit comparison, SEO keywords |
| **Glossary** | pages-glossary | Informational | Awareness | Definitions, internal linking, long-tail traffic |
| **Blog** | pages-blog | Informational | Awareness | Articles, guides, topic clusters |
| **Resources** | pages-resources | Informational | Awareness | Content hub, guides, templates, tools |
| **FAQ** | pages-faq | Informational | Consideration | Common questions, Q&A, Featured Snippet |
| **API** | pages-api | Informational | Consideration | API introduction page (typically /api); overview, links to docs; docs are separate |

---

### Marketing (Conversion)

Focused on conversion, acquisition, and partnership recruitment. Goals: signups, purchases, applications, partnerships.

| Page | Skill | Intent | Funnel | Notes |
|------|-------|--------|--------|-------|
| **Pricing** | pages-pricing | Transactional | Decision | Plans, pricing, objection handling |
| **Products** | pages-products | Transactional | Decision | Product listing, e-commerce |
| **Services** | pages-services | Commercial | Consideration | Service overview, consulting/agency |
| **Category pages** | pages-category-pages | Commercial | Consideration | E-commerce categories, faceted navigation |
| **Customer stories** | pages-customer-stories | Commercial | Consideration | Case studies, social proof |
| **Affiliate program** | pages-affiliate-program | Transactional | Decision | Commission, recruitment, partnership signup |
| **Media kit** | pages-media-kit | Commercial | Consideration | Press assets, brand materials, PR |

> **Creator Program page**: If you create a standalone Creator Program landing page, place it under marketing, similar to affiliate-program.

---

### Legal (Compliance)

Legal compliance, transparency, user rights. Goals: reduce risk, meet regulations, build trust.

| Page | Skill | Intent | Funnel | Notes |
|------|-------|--------|--------|-------|
| **Privacy** | pages-privacy | — | Support | Data handling, GDPR, CCPA |
| **Terms** | pages-terms | — | Support | Terms of use, liability |
| **Cookie policy** | pages-cookie-policy | — | Support | Cookies, tracking, consent |
| **Legal** | pages-legal | — | Support | Legal overview, compliance entry |
| **Refund** | pages-refund | — | Support | Refund/return policy (e-commerce) |
| **Shipping** | pages-shipping | — | Support | Delivery info (e-commerce) |

---

### Utility (System)

Support navigation, error handling, system functions. Not optimized for rankings; serves UX and crawlers.

| Page | Skill | Intent | Funnel | Notes |
|------|-------|--------|--------|-------|
| **404** | pages-404 | — | — | Error page, recovery path, UX |
| **Careers** | pages-careers | Commercial | Consideration | Jobs, employer branding |

---

## Best Practices Summary

### 1. Match Intent to Page Type

- Informational keywords → Blog, guides, FAQ, glossary
- Commercial keywords → Features, services, pricing, case studies
- Transactional keywords → Products, pricing, landing pages
- Navigational keywords → Homepage, about

### 2. Avoid Intent Mismatch

- Don't write purchase-focused content on a blog
- Don't overload landing pages with educational long-form content
- Each page should have one clear primary goal

### 3. Internal Linking Strategy

- Brand pages → Link to core conversion paths
- SEO pages → Link to commercial/transactional pages
- Legal pages → Place in footer, no need to promote heavily

### 4. Indexing & Crawling

- Brand, SEO, marketing pages: Index by default
- Legal pages: Index but not keyword-optimized
- System pages (e.g. confirmation, search results): Noindex recommended

### 5. Navigation & Information Architecture

- Primary nav: Brand + core marketing pages
- Secondary nav: SEO content (blog, resources, glossary)
- Footer: Legal, contact, utility pages

---

## Quick Reference

- **Brand**: home, about, contact → `skills/pages/brand/`
- **SEO / Content**: features, glossary, blog, resources, faq, api → `skills/pages/content/`
- **Marketing**: pricing, products, services, category-pages, customer-stories, affiliate-program, media-kit → `skills/pages/marketing/`
- **Legal**: privacy, terms, cookie-policy, legal, refund, shipping → `skills/pages/legal/`
- **Utility**: 404, careers → `skills/pages/utility/`
