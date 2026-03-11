---
name: pricing-strategy
description: When the user wants to plan, design, or optimize pricing strategy and structure. Also use when the user mentions "pricing strategy," "pricing model," "pricing tiers," "freemium," "value-based pricing," "anchoring," "price structure," or "monetization strategy."
metadata:
  version: 1.0.0
---

# Strategies: Pricing

Guides pricing strategy and structure for SaaS, tools, and products. Covers pricing models, tier design, anchoring, and when to apply discounts. For pricing **page** content and layout, see **pricing-page-generator**. For **discount** and promotional pricing, see **discount-marketing-strategy**.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, value proposition, and competitors.

Identify:
1. **Product type**: SaaS, tool, e-commerce
2. **Value metric**: What drives value (seats, usage, features)
3. **Market**: Competitor pricing; willingness to pay
4. **Goals**: Revenue, adoption, retention

## Pricing Models

| Model | Use |
|-------|-----|
| **Subscription** | Recurring; monthly/annual; most SaaS |
| **Freemium** | Free tier + paid; adoption then conversion |
| **Usage-based** | Pay per use; API, credits |
| **One-time** | Perpetual license; some tools |
| **Hybrid** | Base + usage; tiered + overage |

**Variable-cost products** (compute, API, AI): When per-user cost varies widely (heavy users cost 10×+ light users), uniform subscription often fails. Use usage-based, credits, or tiered-by-usage; align price to cost structure.

## Tier Design

- **2–4 tiers** typical; avoid too many options
- **Differentiation**: Clear "best for" per tier; feature gates
- **Anchoring**: Lead with mid-tier or annual; make target option obvious
- **Value metric**: Align price to value (seats, projects, API calls)

## Anchoring & Presentation

- **Annual discount**: 15–25% for annual prepay; improves cash flow
- **Decoy**: Higher tier makes mid-tier look better
- **Most popular**: Highlight recommended plan
- **Price display**: Monthly vs annual; show savings

## When to Use Discounts

Discounts apply on top of base pricing. See **discount-marketing-strategy** for:

- Annual commitment discounts
- First-time / new customer promotions
- Lifetime deals (LTD)
- Seasonal (BFCM)
- Referral, contest, affiliate codes

**Principle**: Set base price for long-term value; use discounts tactically for acquisition, retention, or cash flow.

## Output Format

- **Pricing model** recommendation
- **Tier structure** (plans, features, price points)
- **Anchoring** approach
- **Discount** fit (when to use; reference discount-marketing-strategy)
- **pricing-page-generator** (page execution)

## Related Skills

- **discount-marketing-strategy**: Promotional pricing; when and how to discount
- **pricing-page-generator**: Pricing page content, structure, conversion
- **landing-page-generator**: Click-through to pricing
- **localization-strategy**: Pricing by market (true localization vs cosmetic); see Pricing Strategies section
