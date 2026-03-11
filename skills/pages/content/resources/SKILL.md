---
name: resources-page-generator
description: When the user wants to create, optimize, or audit resources page or content hub. Also use when the user mentions "resources page," "resource center," "content hub," "learning center," "resource library," "downloads," "templates," "guides," or "resource hub."
metadata:
  version: 1.0.0
---

# Pages: Resources

Guides resources page and content hub structure for discovery and SEO.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for content themes and audience.

Identify:
1. **Content types**: Blog, guides, webinars, templates, tools (or standalone /tools; see **tools-page-generator**)
2. **Audience**: Buyers, users, both
3. **Funnel stage**: Top, middle, bottom

## Best Practices

### Purpose

- **Help buyers buy**: Content that supports decision-making
- **Help users succeed**: How-to, best practices
- **SEO**: Organize for discoverability and topical authority

### Structure

| Element | Purpose |
|---------|---------|
| **Categories** | By topic, format, or funnel stage |
| **Filters** | Format (blog, guide, video), topic, date |
| **Featured** | Highlight key assets |
| **Search** | Help users find specific content |
| **Contextual embeds** | Resource tiles on product pages |

### Navigation

- **Visible**: Resources in main nav or top-level section
- **Not buried**: Higher than content hubs in hierarchy
- **Clear labels**: "Resources," "Learn," "Content Library"

### Organization

- **Avoid junk drawer**: Intentional structure; not a catch-all
- **Logical hierarchy**: Folders, tags, categories
- **Internal linking**: Connect related content

### Integration

- **Product pages**: Embed relevant resources (streams, tiles)
- **Landing pages**: Lead magnet (ebook, template) or webinar as resource; LP exchanges value for email
- **Blog**: Part of resources or separate with cross-links
- **Glossary**: Link from resources

## Tools Integration

- **Standalone /tools**: When many free tools; use **tools-page-generator**; toolkit hub + per-tool pages
- **Resources section**: When few tools; embed tool cards in resources hub

## Output Format

- **Structure** (categories, filters)
- **Navigation** placement
- **Content** types to include
- **Internal linking** strategy
- **SEO** metadata

## Related Skills

- **card**: Resource card structure; thumbnail, title, format, CTA; tiles in hub
- **grid**: Resource hub grid layout; tiles
- **tools-page-generator**: Standalone /tools when many free tools; toolkit hub

- **landing-page-generator**: Lead magnet (ebook, webinar) as LP offer; LP exchanges resource for email
- **url-slug-generator**: URL slug for resource pages (e.g. /resources/guide-slug); 3-5 words
- **blog-page-generator**: Blog may be part of resources
- **glossary-page-generator**: Glossary as resource
- **tools-page-generator**: Standalone /tools when many free tools; toolkit hub
- **content-strategy**: Content hub strategy
- **internal-links**: Resource page linking
