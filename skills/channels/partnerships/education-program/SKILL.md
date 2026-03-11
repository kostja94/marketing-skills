---
name: education-program
description: When the user wants to plan, implement, or optimize student and education discount programs. Also use when the user mentions "student discount," "education discount," "student plan," "for students," ".edu discount," "academic pricing," "student verification," "SheerID," "UNiDAYS," or "education program."
metadata:
  version: 1.0.0
---

# Channels: Education Program

Guides student and education discount programs as an acquisition channel. Targets students and educators; common for SaaS, dev tools, and productivity apps. ~65% of students who use professional tools in school continue using them in their first jobs—education discounts are long-term customer acquisition, not just revenue loss.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, audience, and pricing.

Identify:
1. **Product type**: SaaS, dev tool, design tool, productivity
2. **Student fit**: Is your ICP or future ICP student-aged?
3. **Discount structure**: First-time vs renewal; % or fixed
4. **Verification**: .edu, student ID, third-party (SheerID, UNiDAYS)

## Education Program vs Other Channels

| Dimension | Education Program | Startups Program | Referral |
|-----------|-------------------|------------------|----------|
| **Audience** | Students, educators | Founders, early-stage | Existing users |
| **Incentive** | Discount, free tier | Discount, credits | Discount, credits |
| **Verification** | .edu, student ID, SheerID/UNiDAYS | Revenue, team size | None (user-driven) |
| **LTV focus** | Future customers; 65% continue post-grad | Early adopters | Referred users |

## Discount Structures

| Type | Typical Range | Use |
|------|---------------|-----|
| **First-time / registration** | 30–50% off | Apply at signup; drives conversion |
| **Ongoing / renewal** | 15–25% off | Retain students; lower than first-time |
| **Free tier** | Full access free | JetBrains, GitHub Education; highest adoption |
| **Flat academic rate** | Simplified pricing | Easier for students to understand |

**Example**: 30% off on registration day; 15% off on renewal. Align with **discount-marketing-strategy** for financial guardrails (LTV:CAC, qualification criteria).

## Verification

| Method | Use |
|--------|-----|
| **.edu email** | Instant; low friction; US-centric |
| **Student ID upload** | Manual review; global; document must show name, institution, expiry |
| **SheerID** | Third-party; 200K+ data sources; verify → promo code at checkout |
| **UNiDAYS** | Third-party; 98%+ automated; 800+ brands; marketplace reach |

**When to verify**: At registration (recommended when discount applies at signup) or at checkout. Registration-time verification = single decision point; user claims discount where they convert.

## Placement Priority

| Priority | Location | Purpose |
|----------|----------|---------|
| **P0** | Registration / signup flow | User claims discount here; must show when discount applies at signup |
| **P1** | Pricing page | Student tier or "Student discount" block; keeps single decision point |
| **P1** | Homepage banner or CTA | "Students: 30% off today, 15% off ongoing"; top-banner-generator |
| **P2** | Standalone page /student-discount | Optional; for "student discount" SEO or paid ad landing page |

**Principle**: When discount applies at registration, core placement is registration flow. Pricing page and homepage support discovery. Standalone page only if needed for SEO or ads—avoid duplication when persona pages (e.g. "for students") already exist.

## Page Strategy

| Approach | When |
|----------|------|
| **Embed in pricing** | Student as tier or block; link to full pricing; no separate page |
| **Registration only** | Discount claimed at signup; pricing page shows "Student discount available—verify at signup" |
| **Standalone /student-discount** | "Student discount" search intent; paid ad landing; persona page would duplicate |

See **startups-page-generator** for page structure when a standalone education page is needed; **pricing-page-generator** for Special programs section.

## Implementation Flow

1. **Define discount**: First-time %, renewal %; align with **pricing-strategy**, **discount-marketing-strategy**
2. **Choose verification**: .edu (instant) vs SheerID/UNiDAYS (broader, automated)
3. **Placement**: Registration (P0); pricing page (P1); homepage banner (P1); standalone page (P2 if needed)
4. **Graduation transition**: Plan how students convert to full price when eligibility ends
5. **Track**: Student signups, conversion rate, LTV of student cohort

## Best Practices

- **Low friction**: .edu = instant; ID upload = clear requirements; third-party = one-click verify
- **Abuse prevention**: Revoke if ineligible; annual re-verification; limit per person
- **Messaging**: "We've been there"; "Grow with us"; social proof ("X students use [Product]")
- **Graduation**: Email before expiry; offer transition discount to full plan

## Output Format

- **Discount structure** (first-time, renewal)
- **Verification** method
- **Placement** (registration, pricing, homepage, standalone)
- **Page strategy** (embed vs standalone)
- **Related** skills for execution (pricing-page, startups-page, top-banner, discount-marketing)

## Related Skills

- **discount-marketing-strategy**: Discount structure, financial guardrails; education is a campaign type
- **pricing-strategy**: Base price; education discount applies on top
- **pricing-page-generator**: Special programs section; Student tier or block; placement P1
- **startups-page-generator**: Standalone education page when needed; same structure for startups + education
- **top-banner-generator**: Homepage banner "Students: X% off"; placement P1
- **landing-page-generator**: /student-discount landing page when used for SEO or ads
- **signup-login-page-generator**: Signup is P0 for student discount; discount block, verification at registration
- **use-cases-page-generator**: "For students" use case; avoid duplicate "for students" page
