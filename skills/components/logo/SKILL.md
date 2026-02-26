---
name: components-logo
description: When the user wants to optimize logo placement, linking, or branding on a website. Also use when the user mentions "logo," "brand logo," "header logo," or "logo placement."
metadata:
  version: 1.0.0
---

# Components: Logo

Guides logo placement and implementation for brand recall and navigation. Logo placement affects user orientation and conversion.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for brand guidelines.

Identify:
1. **Context**: Header, footer, standalone
2. **Platform**: Web, mobile, both
3. **Brand guidelines**: Size, clear space, variants

## Placement Best Practices

### Optimal: Top-Left

- **Brand recall**: Users are 89% more likely to remember logos in top-left vs. right
- **Left-aligned**: ~39% brand recall vs. 21% for right-aligned
- **Navigation anchor**: Users expect logo to link to homepage; left placement is intuitive
- **Scan pattern**: Aligns with left-to-right reading flow

### Avoid

- **Centered logos**: Users navigating home from centered logos are ~6× more likely to fail
- **Right-aligned**: Violates conventions; harms brand recognition

### When Center May Work

- Minimal headers with few elements
- Brand-heavy landing pages where logo is focal point
- Ensure logo still links to homepage and is clearly clickable

## Implementation

### Linking

- **Always link to homepage** from logo
- Use `<a href="/">` wrapping logo image
- Expected behavior; don't break convention

### Image

- Use appropriate format (SVG preferred for scalability)
- Provide `alt` text: company/product name, not "logo"
- Example: `alt="Acme Inc."` not `alt="Logo"`

### Size & Clear Space

- Adequate size for recognition; not competing with nav or CTA
- Maintain clear space around logo per brand guidelines
- Responsive: ensure readability on mobile

## SEO

- Alt text supports accessibility and image SEO
- Logo link contributes to internal linking (homepage)

## Accessibility

| Requirement | Practice |
|-------------|----------|
| **Alt text** | Descriptive; company name |
| **Contrast** | Logo visible against background |
| **Focus** | Link receives visible focus state |
| **Touch targets** | Adequate size on mobile (≥44×44px) |

## Output Format

- **Placement** recommendation
- **Implementation** notes (HTML, alt, link)
- **Accessibility** checklist

## Related Skills

- **components-navigation-menu**: Logo typically sits in header with nav
- **components-hero**: Logo appears in hero context on landing pages
