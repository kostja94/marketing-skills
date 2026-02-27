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

65 skills in 7 categories. [Full list with descriptions](docs/skills-list.md) · Run `npx skills add kostja94/marketing-skills --list` to discover all.

| Category | Skills |
|----------|--------|
| **SEO** (15) | [Technical](skills/seo/technical/): robots, sitemap, canonical, indexing, indexnow, crawlability · [On-Page](skills/seo/on-page/): metadata, schema, internal-links, url-structure, heading · [Off-Page](skills/seo/off-page/): link-building, backlink-analysis · [Content](skills/seo/content/): keyword-research, content-strategy |
| **Pages** (24) | [page-types-taxonomy](docs/page-types-taxonomy.md) — brand (home, about, contact), content (features, blog, faq, api…), marketing (pricing, products, services…), legal (privacy, terms…), utility (404, careers) |
| **Components** (9) | [nav](skills/components/navigation-menu/), [footer](skills/components/footer/), [hero](skills/components/hero/), [toc](skills/components/toc/), [logo](skills/components/logo/), [trust-badges](skills/components/trust-badges/), [testimonials](skills/components/testimonials/), [cta](skills/components/cta/), [newsletter-signup](skills/components/newsletter-signup/) |
| **Channels** (5) | [affiliate](skills/channels/affiliate/), [influencer](skills/channels/influencer/), [referral](skills/channels/referral/), [creator-program](skills/channels/creator-program/), [directories](skills/channels/directories/) |
| **Platforms** (5) | [x](skills/platforms/x/), [reddit](skills/platforms/reddit/), [linkedin](skills/platforms/linkedin/), [tiktok](skills/platforms/tiktok/), [grokipedia](skills/platforms/grokipedia/) |
| **Strategies** (2) | [geo](skills/strategies/geo/), [localization](skills/strategies/localization/) |
| **Analytics** (4) | [traffic](skills/analytics/traffic/), [tracking](skills/analytics/tracking/), [ai-traffic](skills/analytics/ai-traffic/), [google-search-console](skills/analytics/google-search-console/) |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or improve skills. Rules and specs → [SKILLS_GUIDE](SKILLS_GUIDE.md).

## References

| Resource | Purpose |
|----------|---------|
| [Alignify](https://alignify.co/) | SEO guides, growth strategies, AI tools — for human reading |
| [skills.sh](https://skills.sh) | Skill directory and discovery |
| [product-marketing-context template](templates/product-marketing-context.md) | Context file template (copy to `.cursor/`) |
| [page-types-taxonomy](docs/page-types-taxonomy.md) | Page classification by purpose (brand, SEO, marketing, legal, utility) |
| [skills-list](docs/skills-list.md) | Full list of all 65 skills with descriptions |
| [SKILLS_GUIDE](SKILLS_GUIDE.md) | Rules, specs, skill authoring, quality checklist |

## License

[MIT](LICENSE)
