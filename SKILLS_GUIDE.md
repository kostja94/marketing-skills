# Agent Skills Writing Guide

> Based on [Agent Skills Specification](https://agentskills.io/specification), [skills.sh Documentation](https://skills.sh/docs), and [Vercel skills CLI](https://github.com/vercel-labs/skills).

---

## 1. What Are Agent Skills

Agent Skills are reusable capability packages that provide **procedural knowledge** to AI agents, helping them complete specific tasks more accurately and efficiently. Think of them as "plugins" or "extensions" for agents.

- **Skill authors**: Write once, reuse across platforms
- **Agents**: Load on demand, extend capabilities
- **Teams/Enterprises**: Package organizational knowledge into version-controlled bundles

---

## 2. Directory Structure

### 2.1 Minimum Structure

```
skill-name/
└── SKILL.md          # Required
```

### 2.2 Full Structure (Recommended)

```
skill-name/
├── SKILL.md              # Required - main instruction file
├── references/           # Optional - detailed reference docs
│   ├── spec.md
│   └── examples.md
├── scripts/              # Optional - executable scripts
│   └── helper.sh
└── assets/               # Optional - static resources
    └── template.json
```

### 2.3 Category Hierarchy (This Repository)

```
skills/
├── seo/
│   ├── technical/        # Technical SEO
│   ├── on-page/          # On-page SEO
│   ├── off-page/         # Off-page SEO
│   └── content/          # Content SEO
├── pages/                # Page types
├── components/           # UI components (navigation, etc.)
├── channels/             # Acquisition channels (affiliate, influencer, referral, creator-program)
├── platforms/            # Publishing platforms (x, reddit, linkedin, tiktok)
├── strategies/           # Cross-cutting strategies (geo, localization)
├── analytics/            # Traffic, tracking
└── ...
```

The CLI supports **recursive discovery**; `SKILL.md` files in nested directories are found automatically.

---

## 3. SKILL.md Format

### 3.1 Required Frontmatter

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it.
---
```

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | Max 64 chars; lowercase letters, numbers, hyphens only; cannot start/end with hyphen; no consecutive hyphens `--` |
| `description` | Yes | Max 1024 chars; non-empty; describes what it does and when to use it |

### 3.2 name Field Rules

- Must match parent directory name (for flat structure)
- Allowed characters only: `a-z`, `0-9`, `-`
- Length: 1–64 characters

**Valid examples**: `pdf-processing`, `seo-technical-sitemap`, `pages-home`

**Invalid examples**:
- `PDF-Processing` (uppercase)
- `-pdf` (starts with hyphen)
- `pdf--processing` (consecutive hyphens)

### 3.3 description Field Rules

**Must include**:
1. **WHAT**: What the skill does (specific capabilities)
2. **WHEN**: When to use it (trigger scenarios, keywords)
3. **Third person**: Description is injected into system prompt; use third person

**Recommended format**:
```yaml
description: [What it does]. Also use when the user mentions "[keyword1]," "[keyword2]," or "[keyword3]."
```

**Examples**:

```yaml
# Good
description: When the user wants to configure, audit, or optimize robots.txt. Also use when the user mentions "robots.txt," "crawler rules," "block crawlers," or "AI crawlers."

# Avoid
description: Helps with robots.  # Too vague
description: I can help you with robots.  # First person
```

### 3.4 Optional Frontmatter

| Field | Description | Example |
|-------|-------------|---------|
| `license` | License | `license: MIT` |
| `compatibility` | Environment requirements (≤500 chars) | `compatibility: Requires git, docker` |
| `metadata` | Arbitrary key-value pairs | `metadata:\n  version: 1.0.0` |
| `allowed-tools` | Pre-approved tools list (experimental) | `allowed-tools: Bash(git:*) Read` |

**metadata example**:
```yaml
metadata:
  version: 1.0.0
  author: your-org
```

---

## 4. Body Content (Markdown Body)

The Markdown body after the frontmatter has no fixed structure. Recommended sections:

- **Step-by-step instructions**: Clear procedural guidance
- **Edge cases**: Common exceptions and handling
- **Input/output examples**: Concrete examples
- **Output format**: Expected output structure
- **Related Skills**: References to related skills

### 4.1 Progressive Disclosure

| Level | Content | Suggested Tokens |
|-------|---------|------------------|
| Metadata | name + description | ~100 |
| Main instructions | SKILL.md body | < 5000 (recommend < 500 lines) |
| Reference files | references/*.md | Load on demand |

- Keep main `SKILL.md` under **500 lines**
- Put detailed references in `references/` and link with relative paths
- Keep reference depth to **one level**; avoid deep nesting

### 4.2 File References

```markdown
See [the reference guide](references/spec.md) for details.

Run: `scripts/extract.py`
```

---

## 5. Optional Directories

### 5.1 scripts/

- Executable code (Python, Bash, JavaScript, etc.)
- Handle edge cases and provide clear error messages
- Self-contained or clearly document dependencies

### 5.2 references/

- Domain docs, technical references, templates
- Keep files focused for on-demand loading
- Common names: `spec.md`, `REFERENCE.md`, `FORMS.md`

### 5.3 assets/

- Static resources: lookup tables, images, templates
- e.g. `template.json`, `diagram.png`

---

## 6. skills.sh and Installation

### 6.1 Install Commands

```bash
# Install all
npx skills add owner/repo

# Install specific skills
npx skills add owner/repo --skill skill-name-1 skill-name-2

# List only (no install)
npx skills add owner/repo --list

# Non-interactive mode
npx skills add owner/repo -y
```

### 6.2 Listing and Leaderboard

- **No manual submission**: Skills are tracked via telemetry when users run `npx skills add`
- **Install count**: Determines ranking on [skills.sh](https://skills.sh/) leaderboard
- **Telemetry**: Anonymous, install counts only; set `DISABLE_TELEMETRY=1` to opt out

### 6.3 Discovery Paths

The CLI recursively searches for `SKILL.md` in:

- Repository root
- `skills/`
- `skills/.curated/`
- `skills/.experimental/`
- Agent-specific paths (e.g. `.cursor/skills/`, `.claude/skills/`)

---

## 7. Naming and Categorization

### 7.1 Naming Conventions

| Scenario | Format | Example |
|----------|--------|---------|
| Single level | `topic-action` | `seo-audit` |
| Category hierarchy | `category-subcategory-specific` | `seo-technical-sitemap` |
| Page types | `pages-type` | `pages-home`, `pages-pricing` |

### 7.2 Names to Avoid

- Too generic: `helper`, `utils`, `tools`
- Vague: `seo` (prefer specific, e.g. `seo-technical-robots`)

---

## 8. Quality Checklist

Before creating or modifying a skill, verify:

- [ ] `name` follows spec (lowercase, hyphens, ≤64 chars)
- [ ] `description` includes WHAT and WHEN, in third person
- [ ] `description` includes trigger keywords
- [ ] SKILL.md body < 500 lines
- [ ] Reference depth ≤ 1 level
- [ ] Consistent terminology
- [ ] No time-sensitive info (e.g. "before August 2025")

---

## 9. Reference Links

| Resource | URL |
|----------|-----|
| Agent Skills Specification | https://agentskills.io/specification |
| Agent Skills Homepage | https://agentskills.io |
| skills.sh Directory | https://skills.sh |
| skills.sh Documentation | https://skills.sh/docs |
| Vercel skills CLI | https://github.com/vercel-labs/skills |
| skills.sh FAQ | https://skills.sh/docs/faq |
