---
name: alternatives-page-generator
description: When the user wants to create, optimize, or audit alternatives or comparison content (page or blog article). Also use when the user mentions "alternatives page," "alternatives listicle," "X alternatives," "competitor comparison," "vs page," "compare page," "best alternatives to X," or "switch from X."
metadata:
  version: 1.0.0
---

# Pages: Alternatives / Compare

Guides alternatives and comparison content that target "X alternatives" and "X vs Y" search intent. High SEO value for SaaS and tools; captures bottom-of-funnel traffic evaluating options. **Content format**: Can be a standalone page (/alternatives, /alternatives-to-notion) or a **blog article** (/blog/notion-alternatives). Same structure applies; blog format builds topical authority and fits content hubs.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Content Format: Page vs Blog Article

| Format | Path | Use |
|--------|------|-----|
| **Standalone page** | /alternatives, /alternatives-to-[competitor] | Dedicated hub; strong for your own product as alternative |
| **Blog article** | /blog/[product]-alternatives, /blog/best-[x]-alternatives | Listicle format; common for affiliate, challenger brands; builds topical authority |

Both formats use the same structure (quick verdict, comparison table, individual reviews, FAQ). Blog articles often appear as listicles; challenger brands (e.g. ClickUp, CrazyEgg) publish alternatives content in their blog to leverage competitor brand awareness.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product, competitors, and differentiators.

Identify:
1. **Format**: Standalone page vs. blog article; single hub vs. per-competitor pages
2. **Competitors**: Who to include; avoid over-promoting direct rivals
3. **Primary goal**: Sign up, trial, demo; position as fair comparison
4. **Tone**: Objective, helpful; avoid disparaging competitors

## Page / Article Structure

| Section | Purpose |
|---------|---------|
| **Headline** | "Best [Product Category] Alternatives in [Year]" or "[Product] vs [Competitor]"; plain promise, avoid cute titles |
| **Quick verdict** | 5–8 lines above the fold: who it's for, top picks, decision shortcut |
| **Pros/cons of original** | Build trust; acknowledge why someone might leave; who should still keep it |
| **Comparison table** | Place early, not hidden; 4–6 columns (best for, price, ease, key limit); scannable |
| **Alternatives list** | 6–10 picks; each with "best for" label, proof, tradeoff, pricing snapshot |
| **Migration** | Link to migration-page if applicable |
| **FAQ** | "Is X better than Y?"; "Can I migrate from X?"; pricing, trials |
| **CTA** | Try free, start trial, book demo; one CTA above fold, one near end |

## Best Practices

### SEO

- **Intent**: Commercial; "alternatives to X," "X vs Y," "best X"
- **Title**: "[Product] Alternatives: Top [N] Options Compared | [Your Product]"
- **Content**: 1500+ words for alternatives hub; 800+ for single comparison
- **Internal links**: Link to features, pricing, migration, use cases

### Fairness & Trust

- **Objective tone**: Acknowledge competitor strengths; avoid FUD
- **Transparent criteria**: Explain how you compare (features, pricing, use case)
- **Update regularly**: Pricing and features change; date the comparison
- **Verifiable claims**: Link to pricing pages, docs; cite sources; add "as of [date]" for prices

### Conversion

- **Soft sell**: Position your product as one option; let value speak
- **Migration CTA**: "Switch in minutes" if migration is easy
- **Social proof**: Customer quotes from switchers

## Output Format

- **Headline** and intro copy
- **Comparison structure** (table columns, criteria)
- **Per-competitor** summary (2–3 sentences each)
- **Your product** positioning
- **Internal links** (migration, features, pricing)
- **SEO** metadata

## Related Skills

- **article-page-generator**: Alternatives as blog listicle; same structure, different path
- **migration-page-generator**: Migration guides for switchers; link from alternatives
- **landing-page-generator**: When alternatives page is used for **paid ads** (PPC), apply LP principles; ad-to-page alignment critical
- **features-page-generator**: Feature comparison content
- **pricing-page-generator**: Pricing comparison
- **customer-stories-page-generator**: Switcher testimonials
