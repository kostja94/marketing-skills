---
name: top-banner-generator
description: When the user wants to add, optimize, or audit a top announcement bar or sticky banner. Also use when the user mentions "announcement bar," "top banner," "sticky bar," "promo banner," "discount banner," "student discount banner," "header banner," "announcement bar design," "sticky header," "promo bar," "urgency banner," or "lead capture bar." For promos, use discount-marketing-strategy.
metadata:
  version: 1.1.1
---

# Components: Top Banner (Announcement Bar)

Guides top announcement bar and sticky banner design for conversion. Top banners answer visitor questions in ~3 seconds (trust, discount, free shipping, urgency) and can increase coupon redemption by 30-50% when used well.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for offers, messaging, and Section 12 (Visual Identity).

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

### Discount Banner Types

| Discount Type | Banner Example | Related |
|---------------|----------------|---------|
| **Annual discount** | "Save 20% with annual billing" | discount-marketing-strategy |
| **Student/education** | "Students: 30% off today, 15% off ongoing" | education-program |
| **Startups/education** | "Startups: Special pricing — Apply now" | startups-page-generator |
| **BFCM / seasonal** | "Black Friday: 25% off — Use code BF25" | discount-marketing-strategy |
| **First-time** | "New users: 20% off first year" | discount-marketing-strategy |
| **Referral code** | "Get $10 off — Refer a friend" | referral-program |

**Placement**: Discount banner is P1 for student/education (homepage); pricing page also shows. See **education-program** for placement priority (registration P0, pricing P1, banner P1).

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

- **discount-marketing-strategy**: Promo/discount strategy; banner displays discount code; 30–50% redemption lift
- **education-program**: Student discount banner (P1 placement); "Students: X% off" copy
- **pricing-page-generator**: Discount banner supports pricing page; Special programs, promo placement
- **cta-generator**: Banner CTA design
- **newsletter-signup-generator**: Lead capture in banner
- **brand-visual-generator**: Colors, typography for banner
- **navigation-menu-generator**: Banner sits above or integrates with nav
