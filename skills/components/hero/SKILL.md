---
name: hero-generator
description: When the user wants to design, optimize, or audit hero sections (above-the-fold main visual area). Also use when the user mentions "hero," "hero section," "above the fold," "landing hero," or "main banner."
metadata:
  version: 1.0.0
---

# Components: Hero Section

Guides hero section design for conversion and first impressions. The hero is where users spend ~80% of initial viewing time; first impressions form in milliseconds.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for value proposition, audience, and Section 12 (Visual Identity).

Identify:
1. **Page type**: Homepage, landing, product, pricing
2. **Primary goal**: Signup, trial, purchase, learn more
3. **Platform**: Web, mobile, both

## Core Components

### Required

- **Headline**: Clear value proposition; answer "What's in it for me?" within seconds
- **Subheading**: Concise supporting context
- **Primary CTA**: Single, obvious button or link guiding to next step
- **Visual**: Image, video, or animation that supports the message

### Optional but Effective

- **Trust cues**: 1-3 elements (reviews, logos, statistics)
- **Secondary CTA**: For users not ready for primary action

## Best Practices

### Messaging

- No guessing required; message must be instantly clear
- Single primary CTA to avoid choice overload
- Action-oriented, benefit-focused copy

### Visuals

- Fast-loading; avoid heavy assets that delay LCP
- Brand-aligned; use typography and colors from brand-visual-generator
- Support the message; don't distract

### Technical

- Mobile-first design
- Lightweight for quick loading
- Ensure LCP (Largest Contentful Paint) optimization

## SEO Considerations

- Headline often contains `<h1>`; include primary keyword
- Hero content in initial HTML; avoid JS-only rendering
- Alt text for hero images

## UX Guidelines

### Hierarchy

- Headline > Subheading > CTA
- Visual should complement, not compete with, text

### Accessibility

| Requirement | Practice |
|-------------|----------|
| **Contrast** | Text over images: sufficient contrast or overlay |
| **Touch targets** | CTA >=44x44px |
| **Keyboard** | CTA keyboard-accessible |
| **Screen readers** | Proper heading order; image alt text |

## Testing

- A/B test headline, CTA copy, and visuals
- Measure bounce rate, conversion rate, time to first interaction

## Output Format

- **Hero structure** (headline, subheading, CTA, visual)
- **Copy suggestions**
- **Technical** checklist (LCP, accessibility)
- **Testing** recommendations

## Related Skills

- **cta-generator**: Hero typically contains primary CTA
- **trust-badges-generator**: Trust cues in hero
- **logo-generator**: Logo appears in hero context
- **brand-visual-generator**: Typography, colors, spacing for hero design
- **homepage-generator**: Hero is central to homepage design
