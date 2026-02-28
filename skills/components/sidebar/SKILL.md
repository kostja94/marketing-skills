---
name: sidebar-generator
description: When the user wants to design, optimize, or audit a sidebar for blogs, docs, or content pages. Also use when the user mentions "sidebar," "blog sidebar," "content sidebar," or "side panel."
metadata:
  version: 1.0.0
---

# Components: Sidebar

Guides sidebar design for content sites (blogs, docs). ~80% of users focus on the left; sidebars influence flow but can hurt conversion if overused. Posts without sidebars show 3.1x higher conversion; bottom-right sticky CTAs outperform sidebars (5.62% vs 0.58% CTR).

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for content structure and conversion goals.

Identify:
1. **Content type**: Blog, docs, e-commerce
2. **Primary goal**: Navigation, CTA, related content
3. **Mobile**: Collapse to hamburger or hide on small screens

## Best Practices

### Placement

- **Left sidebar**: Prime for nav; 80% of users focus left
- **Right sidebar**: Secondary content, ads, related posts
- **Static vs sticky**: Static for content-focused; sticky for persistent CTA (subscription, cart)

### Conversion Reality

| Approach | Typical result |
|----------|----------------|
| **Sidebar CTA** | <1% opt-in for blog sidebars |
| **In-content CTA** | 3x+ higher conversion |
| **Bottom-right sticky** | 5.62% CTR vs 0.58% sidebar |
| **No sidebar** | 3.1x higher conversion vs with sidebar |

**Recommendation**: Prefer in-content CTAs or bottom-right sticky over sidebar CTAs. Use sidebar for nav and discovery, not primary conversion.

### Widget Guidelines

- **One high-value CTA** max; avoid clutter
- **Social proof**: Testimonials, logos
- **Popular/related posts**: Discovery, internal linking
- **Avoid**: Too many ads, affiliate links; reduces trust and speed

### Mobile

- **Collapse**: Hamburger or off-canvas drawer
- **57%+ mobile traffic**: Responsive design non-negotiable
- **Reduce clutter**: Hide or simplify sidebar on small screens

## Output Format

- **Placement** (left/right, static/sticky)
- **Widget** list (nav, CTA, related, social proof)
- **Mobile** behavior
- **Conversion** note (in-content vs sidebar CTA)

## Related Skills

- **toc-generator**: TOC often in sidebar for long content
- **cta-generator**: Sidebar CTA (use sparingly)
- **newsletter-signup-generator**: Sidebar signup; consider in-content instead
- **internal-links**: Related posts in sidebar
