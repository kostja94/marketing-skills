---
name: signup-login-page-generator
description: When the user wants to create, optimize, or audit signup and login pages. Also use when the user mentions "signup page," "login page," "registration page," "auth page," "sign up form," "create account," "student discount at signup," or "auth subdomain."
metadata:
  version: 1.0.0
---

# Pages: Signup / Login

Guides signup and login page structure, domain choice, modal vs dedicated page, discount integration, and SEO. Signup is the conversion endpoint from landing pages and pricing; when discounts apply at registration (e.g., student discount), signup is the P0 placement. Distinct from **landing-page-generator** (acquisition); **newsletter-signup-generator** (email capture only).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, audience, and offers.

Identify:
1. **Goal**: Account creation, trial, paid signup
2. **Discounts**: Student, annual, promo code—apply at signup?
3. **Auth**: Self-built vs third-party (Auth0, Clerk, etc.)
4. **Audience**: General vs segmented (students, startups)

## Domain & URL

| Option | Use |
|--------|-----|
| **Main domain** | /signup, /login, /auth; simple; common for SaaS |
| **Subdomain** | auth.example.com; Universal Login pattern; credentials not cross-origin; requires Cookie domain config for cross-subdomain session |
| **Third-party** | Redirect to Auth0, Clerk, etc.; provider hosts auth |

**Paths**: /signup, /login, /register, /auth; keep short and consistent.

## Modal vs Dedicated Page

| Approach | Use |
|----------|-----|
| **Dedicated page** | Account creation; discount verification; student verification; higher-quality leads; fewer fake emails |
| **Modal / popup** | Lightweight lead capture; newsletter; quick demo request; lower quality, higher volume |

**When discount applies at signup** (e.g., student 30% off): Use **dedicated page**—user needs space for verification, discount display, and form. Modal can work for simple email-only capture; avoid for full account + verification flows.

**Mobile**: Google penalizes intrusive interstitials; dedicated page avoids penalty.

## Page Structure

| Section | Purpose |
|---------|---------|
| **Headline** | Value-focused; "Start free" or "Students: 30% off today, 15% off ongoing" |
| **Trust signals** | SSL, payment logos, privacy, customer logos; see **trust-badges-generator** |
| **Media** | Product screenshot, short video, or demo GIF above fold; reinforces value |
| **Form** | Minimal fields; email first; social login (Google, GitHub) reduces friction |
| **Discount block** | Student discount, annual discount, promo code; verification entry when applicable |
| **Privacy / Terms** | Links; compliance |

## Discount Integration

### Student / Education (education-program)

| Element | Placement |
|---------|-----------|
| **Headline or subhead** | "Students: 30% off today, 15% off ongoing" |
| **Verification** | .edu, SheerID, UNiDAYS; verify at signup to apply discount |
| **Eligibility** | Brief eligibility; link to full terms |

**P0 placement**: When student discount applies at registration, signup page is primary; pricing page and homepage banner are P1.

### Other Discounts

- **Annual discount**: Show when user selected annual plan from pricing; confirm before submit
- **Promo code**: "Have a code?" link or inline field; validate before or after submit

## Form & Verification

- **Minimal fields**: Email only when possible; add name only if needed; see **newsletter-signup-generator**
- **Social login**: Google, GitHub; reduces friction; faster than email form
- **Verification entry**: .edu (instant), SheerID/UNiDAYS (broader); see **education-program**
- **Progressive**: Collect email first; verify student; then complete profile if needed

## SEO

| Page | Meta | Reason |
|------|------|--------|
| **Login** | `noindex, nofollow` | No search value; security risk; indexed login pages can confuse users |
| **Signup** | `noindex, follow` | Block from SERP; allow crawl of links (Privacy, Terms) |

**Implementation**: Use `<meta name="robots" content="noindex">` or `X-Robots-Tag` header. robots.txt does not prevent indexing—crawlers must access the page to read the directive. See **indexing** for full noindex page-type list.

## Output Format

- **Domain** and URL choice
- **Modal vs page** recommendation
- **Structure** (headline, trust, media, form, discount block)
- **Discount** integration (student, annual, promo)
- **SEO** meta tags
- **Related** skills for execution

## Related Skills

- **indexing**: Full noindex page-type list; noindex,follow vs noindex,nofollow
- **education-program**: Student discount at signup (P0); verification; placement
- **landing-page-generator**: Signup is CTA destination; landing page structure applies to signup when signup is conversion endpoint
- **popup-generator**: Modal option for lightweight capture; signup as full form → dedicated page
- **newsletter-signup-generator**: Form design; minimal fields; trust signals
- **trust-badges-generator**: Trust signals on signup
- **pricing-page-generator**: Pricing CTA → signup; annual discount flows to signup
- **website-structure**: /login, /signup in Standalone paths
