# Marketing & SEO Skills for AI Agents

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

65 specialized skills for Claude Code, Cursor, and other AI agents — SEO, 24 page types, channels, platforms, strategies, components, and analytics.

By [kostja94](https://github.com/kostja94)

> **README** = overview & quick start. For rules, specs, and skill authoring → [SKILLS_GUIDE](SKILLS_GUIDE.md).

## Table of Contents

- [What are Skills?](#what-are-skills)
- [Installation](#installation) — Full or selective; delete what you don't need
- [Linking to Your Project](#linking-to-your-project) — Connect skills with your project
- [Usage](#usage)
- [Project Context](#project-context) — Add context for tailored results
- [How Skills Work Together](#how-skills-work-together)
- [Skill Uniqueness and Cross-References](#skill-uniqueness-and-cross-references)
- [Output Structure: Context First, Then Action](#output-structure-context-first-then-action)
- [Tips & Rules](#tips--rules)
- [Available Skills](#available-skills)
- [Contributing](#contributing)
- [References](#references)
- [License](#license)

## What are Skills?

Skills are markdown files that give AI agents focused knowledge and workflows for specific tasks. Add them to your project, and your agent can handle SEO and page optimization with the right frameworks and best practices.

**Skills = for agents.** For human-readable SEO guides and growth strategies, see [Alignify](https://alignify.co/).

**For best results**: Add a [Project Context](#project-context) file — without it, outputs stay generic.

## Installation

**Full or selective.** Install all 65 skills, or only the ones you need. You can also delete unwanted skills after install — skills are independent.

### CLI (Recommended)

```bash
# Install all skills
npx skills add kostja94/marketing-skills

# Install specific skills only
npx skills add kostja94/marketing-skills --skill seo-technical-robots seo-on-page-metadata pages-pricing

# List available skills
npx skills add kostja94/marketing-skills --list
```

### Clone and Copy

```bash
git clone https://github.com/kostja94/marketing-skills.git
cp -r marketing-skills/skills/* .cursor/skills/
cp -r marketing-skills/templates .cursor/
cp -r marketing-skills/tools .cursor/
# For Claude Code: use .claude/ instead of .cursor/
# To keep only some skills: copy selectively, or delete unwanted folders from .cursor/skills/
```

### Git Submodule

```bash
git submodule add https://github.com/kostja94/marketing-skills.git .cursor/marketing-skills
# Reference skills from .cursor/marketing-skills/skills/
# To use fewer skills: symlink or copy only the skill folders you need into .cursor/skills/
```

## Linking to Your Project

Marketing skills are generic. To get tailored output, connect them with your project:

| Method | Purpose |
|--------|---------|
| **[Product Context](#project-context)** | Product, audience, brand — skills read this automatically |
| **Project Rules** (`.cursor/rules/`) | Code style, architecture, conventions — applied alongside skills |
| **AGENTS.md** | Simple project instructions — alternative to rules |
| **@file references** | In chat: `@package.json` `@README.md` — agent includes them when relevant |

**Recommended**: Start with [Product Context](#project-context). Add rules or AGENTS.md for project-specific patterns. See [SKILLS_GUIDE §10 Customization](SKILLS_GUIDE.md#10-customization) for details.

## Usage

Ask your agent — it picks the right skill from your prompt. Examples:

| You say | Skill |
|---------|-------|
| "Configure robots.txt" / "Audit sitemap" / "Fix canonical URLs" | seo-technical-* |
| "Optimize meta tags" / "Add schema markup" / "Fix heading structure" | seo-on-page-* |
| "Keyword research" / "Content strategy" / "Link building" | seo-content-* / seo-off-page-* |
| "Create pricing page" / "Optimize homepage" / "Create FAQ" | pages-* |
| "Submit to Taaft, Product Hunt" / "Directory submission" | channels-directories |
| "Add to Grokipedia" / "GEO for AI search" | platforms-grokipedia / strategies-geo |
| "GA4 tracking" / "Search Console" / "AI traffic" | analytics-* |

See [Tips & Rules](#tips--rules) for best practices.

## Project Context

**Without context, outputs stay generic.** Add `.cursor/product-marketing-context.md` (or `.claude/`) so the agent delivers tailored copy and strategy. Skills read it automatically.

**Get template**: `cp marketing-skills/templates/product-marketing-context.md .cursor/` or [download](https://raw.githubusercontent.com/kostja94/marketing-skills/main/templates/product-marketing-context.md).

**Start with**: Product Overview, Positioning, Target Audience, Brand & Voice. Add Keywords, Competitors, Website as you have them. Update regularly — stale context degrades quality.

## How Skills Work Together

Recommended workflow: **Technical** → **On-Page** → **Content** → **Off-Page**. Page skills apply SEO when optimizing specific page types. See each skill's **Related Skills** for the full dependency map.

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
│  Channels: affiliate · influencer · referral · creator-program · directories             │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  Platforms: x · reddit · linkedin · tiktok · grokipedia  |  Strategies: geo · localization          │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  Components: nav · footer · hero · toc · logo · trust-badges · testimonials · cta ·     │
│  newsletter-signup  |  Analytics: traffic · tracking · ai-traffic · google-search-console │
└─────────────────────────────────────────────────────────────────────────────────────────┘

Cross-references: metadata ↔ schema ↔ heading  |  sitemap ↔ indexnow
                internal-links ↔ crawlability  |  link-building ↔ backlink-analysis
```

### Skill Uniqueness and Cross-References

Each skill keeps only topic-relevant content. Overlapping topics use **Related Skills** references instead of duplication. See [SKILLS_GUIDE §4.2](SKILLS_GUIDE.md#42-skill-uniqueness-and-cross-references) for rules.

### Output Structure: Context First, Then Action

Platform skills (directories, Grokipedia) use full structure (Introduction → Importance → Methods → Rules → Avoid → Action); others use brief context + main output. Say "skip intro" or "just do it" for repeat tasks. See [SKILLS_GUIDE §4.4](SKILLS_GUIDE.md#44-output-structure-context-first-then-action) for spec.

## Tips & Rules

| Tip | Description |
|-----|-------------|
| **Project Context** | Add `.cursor/product-marketing-context.md` for tailored output |
| **Skip intro** | "skip intro" or "just do it" → go straight to Action |
| **Workflow order** | Technical → On-Page → Content → Off-Page |
| **Related Skills** | Use each skill's Related Skills for dependencies |
| **Rules & specs** | See [SKILLS_GUIDE](SKILLS_GUIDE.md) for output structure, skill authoring, quality checklist |

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
| [channels-directories](skills/channels/directories/) | Directory submission (Taaft, Product Hunt, Shopify App Store) |

### Platforms

| Skill | Description |
|-------|-------------|
| [platforms-x](skills/platforms/x/) | X (Twitter) post copy, threads, image specs |
| [platforms-reddit](skills/platforms/reddit/) | Reddit post copy, subreddit rules, engagement |
| [platforms-linkedin](skills/platforms/linkedin/) | LinkedIn post copy, professional content |
| [platforms-tiktok](skills/platforms/tiktok/) | TikTok caption, video specs, script |
| [platforms-grokipedia](skills/platforms/grokipedia/) | Grokipedia recommendations, parasite SEO, GEO |

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
| [analytics-google-search-console](skills/analytics/google-search-console/) | GSC analysis, indexing, Core Web Vitals, performance |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or improve skills. Rules and specs → [SKILLS_GUIDE](SKILLS_GUIDE.md).

## References

| Resource | Purpose |
|----------|---------|
| [Alignify](https://alignify.co/) | SEO guides, growth strategies, AI tools — for human reading |
| [skills.sh](https://skills.sh) | Skill directory and discovery |
| [product-marketing-context template](templates/product-marketing-context.md) | Context file template (copy to `.cursor/`) |
| [page-types-taxonomy](docs/page-types-taxonomy.md) | Page classification by purpose (brand, SEO, marketing, legal, utility) |
| [SKILLS_GUIDE](SKILLS_GUIDE.md) | Rules, specs, skill authoring, quality checklist |

## License

[MIT](LICENSE)
