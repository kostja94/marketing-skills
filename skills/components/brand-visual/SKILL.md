---
name: components-brand-visual
description: When the user wants to define, audit, or apply visual identity (typography, colors, spacing). Also use when the user mentions "brand style guide," "visual identity," "design system," "typography," "color palette," "brand guidelines," or "AI brand aesthetics."
metadata:
  version: 1.0.0
---

# Components: Brand Visual Identity

Guides visual identity for consistent brand presentation. Companies with consistent branding see up to 23-33% revenue lift; 94% of consumers say consistency influences buying decisions.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read Section 12 (Visual Identity) for colors, typography, spacing.

Identify:
1. **Scope**: New brand, audit, or component design
2. **Touchpoints**: Web, print, social, product UI
3. **Existing assets**: Logo, style guide, design files

## Best Practices (2025)

### Typography

- **Font families**: Primary (headings), secondary (body); specify weights (Regular, Semi Bold, Bold)
- **Hierarchy**: Hero, section, subheading, body, caption; limit to 3-4 styles per block
- **Sizes**: Use scale (e.g. 120pt, 60pt, 28pt, 16pt); responsive scaling
- **Line length**: Max 120 chars for body; generous line-height for readability
- **Color**: HEX codes for text (e.g. #191919 headings, #666666 body)

### Color Palette

- **Primary, secondary, accent**: HEX, RGB, CMYK for reproduction
- **Backgrounds**: Light, dark, gradient; specify opacity when layered
- **Accessibility**: Contrast ratio >=4.5:1 for text; don't rely on color alone

### Spacing

- **Margins**: Horizontal (e.g. 120px), vertical section padding
- **Grid**: Consistent spacing scale (8px base common)
- **Logo clear space**: Minimum space around logo; document in brand guide

### Logo Usage

- **Variants**: Primary, secondary, monogram; light/dark backgrounds
- **Minimum size**: Prevent illegibility
- **Don't**: Stretch, recolor, add effects without approval

## AI Brand Aesthetics (Optional)

For AI/SaaS products, [Aesthetics of AI](https://www.acolorbright.com/en/insights/aesthetics-of-ai) identifies 14 visual trends and 5 brand archetypes. Adopt, ignore, or counter trends consciously to avoid sameness.

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

## Output Format

- **Typography** spec (fonts, weights, sizes, colors)
- **Color** palette (HEX, usage rules)
- **Spacing** scale
- **Logo** clear space and variants
- **AI products** (optional): Visual trend and archetype alignment
- **Context template** for product-marketing-context Section 12

## Related Skills

- **components-logo**: Logo placement, clear space; brand visual defines logo rules
- **components-favicon**: Favicon aligns with brand mark and colors
- **pages-media-kit**: Media kit hosts brand guidelines document; links to logo, favicon
- **components-hero**: Hero uses brand typography, colors, spacing
- **pages-404**: Error pages maintain brand consistency
