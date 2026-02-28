# Marketing & SEO Skills for AI Agents

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

83 specialized skills for Cursor, Claude Code, and other AI agents — SEO, 25 page types, channels, platforms, strategies, components, and analytics.

**By [kostja](https://github.com/kostja94)** — I add new skills daily; please download the latest version. Questions or feedback? zyjstc@gmail.com

**Works beyond Cursor/Claude**: Lovable, ChatGPT, Gemini, and any AI that reads markdown — see [Using Beyond Cursor](docs/using-beyond-cursor.md).

> **README** = overview & quick start. For rules, specs, and skill authoring → [SKILLS_GUIDE](SKILLS_GUIDE.md). For updates → [CHANGELOG](CHANGELOG.md).

## Table of Contents

- [What are Skills?](#what-are-skills)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Using Beyond Cursor & Claude](#using-beyond-cursor--claude)
- [Linking to Your Project](#linking-to-your-project)
- [Project Context](#project-context)
- [Usage](#usage)
- [How Skills Work Together](#how-skills-work-together)
- [Tips & Rules](#tips--rules)
- [Available Skills](#available-skills)
- [Contributing](#contributing)
- [References](#references)
- [License](#license)

## What are Skills?

Skills are **markdown files** that give AI agents focused knowledge and workflows for specific tasks. Add them to your project, and your agent can handle SEO and page optimization with the right frameworks and best practices.

**Skills = for agents.** For human-readable SEO guides and growth strategies, see [Alignify](https://alignify.co/).

**For best results**: Add a [Project Context](#project-context) file — without it, outputs stay generic.

## Project Structure

```
marketing-skills/
├── skills/           # 83 skills — seo/, pages/, components/, channels/, platforms/, strategies/, analytics/
├── docs/             # using-beyond-cursor.md, skills-list.md, page-types-taxonomy.md
├── templates/        # product-marketing-context.md, skills-task-progress.md, report templates
├── tools/            # Report generation — generate-report.py, *-guide.md
├── README.md
├── SKILLS_GUIDE.md   # Rules, specs, skill authoring
├── CHANGELOG.md      # What changed, when
└── CONTRIBUTING.md
```

## Installation

**Full or selective.** Install all 83 skills, or only the ones you need. Skills are independent — delete unwanted ones after install.

### CLI (Recommended)

```bash
# Install all
npx skills add kostja94/marketing-skills

# Install specific skills only
npx skills add kostja94/marketing-skills --skill robots-txt title-tag meta-description pricing-page-generator

# List available
npx skills add kostja94/marketing-skills --list
```

### Clone and Copy

```bash
git clone https://github.com/kostja94/marketing-skills.git
cp -r marketing-skills/skills/* .cursor/skills/
cp -r marketing-skills/templates .cursor/
cp -r marketing-skills/tools .cursor/
# For Claude Code: use .claude/ instead of .cursor/
```

### Git Submodule

```bash
git submodule add https://github.com/kostja94/marketing-skills.git .cursor/marketing-skills
# Symlink or copy only the skill folders you need into .cursor/skills/
```

## Using Beyond Cursor & Claude

**Skills are markdown.** They work anywhere an AI can read text — no native skill support required.

| Platform | How |
|----------|-----|
| **Lovable, Bolt, v0** | Copy skills to `.lovable/skills/` (or equivalent); adapt context path to `.lovable/product-marketing-context.md` |
| **ChatGPT, Gemini, Claude Web** | Paste a skill's markdown as context, then ask your question |
| **Any AI with file access** | Place skills in project root; reference in prompts |

**Full tutorial**: [Using Beyond Cursor](docs/using-beyond-cursor.md) — Lovable setup, chat-model usage, path adaptation.

## Linking to Your Project

Marketing skills are generic. Connect them with your project for tailored output:

| Method | Purpose |
|--------|---------|
| **[Product Context](#project-context)** | Product, audience, brand — skills read automatically |
| **[Skills Task Progress](#project-context)** | Task status (pending/done), priority — agent suggests next steps |
| **Project Rules** (`.cursor/rules/`) | Code style, architecture, conventions |
| **AGENTS.md** | Simple project instructions |
| **@file references** | In chat: `@package.json` `@README.md` — agent includes when relevant |

**Recommended**: Start with [Product Context](#project-context). See [SKILLS_GUIDE §10 Customization](SKILLS_GUIDE.md#10-customization) for details.

## Project Context

**Without context, outputs stay generic.** Add `product-marketing-context.md` so the agent delivers tailored copy and strategy. Place in `.cursor/`, `.claude/`, `.lovable/`, or your platform's config directory.

**Templates**:
- **Product context**: [product-marketing-context.md](templates/product-marketing-context.md) · [download](https://raw.githubusercontent.com/kostja94/marketing-skills/main/templates/product-marketing-context.md)
- **Task progress**: [skills-task-progress.md](templates/skills-task-progress.md) · [download](https://raw.githubusercontent.com/kostja94/marketing-skills/main/templates/skills-task-progress.md) — track status, priority; agent avoids redundant work

**Start with**: Product Overview, Positioning, Target Audience, Brand & Voice. Add Keywords, Competitors, Website as you have them. Update regularly — stale context degrades quality.

## Usage

Ask your agent — it picks the right skill from your prompt. Examples:

| You say | Skill |
|---------|-------|
| "Configure robots.txt" / "Audit sitemap" / "Fix canonical URLs" | robots-txt, xml-sitemap, canonical-tag |
| "Optimize title tag" / "Meta description" / "Open Graph" / "Twitter Cards" / "Add schema markup" / "Fix heading structure" | title-tag, meta-description, open-graph, twitter-cards, schema-markup, heading-structure |
| "Keyword research" / "Content strategy" / "Link building" | keyword-research, content-strategy, link-building |
| "Create pricing page" / "Optimize homepage" / "Create FAQ" | pricing-page-generator, homepage-generator, faq-page-generator |
| "Submit to Taaft, Product Hunt" / "Directory submission" | directory-submission |
| "Add to Grokipedia" / "GEO for AI search" | grokipedia-recommendations, generative-engine-optimization |
| "GA4 tracking" / "Search Console" / "AI traffic" | analytics-tracking, google-search-console, ai-traffic-tracking |

## How Skills Work Together

**Workflow order**: Technical → On-Page → Content → Off-Page. Page skills apply SEO when optimizing specific page types. See each skill's **Related Skills** for the dependency map.

```
                    ┌─────────────────────────────────────────────────────────┐
                    │              Technical SEO (Foundation)                 │
                    │  robots · sitemap · canonical · indexing · crawlability │
                    │  indexnow                                              │
                    └──────────────────────────┬──────────────────────────────┘
                                               │
         ┌─────────────────────────────────────┼─────────────────────────────────────┐
         ▼                                     ▼                                     ▼
┌─────────────────────┐           ┌─────────────────────┐           ┌─────────────────────┐
│      On-Page        │           │       Content       │           │      Off-Page       │
│  metadata · schema  │◄─────────►│ keyword-research   │           │  link-building      │
│  internal-links     │           │ content-strategy    │           │  backlink-analysis  │
│  url-structure      │           └─────────────────────┘           └─────────────────────┘
│  heading           │
└─────────┬───────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  Pages: home · about · contact | features · glossary · blog · resources · faq · api |   │
│  pricing · products · services · category-pages · customer-stories · affiliate ·     │
│  media-kit | privacy · terms · cookie-policy · legal · refund · shipping | 404 · careers│
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  Channels: affiliate · email-marketing · egc · influencer · referral · creator-program · community-forum · directories │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  Platforms: x · reddit · linkedin · tiktok · grokipedia  |  Strategies: geo · integrated-marketing · localization│
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  Components: nav · footer · hero · toc · logo · trust-badges · testimonials · cta · url-slug   │
│  newsletter-signup  |  Analytics: traffic · tracking · seo-monitoring · ai-traffic · google-search-console│
└─────────────────────────────────────────────────────────────────────────────────────────┘

Cross-references: metadata ↔ schema ↔ heading  |  sitemap ↔ indexnow
                internal-links ↔ crawlability  |  link-building ↔ backlink-analysis
```

**Skill uniqueness**: Each skill keeps only topic-relevant content. Overlapping topics use **Related Skills** references. See [SKILLS_GUIDE §4.2](SKILLS_GUIDE.md#42-skill-uniqueness-and-cross-references).

**Output structure**: Platform skills (directories, Grokipedia) use full structure (Introduction → Importance → Methods → Rules → Avoid → Action); others use brief context + main output. Say "skip intro" or "just do it" for repeat tasks. See [SKILLS_GUIDE §4.4](SKILLS_GUIDE.md#44-output-structure-context-first-then-action).

## Tips & Rules

| Tip | Description |
|-----|-------------|
| **Project Context** | Add `product-marketing-context.md` to `.cursor/`, `.claude/`, or `.lovable/` for tailored output |
| **Skip intro** | "skip intro" or "just do it" → go straight to Action |
| **Workflow order** | Technical → On-Page → Content → Off-Page |
| **Related Skills** | Use each skill's Related Skills for dependencies |
| **Rules & specs** | See [SKILLS_GUIDE](SKILLS_GUIDE.md) for output structure, skill authoring, quality checklist |

## Available Skills

83 skills in 7 categories. [Full list](docs/skills-list.md) · `npx skills add kostja94/marketing-skills --list` (83 skills)

| Category | Skills |
|----------|--------|
| **SEO** (19) | [Technical](skills/seo/technical/): robots, sitemap, canonical, indexing, indexnow, crawlability · [On-Page](skills/seo/on-page/): title, description, metadata, open-graph, twitter-cards, schema, internal-links, url-structure, heading · [Off-Page](skills/seo/off-page/): link-building, backlink-analysis · [Content](skills/seo/content/): keyword-research, content-strategy |
| **Pages** (24) | [page-types-taxonomy](docs/page-types-taxonomy.md) — brand, content, marketing, legal, utility |
| **Components** (11) | nav, breadcrumb, footer, hero, toc, logo, trust-badges, testimonials, cta, newsletter-signup, url-slug |
| **Channels** (8) | affiliate, email-marketing, egc, influencer, referral, creator-program, community-forum, directories |
| **Platforms** (5) | x, reddit, linkedin, tiktok, grokipedia |
| **Strategies** (3) | geo, integrated-marketing, localization |
| **Analytics** (5) | traffic, tracking, seo-monitoring, ai-traffic, google-search-console |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Rules and specs → [SKILLS_GUIDE](SKILLS_GUIDE.md).

## References

**External**

| Resource | Purpose |
|----------|---------|
| [Alignify](https://alignify.co/) | SEO guides, growth strategies — for human reading |
| [skills.sh](https://skills.sh) | Skill directory and discovery |

**Internal**

| Resource | Purpose |
|----------|---------|
| [product-marketing-context](templates/product-marketing-context.md) | Context template |
| [skills-task-progress](templates/skills-task-progress.md) | Task tracker — status, priority |
| [using-beyond-cursor](docs/using-beyond-cursor.md) | Lovable, ChatGPT, Gemini — no native support needed |
| [page-types-taxonomy](docs/page-types-taxonomy.md) | Page classification |
| [skills-list](docs/skills-list.md) | Full list of all 83 skills |
| [SKILLS_GUIDE](SKILLS_GUIDE.md) | Rules, specs, skill authoring |
| [CHANGELOG](CHANGELOG.md) | What changed, when |
| [tools/](tools/README.md) | Report generation (keyword, competitor) |

## License

[MIT](LICENSE)
