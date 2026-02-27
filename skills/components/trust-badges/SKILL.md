---
name: components-trust-badges
description: When the user wants to add or optimize trust badges, "Trusted by" logos, security seals, or social proof elements. Also use when the user mentions "trust badges," "trusted by," "security badges," "payment logos," or "social proof."
metadata:
  version: 1.0.0
---

# Components: Trust Badges

Guides trust badge design and placement for conversion. Trust badges borrow authority from third-party organizations to signal legitimacy and reduce purchase anxiety.

**When invoking**: On **first use**, if helpful, open with 1?2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for key partners and certifications.

Identify:
1. **Site type**: E-commerce, SaaS, lead gen
2. **Available badges**: Security, payment, reviews, guarantees
3. **Placement goals**: Hero, checkout, product pages

## Badge Types & Impact

| Type | Best Placement | Conversion Impact |
|------|----------------|-------------------|
| **Security** (SSL, Norton, McAfee) | Checkout, payment forms | +15??0% for unfamiliar brands |
| **Payment logos** (Visa, PayPal, Stripe) | Checkout, cart | +8??2% trust |
| **Money-back guarantee** | Product, checkout | +6??0% |
| **Reviews/ratings** (Trustpilot, BBB) | Product, hero | +12??8% |
| **Privacy/compliance** (GDPR, CCPA) | Forms, checkout | Data-sensitive transactions |

**"Trusted by" logos**: Client/customer logos in hero or footer; social proof for B2B.

## Best Practices

### Quantity

- **3?? badge types max**; more can cause "badge bloat" and reduce conversions by 5??%
- Quality over quantity; use only legitimate, verifiable badges

### Placement

- **Highest leverage**: Cart and checkout (near payment fields)
- **Product pages**: Near add-to-cart button
- **Hero**: "Trusted by" logos for brand credibility
- **Footer**: Secondary trust signals

### Authenticity

- Use only real, verifiable badges
- Fake or irrelevant badges create skepticism
- Link to verification where appropriate

## Design Guidelines

- Consistent size and style; don't mix clashing visuals
- Adequate spacing; avoid clutter
- Grayscale or muted for "Trusted by" logos (don't compete with primary content)
- Ensure badges are recognizable at display size

## Accessibility

- Provide `alt` text for badge images (e.g., "Norton Secured")
- Don't rely on badges alone for critical information

## Output Format

- **Badge recommendations** by type and placement
- **Placement map** (hero, product, checkout)
- **Quantity** guidance (avoid bloat)

## Related Skills

- **components-hero**: "Trusted by" often in hero
- **components-testimonials**: Complementary social proof
- **components-cta**: Badges near CTAs increase conversion
- **pages-pricing**: Trust badges on pricing pages
