# Using Marketing Skills Beyond Cursor & Claude Code

Skills are **markdown instruction files**. They work anywhere an AI can read text — not just Cursor or Claude Code. Non-developers and products without native skill support can use them too.

---

## 1. Vibe Coding / No-Code Platforms (Lovable, Bolt, etc.)

Products like **Lovable**, **Bolt**, **v0**, and similar vibe-coding tools often don't support `.cursor/skills/` or `.claude/` directories. You can still use marketing skills by placing them in a project-root directory the AI can access.

### Approach

1. Create a product-specific directory (e.g. `.lovable/`, `.bolt/`, or a custom folder).
2. Copy the product context template and fill it in for your project.
3. Copy the skill files you need. Each skill is a single markdown file — copy the content from `skills/*/SKILL.md` and save as `skill-name.md`.
4. Adapt path references: if the skill mentions `.cursor/product-marketing-context.md` or `.claude/product-marketing-context.md`, change to your path (e.g. `.lovable/product-marketing-context.md`).

### Example: Lovable

**Directory structure:**

```
.lovable/
  product-marketing-context.md    # Pre-filled with your product info
  skills/
    seo-technical-robots.md
    seo-technical-sitemap.md
    seo-on-page-title.md
    seo-on-page-description.md
    seo-on-page-metadata.md
    seo-on-page-open-graph.md
    seo-on-page-twitter-cards.md
    seo-on-page-schema.md
    seo-on-page-heading.md
    seo-on-page-url-structure.md
    components-hero.md
    components-cta.md
    components-testimonials.md
    components-footer.md
```

**Files to create:**

| File | Source | Notes |
|------|--------|-------|
| `product-marketing-context.md` | [templates/product-marketing-context.md](../templates/product-marketing-context.md) | Fill in product, audience, brand, keywords |
| `seo-technical-robots.md` | [skills/seo/technical/robots/SKILL.md](../skills/seo/technical/robots/SKILL.md) | Change context path to `.lovable/product-marketing-context.md` |
| `seo-technical-sitemap.md` | [skills/seo/technical/sitemap/SKILL.md](../skills/seo/technical/sitemap/SKILL.md) | Same path adaptation |
| `seo-on-page-title.md` | [skills/seo/on-page/title/SKILL.md](../skills/seo/on-page/title/SKILL.md) | Change context path |
| `seo-on-page-description.md` | [skills/seo/on-page/description/SKILL.md](../skills/seo/on-page/description/SKILL.md) | Same path adaptation |
| `seo-on-page-metadata.md` | [skills/seo/on-page/metadata/SKILL.md](../skills/seo/on-page/metadata/SKILL.md) | Same path adaptation |
| `seo-on-page-open-graph.md` | [skills/seo/on-page/open-graph/SKILL.md](../skills/seo/on-page/open-graph/SKILL.md) | Same path adaptation |
| `seo-on-page-twitter-cards.md` | [skills/seo/on-page/twitter-cards/SKILL.md](../skills/seo/on-page/twitter-cards/SKILL.md) | Same path adaptation |
| *…other skills* | `skills/*/SKILL.md` | Copy content, adapt paths |

**What this enables:** When you ask the AI to optimize SEO, redesign components, or improve copy, it can reference these skill files for structured, best-practice-driven outputs tailored to your project.

**Excluded by default** (add later if needed): channels (affiliate, influencer), platforms (X, Reddit, LinkedIn, TikTok, Grokipedia), strategies (GEO, localization), analytics, page-type skills.

---

## 2. ChatGPT, Gemini, Claude Web, and Other Chat Models

Skills are **plain markdown**. You can use them with any LLM that accepts text input.

### Single-skill usage

1. Open a skill file (e.g. [skills/seo/on-page/metadata/SKILL.md](../skills/seo/on-page/metadata/SKILL.md)).
2. Copy the full content.
3. In ChatGPT, Gemini, Claude, or similar: paste the skill as context, then ask your question.

**Example prompt:**

```
[Paste seo-on-page-title or seo-on-page-description skill content]

Using these guidelines, optimize the meta title and description for my homepage. 
Product: [brief description]. Target keyword: [keyword].
```

### Multi-skill usage

For complex tasks, paste multiple skills or reference them in sequence. The model will follow the structured instructions.

### Tips

- **Product context**: Paste your filled-in product-marketing-context (or a shortened version) before the skill for tailored output.
- **Token limits**: If the skill is long, paste the most relevant sections or summarize key rules.
- **File upload**: Some chat UIs let you upload files — upload the skill `.md` file and ask the model to follow it.

---

## 3. Path Reference Cheat Sheet

When adapting skills for non-Cursor/Claude environments, replace:

| Original | Replace with |
|----------|--------------|
| `.cursor/product-marketing-context.md` | `.lovable/product-marketing-context.md` (or your path) |
| `.claude/product-marketing-context.md` | Same as above |
| `.cursor/skills-task-progress.md` | `.lovable/skills-task-progress.md` (optional) |

---

## 4. Summary

| Use case | How |
|----------|-----|
| **Cursor / Claude Code** | Native: `npx skills add kostja94/marketing-skills` or copy to `.cursor/skills/` |
| **Lovable, Bolt, v0, etc.** | Copy skills to `.lovable/skills/` (or equivalent), adapt context path |
| **ChatGPT, Gemini, Claude Web** | Paste skill markdown as context, then ask your question |
| **Any AI with file access** | Place skills in project root; reference in prompts |

**Skills = markdown.** No special runtime required. Copy, adapt paths, and use.
