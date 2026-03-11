# Installation & Use Cases

> Skills are **markdown instruction files**. They work anywhere an AI can read text — IDEs, vibe-coding tools, chat models, and any platform with file access. This doc covers platforms, installation, use cases, and content roadmap.

**Reference**: [Agent Skills spec](https://agentskills.io/specification) · [skills.sh](https://skills.sh) (40+ agents) · [agentskills.help](https://agentskills.help)

---

## 0. Agent Skills Overview

**What they are**: Agent Skills are a lightweight, open format for extending AI agents with procedural knowledge — the "how to" steps and rules, not static descriptions. Think of them as "skill packs" or "plugins": authors write once; agents load on demand when the task matches. They solve the context gap — packaging organizational knowledge, team workflows, and domain norms into reusable Markdown that agents read at the right moment for more consistent, auditable behavior.

**How they differ**: **Prompt** is one-off, per conversation. **Skill** is reusable, version-controlled, loaded when needed. **Tool** is a single executable (API call, file write). **MCP** connects agents to external services. **RAG** retrieves docs to augment context but doesn't execute. Skills complement all of these.

**Discovering skills**: Browse [skills.sh](https://skills.sh) (All Time, Trending, Hot); search with `npx skills find [keyword]`; or `npx skills add owner/repo --list` to see a repo's skills. Check [skills.sh/kostja94](https://skills.sh/kostja94) for this repo's listing.

**SkillsBench tip** (*for reference only — one paper's findings*): 2–3 relevant skills per task may be a performance sweet spot; 4+ skills can cause context overload. Prefer selective install (`--skill a b c`) when you know the task. See [skill-authoring §9](skill-authoring.md#9-skillsbench-reference-informational).

---

## Quick Summary

| Platform Type | Platforms | How |
|---------------|-----------|-----|
| **Native Skills** | Cursor, Claude Code, Codex, OpenCode, Gemini CLI, GitHub Copilot, Windsurf, Cline, Base44, Trae | `npx skills add kostja94/marketing-skills` or copy to `.agents/skills/` |
| **AGENTS.md** | Lovable, Replit | OpenSkills sync or `.lovable/skills/` + adapt paths |
| **Paste / Reference** | v0, Bolt.new, Medo, ChatGPT, Gemini, Claude Web | Paste skill markdown as context, or copy to project root |
| **CLI Multi-Platform** | AMP, KiloCode, Roo, Goose, Kiro, OpenClaw | `npx skills add ... -a <platform>` |

---

## 1. Platforms with Native Agent Skills Support

These platforms auto-discover skills from standard directories. Install once, agent loads on demand.

### Platform Table

| Platform | Project Dir | User Dir | Notes |
|----------|-------------|----------|-------|
| **Cursor** | `.cursor/skills/`, `.agents/skills/`, `.claude/skills/`, `.codex/skills/` | `~/.cursor/skills/`, `~/.claude/skills/`, `~/.codex/skills/` | [Cursor docs](https://cursor.com/docs/context/skills) |
| **Claude Code** | `.claude/skills/`, `.agents/skills/` | `~/.claude/skills/`, `~/.agents/skills/` | [Claude Code docs](https://code.claude.com/docs/en/skills) |
| **Codex** | `.agents/skills/` | `~/.agents/skills/`, `/etc/codex/skills` | [OpenAI Codex docs](https://developers.openai.com/codex/skills) |
| **OpenCode** | `.opencode/skills/`, `.agents/skills/`, `.claude/skills/` | `~/.config/opencode/skills/`, `~/.agents/skills/`, `~/.claude/skills/` | [OpenCode docs](https://open-code.ai/en/docs/skills) |
| **Gemini CLI** | `.gemini/skills/`, `.agents/skills/` | `~/.gemini/skills/`, `~/.agents/skills/` | [Gemini CLI docs](https://geminicli.com/docs/cli/skills/) |
| **GitHub Copilot** | `.github/skills/`, `.claude/skills/`, `.agents/skills/` | `~/.copilot/skills/`, `~/.claude/skills/` | [GitHub Copilot docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills) |
| **Windsurf** | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` | [Windsurf docs](https://docs.windsurf.com/windsurf/cascade/skills) |
| **Cline** | `.cline/skills/` | `~/.cline/skills/` | [Cline docs](https://docs.cline.bot/customization/skills) |
| **Base44** | `.cursor/skills/`, `.claude/skills/`, `.agents/skills/` | — | [Base44 docs](https://docs.base44.com/developers/backend/overview/skills) |
| **Trae** | `.cursor/skills/`, `.claude/skills/`, `.agents/skills/` | — | [Trae docs](https://docs.trae.ai/ide/skills) |

**Universal path**: **`.agents/skills/`** works on Cursor, Claude Code, Codex, OpenCode, Gemini CLI, and GitHub Copilot.

### Install Command

```bash
# Install to default platform
npx skills add kostja94/marketing-skills

# Install to multiple platforms
npx skills add kostja94/marketing-skills -a cursor -a claude-code -a codex -a opencode
```

### Syncing with GitHub

To keep skills updated: **CLI** — re-run `npx skills add kostja94/marketing-skills` (overwrites); **Git submodule** — `git submodule add https://github.com/kostja94/marketing-skills.git .cursor/marketing-skills`, then `cp -r .cursor/marketing-skills/skills/* .cursor/skills/`; update with `cd .cursor/marketing-skills && git pull`.

---

## 2. OpenClaw

[OpenClaw](https://openclaw.ai/) is an open-source personal AI assistant. It uses **AgentSkills-compatible** skill folders — the same `SKILL.md` format as this repo.

### Skill locations (precedence)

| Location | Scope |
|----------|-------|
| `./skills` (workspace) | Per-agent; highest priority |
| `~/.openclaw/skills/` | Shared across all agents |
| Bundled skills | Shipped with OpenClaw (lowest) |

### Install

```bash
# Install all marketing skills to OpenClaw
npx skills add kostja94/marketing-skills -a openclaw

# Install specific skills only
npx skills add kostja94/marketing-skills -a openclaw --skill robots-txt title-tag meta-description pricing-page-generator
```

**Product context**: Add `project-context.md` to your OpenClaw workspace. Skills read it automatically. See [README § Project Context](../README.md#project-context--linking).

---

## 3. Other Platforms (skills.sh CLI)

| Platform | Config Path | Docs |
|----------|-------------|------|
| **AMP** | `~/.config/agents/skills/` | [AMP docs](https://docs.augmentcode.com/cli/skills) |
| **KiloCode** | `~/.kilocode/skills/` | [Kilo docs](https://kilo.ai/docs/features/skills) |
| **Roo** | `~/.roo/skills/` | [Roo docs](https://docs.roocode.com/features/skills) |
| **Goose** | `~/.config/goose/skills/` | [Goose docs](https://block.github.io/goose/docs/guides/context-engineering/using-skills/) |
| **Kiro** | `~/.kiro/skills/` | [Kiro docs](https://kiro.dev/docs/cli/skills/) |
| **OpenClaw** | `./skills` or `~/.openclaw/skills/` | [OpenClaw Skills docs](https://docs.openclaw.ai/tools/skills) |

---

## 4. Vibe Coding / No-Code Platforms

| Platform | How to Use | Docs |
|----------|------------|------|
| **Lovable** | AGENTS.md in project root; OpenSkills (`openskills sync`); or copy to `.lovable/skills/` and adapt paths | [Lovable docs](https://docs.lovable.dev/AGENTS) |
| **Replit** | Same as Lovable. OpenSkills can sync skills to AGENTS.md | [Replit docs](https://docs.replit.com/replitai/skills) |
| **v0** (Vercel) | Uses `CLAUDE.md`. Copy skills to project root or paste in prompts | [Vercel v0](https://v0.dev) |
| **Bolt.new** | Browser-based; no project file structure. Paste skill markdown as context | [Bolt.new](https://bolt.new) |
| **Medo** | Paste skill content into dialogue | [medo.dev](https://medo.dev) |

**Approach**: Create a product-specific directory (e.g. `.lovable/`); copy [project-context.md](../templates/project-context.md) and fill it in; copy skill files from `skills/*/SKILL.md`; adapt path references (e.g. `.cursor/project-context.md` → `.lovable/project-context.md`).

---

## 5. ChatGPT, Gemini, Claude Web

Skills are **plain markdown**. Use them with any LLM that accepts text input.

1. Open a skill file (e.g. [skills/seo/on-page/metadata/SKILL.md](../skills/seo/on-page/metadata/SKILL.md)).
2. Copy the full content.
3. In ChatGPT, Gemini, Claude, or similar: paste the skill as context, then ask your question.

**Example prompt**: Paste title-tag or meta-description skill content, then: "Using these guidelines, optimize the meta title and description for my homepage. Product: [brief description]. Target keyword: [keyword]."

**Tips**: Paste project-context before the skill for tailored output; paste most relevant sections if token limits apply.

---

## 6. Path Reference Cheat Sheet

| Original | Replace with |
|----------|--------------|
| `.cursor/project-context.md` | `.lovable/project-context.md` (or your path) |
| `.claude/project-context.md` | Same as above |
| `.cursor/project-task-tracker.md` | `.lovable/project-task-tracker.md` (optional) |
| `.cursor/skills/` | `.agents/skills/`, `.claude/skills/`, `./skills` (OpenClaw), `~/.openclaw/skills/`, or platform-specific dir |

---

## 7. Use Cases

### 7.1 Personal Developer — SEO-Friendly Personal Site

**Scenario**: Individual developers want to build a personal website (portfolio, blog, landing page) with SEO built in.

**Why this works**: One-click install; no need to learn SEO from scratch — the agent applies best practices when you ask.

**Recommended skills subset**: Technical: `robots-txt`, `xml-sitemap`, `canonical-tag`, `indexing`; On-page: `title-tag`, `meta-description`, `open-graph`, `twitter-cards`, `schema-markup`, `heading-structure`; Pages: `homepage-generator`, `about-page-generator`, `contact-page-generator`, `blog-page-generator`; Components: `hero-generator`, `footer-generator`, `cta-generator`.

### 7.2 Product Website — SEO Growth with Frontend + Ops Split

**Scenario**: A product website wants to drive SEO growth. Frontend uses optimization techniques; operations can build marketing pages independently via rewrite without depending on engineering.

**Recommended skills subset**: Technical + on-page (frontend team); Pages (marketing): `pricing-page-generator`, `landing-page-generator`, `use-cases-page-generator`, `customer-stories-page-generator`, `alternatives-page-generator`, `integrations-page-generator`; Strategies: `seo-strategy`, `paid-ads-strategy`, `website-structure`.

### 7.3 Vibe Coding Beginner — Learn SEO Standalone

**Scenario**: Someone new to vibe coding (Bolt.new, v0, Lovable, etc.) wants to learn SEO and website construction.

**Why this works**: Skills are markdown — install and read them as learning material. Use ChatGPT, Claude Web, or Gemini: paste a skill, ask questions, get explanations.

**Recommended approach**: Start with `seo-strategy` for workflow overview; then technical: `robots-txt`, `xml-sitemap`, `title-tag`, `meta-description`; use [skill-authoring](skill-authoring.md) and [skills-reference §2](skills-reference.md#2-page-taxonomy) for structure.

### 7.4 Vibe Coding Product — Built-in Skills as Templates

**Scenario**: Vibe coding platforms want to ship SEO-friendly outputs by default. Built-in skills act as templates so user-generated projects are more discoverable.

**Partnership**: If you build a vibe coding product and want to integrate these skills, [contact me](mailto:zyjstc@gmail.com) for collaboration.

### 7.5 Want to Build Your Own Skills — Fork & Adapt

**Scenario**: You want to create your own agent skills but don't know where to start.

**Why this works**: Fork the repo — you get 100+ working examples to modify and adapt. Learn from structure — SKILL.md format, frontmatter, Related Skills, output patterns are all documented.

**How to start**:
1. Fork [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills)
2. Read [skill-authoring](skill-authoring.md) for format and authoring rules
3. Pick a skill similar to what you want (e.g. `pricing-page-generator` → your `custom-page-generator`)
4. Copy, rename, edit — then install with `npx skills add your-username/your-fork`

### 7.6 Future — Non-Website Agents

| Agent Type | Relevant Skills Today | Future Expansion |
|------------|------------------------|------------------|
| **Image / Video** | — | New skills: image generation prompts, video script/storyboard |
| **Marketing (Influencer)** | `influencer-marketing`, `creator-program`, `twitter-x-posts`, `tiktok-captions`, `linkedin-posts` | Campaign briefs, creator discovery criteria |
| **Marketing (Ads)** | `paid-ads-strategy` | Ad copy, landing page alignment, ROAS optimization |
| **Analytics** | `analytics-tracking`, `google-search-console`, `ai-traffic-tracking`, `traffic-analysis` | Dashboard design, report templates |
| **Content** | `keyword-research`, `content-strategy`, `content-optimization` | Editorial workflows, content repurposing |

---

## 8. Content Roadmap

Content creation recommendations based on existing skills and market trends:

- **Personal Site Quick Start**: Minimal skill subset (10–15 skills); one-command install; order of operations
- **Product Website SEO Playbook**: Frontend vs ops ownership; rewrite rules for marketing pages; page priority
- **Vibe Coding SEO Learning Path**: Week 1–4 structure; which skill to use; example prompts
- **Vibe Coding Integration Guide**: How to bundle skills; AGENTS.md integration; partnership CTA
- **Non-Website Agent Roadmap**: Proposed new skills; multi-agent reuse structure
- **Skill Authoring from Fork**: Step-by-step fork → copy → edit → publish

---

## 9. Partnership

If you are building:
- A **vibe coding product** and want SEO-friendly defaults
- An **AI marketing agent** (influencer, ads, content)
- A **learning platform** for SEO or website building

Reach out: **zyjstc@gmail.com**
