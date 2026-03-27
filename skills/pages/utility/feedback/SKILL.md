---
name: feedback-page-generator
description: When the user wants to create, optimize, or audit a feedback or roadmap page. Also use when the user mentions "feedback page," "roadmap," "feature requests," "vote on features," "Canny," "UserVoice," or "product feedback." For sitewide page planning, use website-structure.
metadata:
  version: 1.0.1
---

# Pages: Feedback / Roadmap

Guides feedback and roadmap pages that collect user input and communicate product direction. Often integrates with Canny, FeatureBase, UserVoice, or similar. Supports product-led growth and community engagement.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product and roadmap priorities.

Identify:
1. **Tool**: Canny, FeatureBase, UserVoice, custom, or embedded form
2. **Scope**: Feedback only, roadmap only, or both
3. **Primary goal**: Collect requests, show transparency, build community
4. **Audience**: Users, prospects, or both

## Page Structure

| Section | Purpose |
|---------|---------|
| **Headline** | "Share Your Ideas" or "Product Roadmap" |
| **Value** | We listen; your input shapes the product |
| **Feedback** | Form or embed; categories (feature, bug, other) |
| **Roadmap** | In progress, planned, completed; or link to external board |
| **Process** | How we prioritize; what happens after you submit |
| **CTA** | Submit idea, vote, view roadmap |

## Best Practices

### Feedback Collection

- **Low friction**: Few fields; optional details
- **Categories**: Feature request, Bug, General
- **Duplicate detection**: "Similar ideas" to merge votes

### Roadmap Display

- **Status**: In progress, planned, completed
- **Transparency**: Don't over-promise; "Exploring" vs "Committed"
- **Update regularly**: Stale roadmap hurts trust

### Integration

- **Embed**: Canny, FeatureBase embed on your domain
- **Or link**: /feedback → feedback.yourproduct.com
- **SEO**: Often noindex for external boards; index if on your site

## Output Format

- **Headline** and value proposition
- **Page structure** (feedback + roadmap sections)
- **Process** copy (how we use feedback)
- **Integration** notes (Canny, etc.)
- **SEO** (index vs noindex)

## Related Skills

- **docs-page-generator**: Feedback process in docs
- **contact-page-generator**: Alternative for simple feedback
- **changelog-page-generator**: Completed roadmap items → changelog
