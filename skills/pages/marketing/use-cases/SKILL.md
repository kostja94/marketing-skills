---
name: use-cases-page-generator
description: When the user wants to create, optimize, or audit use case pages. Also use when the user mentions "use cases," "use case page," "for [role]," "by persona," "by scenario," "by business goal," "ICP pages," or "audience-specific pages." For sitewide page planning, use website-structure.
metadata:
  version: 1.2.1
---

# Pages: Use Cases

Guides use case pages that bridge product features and real-world customer problems. **Scenario-first** is the primary organization. BOFU (bottom-of-funnel) pages for SaaS/B2B. Answer "when would I use it?" and "how does it help me?" — distinct from solutions (industry/outcome).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, ICP, and proof points.

Identify:
1. **Scenarios**: Concrete situations (event marketing, lead nurturing)
2. **Personas**: Roles (Marketer, Sales Rep, Realtor)
3. **Business goals**: Acquisition, Retention, Upsell
4. **Format**: Single page vs. per-use-case pages; standalone or under solutions
5. **Primary goal**: Demo, sign up, contact sales

## Use Case Page Structure

| Section | Purpose |
|---------|---------|
| **Headline** | "When you need to X, we help you Y" or "For [role]: solve X" |
| **Problem** | Pain points, day-to-day challenges |
| **Solution** | How product addresses them; link to relevant features (do not duplicate feature copy) |
| **Proof** | Case study, testimonial, metrics |
| **CTA** | Try free, book demo, contact |
| **Related** | Link to other use cases, parent solution |

## Best Practices

### Scenario-First

- **Concrete situations**: "When you need to run event marketing at scale..."
- **Before-after**: Show transformation, not just features
- **One scenario per page**: Don't mix "event marketing" and "lead nurturing"

### Content Differentiation (vs Features)

- **Use case = scenario + problem + outcome**: Write the story (when, who, why, result); reference features via links.
- **Do not duplicate feature copy**: Avoid repeating capability lists or benefit bullets from the features page; instead, describe how the product solves this scenario and link to /features for details.
- **Avoid content cannibalization**: Each use case page targets a unique scenario intent; overlap with features (both Commercial/Consideration) dilutes SEO — differentiate by content angle (scenario vs capability).

### Organization (Primary → Secondary)

| Dimension | Priority | Examples |
|-----------|----------|----------|
| **By Scenario** | Primary | Event marketing, Lead nurturing, Churn prevention, Customer onboarding |
| **By Persona/Role** | Primary | For Realtors, For CMOs, For Sales Reps |
| **By Business Goal** | Secondary | Acquisition, Retention, Upsell/Cross-sell |
| **By Industry** | Secondary (ICP) | Use as ICP tag; or as sub-page under Solutions |

### Scenario Examples

Event marketing, Lead nurturing, Churn prevention, Customer onboarding, Patient scheduling, Telemedicine, Inventory management, Demand forecasting.

### Business Goal Examples

Acquisition (signups, trials), Retention (reduce churn, re-engagement), Upsell/Cross-sell (expand revenue).

### vs. Solutions vs. Features

| Page | Answers | Primary Organization |
|------|---------|----------------------|
| **Features** | What does it do? | Capabilities |
| **Solutions** | What outcome do I get? | By industry, company size, team |
| **Use cases** | When would I use it? | By scenario, persona, business goal |

**Hierarchy**: Use cases can be standalone or sub-pages under Solutions. Example: /solutions/healthcare/patient-scheduling (use case under industry solution).

### When to Use Use Cases vs Solutions

| Need | Use |
|------|-----|
| By scenario (Event marketing) | Use Cases |
| By persona (For Realtors, For CMOs) | Use Cases |
| By business goal (Acquisition, Retention) | Use Cases |
| By industry | Solutions |
| By company size (SMB, Enterprise) | Solutions |
| By team (Marketing, Sales) | Solutions |
| Industry-specific application | Use Cases (as Solutions sub-page) |

### Internal Linking

- Use cases ↔ features ↔ solutions ↔ customer stories
- If under a solution: link to parent solution; parent links to use cases

### SEO

- **Intent**: Commercial; "X software for [scenario]" or "[Product] for [role]"
- **Title**: "When to Use [Product] for [Scenario]" or "[Product] for [Role]"
- **Differentiate**: Unique workflows, pain points per scenario/persona

## Output Format

- **Use case list** (scenarios/personas to cover)
- **Per-page structure** (sections, messaging)
- **Headline** options per segment
- **Internal linking** plan (including parent solution if applicable)
- **SEO** metadata

## Related Skills

- **features-page-generator**: Features = what it does; use cases = when/how to use it; reference features via links, don't duplicate; see Content Differentiation above
- **solutions-page-generator**: Solutions are industry/outcome-focused; use cases are scenario-focused; use cases can be sub-pages under solutions
- **customer-stories-page-generator**: Case studies as proof on use case pages
- **landing-page-generator**: Use case pages are a type of landing page; apply LP principles
- **pricing-page-generator**: Use case pages link to pricing
