---
name: hero-generator
description: When the user wants to design, optimize, or audit hero sections (above-the-fold main visual area). Also use when the user mentions "hero," "hero section," "hero area," "above the fold," "above the fold content," "landing hero," "main banner," "banner section," "first fold," "hero section design," "hero conversion," "split layout hero," "centered hero," or "hero alignment." For homepage, use homepage-generator.
metadata:
  version: 1.2.1
---

# Components: Hero Section

Guides hero section design for conversion and first impressions. The hero is where users spend ~80% of initial viewing time; first impressions form in milliseconds.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for value proposition, audience, and Section 12 (Visual Identity).

Identify:
1. **Page type**: Homepage, landing, product, pricing
2. **Primary goal**: Signup, trial, purchase, learn more
3. **Platform**: Web, mobile, both

## Core Components (Four Essentials)

- **Headline (H1)**: 6–10 words max; instantly communicate core value and benefit. Answer "What's in it for me?" within seconds.
- **Subheading**: Clear, concise explanation reinforcing why the product/service is valuable.
- **Primary CTA**: Single, prominent action button visible without scrolling. One per hero to avoid choice overload.
- **Visual**: High-quality image, video, or animation that amplifies the message.

### Optional but Effective

- **Trust cues**: 1–3 elements (reviews, logos, statistics)
- **Secondary CTA**: For users not ready for primary action

## Layout Types

Hero is a **Spotlight layout**—single focus, primary element with secondary around it. Choose layout by content balance and conversion goal.

| Layout | Structure | Best for |
|--------|-----------|----------|
| **Split (50/50)** | Text left, visual right (or vice versa); equal weight | Product, SaaS; clear value + demo |
| **Split (75/25)** | Text dominant; smaller image column | Copy-heavy; trust-first |
| **Split (25/75 "Signpost")** | Small image beside primary content | Minimal visual; emphasis on headline |
| **Centered** | Text + CTA centered; visual full-width or stacked | Brand, landing; single CTA |
| **Full-width image** | Image background; overlay text | Emotional; lifestyle, brand |

**Responsive**: Split layouts stack vertically on mobile (text above image); centered maintains center. Mobile-first; ensure CTA above fold on small screens.

## Alignment

| Axis | Options | Use |
|------|---------|-----|
| **Horizontal** | Left, center, right | Left align for text-heavy; center for minimal |
| **Vertical** | Top, center, bottom | Center for full-viewport hero; top for short hero |

## Best Practices

### 3-Second Rule

The hero must answer three questions within 3 seconds: **What is this?** **Why should I care?** **What should I do next?** ~80% of users never scroll beyond the hero; make an immediate impact.

### Messaging

- No guessing required; message must be instantly clear.
- Single primary CTA to avoid choice overload.
- Action-oriented, benefit-focused copy.
- **Emotional intent first**: Evoke emotion (trust, excitement, confidence) before users read the headline. Avoid generic phrases ("Welcome to Our Website") or overly clever wordplay.

### Visuals

- Fast-loading; avoid heavy assets that delay LCP
- Brand-aligned; use typography and colors from brand-visual-generator
- Support the message; don't distract
- **Frontend aesthetics**: For motion (staggered reveals, hover), spatial composition, and backgrounds—see **brand-visual-generator** Frontend Aesthetics

### Technical

- Mobile-first design
- Lightweight for quick loading
- Ensure LCP (Largest Contentful Paint) optimization

## SEO Considerations

- Headline often contains `<h1>`; include primary keyword
- Hero content in initial HTML; avoid JS-only rendering. See **rendering-strategies**
- **Image optimization**: Alt text, format (WebP), LCP, responsive—see **image-optimization**

## UX Guidelines

### Hierarchy

- Headline > Subheading > CTA
- Visual should complement, not compete with, text

### Accessibility

| Requirement | Practice |
|-------------|----------|
| **Contrast** | Text over images: >=4.5:1; use overlay if needed |
| **Touch targets** | CTA >=44x44px |
| **Keyboard** | CTA keyboard-accessible; visible focus indicator |
| **Screen readers** | Proper heading order; image alt text; `aria-label` for icon-only buttons |
| **Reduced motion** | Respect `prefers-reduced-motion` for animations |
| **Interaction** | CTA has `cursor-pointer`; hover uses color/opacity (not scale) to avoid layout shift |

## Testing

- A/B test headline, CTA copy, and visuals
- Measure bounce rate, conversion rate, time to first interaction

## Output Format

- **Hero structure** (headline, subheading, CTA, visual)
- **Copy suggestions**
- **Technical** checklist (LCP, accessibility, image optimization)
- **Testing** recommendations

## Related Skills

- **card**: Hero vs card—hero is single above-fold; cards are repeated units in grid
- **grid**: Hero is one section; content below often uses grid (products, features)
- **cta-generator**: Hero typically contains primary CTA
- **trust-badges-generator**: Trust cues in hero
- **logo-generator**: Logo appears in hero context
- **brand-visual-generator**: Typography, colors, spacing for hero design
- **homepage-generator**: Hero is central to homepage design
- **landing-page-generator**: Hero is step 1 of landing page flow; campaign pages
- **image-optimization**: Hero image optimization (alt, WebP, LCP, responsive)
- **rendering-strategies**: Content in initial HTML; SSR/SSG for hero
