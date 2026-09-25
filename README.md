# Marketing Skills: Marketing & SEO Workflows for AI Agents

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/kostja94/marketing-skills)](https://github.com/kostja94/marketing-skills/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/kostja94/marketing-skills)](https://github.com/kostja94/marketing-skills/commits/main)

**Marketing Skills** is an open-source library of reusable marketing and SEO workflows for AI agents. Install the skills your task needs, provide real product context, and get structured work grounded in explicit methods, checks, and source rules.

The library covers technical and on-page SEO, research, content, channels, paid advertising, launch and commercial strategy, platforms, and analytics. Page construction routes to [Pagina](https://github.com/kostja94/pagina); interface component construction routes to [Bricks](https://github.com/kostja94/bricks).

> **Marketing methods for agents. Project truth stays with the project.**

## Quick start

Install a focused set of skills for the task:

```bash
npx skills add kostja94/marketing-skills \
  --skill seo-strategy keyword-research content-strategy
```

Then give your agent a real assignment:

```text
Use seo-strategy to create a prioritized SEO plan for this product.
Read contextus.md and the current website first. Separate verified facts,
assumptions, opportunities, and next actions.
```

Other useful commands:

```bash
# Browse available entries
npx skills add kostja94/marketing-skills --list

# Install the complete library
npx skills add kostja94/marketing-skills
```

Install two or three relevant skills when the task is known instead of loading the entire library into one task. The CLI installs skills only; clone the repository when you also need `templates/` or the full documentation set.

## Choose a workflow

| Goal | Start with |
|---|---|
| Build an SEO roadmap | `seo-strategy` |
| Fix crawling, indexing, sitemap, or canonical issues | `robots-txt`, `indexing`, `xml-sitemap`, `canonical-tag` |
| Improve titles, descriptions, schema, and internal links | `title-tag`, `meta-description`, `schema-markup`, `internal-links` |
| Research keywords, competitors, or content opportunities | `keyword-research`, `competitor-research`, `content-strategy` |
| Plan launch, positioning, pricing, or acquisition | `product-launch`, `gtm-strategy`, `pricing-strategy`, `cold-start-strategy` |
| Plan paid acquisition | `paid-ads-strategy` plus the relevant platform skill |
| Track search and AI traffic | `analytics-tracking`, `google-search-console`, `ai-traffic-tracking` |
| Build a complete page | [Pagina](https://github.com/kostja94/pagina) `page-builder` |
| Build an interface component | [Bricks](https://github.com/kostja94/bricks) `component-builder` |

See the [full prompt-to-skill mapping](docs/usage.md) and [skill reference](docs/skills-reference.md).

## What Agent Skills add

An Agent Skill is a version-controlled directory with a `SKILL.md` file containing discovery metadata and procedural instructions. It differs from a one-off prompt by giving agents a reusable workflow they can load when a matching task appears.

Marketing Skills packages:

- task scope and routing rules;
- step-by-step methods and decision criteria;
- required inputs and missing-information checks;
- output structures and verification steps;
- boundaries between adjacent skills and repositories;
- reference rules for claims that require current external evidence.

The skills do not replace product facts, professional judgment, platform access, or human approval. Results still depend on the task, evidence, agent, tools, and review process.

## Library scope

The repository currently contains **170+ installable entries across 9 top-level categories**. That total includes active marketing skills and compatibility entries for page and component names that have moved to Pagina and Bricks.

| Category | Maintained responsibility |
|---|---|
| **SEO** | Technical, on-page, content, off-page, local, programmatic, entity, and SERP workflows |
| **Content** | Articles, copywriting, translation, video, podcast, and visual content |
| **Paid Ads** | Cross-platform strategy plus platform and format guidance |
| **Channels** | Affiliate, email, influencer, referral, directories, community, and PR |
| **Platforms** | X, Reddit, LinkedIn, TikTok, YouTube, Medium, Pinterest, GitHub, and Grokipedia |
| **Strategies** | Launch, brand, SEO structure, pricing, domain, localization, GEO, GTM, and PMF |
| **Analytics** | Traffic, tracking, Search Console, SEO monitoring, and AI traffic |
| **Pages** | Compatibility entries routing complete page construction to Pagina |
| **Components** | Compatibility entries routing interface components to Bricks; brand visual, favicon, and URL slug remain here |

The machine-discoverable list is available through `npx skills add kostja94/marketing-skills --list`. Detailed ownership and dependencies live in [docs/skills-reference.md](docs/skills-reference.md).

## How the ecosystem fits together

```text
Contextus
durable product and project truth
        ↓
Marketing Skills
SEO · content · channels · ads · strategy · analytics
        ├── complete page construction → Pagina
        └── interface component construction → Bricks
```

| Project | Single source of truth |
|---|---|
| [Contextus](https://github.com/kostja94/contextus) | Durable organization, product, audience, brand, website, technical, decision, and change context |
| **Marketing Skills** | Reusable marketing, SEO, channel, platform, strategy, and analytics methods |
| [Pagina](https://github.com/kostja94/pagina) | Complete page responsibilities, composition, states, and verification |
| [Bricks](https://github.com/kostja94/bricks) | Interface component responsibilities, variants, boundaries, and verification |

These repositories work independently. Compatibility entries preserve old skill names without creating duplicate page or component guidance.

## Project context

Tailored marketing work needs real product facts. [Contextus](https://github.com/kostja94/contextus) is the recommended maintained source, with a root `contextus.md` as the standard entry.

Marketing Skills reads only task-relevant context. It does not create a second context schema or silently promote agent research into confirmed product truth. Without Contextus, provide sufficient project documents or facts in the task; the skills remain usable and should ask only for missing information that would materially change the result.

```bash
npx skills add kostja94/contextus --skill contextus
```

Legacy `project-context.md` files remain readable as fallback material. The compatibility entry under [templates](templates/README.md) is not a second maintained context system.

## Installation and compatibility

| Method | Use when |
|---|---|
| `npx skills add ...` | Your agent is supported by the skills CLI and you want all or selected skills |
| Clone or copy | You need templates, documentation, or direct control over the repository layout |
| Git submodule | You want to track this repository inside another project |
| Paste or reference Markdown | The tool accepts text context but does not natively discover Agent Skills |

Agent Skills-aware tools can discover installed `SKILL.md` files and activate them from metadata. Other AI tools may still use the Markdown instructions manually, but automatic discovery, routing, tool access, and path behavior depend on the host.

Platform paths, native-support notes, copy instructions, and usage examples are maintained in [docs/usage.md](docs/usage.md). The file format follows the [Agent Skills specification](https://agentskills.io/specification).

## Evidence and limitations

[SkillsBench](https://arxiv.org/abs/2602.12670) is one independent benchmark, not a guarantee for this repository. Its 2026 v4 evaluation covers 87 tasks across 8 domains and 18 model-harness configurations. Curated Skills increased average pass rate from 33.9% to 50.5% (`+16.6` percentage points); focused Skills with at most three modules outperformed larger bundles in that evaluation.

This supports focused, task-relevant installation and review—not the claim that every skill or agent output is automatically production-ready. See [skill authoring](docs/skill-authoring.md) for how this repository applies those lessons.

Representative use cases include product-site SEO, technical audits, launch planning, content research, paid acquisition, analytics, and authoring your own skills. Detailed scenarios are in [docs/usage.md](docs/usage.md#7-use-cases).

## Security

This repository ships Markdown instructions and templates, not executable skill code. The published audit checks for hidden instructions, prompt-injection patterns, executable URL schemes, and credential-exfiltration directives.

Individual marketing workflows may still require web research or external platforms. Permissions, credentials, data access, and side effects remain controlled by the host agent and user. Review Skills as trusted context before installation. See the [security model and audit commands](docs/SECURITY.md).

## Build with the library

Building a vibe-coding product, an AI marketing agent, or an SEO learning experience? The skills can serve as maintained workflow references or integration inputs.

[Contact the maintainer](mailto:zyjstc@gmail.com) to discuss collaboration. To add or improve skills, read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Agent Skills writing guide](docs/skill-authoring.md).

[![Star History Chart](https://api.star-history.com/image?repos=kostja94/marketing-skills&type=Date)](https://star-history.com/#kostja94/marketing-skills)

If the library is useful, starring or sharing it helps other teams discover the project.

## Documentation

| Document | Purpose |
|---|---|
| [Usage](docs/usage.md) | Installation, platform behavior, use cases, and roadmap |
| [Skills reference](docs/skills-reference.md) | Maintained skill inventory, ownership, and dependency maps |
| [Skill authoring](docs/skill-authoring.md) | Format, naming, writing, and quality rules |
| [Security](docs/SECURITY.md) | Threat model, audit checklist, and verification commands |
| [Templates](templates/README.md) | Context compatibility entry and task tracker |
| [Changelog](docs/CHANGELOG.md) | Repository changes and migrations |

## License

[MIT](LICENSE)

Maintained by [kostja](https://github.com/kostja94) · [Human-facing marketing guides](https://alignify.co/) · [Changelog](docs/CHANGELOG.md)
