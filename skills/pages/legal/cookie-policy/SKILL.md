---
name: cookie-policy-page-generator
description: When the user wants to create or optimize a cookie policy page. Also use when the user mentions "cookie policy," "cookies," "cookie consent," "GDPR cookies," "cookie banner," "cookie notice," "tracking cookies," or "cookie settings." For legal overview, use legal-page-generator.
metadata:
  version: 1.1.0
---

# Pages: Cookie Policy

Guides cookie policy page content for transparency and regulatory compliance. Often presented as a standalone page or as part of the Privacy Policy.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

Identify:
1. **Cookie inventory**: List every cookie the site actually sets — check `_ga`, `_ga_*`, session cookies, CSRF tokens, preference cookies, ad cookies
2. **Consent requirement**: Does the site need a notice or a consent banner? See §Notice vs Consent
3. **Jurisdiction**: GDPR/ePrivacy (EU), CCPA (California), other regions
4. **Product category**: Free anonymous, freemium, SaaS, e-commerce — affects which cookies exist

---

## Cookie Inventory: Common Patterns

### Google Analytics 4 (GA4)

| Cookie | Type | Purpose | Duration | How to Opt Out |
|--------|------|---------|----------|----------------|
| `_ga` | Analytics | Distinguishes users; used for aggregate usage measurement | 2 years | [GA opt-out browser add-on](https://tools.google.com/dlpage/gaoptout), block third-party cookies, or enable Do Not Track |
| `_ga_<container-id>` | Analytics | Persists session state; used with `_ga` for session-level metrics | 2 years | Same as `_ga` |

**Disclosure requirement**: If the site uses Google Analytics, the cookie policy MUST list these cookies. GA ToS §7 requires posted privacy/cookie notice.

### Functional / Session Cookies

| Cookie | Type | Purpose | Duration | How to Opt Out |
|--------|------|---------|----------|----------------|
| Session ID | Essential | Maintains user session across page loads | Session (deleted on browser close) | Required for service; cannot be disabled |
| CSRF Token | Essential | Prevents cross-site request forgery attacks | Session | Required for security; cannot be disabled |
| Fair-use quota | Functional | Counts daily usage for rate limiting | 24 hours | Clear browser data; resets on next visit |
| Language preference | Functional | Remembers user's language choice | 30 days – 1 year | Clear browser data |
| Dark mode / theme | Functional | Remembers display preference | 30 days – 1 year | Clear browser data |

### Advertising / Tracking Cookies (If Applicable)

| Cookie | Type | Purpose | Duration | How to Opt Out |
|--------|------|---------|----------|----------------|
| `_fbp` | Marketing | Meta/Facebook pixel — tracks ad conversions | 90 days | [Meta ad preferences](https://www.facebook.com/ads/preferences) or block third-party cookies |
| `_gcl_au` | Marketing | Google Ads conversion linker | 90 days | Block third-party cookies |
| `_rdt_uuid` | Marketing | Reddit Ads conversion tracking | 90 days | Block third-party cookies |

---

## Notice vs Consent — Critical Distinction

This is the most common compliance confusion. Determining which mechanism is needed depends on cookie type:

### Cookie Notice (Informational)
**When to use**: Site uses only **strictly necessary** and **analytics** cookies (no advertising, no tracking, no third-party marketing cookies).

**What it is**: A banner or page section stating "We use cookies for [analytics/functionality]. By continuing, you accept this." No accept/reject toggle needed.

**Sufficient for**: GA4 analytics only, session cookies, CSRF tokens, functional preference cookies.

### Cookie Consent Banner (Interactive)
**When to use**: Site uses **any** of: advertising cookies, third-party tracking cookies, social media pixels, or cookies that share data with ad networks.

**What it is**: An interactive banner with accept/reject/customize options. Must allow granular consent by cookie category. Must be as easy to reject as to accept. Must not use dark patterns (pre-checked boxes, confusing language, "accept all" only).

**Required for**: Meta pixel, Google Ads conversion tracking, retargeting cookies, any cross-site tracking.

### Do Not Track (DNT)

State whether the site responds to browser DNT signals. Most sites do not, which is acceptable as long as disclosed. Example: "[Product] does not currently respond to Do Not Track signals because no uniform standard exists."

---

## Essential Elements

### 1. What Are Cookies
Brief, plain-language explanation: "Cookies are small text files stored on your device by websites you visit. They help sites remember your preferences and understand how you use them."

### 2. Cookie Types Used
Categorize by function:
- **Essential / Strictly Necessary**: Required for the site to work (session, CSRF)
- **Functional**: Remember preferences (language, theme, fair-use quota)
- **Analytics / Performance**: Measure usage in aggregate (GA4)
- **Marketing / Advertising**: Track ad effectiveness, retargeting (if applicable)

### 3. Full Cookie Table

Table format for every cookie:

| Cookie Name | Type | Purpose | Duration | How to Opt Out |
|-------------|------|---------|----------|----------------|
| [name] | [essential/functional/analytics/marketing] | [1-sentence purpose] | [duration] | [specific actionable instruction] |

The **"How to Opt Out" column** is critical — don't just list cookies, tell users how to control them. This builds trust and satisfies regulatory expectations.

### 4. Third-Party Cookies
- Which third parties set cookies through the site (GA4, Meta, Stripe, etc.)
- Link to each third party's own privacy/cookie policy
- Whether those third parties use cookies for their own purposes

### 5. How to Manage Cookies
- Browser settings: link to instructions for Chrome, Firefox, Safari, Edge
- GA4-specific: link to [GA opt-out browser add-on](https://tools.google.com/dlpage/gaoptout)
- Mobile: how to manage cookies in iOS/Android settings
- Effect of disabling: note that disabling essential cookies may break functionality

### 6. Updates
- When the cookie policy was last updated
- How users will be notified of changes

---

## Content Principles

- **Be exhaustive**: List every cookie the site sets — missing one is worse than having no cookie policy
- **Actionable opt-out**: Every cookie should have a clear "how to opt out" instruction
- **Categorize clearly**: Essential / Functional / Analytics / Marketing — users understand these categories
- **Notice-vs-consent clarity**: Be explicit about which mechanism the site needs and why
- **Plain language**: "This cookie counts your daily usage" > "This cookie is used for rate-limiting enforcement"
- **Placement**: Footer; cookie banner links here; Privacy Policy links here

---

## Output Format

- **Cookie inventory**: Complete table of all cookies the site sets
- **Consent mechanism recommendation**: Notice or consent banner, with rationale
- **Opt-out instructions**: Browser-level and cookie-specific
- **Third-party cookie disclosure**: If applicable, with links to third-party policies
- **Do Not Track disclosure**: Whether the site responds to DNT
- **Disclaimer**: Recommend legal review for jurisdiction-specific compliance

---

## Related Skills

- **privacy-page-generator**: Cookie policy often embedded in or linked from Privacy Policy
- **legal-page-generator**: Cookie policy is a legal page type; platform readiness
- **indexing**: Often noindex for cookie policy
