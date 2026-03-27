---
name: website-structure
description: When the user wants to plan website structure, decide which pages to build, or prioritize pages for a new or existing site. Also use when the user mentions "website structure," "site structure," "which pages do I need," "page planning," "sitemap planning," "Must Have pages," "website architecture," or "site hierarchy." For a specific page template (e.g. homepage), use homepage-generator or landing-page-generator as appropriate. Not for organic SEO roadmap alone; use seo-strategy.
metadata:
  version: 1.5.0
---

# Strategy: Website Structure

Guides website structure planning: which pages to build, page priority, and how structure supports UX, SEO, and growth. Structure is the organization and connection of pages; it affects user navigation, Google's understanding of content importance, crawlability, and sitelinks in SERPs. See **serp-features** for sitelinks and SERP optimization.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product type, audience, and growth goals.

Identify:
1. **Website type**: Product/SaaS, B2B, E-commerce, Portfolio, Forum, Directory
2. **Stage**: New site (plan from scratch) vs. existing (extend or audit)
3. **Growth strategy**: Affiliate, education, multi-language, community, B2B, developer
4. **Constraints**: Team size, budget, tech stack

## Page Priority Framework

Plan pages by priority for development scheduling. See [skills-reference §2 Page Taxonomy](../../../docs/skills-reference.md#2-page-taxonomy) for full page types and website-type mapping.

| Priority | Pages | Notes |
|----------|-------|-------|
| **Must Have** | Home, Product/Features, Pricing, Blog, About, Privacy, Terms, Contact | Essential for trust and conversion; Pricing: public page in nav for self-serve; enterprise-only may use "Contact sales" instead; see **pricing-page-generator** (Visibility & Placement) |
| **Great to Have** | Testimonials, FAQ, Sitemap (HTML), 404, Refund/Returns | Support UX and SEO |
| **Optional** | Search Results, News, Careers, Disclosure | Situational |
| **Traffic-driven** | Category/Collection pages | For content-heavy or e-commerce; needs Category + Tags |

## Generic Template Structure

Applicable to SaaS, tools, and content sites. Adapt by removing unused nodes (e.g. no API → drop API) and adding specific modules (e.g. industry, region).

| Section | Typical Paths | Page Skills |
|---------|---------------|-------------|
| **Root** | /, /features, /pricing, /demo, /contact | homepage-generator, features-page-generator, pricing-page-generator |
| **Tools** | /tools, /free-tools; hub + per-tool pages | tools-page-generator; free tools for lead gen; often SPA; programmatic; see **programmatic-seo** |
| **Resources** | /blog, /changelog, /glossary, /faq, /tutorials | blog-page-generator, changelog-page-generator, glossary-page-generator, faq-page-generator |
| **Partnership** | /affiliate, /startups, /ambassadors | affiliate-page-generator, landing-page-generator |
| **Legal** | /terms, /privacy, /careers | terms-page-generator, privacy-page-generator, careers-page-generator |
| **Competitor** | /alternatives, /compare, /migrate | alternatives-page-generator, migration-page-generator |
| **Standalone** | /dashboard, /login, /signup, /docs, /api, /status, /support | signup-login-page-generator, docs-page-generator, api-page-generator, status-page-generator |

## Growth Strategy → Structure Mapping

Structure reflects growth strategy. Subdirectories signal channels:

| Goal | Path Example | Page/Channel |
|------|--------------|--------------|
| Affiliate conversion | /affiliate | affiliate-page-generator |
| Education/student plan | /education, /startups, /student-discount | education-program, startups-page-generator |
| Multi-language | /zh-CN, /ja | localization-strategy |
| Community | /ambassadors, /showcase | creator-program, landing-page-generator |
| B2B / Enterprise | Solutions (industry-first), Use cases (scenario-first; can be sub-pages), Customer stories | solutions-page-generator, use-cases-page-generator, customer-stories-page-generator |
| Developer product | /api, /docs, /status | api-page-generator, docs-page-generator, status-page-generator |
| User feedback | Feedback, Roadmap | feedback-page-generator; External (Canny, FeatureBase) |
| Plugins/Integrations | /integrations, /plugins | integrations-page-generator, category-page-generator |
| Giveaway/Contest | /giveaway | contest-page-generator |

## Domain Structure (Multiple Products)

When planning for multiple products or brands, see **domain-architecture** for subfolder vs subdomain vs independent domain. This skill covers page structure within a single domain. For initial domain choice (Brand vs PMD vs EMD, TLD), see **domain-selection**.

## Planning Workflow

1. **Choose template**: Start from generic structure; map to [skills-reference §2](../../../docs/skills-reference.md#2-page-taxonomy) website types
2. **Trim modules**: Remove irrelevant nodes (e.g. no API → drop /api, /docs)
3. **Add specifics**: Industry pages, region, product variants
4. **Assign URLs**: Per node; follow **url-structure** (lowercase, hyphens, short, keyword-rich)
5. **Export list**: "Page type + URL + Priority" for dev scheduling
6. **Tech stack**: Match page types to services (DNS, auth, CMS, status page, etc.)
7. **Iterate**: Expand with new features, markets; keep structure clear

## Structure Principles

| Principle | Guideline |
|-----------|-----------|
| **Flat structure** | Max 4 clicks from homepage to any page; improves crawlability and weight distribution |
| **Early planning** | Plan structure before growth; can start right after domain purchase |
| **Sitelinks** | Good structure + TOC + authoritative internal links → natural sitelinks in SERP (cannot be forced via schema); see **serp-features** |
| **Orphan prevention** | Every page needs internal links; see **site-crawlability** and **internal-links** |
| **Features vs Use cases** | /features = capability-first; /use-cases = scenario-first; differentiate content angle, link between, avoid overlap; see **features-page-generator**, **use-cases-page-generator** |
| **Clear navigation** | Clear hierarchy and nav improve task completion; users find what they need faster; see **navigation-menu-generator** |
| **Pricing placement** | Marketing site: /pricing in main nav for prospects; in-app: Settings → Billing in sidebar for logged-in users (subscription management). Enterprise-only: "Contact sales" may replace public pricing page; see **pricing-page-generator** |

## Homepage Module Reference

See **homepage-generator** for common modules (Headline, Subheadline, CTA, Benefits, Social Proof, etc.), navigation options, and **hero-generator** for hero design.

## Output Format

- **Page list** with priority (Must Have / Great to Have / Optional)
- **URL structure** (paths per section)
- **Website-type fit** (which pages apply per [skills-reference §2](../../../docs/skills-reference.md#2-page-taxonomy))
- **Growth mapping** (which paths support which channels)
- **Next steps**: url-structure for URL rules; xml-sitemap for submission; site-crawlability for audit

## References

- [Website structure SEO guide](https://alignify.co/zh/seo/website-structure) — Alignify: structure importance, page priority, generic template, planning workflow, growth mapping, homepage modules
- **skills-reference §2** (docs/skills-reference.md#2-page-taxonomy) — Full page types, website-type matrix, core vs extended; use for page selection

## Related Skills

- **seo-strategy**: SEO workflow order; structure planning fits before Technical phase
- **domain-selection**: Initial domain choice; do before structure when choosing domain
- **domain-architecture**: Subfolder vs subdomain vs independent; do before structure if domain decision pending
- **url-structure**: URL optimization, hierarchy, slugs; apply after structure is defined
- **site-crawlability**: Crawlability, orphan pages, redirects; audit existing structure
- **internal-links**: Link strategy, hub-spoke; implement after pages exist
- **xml-sitemap**: Sitemap creation; include planned URLs
- **breadcrumb-generator**: Breadcrumb for hierarchy; large sites, e-commerce
- **navigation-menu-generator**: Nav design; primary, footer, mobile
- **content-strategy**: Content clusters, pillar pages; complements structure planning
