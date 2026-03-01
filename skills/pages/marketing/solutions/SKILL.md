---
name: solutions-page-generator
description: When the user wants to create, optimize, or audit solutions pages. Also use when the user mentions "solutions," "solutions page," "by industry," "by outcome," "business outcomes," or "how we solve X."
metadata:
  version: 1.0.0
---

# Pages: Solutions

Guides solutions pages focused on business outcomes. Answer "how does this solve my problem?" rather than "what does it do?" Distinct from features (capabilities) and use cases (scenarios); solutions emphasize measurable value.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product, outcomes, and proof points.

Identify:
1. **Outcomes**: Revenue growth, cost savings, efficiency, compliance
2. **Segments**: Industry, team, function
3. **Format**: Hub + per-solution pages, or single solutions page
4. **Primary goal**: Demo, sign up, contact

## Solutions Page Structure

| Section | Purpose |
|---------|---------|
| **Headline** | Outcome-led; "Achieve X with [Product]" |
| **Challenge** | Business problem, context |
| **Solution** | How product delivers the outcome |
| **Proof** | Metrics, case study, ROI |
| **Features used** | Link to relevant features |
| **CTA** | Book demo, start trial, see case study |
| **Related** | Other solutions, use cases |

## Best Practices

### Outcome-First

- **Lead with result**: "Increase conversion by 30%" not "We have A/B testing"
- **Measurable**: Time saved, revenue gained, cost reduced
- **Specific**: Industry workflows, not generic claims
- **Differentiate**: Each industry/segment gets unique content

### Organization

- **By industry**: Healthcare, Finance, Retail — each with distinct workflows
- **By team**: Marketing, Sales, Support
- **By outcome**: "Scale support," "Reduce churn," "Accelerate sales"
- **Avoid duplication**: Don't copy-paste; tailor to segment

### vs. Use Cases vs. Features

| Page | Answers | Focus |
|------|---------|-------|
| **Features** | What does it do? | Capabilities |
| **Use cases** | When would I use it? | Scenarios, personas |
| **Solutions** | What outcome do I get? | Business value, ROI |

## Output Format

- **Solutions list** (outcomes/segments)
- **Per-page structure** (sections, messaging)
- **Headline** options
- **Proof** integration (case studies, metrics)
- **Internal linking** (features, use cases, pricing)
- **SEO** metadata

## Related Skills

- **use-cases-page-generator**: Use cases and solutions often paired; link between
- **features-page-generator**: Solutions reference features; link to feature pages
- **customer-stories-page-generator**: Case studies as proof on solutions pages
- **pricing-page-generator**: Solutions pages link to pricing
- **landing-page-generator**: Solutions pages apply LP principles
