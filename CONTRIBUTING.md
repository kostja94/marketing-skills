# Contributing

Contributions are welcome! Here's how to add or improve skills.

## Adding a New Skill

1. Create a new directory under the appropriate category:
   - SEO: `skills/seo/{technical,on-page,off-page,content}/skill-name/`
   - Pages: `skills/pages/{brand,content,marketing,legal,utility}/skill-name/` (see [page-types-taxonomy](docs/page-types-taxonomy.md))
2. Add `SKILL.md` with:
   - YAML frontmatter: `name`, `description`, `metadata.version`
   - Scope section (what the skill covers)
   - Clear instructions for the agent
   - Related skills section
3. Update [README.md](README.md) with the new skill in the table
4. Run `npx skills add kostja94/marketing-skills --list` to verify discovery

## Skill Naming

- Use lowercase letters and hyphens only
- Follow category prefix: `seo-technical-robots`, `seo-on-page-metadata`, `pages-home`
- Be specific: `seo-technical-sitemap` not `sitemap`

## Description Best Practices

- Write in third person
- Include trigger terms (when users say X, Y, Z)
- Be specific about what the skill does
- Mention when to use vs. when to use related skills

## Full Specification

See [SKILLS_GUIDE.md](SKILLS_GUIDE.md) for the complete specification, frontmatter rules, and quality checklist.

## Testing

1. Install locally: `npx skills add . --skill your-skill-name`
2. Ask the agent to perform the task
3. Verify the skill is invoked correctly
