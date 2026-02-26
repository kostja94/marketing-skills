---
name: components-cta
description: When the user wants to design, optimize, or audit call-to-action (CTA) buttons. Also use when the user mentions "CTA," "call to action," "button design," "conversion button," or "primary action."
metadata:
  version: 1.0.0
---

# Components: Call-to-Action (CTA)

Guides CTA button design for conversion. A well-designed CTA can increase conversion by 25–30%.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for conversion goals.

Identify:
1. **Context**: Hero, form, pricing, product page
2. **User stage**: Awareness, consideration, decision
3. **Primary action**: Sign up, buy, trial, download

## Design Principles

### Visual Clarity

- **Look like buttons**: Background, border, corner radius, shadow
- **Stand out**: Contrasting color; clear hierarchy
- **Size**: ≥48×48px for touch; minimum 48px wide

### Hierarchy

- **Primary CTA**: One per section; impossible to miss
- **Secondary CTA**: Lower priority; visually distinct
- **Avoid**: Multiple competing CTAs causing choice overload

### Color & Shape

- **Color**: High contrast; red/orange for urgency
- **Shape**: Rounded = friendly; angled = dynamic
- **Accessibility**: ≥4.5:1 contrast for text

## Copy Best Practices

- **Action-oriented**: "Buy," "Sign up," "Subscribe," "Get started"
- **Loss aversion**: "Claim Your Discount Before It's Gone" vs "Get 10% Off"
- **Clear, no ambiguity**: User knows exactly what happens
- **Scarcity/urgency**: When appropriate; avoid overuse

## Placement

- **Above the fold** for primary actions
- **After value proposition**; build value before CTA
- **Near trust signals** (testimonials, badges)
- **Sticky/fixed** for long pages (use sparingly)

## Technical

- **Semantic HTML**: `<button>` or `<a>` with `role="button"` when needed
- **Visible focus state** for keyboard users
- **Loading state** for async actions (don't double-submit)

## Testing

- A/B test: color, copy, placement, size
- Measure: click-through rate, conversion rate

## Output Format

- **CTA copy** suggestions
- **Design** notes (color, size, hierarchy)
- **Placement** recommendations
- **Accessibility** checklist

## Related Skills

- **components-hero**: Hero typically contains primary CTA
- **components-testimonials**: Testimonials near CTAs boost conversion
- **components-trust-badges**: Badges near CTAs increase trust
- **pages-pricing**: CTA on pricing pages (e.g., "Start free trial")
