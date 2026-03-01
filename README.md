# Marketing & SEO Skills for AI Agents

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

109 specialized skills for Cursor, Claude Code, and other AI agents — SEO, 39 page types, channels, platforms, strategies, components, and analytics. Works with Lovable, ChatGPT, Gemini, and any AI that reads markdown ([Where to Use](docs/where-to-use-skills.md)).

**By [kostja](https://github.com/kostja94)** · I add new skills daily · [SKILLS_GUIDE](docs/SKILLS_GUIDE.md) · [CHANGELOG](docs/CHANGELOG.md) · zyjstc@gmail.com

## Table of Contents

- [What are Skills?](#what-are-skills)
- [Use Cases](#use-cases)
- [Installation](#installation)
- [Where to Use Skills](#where-to-use-skills)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Project Context & Linking](#project-context--linking)
- [Available Skills](#available-skills)
- [How Skills Work Together](#how-skills-work-together)
- [Tips & Rules](#tips--rules)
- [Contributing](#contributing)
- [References](#references)
- [License](#license)

## What are Skills?

Skills are **markdown files** that give AI agents focused knowledge and workflows for specific tasks. Add them to your project, and your agent can handle SEO and page optimization with the right frameworks and best practices.

**Skills = for agents.** For human-readable SEO guides and growth strategies, see [Alignify](https://alignify.co/). For best results, add [Project Context](#project-context--linking).

## Use Cases

| Scenario | How |
|----------|-----|
| **Personal developer** — SEO-friendly personal site | Quick install, build portfolio/blog/landing with SEO built in. [Guide →](docs/use-cases-and-roadmap.md#11-personal-developer--seo-friendly-personal-site) |
| **Product website** — SEO growth | Frontend: optimization tech. Ops: build marketing pages via rewrite, no engineering dependency. [Playbook →](docs/use-cases-and-roadmap.md#12-product-website--seo-growth-with-frontend--ops-split) |
| **Vibe coding beginner** — Learn SEO | Install skills standalone; use ChatGPT/Claude/Gemini to paste and learn. No project required. [Learning path →](docs/use-cases-and-roadmap.md#13-vibe-coding-beginner--learn-seo--website-building-standalone) |
| **Vibe coding product** — Built-in skills | Ship SEO-friendly outputs by default. Skills as templates = better user-generated projects. [Partnership →](docs/use-cases-and-roadmap.md#14-vibe-coding-product--built-in-skills-as-templates) |
| **Build your own skills** — Fork & adapt | Don't know where to start? Fork the repo, modify and adapt on top of 100+ working examples. [Guide →](docs/use-cases-and-roadmap.md#15-want-to-build-your-own-skills--fork--adapt) |
| **Future** — Non-website agents | Image/video, influencer marketing, paid ads, analytics — skills reusable across agents. [Roadmap →](docs/use-cases-and-roadmap.md#16-future--non-website-agents) |

**Partnership**: Building a vibe coding product or AI marketing agent? [Contact me](mailto:zyjstc@gmail.com) to integrate these skills.

## Installation

**Full or selective.** Install all skills, or only the ones you need. Skills are independent — delete unwanted ones after install.

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

### Agent Skills Standard — Skill Directories

Skills are loaded from these locations per the [Agent Skills specification](https://agentskills.io/specification) and [Cursor docs](https://cursor.com/docs/context/skills):

| Location | Scope |
|----------|-------|
| `.agents/skills/` | Project-level |
| `.cursor/skills/` | Project-level |
| `~/.cursor/skills/` | User-level (global) |
| `.claude/skills/` | Project-level (compatibility) |
| `.codex/skills/` | Project-level (compatibility) |
| `~/.claude/skills/` | User-level (compatibility) |
| `~/.codex/skills/` | User-level (compatibility) |

Each skill is a folder with a `SKILL.md` file. **Platforms with native support**: Cursor, Claude Code, Codex, OpenCode, Gemini CLI, GitHub Copilot, Windsurf, Cline, Base44, Trae. [Full guide →](docs/where-to-use-skills.md)

### Git Submodule

```bash
git submodule add https://github.com/kostja94/marketing-skills.git .cursor/marketing-skills
# Symlink or copy only the skill folders you need into .cursor/skills/
```

## Where to Use Skills

Skills are markdown — they work anywhere an AI can read text. No native skill support required.

| Platform | How |
|----------|-----|
| **Cursor, Claude Code, Codex, OpenCode, Gemini CLI, GitHub Copilot, Windsurf, Cline, Base44, Trae** | Native: use `.agents/skills/`, `.cursor/skills/`, `.claude/skills/`, or platform dir |
| **Lovable, v0, Bolt, Replit** | AGENTS.md or platform-specific dir; copy skills, adapt context path |
| **ChatGPT, Gemini, Claude Web** | Paste a skill's markdown as context, then ask your question |
| **Any AI with file access** | Place skills in project root; reference in prompts |

**Full guide**: [where-to-use-skills.md](docs/where-to-use-skills.md) — all platforms, install commands, path reference, Lovable example

## Project Structure

```
marketing-skills/
├── skills/           # seo/, pages/, components/, channels/, platforms/, strategies/, analytics/
├── docs/             # skills-list, page-taxonomy, SKILLS_GUIDE, CHANGELOG, naming-rules, description-rules, reference-rules
├── templates/       # product-marketing-context.md, skills-task-progress.md, report templates
├── tools/            # Report generation — generate-report.py, *-guide.md
├── README.md
└── CONTRIBUTING.md
```

## Usage

Ask your agent — it picks the right skill from your prompt. Examples:

| You say | Skill |
|---------|-------|
| "SEO strategy" / "SEO plan" / "Where to start SEO" / "SEO audit" | seo-strategy |
| "Paid ads" / "PPC" / "Google Ads" / "ad budget" / "ROAS" | paid-ads-strategy |
| "Configure robots.txt" / "Audit sitemap" / "Fix canonical URLs" | robots-txt, xml-sitemap, canonical-tag |
| "Optimize title tag" / "Meta description" / "Open Graph" / "Twitter Cards" / "Add schema markup" / "Fix heading structure" | title-tag, meta-description, open-graph, twitter-cards, schema-markup, heading-structure |
| "Keyword research" / "Content strategy" / "Link building" | keyword-research, content-strategy, link-building |
| "Create pricing page" / "Optimize homepage" / "Create landing page" / "Create FAQ" | pricing-page-generator, homepage-generator, landing-page-generator, faq-page-generator |
| "Cold start" / "First users" / "Submit to Product Hunt" / "Directory submission" | cold-start-strategy, directory-submission |
| "Add to Grokipedia" / "GEO for AI search" | grokipedia-recommendations, generative-engine-optimization |
| "Parasite SEO" / "High-authority platforms" / "Programmatic SEO" / "Pages at scale" | parasite-seo, programmatic-seo |
| "GitHub SEO" / "Awesome list" / "curated list" | github-seo |
| "GA4 tracking" / "Search Console" / "AI traffic" | analytics-tracking, google-search-console, ai-traffic-tracking |

## Project Context & Linking

**Without context, outputs stay generic.** Add `product-marketing-context.md` so the agent delivers tailored copy and strategy. Place in `.cursor/`, `.claude/`, `.lovable/`, or your platform's config directory.

| Method | Purpose |
|--------|---------|
| **Product Context** | Product, audience, brand — skills read automatically |
| **Skills Task Progress** | Task status (pending/done), priority — agent suggests next steps |
| **Project Rules** (`.cursor/rules/`) | Code style, architecture, conventions |
| **AGENTS.md** | Simple project instructions |
| **@file references** | In chat: `@package.json` `@README.md` — agent includes when relevant |

**Templates**:
- [product-marketing-context.md](templates/product-marketing-context.md) · [download](https://raw.githubusercontent.com/kostja94/marketing-skills/main/templates/product-marketing-context.md)
- [skills-task-progress.md](templates/skills-task-progress.md) · [download](https://raw.githubusercontent.com/kostja94/marketing-skills/main/templates/skills-task-progress.md)

**Start with**: Product Overview, Positioning, Target Audience, Brand & Voice. Add Keywords, Competitors, Website as you have them. Update regularly — stale context degrades quality. See [SKILLS_GUIDE §10 Customization](docs/SKILLS_GUIDE.md#10-customization).

## Available Skills

104 skills in 7 categories. [Full list](docs/skills-list.md) · `npx skills add kostja94/marketing-skills --list`

| Category | Skills |
|----------|--------|
| **SEO** (19) | [Technical](skills/seo/technical/): robots, sitemap, canonical, indexing, indexnow, crawlability · [On-Page](skills/seo/on-page/): title, description, metadata, open-graph, twitter-cards, schema, internal-links, url-structure, heading · [Off-Page](skills/seo/off-page/): link-building, backlink-analysis · [Content](skills/seo/content/): keyword-research, content-strategy |
| **Pages** (31) | [skills-list](docs/skills-list.md#pages) — brand, content, marketing, legal, utility; [page-taxonomy](docs/page-taxonomy.md) — core vs extended, website types |
| **Components** (11) | nav, breadcrumb, footer, hero, toc, logo, trust-badges, testimonials, cta, newsletter-signup, url-slug |
| **Channels** (8) | affiliate, email-marketing, egc, influencer, referral, creator-program, community-forum, directories |
| **Platforms** (6) | x, reddit, linkedin, tiktok, github, grokipedia |
| **Strategies** (9) | seo-strategy, paid-ads-strategy, website-structure, cold-start, geo, integrated-marketing, localization, parasite-seo, programmatic-seo |
| **Analytics** (5) | traffic, tracking, seo-monitoring, ai-traffic, google-search-console |

## How Skills Work Together

**Workflow order**: Technical → On-Page → Content → Off-Page. Page skills apply SEO when optimizing specific page types. See each skill's **Related Skills** for the dependency map.

**[Full dependency maps →](docs/skills-relationships.md)** — 5 ASCII trees: SEO Foundation | SERP & Rich Results | Pages | Growth (Channels/Platforms/Strategies) | Components & Analytics. **seo-strategy** orchestrates the SEO workflow.

```
┌──────────────────────────────────────────┐
│       Technical SEO (Foundation)         │
│  robots · sitemap · canonical · indexing  │
│  indexnow · crawlability                 │
└─────────────────────┬────────────────────┘
                      │
    ┌─────────────────┼─────────────────┐
    ▼                 ▼                 ▼
┌─────────┐    ┌─────────────┐    ┌─────────────┐
│ On-Page │◄──►│    Content  │    │  Off-Page   │
│ metadata│    │ keyword ·  │    │ link-build  │
│ schema  │    │ content-*  │    │ backlink    │
└────┬────┘    └─────────────┘    └─────────────┘
     │
     ▼
┌──────────────────────────────────────────┐
│  Pages → Channels → Platforms → Analytics │
└──────────────────────────────────────────┘
```

**Skill uniqueness**: Each skill keeps only topic-relevant content. Overlapping topics use **Related Skills** references. See [SKILLS_GUIDE §4.2](docs/SKILLS_GUIDE.md#42-skill-uniqueness-and-cross-references).

**Output structure**: Platform skills use full structure (Introduction → Importance → Methods → Rules → Avoid → Action); others use brief context + main output. Say "skip intro" or "just do it" for repeat tasks. See [SKILLS_GUIDE §4.4](docs/SKILLS_GUIDE.md#44-output-structure-context-first-then-action).

## Tips & Rules

| Tip | Description |
|-----|-------------|
| **Project Context** | Add `product-marketing-context.md` to `.cursor/`, `.claude/`, or `.lovable/` for tailored output |
| **Skip intro** | "skip intro" or "just do it" → go straight to Action |
| **Related Skills** | Use each skill's Related Skills for dependencies |
| **Rules & specs** | See [SKILLS_GUIDE](docs/SKILLS_GUIDE.md) for output structure, skill authoring, quality checklist |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Rules and specs → [SKILLS_GUIDE](docs/SKILLS_GUIDE.md).

## References

*Product and website examples in skills are illustrative only; no affiliation, partnership, or endorsement implied. See [reference-rules §6](docs/reference-rules.md#6-product-and-website-examples).*

| Resource | Purpose |
|----------|---------|
| [Alignify](https://alignify.co/) | SEO guides, growth strategies — for human reading |
| [skills.sh](https://skills.sh) | Skill directory; 40+ agents; `npx skills add` |
| [where-to-use-skills.md](docs/where-to-use-skills.md) | Where to use skills — all platforms (native, AGENTS.md, paste), install, path reference |
| [use-cases-and-roadmap.md](docs/use-cases-and-roadmap.md) | Use cases, content roadmap, partnership |
| [docs/](docs/README.md) | Documentation index · skills-list · page-taxonomy · where-to-use-skills |
| [templates/](templates/README.md) | product-marketing-context · skills-task-progress · report templates |
| [SKILLS_GUIDE](docs/SKILLS_GUIDE.md) | Rules, specs, skill authoring |
| [CHANGELOG](docs/CHANGELOG.md) | What changed, when |
| [tools/](tools/README.md) | Report generation (keyword, competitor) |

## License

[MIT](LICENSE)
