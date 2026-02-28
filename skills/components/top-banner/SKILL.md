---
name: components-top-banner
description: When the user wants to add, optimize, or audit a top announcement bar or sticky banner. Also use when the user mentions "announcement bar," "top banner," "sticky bar," "promo banner," or "header banner."
metadata:
  version: 1.0.0
---

# Components: Top Banner (Announcement Bar)

Guides top announcement bar and sticky banner design for conversion. Top banners answer visitor questions in ~3 seconds (trust, discount, free shipping, urgency) and can increase coupon redemption by 30-50% when used well.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for offers, messaging, and Section 12 (Visual Identity).

Identify:
1. **Goal**: Lead capture, promo, urgency, trust, free shipping
2. **Placement**: Above header (sticky) or below; dismissible or persistent
3. **Audience**: All visitors vs segmented (geo, returning, cart abandoners)

## Best Practices

### Use Cases

| Use | Example |
|-----|---------|
| **Lead capture** | Newsletter, lead magnet, demo request |
| **Promo** | Discount code, flash sale, free shipping threshold |
| **Urgency** | Limited-time offer, countdown |
| **Trust** | Guarantee, security, shipping info |
| **Launch** | Product launch, event, cross-sell |

### Design

- **Clear hierarchy**: Message + CTA in ~400ms "blink test"
- **Minimal copy**: One line typical; link for "Learn more"
- **High contrast**: Stand out from page; CTA color distinct
- **Mobile-first**: 70%+ traffic on mobile; thumb-friendly close/CTA

### Technical

- **Desktop**: 1920x600px keeps content above fold; 16:9 common
- **Mobile**: 800x1200px (2:3 portrait); use separate assets, not scaled
- **Performance**: Optimize images; oversized banners hurt LCP and SEO

### Avoid

- Crowding the header; leave space for nav and logo
- Too many CTAs; one primary action
- Stale messaging; refresh every 2-4 weeks

## Output Format

- **Message** and CTA copy
- **Placement** (sticky top, below header)
- **Targeting** (all vs segment)
- **Design** notes (contrast, mobile)

## Related Skills

- **components-cta**: Banner CTA design
- **components-newsletter-signup**: Lead capture in banner
- **components-brand-visual**: Colors, typography for banner
- **components-navigation-menu**: Banner sits above or integrates with nav
