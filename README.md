# Marketing & SEO Skills for AI Agents

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/kostja94/marketing-skills)](https://github.com/kostja94/marketing-skills/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/kostja94/marketing-skills)](https://github.com/kostja94/marketing-skills/commits/main)

Markdown skill library for AI agents - SEO, content, pages, paid ads, channels, strategies. Add project context + skills; your agent delivers tailored, production-ready output. Works with Cursor, Claude Code, OpenClaw, Lovable, and any AI that reads markdown.

**By [kostja](https://github.com/kostja94)** | [skill-authoring](docs/skill-authoring.md) | [CHANGELOG](docs/CHANGELOG.md) | zyjstc@gmail.com

---

## Quick Start

```bash
# Install specific skills (recommended - 2-3 per task; SkillsBench ref, one paper)
npx skills add kostja94/marketing-skills --skill robots-txt title-tag meta-description

# Install all skills
npx skills add kostja94/marketing-skills

# List available
npx skills add kostja94/marketing-skills --list
```

**Context** (required for tailored output): Copy [project-context.md](templates/project-context.md) to `.cursor/` or `.claude/` and fill in. [Templates](templates/README.md) | [Project Task Tracker](templates/project-task-tracker.md)

**Note**: CLI installs skills only (flat layout), not `templates/` or `docs/`. Need templates? Use [Clone + copy](#installation) below.

---

## What are Skills?

Skills are **markdown files** that give AI agents focused knowledge and workflows. Add them to your project; the agent picks the right skill from your prompt and applies SEO, content, and marketing best practices.

**SkillsBench** ([2025](https://arxiv.org/abs/2602.12670), *for reference only - one paper's findings*): Human-curated skills yield +16.2pp task success; vertical domains (e.g. marketing, SEO) benefit most.

**Skills = for agents.** Human guides -> [Alignify](https://alignify.co/).

---

## Use Cases

| Scenario | Link |
|----------|------|
| Personal site / portfolio | [usage.md S7.1](docs/usage.md#71-personal-developer--seo-friendly-personal-site) |
| Product website - SEO growth | [usage.md S7.2](docs/usage.md#72-product-website--seo-growth-with-frontend--ops-split) |
| Learn SEO standalone | [usage.md S7.3](docs/usage.md#73-vibe-coding-beginner--learn-seo-standalone) |
| Vibe coding product - built-in skills | [usage.md S7.4](docs/usage.md#74-vibe-coding-product--built-in-skills-as-templates) |
| Build your own skills | [usage.md S7.5](docs/usage.md#75-want-to-build-your-own-skills--fork--adapt) |

**Partnership**: Building a vibe coding product or AI marketing agent? [Contact](mailto:zyjstc@gmail.com) to integrate.

[![Star History Chart](https://api.star-history.com/image?repos=kostja94/marketing-skills&type=Date)](https://star-history.com/#kostja94/marketing-skills)

**Found this useful?** Star or share with colleagues helps others discover it - thank you.

---

## Installation

| Method | When |
|--------|------|
| **CLI** | Full or selective; skills only, flat layout |
| **Clone + copy** | Need templates or full structure: `cp -r marketing-skills/skills/* .cursor/skills/` and `cp -r marketing-skills/templates .cursor/` |
| **Git submodule** | `git submodule add https://github.com/kostja94/marketing-skills.git .cursor/marketing-skills` |

**Skill directories** ([Agent Skills spec](https://agentskills.io/specification)): `.agents/skills/`, `.cursor/skills/`, `.claude/skills/`, `~/.cursor/skills/`. **Platforms**: Cursor, Claude Code, OpenClaw, Lovable, v0, Bolt - native or copy to project; ChatGPT/Claude Web - paste skill markdown. [Full guide](docs/usage.md)

---

## Usage

Ask your agent - it picks the right skill. Examples:

| You say | Skill |
|---------|-------|
| "SEO strategy" / "SEO plan" / "Where to start SEO" | seo-strategy |
| "Configure robots.txt" / "Audit sitemap" / "Fix canonical" | robots-txt, xml-sitemap, canonical-tag |
| "Optimize title" / "Meta description" / "Schema markup" | title-tag, meta-description, schema-markup |
| "Keyword research" / "Content strategy" / "Link building" | keyword-research, content-strategy, link-building |
| "Create pricing page" / "Homepage" / "Landing page" / "FAQ" | pricing-page-generator, homepage-generator, landing-page-generator, faq-page-generator |
| "HowTo section" / "Step-by-step block" / "HowTo schema" | howto-section-generator, schema-markup |
| "Cold start" / "Product Hunt" / "Directory submission" | cold-start-strategy, directory-submission |
| "Indie hacker" / "PMF" / "Parasite SEO" / "GitHub SEO" | indie-hacker-strategy, pmf-strategy, parasite-seo, github |
| "GA4 tracking" / "Search Console" / "AI traffic" | analytics-tracking, google-search-console, ai-traffic-tracking |

[Full prompt -> skill mapping](docs/usage.md)

---

## Project Context

**Without context, outputs stay generic.** Add `project-context.md` for product, audience, brand - skills read it automatically.

| Context | Purpose |
|---------|---------|
| **project-context.md** | Product, audience, brand, keywords - skills read automatically |
| **project-task-tracker.md** | Task status, priority - agent suggests next steps |
| **Project rules** (`.cursor/rules/`) | Code style, conventions |
| **AGENTS.md** | Project instructions |

**Start with**: Overview, 1-4, 8. Add 5-7 as you have them. Update regularly - stale context degrades quality. [Templates](templates/README.md) | [skill-authoring S8](docs/skill-authoring.md#8-customization)

---

## Skills Overview

**160+ skills** in 9 categories. [Full list](docs/skills-reference.md) | `npx skills add kostja94/marketing-skills --list`

| Category | Scope |
|----------|-------|
| **SEO** | Technical (robots, sitemap, canonical, crawlability), On-Page (title, meta, schema, heading), Content (keyword, content, competitor), Off-Page, Local, Tactics |
| **Content** | Copywriting, video, visual, translation |
| **Paid Ads** | Strategy + 12 platforms (Google, Meta, LinkedIn, TikTok, etc.) |
| **Pages** | 40+ types - brand, content, marketing, legal, utility; Features vs Use cases vs Solutions |
| **Components** | Nav, breadcrumb, footer, hero, CTA, logo, testimonials, etc. |
| **Channels** | Affiliate, email, influencer, referral, directories, PR |
| **Platforms** | X, Reddit, LinkedIn, TikTok, YouTube, Medium, GitHub, Grokipedia |
| **Strategies** | launch | brand | commercial | structure (SEO, cold-start, GEO, branding, GTM, PMF, pricing, domain, etc.) |
| **Analytics** | Traffic, tracking, Search Console, AI traffic |

**Workflow**: Technical SEO -> On-Page -> Content -> Off-Page. **seo-strategy** orchestrates. Each skill has **Related Skills**; say "skip intro" or "just do it" for repeat tasks. [Dependency maps](docs/skills-reference.md#3-how-skills-work-together)

```
                    +-------------------------------------------------------------+
                    |              Technical SEO (Foundation)                     |
                    |  robots | sitemap | canonical | indexing | indexnow |       |
                    |  crawlability | core-web-vitals | mobile-friendly | rendering |
                    +---------------------------------+-----------------------------+
                                                      |
         +---------------------------------------------+---------------------------------------------+
         v                                             v                                             v
+---------------------+                   +-------------------------+                   +---------------------+
|      On-Page        |                   |       Content            |                   |     Off-Page        |
| title | meta-desc | |<----------------->| keyword-research |      |                   | link-building |     |
| schema | heading | |                   | content-strategy |       |                   | backlink-analysis   |
| internal-links |    |                   | eeat-signals |           |                   +---------------------+
| image | video | url |                   | competitor-research |    |
+------------------+--+                   | parasite | programmatic  |
             |                            +----------------+---------+
             +-----------------------------------+---------+
                                                v
                    +-------------------------------------------------------------+
                    |  Pages | Brand | Content | Marketing | Legal | Utility (40+) |
                    +---------------------------------+-----------------------------+
                                                      |
         +---------------------------------------------+---------------------------------------------+
         v                                             v                                             v
+---------------------+                   +-------------------------+                   +---------------------+
| Channels            |                   | Platforms | Strategies   |                   | Components |        |
| affiliate | email | |                   | x | reddit | linkedin |   |                   | Analytics           |
| directories | pr |  |                   | cold-start | GEO |       |                   | nav | hero | cta |  |
| influencer | referral|                  | paid-ads | branding     |                   | tracking | GSC      |
+---------------------+                   +-------------------------+                   +---------------------+
```

---

## Tips

| Tip | Action |
|-----|--------|
| **Project Context** | Add `project-context.md` for tailored output |
| **Skip intro** | "skip intro" or "just do it" -> go straight to Action |
| **Related Skills** | Each skill has Related Skills for dependencies |

---

## Security

All skills are pure Markdown - no executable code. Scope limited to SEO, content, marketing. No data exfiltration. [Full audit](docs/SECURITY.md)

---

## Docs & References

| Doc | Purpose |
|-----|---------|
| [usage](docs/usage.md) | Platforms, install, use cases, roadmap |
| [skills-reference](docs/skills-reference.md) | Full skill list, page taxonomy, dependency trees |
| [skill-authoring](docs/skill-authoring.md) | Rules, specs, authoring |
| [templates](templates/README.md) | project-context | project-task-tracker |
| [CONTRIBUTING](CONTRIBUTING.md) | How to contribute |

**Ecosystem**: [Agent Skills Specification](https://agentskills.io/specification) | [skills.sh](https://skills.sh) | [Vercel skills CLI](https://github.com/vercel-labs/skills)

---

## License

[MIT](LICENSE)
