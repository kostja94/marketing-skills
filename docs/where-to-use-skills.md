# Where to Use Marketing Skills

> Skills are **markdown instruction files**. They work anywhere an AI can read text — IDEs, vibe-coding tools, chat models, and any platform with file access. This doc covers all supported platforms and how to use skills on each.

**Reference**: [Agent Skills spec](https://agentskills.io/specification) · [skills.sh](https://skills.sh) (40+ agents) · [agentskills.help](https://agentskills.help)

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

### Full Platform Table

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

### Universal Path

**`.agents/skills/`** works on Cursor, Claude Code, Codex, OpenCode, Gemini CLI, and GitHub Copilot. Use it for maximum portability.

### Install Command

```bash
# Install to default platform
npx skills add kostja94/marketing-skills

# Install to multiple platforms
npx skills add kostja94/marketing-skills -a cursor -a claude-code -a codex -a opencode
```

### Platform-Specific Notes

| Platform | Detail |
|----------|--------|
| **OpenCode** | Permission control via `opencode.json` (`permission.skill`); `allow` / `deny` / `ask` · [docs](https://open-code.ai/en/docs/skills) |
| **Gemini CLI** | `/skills list`, `gemini skills install <source>`, `gemini skills link /path` · [docs](https://geminicli.com/docs/cli/skills/) |
| **GitHub Copilot** | VS Code: `chat.agentSkillsLocations` in settings.json; `.github/skills/` for team repos · [docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills) |
| **Windsurf** | `.windsurf/skills.json` for config; mention `@skill-name` in Cascade chat · [docs](https://docs.windsurf.com/windsurf/cascade/skills) |
| **Cline** | Create via UI (scale icon → New skill) or manually in `.cline/skills/` · [docs](https://docs.cline.bot/customization/skills) |

---

## 2. Other Platforms (skills.sh / SkillsLM CLI)

[skills.sh](https://skills.sh) and [SkillsLM](https://www.sddts.cn/index.php/archives/2618/) support cross-platform installation. The following 6 CLI platforms are officially supported by [vercel-labs/skills](https://github.com/vercel-labs/skills):

| Platform | Config Path | Docs |
|----------|-------------|------|
| **AMP** | `~/.config/agents/skills/` (shares `.agents/skills/` spec with Kimi CLI, Replit) | [AMP docs](https://docs.augmentcode.com/cli/skills) |
| **KiloCode** | `~/.kilocode/skills/` | [Kilo docs](https://kilo.ai/docs/features/skills) |
| **Roo** | `~/.roo/skills/` | [Roo docs](https://docs.roocode.com/features/skills) |
| **Goose** | `~/.config/goose/skills/` | [Goose docs](https://block.github.io/goose/docs/guides/context-engineering/using-skills/) |
| **Kiro** | `~/.kiro/skills/` (add to agent config `resources` after install) | [Kiro docs](https://kiro.dev/docs/cli/skills/) |
| **OpenClaw** | ClawHub (clawhub.com); `~/.openclaw/skills/` | [OpenClaw docs](https://docs.clawd.bot/skills) |

---

## 3. Vibe Coding / No-Code Platforms

These tools don't support `.cursor/skills/` or `.agents/skills/` natively. Use AGENTS.md, platform dirs, or paste.

### Implementation by Platform

| Platform | Skills / Rules | How to Use | Docs |
|----------|---------------|------------|------|
| **Base44** | Native Agent Skills | Uses `.cursor/skills/`, `.claude/skills/`, `.agents/skills/`. `npx skills add base44/skills`. | [Base44 docs](https://docs.base44.com/developers/backend/overview/skills) |
| **Lovable** | AGENTS.md | AI reads `AGENTS.md` in project root. Use [OpenSkills](https://github.com/anthropics/skills) (`openskills sync`) to sync skills into AGENTS.md, or copy to `.lovable/skills/` and adapt paths. | [Lovable docs](https://docs.lovable.dev/AGENTS) |
| **Replit** | AGENTS.md | Same as Lovable. OpenSkills can sync skills to AGENTS.md for Replit/Cursor/Trae. | [Replit docs](https://docs.replit.com/replitai/skills) |
| **v0** (Vercel) | CLAUDE.md, .claude/ | Uses `CLAUDE.md` for project instructions. No skills dir. Copy skills to project root or paste in prompts. | [Vercel v0](https://v0.dev) |
| **Bolt.new** | Prompt-only | Browser-based; no project file structure. Paste skill markdown as context in chat. | [Bolt.new](https://bolt.new) |
| **Medo** | None | Baidu no-code AI platform ([medo.dev](https://medo.dev)). Paste skill content into dialogue, or export project and add skills locally. | — |

### Approach (for tools without native skills)

1. Create a product-specific directory (e.g. `.lovable/`, `.bolt/`, or custom).
2. Copy [product-marketing-context.md](../templates/product-marketing-context.md) and fill it in.
3. Copy the skill files you need from `skills/*/SKILL.md` and save as `skill-name.md`.
4. Adapt path references: change `.cursor/product-marketing-context.md` to your path (e.g. `.lovable/product-marketing-context.md`).

### Example: Lovable

**Directory structure:**

```
.lovable/
  product-marketing-context.md
  skills/
    robots-txt.md
    xml-sitemap.md
    title-tag.md
    meta-description.md
    page-metadata.md
    open-graph.md
    twitter-cards.md
    schema-markup.md
    heading-structure.md
    url-structure.md
    hero-generator.md
    cta-generator.md
    testimonials-generator.md
    footer-generator.md
```

**Files to create:**

| File | Source |
|------|--------|
| `product-marketing-context.md` | [templates/product-marketing-context.md](../templates/product-marketing-context.md) |
| `robots-txt.md` | [skills/seo/technical/robots/SKILL.md](../skills/seo/technical/robots/SKILL.md) |
| `title-tag.md` | [skills/seo/on-page/title/SKILL.md](../skills/seo/on-page/title/SKILL.md) |
| *…other skills* | `skills/*/SKILL.md` |

Change context path references in each skill to `.lovable/product-marketing-context.md`.

---

## 4. ChatGPT, Gemini, Claude Web, and Other Chat Models

Skills are **plain markdown**. Use them with any LLM that accepts text input.

### Single-skill usage

1. Open a skill file (e.g. [skills/seo/on-page/metadata/SKILL.md](../skills/seo/on-page/metadata/SKILL.md)).
2. Copy the full content.
3. In ChatGPT, Gemini, Claude, or similar: paste the skill as context, then ask your question.

**Example prompt:**

```
[Paste title-tag or meta-description skill content]

Using these guidelines, optimize the meta title and description for my homepage. 
Product: [brief description]. Target keyword: [keyword].
```

### Tips

- **Product context**: Paste your filled-in product-marketing-context (or shortened version) before the skill.
- **Token limits**: Paste the most relevant sections or summarize key rules.
- **File upload**: Some chat UIs let you upload files — upload the skill `.md` and ask the model to follow it.

---

## 5. Path Reference Cheat Sheet

When adapting skills for non-Cursor/Claude environments:

| Original | Replace with |
|----------|--------------|
| `.cursor/product-marketing-context.md` | `.lovable/product-marketing-context.md` (or your path) |
| `.claude/product-marketing-context.md` | Same as above |
| `.cursor/skills-task-progress.md` | `.lovable/skills-task-progress.md` (optional) |
| `.cursor/skills/` | `.agents/skills/`, `.claude/skills/`, `.codex/skills/`, or platform-specific dir |

---

## 6. Summary Table

| Use case | How |
|----------|-----|
| **Cursor, Claude Code, Codex, OpenCode, Gemini CLI, GitHub Copilot, Windsurf, Cline, Base44, Trae** | Native: `npx skills add kostja94/marketing-skills` or copy to `.agents/skills/`, `.cursor/skills/`, or platform dir |
| **Lovable, Replit** | AGENTS.md in project root; OpenSkills (`openskills sync`); or copy to `.lovable/skills/` and adapt paths |
| **v0, Bolt.new, Medo** | Copy skills to project root and reference in prompts, or paste skill markdown as context |
| **ChatGPT, Gemini, Claude Web** | Paste skill markdown as context, then ask your question |
| **Any AI with file access** | Place skills in project root; reference in prompts |

**Skills = markdown.** No special runtime required. Copy, adapt paths, and use.
