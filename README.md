# Marketing & SEO Skills for AI Agents

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

64 specialized skills for Claude Code, Cursor, and other AI agents — SEO, 24 page types, channels, platforms, strategies, components, and analytics.

By [kostja94](https://github.com/kostja94)

## Table of Contents

- [What are Skills?](#what-are-skills)
- [Installation](#installation)
- [Usage](#usage)
- [Project Context](#project-context) — Add context for tailored results
- [How Skills Work Together](#how-skills-work-together)
- [Available Skills](#available-skills)
- [Contributing](#contributing)
- [References](#references)
- [License](#license)

## What are Skills?

Skills are markdown files that give AI agents focused knowledge and workflows for specific tasks. Add them to your project, and your agent can handle SEO and page optimization with the right frameworks and best practices.

**Skills = for agents.** For human-readable SEO guides and growth strategies, see [Alignify](https://alignify.co/).

**For best results**: Add a [Project Context](#project-context) file — without it, outputs stay generic.

## Installation

### CLI (Recommended)

```bash
# Install all skills
npx skills add kostja94/marketing-skills

# Install specific skills
npx skills add kostja94/marketing-skills --skill seo-technical-robots seo-on-page-metadata

# List available skills
npx skills add kostja94/marketing-skills --list
```

### Clone and Copy

```bash
git clone https://github.com/kostja94/marketing-skills.git
cp -r marketing-skills/skills/* .cursor/skills/
cp -r marketing-skills/templates .cursor/
cp -r marketing-skills/tools .cursor/
# Copy context template: cp marketing-skills/templates/product-marketing-context.md .cursor/
# For Claude Code: use .claude/ instead of .cursor/
```

### Git Submodule

```bash
git submodule add https://github.com/kostja94/marketing-skills.git .cursor/marketing-skills
# Reference skills from .cursor/marketing-skills/skills/
# Copy context template: cp .cursor/marketing-skills/templates/product-marketing-context.md .cursor/
```

## Usage

Ask your AI agent — it will pick the right skill:

| You say | Skill used |
|---------|------------|
| *SEO* | — |
| "Configure robots.txt with AI crawler rules" | seo-technical-robots |
| "Audit and optimize my sitemap" | seo-technical-sitemap |
| "Fix canonical URLs and duplicate content" | seo-technical-canonical |
| "Fix indexing issues in Search Console" | seo-technical-indexing |
| "Implement IndexNow for Bing" | seo-technical-indexnow |
| "Unify sitemap, IndexNow, feed data" | seo-technical-sitemap |
| "Audit redirect chains and crawlability" | seo-technical-crawlability |
| "Optimize meta tags and title" | seo-on-page-metadata |
| "Add schema markup for rich results" | seo-on-page-schema |
| "Audit my internal linking structure" | seo-on-page-internal-links |
| "Optimize URL structure" | seo-on-page-url-structure |
| "Fix heading structure (H1–H6)" | seo-on-page-heading |
| "Keyword research and search intent" | seo-content-keyword-research |
| "Create content strategy with pillar and cluster pages" | seo-content-content-strategy |
| "Link building and outreach" | seo-off-page-link-building |
| "Backlink audit and toxic links" | seo-off-page-backlink-analysis |
| *Pages* | — |
| "Optimize my homepage for conversions" | pages-home |
| "Create pricing page" | pages-pricing |
| "Create features page" | pages-features |
| "Create product listing page" | pages-products |
| "Optimize e-commerce category pages" | pages-category-pages |
| "Create services page" | pages-services |
| "Create a 404 page that recovers users" | pages-404 |
| "Write an About page" | pages-about |
| "Create careers page" | pages-careers |
| "Create affiliate program page" | pages-affiliate-program |
| "Create API introduction page" | pages-api |
| "Create blog page" | pages-blog |
| "Create contact page" | pages-contact |
| "Create refund/return policy" | pages-refund |
| "Create shipping policy" | pages-shipping |
| "Create cookie policy" | pages-cookie-policy |
| "Create customer stories page" | pages-customer-stories |
| "Build high-converting FAQ page" | pages-faq |
| "Create glossary page" | pages-glossary |
| "Create legal pages" | pages-legal |
| "Create media kit" | pages-media-kit |
| "Create privacy policy" | pages-privacy |
| "Create resources page" | pages-resources |
| "Create terms of service" | pages-terms |
| *Components* | — |
| "Design navigation menu for SEO" | components-navigation-menu |
| "Optimize footer for SEO and UX" | components-footer |
| "Add table of contents to long articles" | components-toc |
| "Design hero section for conversion" | components-hero |
| "Optimize logo placement" | components-logo |
| "Add trust badges or Trusted by logos" | components-trust-badges |
| "Design testimonials section" | components-testimonials |
| "Optimize CTA buttons" | components-cta |
| "Design newsletter signup form" | components-newsletter-signup |
| *Channels* | — |
| "Plan affiliate marketing strategy" | channels-affiliate |
| "Plan influencer marketing campaign" | channels-influencer |
| "Set up referral program" | channels-referral |
| "Build creator program" | channels-creator-program |
| *Platforms* | — |
| "Generate X post copy" | platforms-x |
| "Create Reddit post" | platforms-reddit |
| "Write LinkedIn post" | platforms-linkedin |
| "Create TikTok caption" | platforms-tiktok |
| *Strategies* | — |
| "Optimize for AI search (GEO)" | strategies-geo |
| "Plan localization for global markets" | strategies-localization |
| *Analytics* | — |
| "Analyze dark traffic and attribution" | analytics-traffic |
| "Set up GA4 event tracking" | analytics-tracking |
| "Track AI search traffic in GA4" | analytics-ai-traffic |
## Project Context

**Without context, AI outputs stay generic.** Add a context file so the agent delivers tailored SEO, copy, and strategy.

### Step 1: Get the template

```bash
# If you cloned or use submodule:
cp marketing-skills/templates/product-marketing-context.md .cursor/product-marketing-context.md

# If you used CLI install, download the template:
curl -o .cursor/product-marketing-context.md https://raw.githubusercontent.com/kostja94/marketing-skills/main/templates/product-marketing-context.md
```

For Claude Code, use `.claude/product-marketing-context.md` instead.

### Step 2: Fill in (start with essentials)

| Priority | Section | What to add |
|----------|---------|-------------|
| **Must** | 1. Product Overview | One-line description, category, pricing |
| **Must** | 2. Positioning Statement | For [target] who [need], our [product] is a [category] that [benefit] |
| **Must** | 4. Target Audience / ICP | Who, pain points, jobs-to-be-done |
| **Must** | 8. Brand & Voice | Tone, words to avoid |
| **As you have** | 5. Existing Website | URL, tech stack, key pages |
| **As you have** | 6. Keywords | Primary, secondary, intent |
| **As you have** | 7. Competitors | Direct, alternatives, differentiation |

**Tip**: Start with 1, 2, 4, 8. Add the rest as you have them. Update regularly — stale context degrades output quality.

### How it works

Skills automatically read `.cursor/product-marketing-context.md` (or `.claude/`) when executing. No extra prompts needed.

## How Skills Work Together

Recommended workflow: **Technical** → **On-Page** → **Content** → **Off-Page**. Page skills apply SEO when optimizing specific page types.

```
                    ┌─────────────────────────────────────────────────────────┐
                    │              Technical SEO (Foundation)                  │
                    │  robots · sitemap · canonical · indexing · crawlability  │
                    │  indexnow                                              │
                    └──────────────────────────┬──────────────────────────────┘
                                               │
         ┌─────────────────────────────────────┼─────────────────────────────────────┐
         ▼                                     ▼                                     ▼
┌─────────────────────┐           ┌─────────────────────┐           ┌─────────────────────┐
│      On-Page        │           │       Content         │           │      Off-Page        │
│  metadata · schema  │◄─────────►│ keyword-research    │           │  link-building      │
│  internal-links     │           │ content-strategy     │           │  backlink-analysis   │
│  url-structure      │           └─────────────────────┘           └─────────────────────┘
│  heading           │
└─────────┬───────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                    Pages (by purpose: brand · SEO · marketing · legal · utility)         │
│  home · about · contact | features · glossary · blog · resources · faq · api |          │
│  pricing · products · services · category-pages · customer-stories · affiliate ·       │
│  media-kit | privacy · terms · cookie-policy · legal · refund · shipping | 404 · careers  │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  Channels: affiliate · influencer · referral · creator-program                         │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  Platforms: x · reddit · linkedin · tiktok  |  Strategies: geo · localization          │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  Components: nav · footer · hero · toc · logo · trust-badges · testimonials · cta ·     │
│  newsletter-signup  |  Analytics: traffic · tracking · ai-traffic                        │
└─────────────────────────────────────────────────────────────────────────────────────────┘

Cross-references: metadata ↔ schema ↔ heading  |  sitemap ↔ indexnow
                internal-links ↔ crawlability  |  link-building ↔ backlink-analysis
```

See each skill's **Related Skills** section for the full dependency map.

## Available Skills

### SEO

#### Technical

| Skill | Description |
|-------|-------------|
| [seo-technical-robots](skills/seo/technical/robots/) | Configure and audit robots.txt, AI crawler rules |
| [seo-technical-sitemap](skills/seo/technical/sitemap/) | Create, audit, and optimize sitemap.xml |
| [seo-technical-canonical](skills/seo/technical/canonical/) | Configure canonical URLs, fix duplicate content |
| [seo-technical-indexing](skills/seo/technical/indexing/) | Fix indexing issues, noindex, Search Console |
| [seo-technical-indexnow](skills/seo/technical/indexnow/) | Implement IndexNow for faster Bing indexing |
| [seo-technical-crawlability](skills/seo/technical/crawlability/) | Redirect chains, broken links, site structure, orphan pages, pagination |

#### On-Page

| Skill | Description |
|-------|-------------|
| [seo-on-page-metadata](skills/seo/on-page/metadata/) | Meta tags, title, description, hreflang |
| [seo-on-page-schema](skills/seo/on-page/schema/) | Structured data (Schema.org, JSON-LD) |
| [seo-on-page-internal-links](skills/seo/on-page/internal-links/) | Internal linking, link equity, orphan pages |
| [seo-on-page-url-structure](skills/seo/on-page/url-structure/) | URL optimization, hierarchy, slugs |
| [seo-on-page-heading](skills/seo/on-page/heading/) | Heading structure (H1–H6), content outline |

#### Off-Page

| Skill | Description |
|-------|-------------|
| [seo-off-page-link-building](skills/seo/off-page/link-building/) | Link building, outreach, link acquisition |
| [seo-off-page-backlink-analysis](skills/seo/off-page/backlink-analysis/) | Backlink audit, toxic links, competitive analysis |

#### Content

| Skill | Description |
|-------|-------------|
| [seo-content-keyword-research](skills/seo/content/keyword-research/) | Keyword research, search intent, difficulty |
| [seo-content-content-strategy](skills/seo/content/content-strategy/) | Content clusters, pillar pages, editorial calendar |

### Pages

Pages are classified by **purpose** (brand, SEO, marketing, legal, utility). See [docs/page-types-taxonomy.md](docs/page-types-taxonomy.md) for the full taxonomy and best practices.

| Purpose | Skill | Description |
|---------|-------|-------------|
| **Brand** | [pages-home](skills/pages/brand/home/) | Homepage content, structure, conversion |
| Brand | [pages-about](skills/pages/brand/about/) | About page, company story, trust |
| Brand | [pages-contact](skills/pages/brand/contact/) | Contact page, form optimization |
| **SEO** | [pages-features](skills/pages/content/features/) | Features page, benefit-first copy |
| SEO | [pages-glossary](skills/pages/content/glossary/) | Glossary, definitions, internal linking |
| SEO | [pages-blog](skills/pages/content/blog/) | Blog page, SEO, content strategy |
| SEO | [pages-resources](skills/pages/content/resources/) | Resources page, content hub |
| SEO | [pages-faq](skills/pages/content/faq/) | FAQ page, SEO, conversion |
| SEO | [pages-api](skills/pages/content/api/) | API introduction page (typically /api), links to docs |
| **Marketing** | [pages-pricing](skills/pages/marketing/pricing/) | Pricing page, plans, objection handling |
| Marketing | [pages-products](skills/pages/marketing/products/) | Product listing (e-commerce) |
| Marketing | [pages-services](skills/pages/marketing/services/) | Services page (consulting, agencies) |
| Marketing | [pages-category-pages](skills/pages/marketing/category-pages/) | E-commerce category pages, faceted navigation |
| Marketing | [pages-customer-stories](skills/pages/marketing/customer-stories/) | Case studies, success stories |
| Marketing | [pages-affiliate-program](skills/pages/marketing/affiliate-program/) | Affiliate program page, commission structure |
| Marketing | [pages-media-kit](skills/pages/marketing/media-kit/) | Media kit, press resources |
| **Legal** | [pages-privacy](skills/pages/legal/privacy/) | Privacy Policy page |
| Legal | [pages-terms](skills/pages/legal/terms/) | Terms of Service page |
| Legal | [pages-cookie-policy](skills/pages/legal/cookie-policy/) | Cookie policy, GDPR |
| Legal | [pages-legal](skills/pages/legal/legal/) | Legal pages (Privacy, Terms, Cookie Policy) |
| Legal | [pages-refund](skills/pages/legal/refund/) | Refund/return policy (e-commerce) |
| Legal | [pages-shipping](skills/pages/legal/shipping/) | Shipping/delivery info (e-commerce) |
| **Utility** | [pages-404](skills/pages/utility/404/) | 404 error page, UX, conversion recovery |
| Utility | [pages-careers](skills/pages/utility/careers/) | Careers page, jobs, employer branding |

### Components

| Skill | Description |
|-------|-------------|
| [components-navigation-menu](skills/components/navigation-menu/) | Navigation menu design, SEO, UX, accessibility |
| [components-footer](skills/components/footer/) | Footer design, links, SEO, newsletter placement |
| [components-toc](skills/components/toc/) | Table of contents for long-form content, jump links |
| [components-hero](skills/components/hero/) | Hero section design, conversion, above-the-fold |
| [components-logo](skills/components/logo/) | Logo placement, linking, brand recall |
| [components-trust-badges](skills/components/trust-badges/) | Trust badges, "Trusted by" logos, security seals |
| [components-testimonials](skills/components/testimonials/) | Testimonials, reviews, customer quotes |
| [components-cta](skills/components/cta/) | Call-to-action button design, conversion |
| [components-newsletter-signup](skills/components/newsletter-signup/) | Newsletter signup form, email capture |

### Channels

| Skill | Description |
|-------|-------------|
| [channels-affiliate](skills/channels/affiliate/) | Affiliate marketing strategy, CPS model, recruitment |
| [channels-influencer](skills/channels/influencer/) | Influencer marketing strategy, KOL, creator partnership |
| [channels-referral](skills/channels/referral/) | Referral program strategy, user-driven growth |
| [channels-creator-program](skills/channels/creator-program/) | Creator program strategy, content co-creation |

### Platforms

| Skill | Description |
|-------|-------------|
| [platforms-x](skills/platforms/x/) | X (Twitter) post copy, threads, image specs |
| [platforms-reddit](skills/platforms/reddit/) | Reddit post copy, subreddit rules, engagement |
| [platforms-linkedin](skills/platforms/linkedin/) | LinkedIn post copy, professional content |
| [platforms-tiktok](skills/platforms/tiktok/) | TikTok caption, video specs, script |

### Strategies

| Skill | Description |
|-------|-------------|
| [strategies-geo](skills/strategies/geo/) | GEO/AEO for AI search visibility (ChatGPT, Claude, Perplexity) |
| [strategies-localization](skills/strategies/localization/) | Localization strategy, i18n, multilingual, global expansion |

### Analytics

| Skill | Description |
|-------|-------------|
| [analytics-traffic](skills/analytics/traffic/) | Traffic sources, dark traffic, UTM attribution |
| [analytics-tracking](skills/analytics/tracking/) | GA4, event tracking, conversions |
| [analytics-ai-traffic](skills/analytics/ai-traffic/) | Track AI search traffic in GA4 and GSC |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or improve skills. For the full spec, see [SKILLS_GUIDE.md](SKILLS_GUIDE.md).

## References

| Resource | Purpose |
|----------|---------|
| [Alignify](https://alignify.co/) | SEO guides, growth strategies, AI tools — for human reading |
| [skills.sh](https://skills.sh) | Skill directory and discovery |
| [product-marketing-context template](templates/product-marketing-context.md) | Context file template (copy to `.cursor/`) |
| [page-types-taxonomy](docs/page-types-taxonomy.md) | Page classification by purpose (brand, SEO, marketing, legal, utility) |

## License

[MIT](LICENSE)
