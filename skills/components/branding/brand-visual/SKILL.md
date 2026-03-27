---
name: brand-visual-generator
description: When the user wants to define, audit, or apply visual identity (typography, colors, spacing, design tokens, frontend aesthetics). Also use when the user mentions "brand style guide," "visual identity," "design system," "typography," "color palette," "brand guidelines," "AI brand aesthetics," "brand colors," "font choices," "spacing system," "design tokens," "motion," "distinctive design," "frontend aesthetics," "PowerPoint theme," "Google Slides brand," or "slide master colors." For brand story, positioning, and voice, use branding.
license: MIT
metadata:
  version: 1.4.0
---

# Components: Brand Visual Identity

Guides visual identity for consistent brand presentation. Companies with consistent branding see up to 23-33% revenue lift; 94% of consumers say consistency influences buying decisions.

**Keywords**: visual identity, design tokens, color palette, typography, CSS variables, slide deck, brand guidelines, frontend aesthetics, accessibility

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read Section 12 (Visual Identity) for colors, typography, spacing. See **branding** for brand strategy and visual identity strategy layer.

Identify:
1. **Scope**: New brand, audit, or component design
2. **Touchpoints**: Web, print, social, product UI, **slides** (PowerPoint, Google Slides, Keynote), **documents** (Word, Google Docs, PDF reports)
3. **Existing assets**: Logo, style guide, design files

## Best Practices

### Typography

- **Two-font system**: One display font for headlines, one body font for text. Contrast + harmony: different enough for distinct roles, similar enough to feel cohesive.
- **Body font**: Prioritize legibility—large x-height, open counters. For neutral/safe: Source Sans 3, Lora, IBM Plex Sans. **For distinctiveness**: avoid overused AI fonts (Inter, Roboto, Arial, system fonts); prefer characterful choices that elevate the brand. See **Frontend Aesthetics**.
- **Headline font**: Communicates brand voice; must be readable in under one second. Carries personality while body handles infrastructure.
- **Type scale**: Use ratios 1.25–1.5 (Major Third or Perfect Fifth) for hierarchy. Limit to 3–4 styles per block.
- **Pairing rule**: Decorative fonts only with neutral typefaces. Assign distinct roles; avoid mixing more than two families.
- **Sizes**: Hero, section, subheading, body, caption; responsive scaling. Line length max 120 chars; generous line-height.

### Color Palette

- **Structure**: Primary, secondary, CTA, background, text. Use flexible systems (core hero color + complementary shades), not single rigid colors.
- **Industry mapping**: Finance → blue, gray, navy (stability); Luxury → rose gold, burgundy, black (exclusivity); Tech → teal, neon accents, charcoal (innovation); Wellness → lavender, peach, mint (calm); Sustainability → sage green, earthy tones.
- **Reproduction**: HEX, RGB, CMYK for print and digital. For **programmatic slides** (e.g. python-pptx), map brand HEX to RGB tuples `(R, G, B)` for fills and text; keep a single source of truth table (HEX + RGB) in the deliverable.
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
- **Generic AI aesthetics**: Inter, Roboto, Arial, Space Grotesk, and system fonts contribute to cookie-cutter design; avoid clichéd schemes (e.g., purple gradients on white). Prefer distinctive choices when brand differentiation matters.
- **Emoji as icons**: Use SVG icons (Heroicons, Lucide, Simple Icons)—never emojis (🎨 🚀 ⚙️) as UI icons; emojis look unprofessional and inconsistent.
- **Unstable hover states**: Use color/opacity transitions on hover; avoid scale transforms that shift layout or cause content jump.

### Accessibility Checklist

- **Contrast**: Normal text >=4.5:1; large text >=3:1; interactive elements >=3:1.
- **Focus**: Visible focus indicator (>=2px solid, 3:1 contrast); logical Tab order; no keyboard traps.
- **Color**: Never use color alone to convey information; add text or icons for states (error, success).
- **Keyboard**: All interactive elements reachable via Tab, Enter, Spacebar.
- **Reduced motion**: Respect `prefers-reduced-motion` for animations.

## Frontend Aesthetics

Guides distinctive, production-grade frontend implementation. Components (hero, CTA, footer, etc.) and pages (landing, home, features) should reference these principles for visual differentiation. **Intentionality over intensity**: bold maximalism and refined minimalism both work when executed with precision.

### Typography

- **Avoid generic AI fonts**: Inter, Roboto, Arial, system fonts, Space Grotesk. These create cookie-cutter aesthetics.
- **Distinctive pairing**: One display font (headlines, personality) + one refined body font (readability). Choose characterful, unexpected fonts that elevate the interface.
- **Consistency**: Use CSS variables; limit to 3–4 type styles per block.

### Motion

- **High-impact moments**: One well-orchestrated page load with staggered reveals (`animation-delay`) creates more delight than scattered micro-interactions.
- **Prioritize**: CSS-only for HTML; Motion library for React when available. Scroll-triggering and hover states that surprise.
- **Accessibility**: Always respect `prefers-reduced-motion`; provide reduced or no-motion alternatives.

### Spatial Composition

- **Unexpected layouts**: Asymmetry, overlap, diagonal flow, grid-breaking elements.
- **Balance**: Generous negative space OR controlled density—choose intentionally.
- **Hierarchy**: Clear visual flow; avoid predictable, evenly-distributed layouts.

### Backgrounds & Visual Details

- **Atmosphere over flat**: Create depth rather than defaulting to solid colors.
- **Techniques**: Gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, grain overlays.
- **Context**: Match effects to overall aesthetic; don't distract from content.

### Never

- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (e.g., purple gradients on white)
- Predictable layouts and cookie-cutter component patterns
- Design that lacks context-specific character
- Emojis as UI icons (use SVG: Heroicons, Lucide, Simple Icons)

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

When creating or updating `.cursor/project-context.md`, add:

```markdown
## 12. Visual Identity (Optional)

**Colors**: Primary #XXX, secondary #XXX; backgrounds #XXX
**Typography**: Headings (font, weight, color); Body (font, weight, color)
**Sizes**: Hero Xpt, section Xpt, body Xpt
**Spacing**: Margins Xpx; section padding Xpx
**Layout**: Viewport, top bar, footer heights if fixed
```

## Slides & Documents (Non-Web)

When the user asks for **deck or document** branding—not only websites:

- **Slide master**: Background color from token; title font = display/heading token; body = body token; default title/body sizes aligned to type scale from **branding** / Section 12.
- **Theme colors**: Map primary, secondary, background, text, and one accent to the presentation app's theme (PowerPoint *Design → Variants*, Google Slides *Theme*, Keynote *Document* settings) so shapes and charts inherit palette.
- **Charts & shapes**: Cycle accents in a fixed order (e.g. primary → secondary → tertiary) instead of random colors; keeps decks on-brand.
- **Documents**: Same fonts and heading hierarchy as web where possible; specify paragraph style names (Title, Heading 1–3, Normal) with point sizes and colors.

Strategy and narrative layers remain in **branding**; this section is **visual execution** for office/slide tools.

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
- **Frontend aesthetics** (optional): Motion, spatial composition, backgrounds—for distinctive implementation
- **Anti-patterns** and accessibility checklist
- **AI products** (optional): Visual trend and archetype alignment
- **Context template** for project-context Section 12
- **Slides/documents** (when requested): theme mapping + master typography + chart accent order

## Related Skills

- **branding**: Brand strategy; visual identity strategy; this skill implements typography, colors, spacing
- **logo-generator**: Logo placement, clear space; brand visual defines logo rules
- **favicon-generator**: Favicon aligns with brand mark and colors
- **media-kit-page-generator**: Media kit hosts brand guidelines document; links to logo, favicon
- **hero-generator**: Hero uses brand typography, colors, spacing
- **404-page-generator**: Error pages maintain brand consistency
