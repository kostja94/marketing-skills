---
name: solutions-page-generator
description: When the user wants to create, optimize, or audit solutions pages. Also use when the user mentions "solutions," "solutions page," "by industry," "industry solutions," "by company size," "SMB," "enterprise," "by outcome," "business outcomes," or "how we solve X." For sitewide page planning, use website-structure.
metadata:
  version: 1.1.1
---

# Pages: Solutions

Guides solutions pages focused on business outcomes. **Industry-first** is the B2B norm (Salesforce, HubSpot). Answer "what outcome do I get for my industry/team/size?" rather than "what does it do?" Distinct from features (capabilities) and use cases (scenarios); solutions emphasize measurable value by segment.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, outcomes, and proof points.

Identify:
1. **Outcomes**: Revenue growth, cost savings, efficiency, compliance
2. **Segments**: Industry (primary), company size, team
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
| **Related** | Other solutions, use cases (as sub-applications) |

## Best Practices

### Outcome-First

- **Lead with result**: "Increase conversion by 30%" not "We have A/B testing"
- **Measurable**: Time saved, revenue gained, cost reduced
- **Specific**: Industry workflows, not generic claims
- **Differentiate**: Each industry/segment gets unique content

### Organization (Primary → Secondary)

| Dimension | Priority | Examples |
|-----------|----------|----------|
| **By Industry** | Primary | Healthcare, Retail, Manufacturing, Financial Services |
| **By Company Size** | Secondary | SMB, Mid-Market, Enterprise |
| **By Team** | Secondary | Marketing, Sales, Service, Operations |
| **By Outcome** | Alternative | Scale support, Reduce churn, Accelerate sales |

### Common Industries (Reference)

Automotive, Communications, Consumer Goods, Consumer Services, Construction & Real Estate, Education, Energy & Utilities, Financial Services, Government, Healthcare & Life Sciences, Manufacturing, Media, Nonprofit, Professional Services, Retail, Technology, Travel & Hospitality.

### Company Size Segments

| Size | Typical | Focus |
|------|---------|-------|
| Startup | <50 | Speed, agility |
| SMB | 50–500 | Ease of use, affordability |
| Mid-Market | 500–5000 | Scalability |
| Enterprise | 5000+ | Customization, compliance, integration |

### vs. Use Cases vs. Features

| Page | Answers | Primary Organization |
|------|---------|----------------------|
| **Features** | What does it do? | Capabilities |
| **Use cases** | When would I use it? | By scenario, persona, business goal |
| **Solutions** | What outcome do I get? | By industry, company size, team |

**Hierarchy**: Solutions (industry/segment) can contain Use Cases as sub-applications. Example: /solutions/healthcare → use cases: patient scheduling, telemedicine.

### When to Use Solutions vs Use Cases

| Need | Use |
|------|-----|
| By industry (Healthcare, Retail) | Solutions |
| By company size (SMB, Enterprise) | Solutions |
| By team (Marketing, Sales) | Solutions |
| By outcome (Scale support) | Solutions |
| By scenario (Event marketing) | Use Cases |
| By persona (For Realtors, For CMOs) | Use Cases |
| By business goal (Acquisition, Retention) | Use Cases |
| Industry-specific application | Use Cases (as Solutions sub-page) |

## Output Format

- **Solutions list** (industries/segments)
- **Per-page structure** (sections, messaging)
- **Headline** options
- **Proof** integration (case studies, metrics)
- **Internal linking** (features, use cases, pricing)
- **SEO** metadata

## Related Skills

- **use-cases-page-generator**: Use cases as sub-applications under solutions; link between
- **features-page-generator**: Solutions reference features; link to feature pages
- **customer-stories-page-generator**: Case studies as proof on solutions pages
- **pricing-page-generator**: Solutions pages link to pricing
- **landing-page-generator**: Solutions pages apply LP principles
