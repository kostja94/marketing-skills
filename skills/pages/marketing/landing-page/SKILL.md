---
name: landing-page-generator
description: When the user wants to create, optimize, or audit campaign landing pages. Also use when the user mentions "landing page," "landing page design," "conversion page," "campaign page," "lead capture page," "landing page optimization," "LP conversion," "single-page funnel," or "squeeze page."
metadata:
  version: 1.0.0
---

# Pages: Landing Page

Guides campaign landing page structure, conversion flow, and optimization. Applies to affiliate signup, product launch, lead capture, webinar registration, and other single-goal conversion pages. Differs from homepage (multi-purpose) and product pages (catalog).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product, audience, and value proposition.

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

## Page Types

| Type | Use | CTA Destination |
|------|-----|-----------------|
| **Click-through** | Warm audience before sending to offer; best for SaaS, subscriptions | pricing-page, products-page, signup |
| **Lead capture** | Collect email for nurture; forms 5 fields or fewer (longer forms cause ~81% abandonment) | newsletter-signup, contact-page |
| **Product-focused** | Deep-dive features and benefits; product launch | products-page, features-page |
| **Comparison** | X vs Y; commercial intent | features-page, pricing-page |
| **Use cases / Solutions** | For integrated products hard to split into tools | features-page, services-page |
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
- **Disclosure**: FTC-compliant affiliate/paid disclosure when applicable

## Output Format

- **Headline** and subheadline
- **Structure** (5-step flow sections)
- **Trust signals** placement
- **CTA** copy and placement
- **Objection handling** (FAQ, guarantees)
- **Internal links** (destination pages)
- **SEO** metadata (if page is indexed)

## Related Skills

### Pages (destination & content)

- **affiliate-page-generator**: Affiliate signup; apply landing page principles
- **pricing-page-generator**: Click-through LP destination; signup CTA
- **products-page-generator**: Product LP destination; product launch
- **features-page-generator**: Value/benefits content for product LP
- **customer-stories-page-generator**: Testimonials, case studies for social proof
- **faq-page-generator**: Objection-handling FAQ section
- **resources-page-generator**: Lead magnet, webinar; lead capture LP
- **services-page-generator**: Service LP; CTA to contact/quote
- **contact-page-generator**: Lead capture LP form; demo request
- **homepage-generator**: Multi-purpose home vs single-goal landing; similar structure
- **about-page-generator**: LP can link to About for trust
- **privacy-page-generator**: LP form compliance; link near form
- **creator-program**: Creator signup; similar to affiliate

### Components

- **hero-generator**: Hero section (step 1)
- **cta-generator**: CTA button design and placement
- **testimonials-generator, trust-badges-generator**: Social proof (step 2)
- **newsletter-signup-generator**: Lead capture form on LP
- **popup-generator**: Lead capture popup alternative to full-page form

### SEO

- **title-tag, meta-description, page-metadata**: Landing page metadata
