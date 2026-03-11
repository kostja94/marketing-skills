# Contributing

Contributions are welcome! Here's how to add or improve skills.

**Want to build your own skills from scratch?** Fork this repo — you get 100+ working examples to modify and adapt. See [usage § Fork & Adapt](docs/usage.md#75-want-to-build-your-own-skills--fork--adapt).

## Adding a New Skill

1. Create a new directory under the appropriate category:
   - SEO: `skills/seo/{technical,on-page,off-page,content}/skill-name/`
   - Pages: `skills/pages/{brand,content,marketing,legal,utility}/skill-name/` (see [skills-reference §Pages](docs/skills-reference.md#pages--quick-mapping))
   - Paid Ads: `skills/paid-ads/{platforms,formats}/skill-name/`
   - Channels: `skills/channels/{partnerships,community,owned,distribution}/skill-name/` (folder name = skill name; see [skill-authoring §2.4](docs/skill-authoring.md#24-folder-name--skill-name))
   - Analytics: `skills/analytics/{sources,seo,tracking}/skill-name/`
   - Strategies: `skills/strategies/{launch,brand,commercial,structure}/skill-name/` or `skills/strategies/commercial/{domain,pricing}/skill-name/` for domain/pricing (see [skills-reference §Channels, Platforms, Strategies](docs/skills-reference.md#channels-platforms-strategies-analytics))
2. Add `SKILL.md` with:
   - YAML frontmatter: `name`, `description`, `metadata.version`
   - Scope section (what the skill covers)
   - Clear instructions for the agent
   - Related skills section
3. Update [README.md](README.md) with the new skill in the table
4. Run `npx skills add kostja94/marketing-skills --list` to verify discovery

## Skill Naming

**Core principles**: (1) Name must match skill content/function. (2) Use high-search-volume, generic keywords for discoverability.

- Use lowercase letters and hyphens only
- Follow category pattern: `[type]-page-generator` (pages), `[component]-generator` (components), industry terms (SEO)
- Be specific: `schema-markup` not `schema`; `pricing-page-generator` not `pricing`
- Platforms: add suffix (e.g. `twitter-x-posts`, `reddit-posts`)
- No abbreviations: `employee-generated-content` not `egc`; `generative-engine-optimization` not `geo`

**Full rules**: [skill-authoring §3.2](docs/skill-authoring.md#32-name-field-rules) | [reference-rules](docs/reference-rules.md) (references)

## Language

- **All skill content must be in English** — descriptions, instructions, examples, and output formats. This ensures consistency and broad agent compatibility.

## Description Best Practices

- Write in third person
- Include trigger terms (when users say X, Y, Z)
- Be specific about what the skill does
- Mention when to use vs. when to use related skills

**Full specification**: [skill-authoring §3.3](docs/skill-authoring.md#33-description-field-rules)

## Full Specification

See [skill-authoring.md](docs/skill-authoring.md) for the complete specification, frontmatter rules, and quality checklist.

## Testing

1. Install locally: `npx skills add . --skill your-skill-name`
2. Ask the agent to perform the task
3. Verify the skill is invoked correctly
