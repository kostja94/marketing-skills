---
name: landing-page-generator
description: When the user wants to create, optimize, or audit campaign landing pages for paid ads, email, or other traffic. Also use when the user mentions "landing page," "PPC landing page," "SEM landing page," "conversion page," "campaign page," "lead capture page," "landing page optimization," "LP conversion," "single-page funnel," or "squeeze page." Not for the main site homepage; use homepage-generator.
metadata:
  version: 1.4.0
---

# Pages: Landing Page

Guides campaign landing page structure, conversion flow, and optimization. **Primary use**: **Paid ads (PPC/SEM)** — landing pages are typically built to receive paid traffic; ad-to-page alignment is critical for conversion. See **paid-ads-strategy** for when to use paid ads and ad-to-page alignment principles. Also applies to affiliate signup, product launch, lead capture, webinar registration, and other single-goal conversion pages. **Scale**: When building many landing pages (city-specific, product-specific, integration-specific), use **programmatic-seo** (template + data) and **template-page-generator** for template design. Differs from homepage (multi-purpose) and product pages (catalog).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Paid Ads: LP Requirements

When LP receives paid traffic: ad promise on page immediately; mobile-first (CTA above fold, fast load); minimal form (fewer fields); trust above fold. See **paid-ads-strategy** for full ad-to-page alignment and Quality Score.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, audience, and value proposition.

Identify:
1. **Page goal**: Signup, purchase, lead capture, webinar, download
2. **Traffic source**: Paid ads, email, affiliate, organic
3. **Audience**: Cold vs warm; segment if known

## Landing Page Structure (5-Step Flow)

| Step | Purpose | Elements |
|------|---------|----------|
| **1. Stop the scroll** | Capture attention in ~2.6 seconds | Headline, subheadline, hero image or video |
| **2. Earn trust** | Social proof before the ask | Logos, testimonials, ratings, customer count |
| **3. Explain value** | Benefits, features, use cases | Clear copy; who it's for, what it does |
| **4. Remove doubt** | Objection handling | FAQ, guarantees, comparison |
| **5. Make the ask** | Single primary CTA | One clear action; repeat at logical points |

Every element should serve one of these five functions. Pages with multiple competing offers get ~266% fewer leads.

## Headline Formula

**[Who it's for]** + **[Specific outcome]** + **[Time/qualifier]**

- **Avoid**: Abstract promises ("Unlock your potential," "Transform your business")
- **Prefer**: Concrete ("Cut invoice processing by 70%—without new software")

## CTA Best Practices

- **One primary CTA**: No competing actions; create a "one-way street" toward conversion
- **Above the fold on mobile**: Thumb-reachable; ~65%+ traffic is mobile
- **Value-focused copy**: "Start Free Trial" not "Submit"
- **Pair with trust signals**: Customer count, logos, or stats next to the button
- **Remove or minimize navigation**: Can increase conversion 2–28%

## Programmatic Landing Pages (Scale)

When you need **many landing pages** (e.g., city-specific, product-specific, integration-specific), use **programmatic-seo**: one template + data = hundreds or thousands of LPs. Apply landing page structure (5-step flow, CTA, trust) to the template; see **template-page-generator** for template design. Example: "[Product] for [City]" LPs with local data; "[App A] + [App B]" integration signup pages.

## Page Types

| Type | Use | CTA Destination |
|------|-----|-----------------|
| **Click-through** | Warm audience before sending to offer; best for SaaS, subscriptions | pricing-page, products-page, signup |
| **Lead capture** | Collect email for nurture; forms 5 fields or fewer (longer forms cause ~81% abandonment) | newsletter-signup, contact-page |
| **Product-focused** | Deep-dive features and benefits; product launch | products-page, features-page |
| **Comparison** | X vs Y; competitor brand keyword ads; commercial intent | alternatives-page, features-page, pricing-page |
| **Use cases / Solutions** | For integrated products hard to split into tools | features-page, services-page |
| **Free tools** | Standalone utilities; lead gen; same ICP; excerpt from product | tools-page-generator; tool page as LP when gated |
| **Bridge/bonus** | Extra incentive to purchase through your link | pricing-page, products-page |
| **Webinar/event** | Event registration; collect signups before live | resources-page (webinar as resource) |

## Landing Page ↔ Page Types (Content & Flow)

**Pull content from** (step 2–4):
- **customer-stories-page-generator**: Testimonials, case studies for social proof; Challenge→Solution→Results snippets
- **faq-page-generator**: Objection-handling FAQ section; reuse conversion-related Q&A
- **features-page-generator**: Benefit-first feature copy for "Explain value" step
- **resources-page-generator**: Lead magnet (ebook, template) as exchange for email; webinar as resource

**CTA sends to**:
- **pricing-page-generator**: Click-through LP → pricing; signup, trial
- **products-page-generator**: Product LP → product detail or catalog
- **services-page-generator**: Service LP → contact, quote, booking
- **contact-page-generator**: Lead capture LP → contact form; B2B demo request
- **affiliate-page-generator, creator-program**: Partner signup = landing page type

**Internal linking**:
- Link LP to **homepage** (brand anchor); **about-page** (trust); **privacy-page** (form compliance)
- Avoid orphan LPs: ensure at least one internal link from sitemap, nav, or campaign hub

## Performance and Design

- **Load time**: Under 2.5 seconds; each extra second can cost ~7% conversion
- **Mobile-first**: Responsive; CTA visible without scrolling
- **Visuals**: Hero image or video can improve conversion up to 80%
- **Frontend aesthetics**: For distinctive typography, motion, spatial composition, backgrounds—see **brand-visual-generator** Frontend Aesthetics
- **Disclosure**: FTC-compliant affiliate/paid disclosure when applicable

## Pre-Delivery Checklist

Before shipping a landing page, verify:

| Category | Check |
|----------|-------|
| **Visual** | No emojis as icons (use SVG); icons from consistent set (Heroicons/Lucide); hover states don't cause layout shift |
| **Interaction** | All clickable elements have `cursor-pointer`; hover provides clear feedback; transitions 150–300ms |
| **Accessibility** | Images have alt text; form inputs have labels; color not sole indicator; `prefers-reduced-motion` respected |
| **Layout** | No horizontal scroll on mobile; content not hidden behind fixed nav; responsive at 375px, 768px, 1024px |
| **Performance** | Load time under 2.5s; LCP optimized; images use WebP/lazy loading where appropriate |
| **Images** | See **image-optimization** for alt, format, responsive, lazy loading |

## Output Format

- **Headline** and subheadline
- **Structure** (5-step flow sections)
- **Trust signals** placement
- **CTA** copy and placement
- **Objection handling** (FAQ, guarantees)
- **Internal links** (destination pages)
- **SEO** metadata (if page is indexed)

## Related Skills

- **hero-generator**: Hero section (step 1)
- **grid, list**: Content layout below hero; sections, features, testimonials
- **cta-generator**: CTA button design and placement
- **image-optimization**: Alt, WebP, LCP, responsive, lazy loading
- **pricing-page-generator**: Click-through LP destination; signup CTA
- **faq-page-generator**: Objection-handling FAQ section
- **homepage-generator**: Multi-purpose home vs single-goal landing; similar structure
- **paid-ads-strategy**: Ad-to-page alignment; when to use paid ads
- **alternatives-page-generator**: Competitor brand keyword ads → comparison LP (not blog)
- **programmatic-seo**: Scale landing pages via template + data
- **template-page-generator**: Template structure for programmatic LPs
- **title-tag, meta-description, page-metadata**: Landing page metadata
