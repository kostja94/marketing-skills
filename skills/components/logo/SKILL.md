---
name: logo-generator
description: When the user wants to optimize logo placement, linking, or branding on a website. Also use when the user mentions "logo," "brand logo," "header logo," "logo placement," or "AI logo design."
metadata:
  version: 1.0.0
---

# Components: Logo

Guides logo placement and implementation for brand recall and navigation. Logo placement affects user orientation and conversion.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for brand guidelines and visual identity.

Identify:
1. **Context**: Header, footer, standalone
2. **Platform**: Web, mobile, both
3. **Brand guidelines**: Size, clear space, variants (from brand-visual-generator or media kit)

## Placement Best Practices

### Optimal: Top-Left

- **Brand recall**: Users are 89% more likely to remember logos in top-left vs. right
- **Left-aligned**: ~39% brand recall vs. 21% for right-aligned
- **Navigation anchor**: Users expect logo to link to homepage; left placement is intuitive
- **Scan pattern**: Aligns with left-to-right reading flow

### Avoid

- **Centered logos**: Users navigating home from centered logos are ~6x more likely to fail
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
- Maintain clear space around logo per brand guidelines (brand-visual-generator)
- Responsive: ensure readability on mobile

## AI Product Logo Design (Optional)

For AI/SaaS products, [Alignify AI Logo Guide](https://alignify.co/insights/ai-logo-design) and [Aesthetics of AI](https://www.acolorbright.com/en/insights/aesthetics-of-ai) offer industry-specific guidance.

### Design Trends

| Style | Use Case | Examples |
|-------|----------|----------|
| **Hexagon** | Technical platforms, enterprise AI | OpenAI; 4.6x more common in AI vs general logos |
| **Rotation/swirl** | Generative AI, creative tools | DeepMind, Stability AI, Synthesia |
| **Minimalist robot** | Assistants, chatbots | Jasper, Hour One, Replika |
| **Emoji/symbol** | Consumer, friendly AI | Hugging Face, Spotify AI, Zoom AI |

### Design Process

1. **Positioning**: B2B (professional, trustworthy) vs B2C (friendly, approachable)
2. **Core element**: Choose hexagon, rotation, robot, or emoji per product type
3. **Color**: Tech blue, blue-to-purple gradients, monochrome; consider dark mode
4. **Test sizes**: Favicon, mobile, header; ensure recognition at small sizes
5. **Trademark check**: Avoid conflicts (e.g. Dreamina/Tiamat case)

### Avoid

- Overly complex; modern AI logos favor minimalism
- Too similar to competitors; balance industry recognition with uniqueness
- Overly technical symbols for B2C; use friendlier designs
- Ignoring mobile display; test at multiple sizes
- Frequent rebranding; choose a long-term design

## SEO

- Alt text supports accessibility and image SEO
- Logo link contributes to internal linking (homepage)

## Accessibility

| Requirement | Practice |
|-------------|----------|
| **Alt text** | Descriptive; company name |
| **Contrast** | Logo visible against background |
| **Focus** | Link receives visible focus state |
| **Touch targets** | Adequate size on mobile (>=44x44px) |

## Output Format

- **Placement** recommendation
- **Implementation** notes (HTML, alt, link)
- **Accessibility** checklist
- **AI products** (optional): Design trend and archetype suggestions per positioning

## Related Skills

- **navigation-menu-generator**: Logo typically sits in header with nav
- **hero-generator**: Logo appears in hero context on landing pages
- **media-kit-page-generator**: Logo assets, brand guidelines, usage rules
- **favicon-generator**: Favicon derived from logo; consistent brand in browser tabs
- **brand-visual-generator**: Typography, colors, spacing; logo clear space and variants
