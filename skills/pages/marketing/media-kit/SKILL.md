---
name: media-kit-page-generator
description: When the user wants to create, optimize, or audit media kit or press page. Also use when the user mentions "media kit," "press kit," "press page," "press resources," "brand assets," "logo download," "press assets," "media resources," or "brand kit." For PR outreach, use public-relations.
metadata:
  version: 1.0.1
---

# Pages: Media Kit

Guides media kit and press page content, structure, and accessibility for journalists. Media kits provide self-service brand assets; consistent presentation builds trust (companies with strong guidelines are 20% more valuable). **Distinct from press-coverage-page-generator**: Media kit = assets for journalists; press coverage = aggregation of third-party mentions for visitor trust.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for company story, metrics, key messages, and Section 12 (Visual Identity).

Identify:
1. **Audience**: Journalists, bloggers, analysts
2. **Update frequency**: Before launches, events, announcements
3. **Assets**: Logos, brand guidelines, favicon, photos, videos

## Best Practices

### Essential Elements

**Evergreen content:**
- Company overview (background, mission, origin)
- Key team bios and headshots
- High-res logos (multiple sizes, light/dark backgrounds, transparent PNG)
- Brand guidelines document (typography, colors, logo usage)
- Key statistics (customers, growth, metrics)

**Regularly updated:**
- Recent press releases
- Product photos and video clips
- Link to press coverage page (or "As Seen In" section) for media mentions
- Contact for press inquiries

**Note**: Press coverage (third-party mentions) is often a separate page or section. See **press-coverage-page-generator** for aggregating "As Seen In" / "In the News" content.

### Logo Assets (per Alignify-style media kit)

| Asset | Format | Use |
|-------|--------|-----|
| **Main logo** | PNG, SVG; light and dark bg | Primary branding |
| **Icon** | PNG; light and dark bg | Favicon, social, compact use |
| **Brand pattern** | PNG | Visual identity element |
| **Brand guidelines** | PDF or PNG | Typography, colors, usage rules |

### Usage Guidelines

**Allowed**: Media coverage, blog posts, social sharing, product comparisons, educational use. Assets free to download without additional authorization.

**Requirements**: Maintain logo proportions and colors; ensure adequate white space; do not use in contexts that harm brand. For commercial or special use, contact for authorization.

### Media Assets

| Asset | Format |
|-------|--------|
| **Logos** | PNG (transparent), SVG; horizontal and square |
| **Photos** | High-res; horizontal for web, square for social |
| **Videos** | Product demos, interviews |
| **Credits** | Photo credits, usage rights |

### Structure

- **Dedicated page**: Press/Media section on website
- **Self-service**: Journalists find what they need without emailing
- **Concise**: 3-4 pages typical; each element adds value
- **Downloadable**: ZIP or individual asset downloads

### Timing

- **Update before**: Launches, events, announcements
- **Keep current**: Stale info damages credibility

### Placement

- **Discoverable**: Link in footer, About, or dedicated Press section
- **Clear label**: "Press," "Media Kit," "For Journalists"

## Output Format

- **Structure** outline
- **Asset** checklist (logos, brand guidelines, favicon, photos, bios)
- **Copy** for company overview
- **Usage guidelines** (allowed, requirements)
- **Contact** for press inquiries
- **SEO**: Often noindex; or index for "company name press" queries

## Related Skills

- **press-coverage-page-generator**: Aggregation of third-party coverage ("As Seen In"); media kit can link to it; distinct (media kit = assets for journalists; press coverage = social proof for visitors)
- **about-page-generator**: Media kit extends About for press
- **contact-page-generator**: Press contact info
- **customer-stories-page-generator**: Press may reference case studies
- **logo-generator**: Logo assets, placement rules; media kit hosts logo files
- **favicon-generator**: Favicon for browser/app; media kit can link or include
- **brand-visual-generator**: Typography, colors, spacing; brand guidelines document
- **indexing**: noindex vs. index for press page
- **directory-submission**: Media kit required for Product Hunt and directory submissions
