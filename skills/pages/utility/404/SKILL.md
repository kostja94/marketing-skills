---
name: 404-page-generator
description: When the user wants to create, optimize, or audit 404 error pages. Also use when the user mentions "404 page," "404 error," "error page," "page not found," "broken link page," "404 design," "custom 404," "404 redirect," "404 page UX," or "404 recovery."
metadata:
  version: 1.0.0
---

# Pages: 404 Error Page

Guides 404 error page design for UX, conversion recovery, and brand consistency.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for brand voice, key pages, and Section 12 (Visual Identity).

Identify:
1. **Site structure**: Key pages to link (homepage, popular pages, search)
2. **Brand tone**: Friendly, professional, playful
3. **Conversion goal**: Recover lost visitors, drive to key pages

## Best Practices

### Clear Error Messaging

- **User-friendly**: Neutral message explaining the page wasn't found
- **Optional 404 display**: Can show "404" but avoid blaming the user
- **Empathetic tone**: Acknowledge the error gracefully; turn frustration into opportunity

### Navigation and Redirection

| Element | Purpose |
|---------|---------|
| **Site navigation** | Header/footer so users know they're still on your site |
| **Search** | Help users find what they need |
| **Popular pages** | Links to homepage, features, pricing, blog |
| **Similar URLs** | Suggest corrections for common typos |
| **Avoid auto-redirect** | Unless confident of user intent |

### Design and Branding

- **Consistent design**: Same header, footer, colors as rest of site (brand-visual-generator)
- **Avoid confusion**: Users should not think they've left your domain
- **Mobile responsive**: Test on all devices

### Conversion Opportunities

404 pages can drive conversions by:
- Showcasing popular products or features
- Featuring testimonials or social proof
- Offering special promotions or value
- Linking to mobile app or newsletter

### Technical

- **Track 404s**: Monitor broken links, fix or redirect
- **Accessibility**: Maintain WCAG standards
- **HTTP status**: Ensure proper 404 response code

## Output Format

- **Copy** options (headline, message, CTA)
- **Link structure** (what to include)
- **Design** checklist
- **SEO**: Typically noindex; ensure canonical if needed

## Related Skills

- **homepage-generator**: Primary escape route
- **brand-visual-generator**: Typography, colors for consistent 404 design
- **indexing**: noindex for 404 if desired
- **title-tag, meta-description, page-metadata**: 404 page metadata
