---
name: docs-page-generator
description: When the user wants to create, optimize, or structure a documentation site. Also use when the user mentions "docs," "documentation site," "docs subdomain," "docs.yourdomain.com," "help center," "knowledge base," "Getting Started," "API Reference," "user guides," or "tutorials."
metadata:
  version: 1.0.0
---

# Pages: Documentation Site

Guides documentation site structure, navigation, and content organization. Typically hosted on `docs.*` or `help.*` subdomain. Includes Getting Started, guides, tutorials, **API Reference** (endpoint docs), and troubleshooting. Distinct from API introduction page (api-page-generator).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, audience, and use cases.

Identify:
1. **Product type**: Software, API, hardware, service
2. **Audience**: End users, developers, admins
3. **Content sources**: Markdown, MDX, Git, CMS
4. **Subdomain**: docs.*, help.*, or path (/docs)

## Documentation Structure

| Section | Purpose | Typical Content |
|---------|---------|-----------------|
| **Getting Started** | Onboarding, first steps | Quick start, installation, first task |
| **Guides / Tutorials** | Step-by-step learning | How-to articles, workflows |
| **Concepts** | Background, architecture | Key concepts, glossary links |
| **API Reference** | Endpoint docs | Auth, request/response, examples; part of docs, not separate page |
| **Troubleshooting** | Problem solving | FAQ, common errors, support links |

## Best Practices

### Information Architecture

- **Progressive disclosure**: Start simple, link to depth
- **Sidebar navigation**: Hierarchical, collapsible sections
- **Search**: Full-text search for long doc sets
- **Breadcrumbs**: For deep hierarchies

### API Reference (within Docs)

API Reference is a section of docs, not a standalone page. Include: endpoints by resource, auth, request/response schemas, error codes, rate limits, code examples (cURL, SDKs). Use OpenAPI/Swagger for consistency.

### Content

- **Task-oriented**: "How to X" not "X feature"
- **Code examples**: Copy-paste ready, multiple languages if relevant
- **Screenshots/videos**: For UI-heavy products
- **Versioning**: Document product/API version when applicable

### SEO and Discovery

- **Index docs**: Unless internal-only; use robots if needed
- **Internal links**: Cross-link related articles, link to main site
- **Schema**: TechArticle, HowTo for guides

## Output Format

- **Structure** (sections, hierarchy)
- **Navigation** design (sidebar, top-level)
- **Getting Started** outline
- **Content** checklist per section
- **Subdomain/path** recommendation

## Related Skills

- **api-page-generator**: API intro page links to docs
- **sidebar-generator**: Docs sidebar design
- **faq-page-generator**: FAQ can live in docs or main site
- **content-strategy**: Doc content planning
