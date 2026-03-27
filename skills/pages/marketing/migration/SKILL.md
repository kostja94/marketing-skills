---
name: migration-page-generator
description: When the user wants to create, optimize, or audit migration guides for users switching from competitors. Also use when the user mentions "migration guide," "migrate from X," "switch to [product]," "import from X," or "data migration." For rebrand and redirects, use rebranding-strategy.
metadata:
  version: 1.0.1
---

# Pages: Migration

Guides migration pages that help users switch from a competitor to your product. Reduces friction for switchers; often linked from alternatives pages. Common for SaaS, tools, and productivity apps.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, migration capabilities, and source platforms.

Identify:
1. **Source**: Which competitor(s) to cover (Notion, Trello, etc.)
2. **Format**: Single hub vs. per-competitor pages (/migrate-from-notion)
3. **Migration type**: Manual import, automated tool, API
4. **Primary goal**: Sign up, start migration, reduce churn risk

## Page Structure

| Section | Purpose |
|---------|---------|
| **Headline** | "Migrate from [Competitor] to [Product] in Minutes" |
| **Why switch** | Brief; link to alternatives for full comparison |
| **What transfers** | Data, structure, attachments; what's supported |
| **Steps** | Numbered guide; screenshots or video |
| **Troubleshooting** | Common issues, support link |
| **CTA** | Start migration, try free, contact support |

## Best Practices

### Clarity

- **Explicit steps**: "1. Export from X. 2. Upload to [Product]. 3. Map fields."
- **Time estimate**: "Takes ~10 minutes for most workspaces"
- **Data scope**: What transfers; any limitations

### Trust

- **No competitor bashing**: Focus on your product's ease
- **Support**: Offer help; link to docs, chat, email
- **Success stories**: "10,000+ teams migrated from X"

### SEO

- **Intent**: Transactional; "migrate from X to Y"
- **Title**: "Migrate from [Competitor] to [Product] | Step-by-Step Guide"
- **Internal links**: Alternatives, features, pricing, docs

## Output Format

- **Headline** and intro
- **Step-by-step** migration guide
- **Data transfer** scope
- **Troubleshooting** section
- **Internal links**
- **SEO** metadata

## Related Skills

- **alternatives-page-generator**: Link to migration from alternatives
- **docs-page-generator**: Detailed migration docs
- **landing-page-generator**: Migration as conversion page
- **faq-page-generator**: Migration FAQ section
