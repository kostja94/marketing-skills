---
name: components-footer
description: When the user wants to design, optimize, or audit website footers. Also use when the user mentions "footer," "page footer," "site footer," "footer links," "footer navigation," or "footer SEO."
metadata:
  version: 1.0.0
---

# Components: Footer

Guides footer design for SEO, UX, and conversion. Footers provide secondary navigation, support crawlability, and engage users below the fold (66% of engagement happens there).

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for key pages and audience.

Identify:
1. **Site type**: Marketing, e-commerce, SaaS, blog
2. **Footer goals**: Navigation, lead capture, trust, legal
3. **Platform**: Web, mobile, both

## Essential Footer Elements

### Navigation & Links

- Links to high-priority pages: About, Contact, Services, FAQs
- Related blog posts and internal content links
- XML or HTML sitemap links
- Product/service category links (e-commerce)
- **Avoid excessive links**: Google warns that too many internal links can harm SEO; link only to high-priority pages

### Business Information

- Physical address, phone, email
- Social media profile links (Follow us) -> distinct from **components-social-share** (share this page)
- Copyright and legal information (Privacy Policy, Terms of Service)

### User Engagement

- Newsletter signup forms
- Call-to-action buttons
- Customer testimonials or support resources

## SEO Best Practices

| Practice | Purpose |
|----------|---------|
| **Strategic linking** | Link to important pages; avoid link bloat |
| **Descriptive anchor text** | Target keywords; avoid "Click here" |
| **Text links** | Prefer text over images for crawlers |
| **No dead ends** | Ensure pages link to other content |
| **Semantic HTML** | `<footer>`, proper landmark roles |

### Link Strategy

- Footer links help crawlers discover pages and understand site structure
- Too many links can dilute page context; keep focused
- Include sitemap link for comprehensive discovery

## UX Guidelines

### Placement & Visibility

- Footer at bottom; visible without dominating desktop view
- Mobile: Valuable for users who don't scroll to top
- Secondary navigation; complements header nav

### Organization

- Group links by category (Product, Company, Legal, Support)
- Use clear headings for each column
- Prioritize most-used links

### Accessibility

| Requirement | Practice |
|-------------|----------|
| **Contrast** | 4.5:1 for link text |
| **Touch targets** | >=44x44px on mobile |
| **Keyboard** | Full keyboard navigation |
| **Screen readers** | Proper heading hierarchy, landmark roles |

## Output Format

- **Footer structure** (columns, link groups)
- **Link list** with anchor text suggestions
- **SEO** checklist
- **Accessibility** checklist

## Related Skills

- **components-navigation-menu**: Footer complements header nav
- **components-social-share**: Footer has profile links (Follow us); social-share has share buttons (share this page) -> different use cases
- **seo-technical-sitemap**: Footer can link to sitemap
- **seo-on-page-internal-links**: Footer is secondary internal linking
- **components-newsletter-signup**: Footer often hosts signup forms
