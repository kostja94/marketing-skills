---
name: changelog-page-generator
description: When the user wants to create, optimize, or structure a changelog or release notes page. Also use when the user mentions "changelog," "release notes," "what's new," "updates," "product updates," "version history," or "changelog.yourdomain.com." For sitewide page planning, use website-structure.
metadata:
  version: 1.0.1
---

# Pages: Changelog

Guides changelog and release notes pages. Typically at `changelog.*` subdomain or `/changelog`. Builds trust, reduces support, increases feature adoption.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product and release cadence.

Identify:
1. **Product type**: SaaS, API, mobile app, etc.
2. **Audience**: End users, developers, both
3. **Release cadence**: Weekly, monthly, continuous
4. **Format**: Timeline, version-based, category (New, Improved, Fixed)

## Changelog Structure

| Section | Purpose |
|---------|---------|
| **Entry** | Date, version, title |
| **Category** | New, Improved, Fixed, Deprecated (optional) |
| **Description** | What changed, why it matters |
| **Link** | To docs, blog, or in-app |
| **Media** | Screenshots, GIFs, videos (optional) |

## Best Practices

### Content

- **User benefit first**: "You can now X" not "We added X"
- **Concrete**: Specific features, not vague "improvements"
- **Scannable**: Headlines, bullets, tags
- **Searchable**: If many entries, add search/filter

### Organization

- **Reverse chronological**: Newest first
- **Grouping**: By version or date range
- **Tags**: Feature area, product module (optional)
- **RSS/email**: Notify subscribers of updates

### Placement

- **Subdomain**: changelog.yourdomain.com
- **Path**: /changelog, /updates, /releases
- **Embed**: Widget in app or docs sidebar
- **Link from**: Footer, docs, in-app

## Output Format

- **Structure** (layout, entry format)
- **Entry template** (fields, tone)
- **Navigation** (filters, search)
- **SEO** (index, metadata)
- **Integration** (embed, RSS, email)

## Related Skills

- **docs-page-generator**: Changelog linked from docs
- **docs-page-generator**: API changelog for developers; docs includes API Reference
- **blog-page-generator**: Major releases may have blog posts
- **top-banner-generator**: Announce major updates on main site
