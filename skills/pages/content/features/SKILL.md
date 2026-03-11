---
name: features-page-generator
description: When the user wants to create, optimize, or audit features page content. Also use when the user mentions "features page," "product features," "capabilities," "what it does," "feature list," "feature comparison," "product capabilities," or "features section."
metadata:
  version: 1.1.0
---

# Pages: Features

Guides features page content, structure, and conversion optimization.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, differentiation, and proof points.

Identify:
1. **Feature set**: Core features, differentiators
2. **Audience**: Who evaluates features (buyer persona)
3. **Format**: Single page vs. per-feature pages
4. **Primary goal**: Demo, sign up, learn more

## Features Page Structure

| Section | Purpose |
|---------|---------|
| **Headline** | Benefit-led; "Everything you need to..." |
| **Feature grid/list** | Each feature: name, benefit, optional screenshot |
| **Use case links** | "For marketers," "For developers" |
| **Social proof** | Testimonials, logos |
| **CTA** | Try free, see demo, contact |

## Best Practices

### Benefit-First

- **Lead with benefit**: "Save 10 hours/week" not "Automated reporting"
- **Customer outcome**: What they get, not what it does
- **Specificity**: Numbers, examples, not vague claims

### Organization

- **By capability**: Group by product area or capability (e.g., Analytics, Automation, Integrations) — avoid organizing by use case to prevent overlap with use cases pages
- **By priority**: Most important/differentiating first
- **By journey**: Discovery -> evaluation -> decision

### Per-Feature Pages

- Use when features are substantial or rank separately
- Each page: feature name, benefit, how it works, proof
- Internal link from main features page

## SEO

- Title: "Features | [Product]" or "[Feature] | [Product]"
- H1: Main value; H2 per feature or section
- Schema: SoftwareApplication if applicable
- Internal links: To pricing, use cases, blog

### Avoid Overlap with Use Cases

- **Features = What**: Capability + benefit; no scenario narratives. Do not write "When you need to X..." — that belongs on use cases pages.
- **Link, don't duplicate**: Use "Use case links" (e.g., "For marketers," "For developers") to send users to use cases pages; do not replicate scenario content.
- **Content cannibalization**: Both target Commercial/Consideration; differentiate by angle (capability vs scenario) so each page serves unique intent.

## Output Format

- **Feature list** with benefit-first copy
- **Structure** (sections, order)
- **Headline** options
- **Per-feature** content (if separate pages)
- **SEO** metadata and schema

### vs. Tools

| Page | Purpose | Monetization |
|------|---------|--------------|
| **Features** | Paid product capabilities; conversion | Primary revenue |
| **Tools** | Free utilities; lead gen; excerpt from product | Not primary; drives signups |

See **tools-page-generator** for free tools pages.

## Related Skills

- **card**: Feature card structure; name, benefit, screenshot; grid/list layout
- **grid, list**: Feature grid or list layout
- **tools-page-generator**: Tools = free lead gen; features = paid capabilities; link from tools to product/features
- **use-cases-page-generator**: Features = what it does; use cases = when/how to use it; link between; avoid duplicating scenario content on features page
- **landing-page-generator**: Features content for product LP "Explain value" step; product LP links to features
- **url-slug-generator**: URL slug for per-feature pages (e.g. /features/feature-name); 3-5 words
- **homepage-generator**: Homepage links to features
- **pricing-page-generator**: Features inform plan tiers
- **schema-markup**: SoftwareApplication schema
- **heading-structure**: Feature page heading structure
