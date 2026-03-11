---
name: pricing-page-generator
description: When the user wants to create, optimize, or audit pricing page content and structure. Also use when the user mentions "pricing page," "pricing table," "plans," "subscription," "pricing plans," "pricing tiers," "pricing comparison," "SaaS pricing," "enterprise pricing," "API pricing," "contact sales," "pricing in nav," "public pricing," "hide pricing," or "pricing objection handling."
metadata:
  version: 1.2.0
---

# Pages: Pricing

Guides pricing page content, structure, and conversion optimization. Covers self-serve plans, enterprise/contact sales, API/usage-based pricing, and special programs (startups, education).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, audience, and pricing strategy.

Identify:
1. **Pricing model**: Subscription, one-time, usage-based, freemium, hybrid
2. **Plans**: Number of tiers, differentiation; enterprise vs self-serve
3. **Primary goal**: Sign up, contact sales, trial
4. **Objections**: Price sensitivity, "which plan?" confusion
5. **Special programs**: Startups, education, nonprofit (link or embed)
6. **Visibility**: Public page vs contact-sales-only; marketing site vs in-app

## Pricing Visibility & Placement

### Public vs Hidden Pricing

| Show public pricing | Hide (contact sales only) |
|--------------------|---------------------------|
| Self-serve / SMB; standard tiers | Enterprise; highly customized |
| Competitive market; transparency differentiates | Premium positioning; consultative sales |
| Simple pricing model | New category; value exceeds cost in prospect's mind |
| 86% of B2B buyers want transparency; hidden pricing is a top deterrent | Custom deployments, SLA, volume; fixed price misleading |

**Middle ground**: "Starting from," price ranges, or calculator—clarity without rigid commitment.

### Where Pricing Lives

| Location | Audience | Purpose |
|----------|----------|---------|
| **Marketing site** | Unlogged visitors | Acquisition; standalone /pricing page; main nav or footer |
| **In-app / Dashboard** | Logged-in users | Subscription management; Settings → Billing/Subscription in sidebar; upgrade/downgrade, payment |

**Marketing site** = conversion; **In-app billing** = retention and plan management. Not all sites need public pricing in nav—enterprise-only products may use "Contact sales" as primary CTA.

## Pricing Models

| Model | Use |
|-------|-----|
| **Subscription** | Recurring; monthly/annual; most SaaS |
| **Freemium** | Free tier + paid; adoption then conversion |
| **Usage-based** | Pay per use; API calls, tokens, credits |
| **One-time** | Perpetual license; some tools |
| **Hybrid** | Base + usage; tiered + overage |

## Pricing Page Structure

| Section | Purpose |
|---------|---------|
| **Headline** | Value-focused; "Simple pricing" or benefit-led |
| **Pricing model selector** | Monthly/annual toggle; show annual savings (15–25%); usage-based calculator if applicable |
| **Plan comparison** | Clear table or cards; feature comparison; "Best for" per tier |
| **Enterprise / Contact sales** | Separate tier; "Contact us," "Custom pricing"; SLA, dedicated support; volume discount |
| **API / Usage pricing** | If API product: token/request pricing; tiers (Standard/Flex/Batch); overage; link to /api or docs |
| **Special programs** | Startups, education, nonprofit; link to startups-page or embed block |
| **FAQ** | Billing, cancellation, refunds, API limits, enterprise |
| **Social proof** | Testimonials, logos, "X companies trust us" |
| **CTA** | Per plan or unified "Get started"; "Contact sales" for enterprise |
| **Guarantee** | Money-back, free trial, no credit card |
| **Comparison** | Brief price vs alternatives; link to alternatives-page |

## Best Practices

### Plan Presentation

- **Tier design**: 2–4 tiers; avoid too many options; 3 tiers optimal (decoy effect)
- **Anchoring**: Lead with mid-tier or annual discount; anchor high to make mid-tier feel reasonable
- **Decoy effect**: Middle tier as "Goldilocks" choice; "Most popular" or "Best value" badge
- **Differentiation**: Clear "best for" per tier; value metric (seats, API calls, projects)
- **Feature clarity**: What's included; outcome-first ("Save 10 hours/week") over feature-first ("Advanced API"); avoid vague "Advanced features"
- **Price display**: Monthly vs annual; show savings explicitly
- **Comparison**: Help user choose (quiz, comparison table)

### Usage-Based & Credits

- **Consumption visibility**: Show credits/usage clearly; avoid "bill shock" from opaque consumption
- **Wording**: Avoid vague "Unlimited" if soft limits exist; use "Extended" or state limits explicitly

### Enterprise & API Pricing

| Scenario | Use |
|----------|-----|
| **Enterprise** | Separate tier; "Contact sales," "Custom pricing"; SLA, dedicated support, volume discount |
| **API / Usage-based** | Token/request pricing; tier (Standard/Flex/Batch); overage; link to api-page or docs |
| **Hybrid** | Base subscription + usage; show base + overage clearly |

### Conversion Psychology

- **Anchor high**: Present highest tier first; mid-tier feels more reasonable
- **Loss aversion**: Money-back, no CC trial, cancel anytime—reduce perceived risk
- **Transparency**: No hidden fees; 73% of users value transparent pricing
- **Trust signals**: Logo, testimonial, "X+ companies"; guarantee near CTA

### Objection Handling

- **Price**: ROI, cost per use, comparison to alternatives
- **Commitment**: Free trial, no CC, cancel anytime
- **Uncertainty**: Guarantee, case studies, support

### Promo & Discounts

- **Annual discount**: Highlight 15–25% for annual prepay
- **Promo placement**: Top banner or promo block on page; see **top-banner-generator**
- **Startups/Education**: Link to startups-page or education-program page; or "Special plans" block on pricing page. When discount applies at registration, registration flow is P0; pricing page is P1. See **education-program** for placement priority.

### SEO

- Title: "Pricing | [Product]" or "Plans & Pricing"
- Meta: Include price range or "Start free" if applicable
- Schema: Consider Product/Offer structured data

## Output Format

- **Visibility** (public page vs contact-sales-only; marketing nav vs in-app billing)
- **Headline** options
- **Pricing model** (Subscription/Usage-based/Hybrid)
- **Plan structure** (tiers, features, pricing display; include Enterprise, API if applicable)
- **Special programs** (Startups/Education link or block)
- **API/Usage** display (if applicable)
- **Anchoring** and **Decoy** approach
- **FAQ** topics and sample answers (billing, API limits, enterprise, refund)
- **CTA** copy per plan
- **Objection handling** copy
- **SEO** metadata

## Related Skills

- **pricing-strategy**: Base price structure, tier design, anchoring; pricing-page is execution
- **discount-marketing-strategy**: Promotional pricing, annual discount, seasonal campaigns
- **api-page-generator**: API pricing, usage-based limits; developer audience
- **education-program**: Student/education discount channel; placement (registration P0, pricing P1)
- **startups-page-generator**: Special plans; Startups/Education discount; link from pricing
- **services-page-generator**: Service tiers; contact sales; custom quote
- **alternatives-page-generator**: Price comparison; competitor comparison
- **landing-page-generator**: Click-through landing pages often send to pricing; LP CTA destination
- **homepage-generator**: Homepage links to pricing
- **website-structure**: Page priority; when pricing belongs in nav vs contact-sales-only
- **features-page-generator**: Features inform plan differentiation
- **top-banner-generator**: Promo banner; discount code display
- **schema-markup**: Product/Offer schema for pricing
