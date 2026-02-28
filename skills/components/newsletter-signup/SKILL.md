---
name: newsletter-signup-generator
description: When the user wants to design, optimize, or audit newsletter signup forms. Also use when the user mentions "newsletter," "email signup," "subscribe form," "email capture," or "lead magnet."
metadata:
  version: 1.0.0
---

# Components: Newsletter Signup

Guides newsletter signup form design for list growth. Email subscribers spend 138% more than non-subscribers; top popups convert at 23%+.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for audience and value proposition.

Identify:
1. **Placement**: Header, footer, popup, inline, sidebar
2. **Incentive**: What subscribers receive
3. **Platform**: Web, mobile, both

## Form Design

### Minimal Fields

- **Email only** when possible; highest conversion
- Add name only if needed for personalization
- Wrong number of fields significantly impacts conversion

### Value Proposition

- Clear: what subscribers receive, how often
- Transparent: avoid disappointing subscribers
- Incentive: lead magnet, discount, exclusive content

### Visual Design

- Clearly clickable submit button
- Mobile-first; responsive layout
- Appropriate input types (e.g., `type="email"` for mobile keyboards)
- Trust marks or security indicators

## Placement

| Placement | Best For | Pros | Cons |
|-----------|----------|------|------|
| **Header** | High visibility | Always visible | Limited space |
| **Footer** | Secondary capture | Non-intrusive | Lower visibility |
| **Footer bar** | Persistent | Sticky | Can annoy |
| **Popup** | High intent | High conversion | Intrusive |
| **Inline** | Content pages | Contextual | Depends on scroll |

- Avoid hiding forms behind unclicked buttons/links
- Don't place competing forms nearby

## Accessibility

| Requirement | Practice |
|-------------|----------|
| **Labels** | `<label>` for each input; `for`/`id` association |
| **Placeholders** | Don't replace labels; supplement only |
| **Error messages** | Clear, associated with field |
| **Keyboard** | Full tab order; submit via Enter |
| **Touch targets** | ≥44×44px for submit button |

## Technical

- **Validation**: Client-side; server-side required
- **Privacy**: Link to privacy policy; GDPR/CCPA compliance
- **Double opt-in**: When required by jurisdiction or best practice

## Output Format

- **Form structure** (fields, copy)
- **Placement** recommendation
- **Value proposition** suggestions
- **Accessibility** checklist

## Related Skills

- **email-marketing**: Full email marketing strategy; EDM, newsletter, deliverability, content types
- **footer-generator**: Footer often hosts signup forms
- **cta-generator**: Submit button is a CTA
- **trust-badges-generator**: Trust marks near form
