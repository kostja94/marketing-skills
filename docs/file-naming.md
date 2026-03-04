# File and Folder Naming Conventions

> Why some files use uppercase and others lowercase. Reference: [Google developer style](https://developers.google.com/style/filenames), [Keep a Changelog](https://keepachangelog.com/).

## Best Practice: Lowercase Preferred

**Use lowercase** for file and folder names when possible. Benefits:

- **Cross-platform compatibility** — Linux and macOS are case-sensitive; `File.md` and `file.md` are different files
- **Reduces ambiguity** — No decision between "Invoice" vs "invoice"
- **URL/SEO** — Lowercase paths are cleaner when files are referenced in URLs

**Use hyphens** to separate words (e.g. `skills-guide.md`), not underscores.

## Uppercase Exceptions (Tool/Spec Conventions)

The following use **uppercase** because tools and specifications expect them:

| File | Reason |
|------|--------|
| `README.md` | GitHub, GitLab, and most platforms display this as the project homepage |
| `CONTRIBUTING.md` | GitHub contribution guidelines convention |
| `CHANGELOG.md` | [Keep a Changelog](https://keepachangelog.com/) format |
| `LICENSE` | Common convention for license files |
| `SKILL.md` | [Agent Skills specification](https://agentskills.io/specification) — required for skill discovery |

**Do not rename** these files; changing them would break tool integration.

## This Repository

| Location | Convention |
|----------|------------|
| **Folders** | All lowercase, hyphens (e.g. `domain-selection`, `pricing-strategy`) |
| **Skill names** | Lowercase, hyphens (spec requirement) |
| **Docs** | Lowercase (e.g. `skills-guide.md`, `naming-rules.md`) |
| **Root** | README.md, CONTRIBUTING.md, CHANGELOG.md, LICENSE — uppercase per convention |
