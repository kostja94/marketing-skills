---
name: use-cases-page-generator
description: When the user wants to create, optimize, or audit use case pages. Also use when the user mentions "use cases," "use case page," "for [industry]," "for [role]," "by persona," "ICP pages," or "audience-specific pages."
metadata:
  version: 1.0.0
---

# Pages: Use Cases

Guides use case pages that bridge product features and real-world customer problems. BOFU (bottom-of-funnel) pages for SaaS/B2B. Organize by ICP, industry, role, or scenario.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product, ICP, and proof points.

Identify:
1. **ICP**: Ideal Customer Profile; industries, roles, company size
2. **Pain points**: What problems does each segment have?
3. **Format**: Single page vs. per-use-case pages
4. **Primary goal**: Demo, sign up, contact sales

## Use Case Page Structure

| Section | Purpose |
|---------|---------|
| **Headline** | "For [industry/role]: solve X" |
| **Problem** | Pain points, day-to-day challenges |
| **Solution** | How product addresses them; specific features |
| **Proof** | Case study, testimonial, metrics |
| **CTA** | Try free, book demo, contact |
| **Related** | Link to other use cases, solutions |

## Best Practices

### Audience-Specific

- **One primary audience per page**: Don't mix "for marketers" and "for developers"
- **Tailored messaging**: Industry jargon, workflow references
- **Concrete scenarios**: "When you need to X, we help you Y"
- **Overcome objections**: Address doubts proactively

### Organization

- **By ICP**: Industry (Healthcare, Finance), role (Marketer, Developer), company size (SMB, Enterprise)
- **By scenario**: "Event marketing," "Customer support at scale"
- **Internal linking**: Use cases ↔ features ↔ solutions ↔ customer stories

### SEO

- **Intent**: Commercial; "X software for [industry]"
- **Title**: "For [Industry] | [Product]" or "[Product] for [Role]"
- **Differentiate**: Avoid copy-paste across industries; unique workflows, pain points

## Output Format

- **Use case list** (segments to cover)
- **Per-page structure** (sections, messaging)
- **Headline** options per segment
- **Internal linking** plan
- **SEO** metadata

## Related Skills

- **features-page-generator**: Features support use cases; link between
- **solutions-page-generator**: Solutions are outcome-focused; use cases are scenario-focused; often paired
- **customer-stories-page-generator**: Case studies as proof on use case pages
- **landing-page-generator**: Use case pages are a type of landing page; apply LP principles
- **pricing-page-generator**: Use case pages link to pricing
