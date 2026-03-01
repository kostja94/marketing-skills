---
name: brand-visual-generator
description: When the user wants to define, audit, or apply visual identity (typography, colors, spacing). Also use when the user mentions "brand style guide," "visual identity," "design system," "typography," "color palette," "brand guidelines," "AI brand aesthetics," "brand colors," "font choices," "spacing system," or "design tokens."
metadata:
  version: 1.0.0
---

# Components: Brand Visual Identity

Guides visual identity for consistent brand presentation. Companies with consistent branding see up to 23-33% revenue lift; 94% of consumers say consistency influences buying decisions.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read Section 12 (Visual Identity) for colors, typography, spacing. See **branding** for brand strategy and visual identity strategy layer.

Identify:
1. **Scope**: New brand, audit, or component design
2. **Touchpoints**: Web, print, social, product UI
3. **Existing assets**: Logo, style guide, design files

## Best Practices (2025)

### Typography

- **Two-font system**: One display font for headlines, one body font for text. Contrast + harmony: different enough for distinct roles, similar enough to feel cohesive.
- **Body font**: Prioritize legibility—large x-height, open counters. Recommended: Inter, Source Sans 3, Poppins. Neutral personality; supports content without competing.
- **Headline font**: Communicates brand voice; must be readable in under one second. Carries personality while body handles infrastructure.
- **Type scale**: Use ratios 1.25–1.5 (Major Third or Perfect Fifth) for hierarchy. Limit to 3–4 styles per block.
- **Pairing rule**: Decorative fonts only with neutral typefaces. Assign distinct roles; avoid mixing more than two families.
- **Sizes**: Hero, section, subheading, body, caption; responsive scaling. Line length max 120 chars; generous line-height.

### Color Palette

- **Structure**: Primary, secondary, CTA, background, text. Use flexible systems (core hero color + complementary shades), not single rigid colors.
- **Industry mapping**: Finance → blue, gray, navy (stability); Luxury → rose gold, burgundy, black (exclusivity); Tech → teal, neon accents, charcoal (innovation); Wellness → lavender, peach, mint (calm); Sustainability → sage green, earthy tones.
- **Reproduction**: HEX, RGB, CMYK for print and digital.
- **Accessibility**: Contrast >=4.5:1 for normal text, >=3:1 for large text (18px+ or 14px+ bold). Don't rely on color alone for information.

### Spacing

- **Margins**: Horizontal (e.g. 120px), vertical section padding
- **Grid**: Consistent spacing scale (8px base common)
- **Logo clear space**: Minimum space around logo; document in brand guide

### Logo Usage

- **Variants**: Primary, secondary, monogram; light/dark backgrounds
- **Minimum size**: Prevent illegibility
- **Don't**: Stretch, recolor, add effects without approval

### Anti-Patterns (Avoid)

- **Aesthetics over functionality**: Don't sacrifice usability for visual appeal.
- **Unclear CTAs**: Limit primary CTA to one per section; visually differentiate primary vs secondary.
- **Inconsistent elements**: Pixelated icons, mismatched spacing/typography/color reduce trust.
- **Poor text hierarchy**: Disordered, cluttered text confuses users.
- **Overusing effects**: Drop shadows, pop-ups, crowded UI distract from content.
- **Chasing trends blindly**: Adopt trends only when they fit project needs.
- **Ignoring performance**: Heavy assets and complex layouts hurt load times.

### Accessibility Checklist

- **Contrast**: Normal text >=4.5:1; large text >=3:1; interactive elements >=3:1.
- **Focus**: Visible focus indicator (>=2px solid, 3:1 contrast); logical Tab order; no keyboard traps.
- **Color**: Never use color alone to convey information; add text or icons for states (error, success).
- **Keyboard**: All interactive elements reachable via Tab, Enter, Spacebar.
- **Reduced motion**: Respect `prefers-reduced-motion` for animations.

## AI Brand Aesthetics (Optional)

For AI/SaaS products, consider these visual trends and brand archetypes; adopt, ignore, or counter consciously to avoid sameness.

### Visual Trends

| Trend | Signal |
|-------|--------|
| **Off-white / beige** | Trust, restraint, premium without gloss |
| **Organic gradients** | Distinctiveness; add grain, texture |
| **Digital impressionism** | Mood over literal; suggestive, not descriptive |
| **Lomo / imperfect** | Exploratory, human creativity |
| **Contemporary realism** | Precision, reliability, mastery |
| **Sketch / scribble** | Human thought, exploration over certainty |
| **Non-brand academia** | Authority; work speaks for itself |
| **Technical illustrations** | Rigor, engineering depth |
| **Quirky cuteness** | Approachability; counter doomsday narratives |
| **Morphing objects** | Emergence, systems that learn |
| **Futuristic surrealism** | Gateway to new worlds |
| **Outer space** | Exploration, unknown |
| **ASCII / pixels** | Retro, playful, technical |
| **Generative art** | Algorithmic, living system |

### Brand Archetypes

| Archetype | Tone | Visual |
|-----------|------|--------|
| **Likeable Leaders** | Seriousness, stability, trust | Muted greys, warm beiges; impressionistic |
| **Gentle Humanists** | People before tech | Hand-drawn, everyday moments, nature |
| **Nerdy Idealists** | Engineering culture | Unpolished, quirky, non-branded |
| **Bold Builders** | Groundbreaking, transformative | Dark palettes, space references |
| **Utopian Dreamers** | What becomes possible | Retrofuturistic, surreal worlds |

## Product Marketing Context (Section 12)

When creating or updating `.cursor/product-marketing-context.md`, add:

```markdown
## 12. Visual Identity (Optional)

**Colors**: Primary #XXX, secondary #XXX; backgrounds #XXX
**Typography**: Headings (font, weight, color); Body (font, weight, color)
**Sizes**: Hero Xpt, section Xpt, body Xpt
**Spacing**: Margins Xpx; section padding Xpx
**Layout**: Viewport, top bar, footer heights if fixed
```

## Brand Guidelines Structure (Single Source of Truth)

Ensure consistency across touchpoints. Include:

- **Logo**: Usage rules, clear space, minimum sizes, variants (light/dark)
- **Colors**: Primary, secondary, CTA, background, text (HEX, RGB, CMYK)
- **Typography**: Font families, hierarchy, sizing, spacing
- **Imagery**: Photography tone, subject matter, visual mood
- **Iconography**: Style, stroke weight, usage rules

## Output Format

- **Typography** spec (fonts, weights, sizes, colors)
- **Color** palette (HEX, usage rules, industry mapping)
- **Spacing** scale
- **Logo** clear space and variants
- **Anti-patterns** and accessibility checklist
- **AI products** (optional): Visual trend and archetype alignment
- **Context template** for product-marketing-context Section 12

## Related Skills

- **branding**: Brand strategy; visual identity strategy; this skill implements typography, colors, spacing
- **logo-generator**: Logo placement, clear space; brand visual defines logo rules
- **favicon-generator**: Favicon aligns with brand mark and colors
- **media-kit-page-generator**: Media kit hosts brand guidelines document; links to logo, favicon
- **hero-generator**: Hero uses brand typography, colors, spacing
- **404-page-generator**: Error pages maintain brand consistency
