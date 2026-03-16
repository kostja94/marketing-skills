---
name: homepage-generator
description: When the user wants to create, optimize, or audit homepage content and structure. Also use when the user mentions "homepage," "landing page," "main page," "home page," "hero section," "above the fold," "home page design," "landing page optimization," "homepage conversion," or "homepage structure."
metadata:
  version: 1.1.0
---

# Pages: Homepage

Guides homepage content, structure, and conversion optimization.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Homepage Role & Purpose

| Role | Priority | Notes |
|------|----------|-------|
| **Conversion** | Primary | Homepage is a trust machine and conversion engine—not a sales pitch. Most visitors (70–80%) are first-time; they need clarity, credibility, and orientation within 3–5 seconds. Convert through trust-building and guided exploration, not aggressive selling. |
| **Brand** | Primary | First impression, credibility test, orientation center. Answers: Who are you? What do you offer? Why should I care? Brand voice and differentiation live here—see **branding**. |
| **Branded keywords SEO** | Required | Primary SEO goal: rank for brand name so people can find you in SERPs. Branded searches indicate high intent and familiarity; they convert better than non-branded. |
| **Broad/non-branded SEO** | Secondary | Homepage is not the main SEO traffic driver—blog, product pages, and category pages typically carry that. A well-optimized homepage can rank for related non-branded terms as a bonus; do not sacrifice UX or conversion for broad keyword stuffing. |

**Principle**: SEO and CRO work together. Good homepage SEO aligns with user needs; conversion optimization ensures attracted traffic converts. See **landing-page-generator** for single-goal campaign pages (homepage is multi-purpose).

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, audience, and value proposition. See **branding** for brand strategy, positioning, differentiation.

Identify:
1. **Primary goal**: Sign up, demo, purchase, learn more
2. **Audience**: Cold visitors, returning, specific segment
3. **Traffic source**: Organic, paid, referral

## Homepage Structure

| Section | Purpose |
|---------|---------|
| **Hero** | Value proposition, primary CTA, above the fold |
| **Social proof** | Logos, testimonials, metrics; "As Seen In" (press coverage) when applicable; see **customer-stories-page-generator** for case study snippets |
| **Features/Benefits** | What it does, why it matters |
| **Use cases** | Who it's for, how they use it |
| **Objection handling** | FAQ, guarantees, comparisons |
| **Final CTA** | Repeat primary action |

### Common Modules (from website-structure)

Combine as needed: Headline, Subheadline, Primary CTA, Supporting Image/Demo, Benefits Section, Social Proof, Search Box (if applicable), Secondary CTA, Banner. **Navigation**: Horizontal Bar, Dropdown, Hamburger (mobile), Sidebar, Footer; ensure Desktop + Mobile parity. See **hero-generator** for hero design.

## Best Practices

### Value Proposition

- **Clarity**: Visitor understands in 5 seconds
- **Specificity**: Concrete benefit, not vague
- **Differentiation**: Why you, not alternatives — see **branding** for positioning framework
- **Customer language**: Their words, not jargon
- **Avoid "not speaking human"**: Don't over-emphasize brand with vague definitions; communicate in user-friendly ways—if someone searches "AI presentation maker," the answer should be obvious from your headline

### CTA

- One clear primary action (avoid decision paralysis)
- Button copy: value-focused ("Start Free Trial") not generic ("Submit")
- Visible without scrolling
- Repeated at logical points

### Conversion Checklist

- Clear value proposition above the fold
- Single primary CTA; simplified navigation (5–7 menu items)
- Immediate social proof (reviews, trust badges, media logos)
- Mobile-first, fast-loading design

### Visual & Aesthetics

- **Frontend aesthetics**: For distinctive typography, motion, spatial composition, backgrounds—see **brand-visual-generator** Frontend Aesthetics

### SEO

**Branded keywords first**: Title and meta should include brand name; ensure homepage ranks for "[Brand Name]" so users can find the official site. See **brand-protection** when impersonation risk exists—place "Official website: [domain]" above fold or in hero.

- **Title tag** (50–60 chars): Brand name + primary keyword; e.g. "Canva – Free Website Builder"
- **Meta description** (150–160 chars): CTA + secondary keywords; engaging to encourage clicks
- **H1**: Value proposition or primary headline; one per page; include primary keyword naturally
- **Body**: Primary keyword in first 100 words; secondary keywords in H2–H6 and body
- Logical H2–H6 structure for scannability and LLM/AI Overview visibility

**Schema**: Add **Organization + WebSite** JSON-LD on homepage (or in root layout for site-wide). Organization establishes brand entity; WebSite enables sitelinks searchbox. Do not put Organization only on About page—About uses AboutPage schema. See **schema-markup**, **entity-seo**.

## Output Format

- **Structure** outline (sections)
- **Hero** copy options (headline, subheadline, CTA)
- **Key sections** content suggestions
- **SEO** metadata (title, description, H1)
- **Conversion** checklist

## Related Skills

- **branding**: Brand strategy, value prop, differentiation; homepage implements brand voice
- **brand-protection**: "Official website" placement when impersonation risk exists
- **landing-page-generator**: For single-goal campaign pages (affiliate signup, lead capture); homepage is multi-purpose
- **pricing-page-generator**: Homepage often links to pricing
- **features-page-generator**: Features section or link to features page
- **press-coverage-page-generator**: "As Seen In" section (logo strip) when coverage exists; full page links from homepage
- **customer-stories-page-generator**: Testimonials, case study snippets for social proof section
- **schema-markup, entity-seo**: Organization + WebSite schema placement (homepage or root layout)
- **title-tag, meta-description, page-metadata, open-graph, twitter-cards**: Homepage metadata and social previews
- **heading-structure**: Homepage heading structure
