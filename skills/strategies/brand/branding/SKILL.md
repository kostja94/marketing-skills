---
name: branding
description: When the user wants to define, audit, or apply brand strategy—purpose, values, positioning, storytelling, voice, visual identity. Also use when the user mentions "brand strategy," "brand story," "brand storytelling," "brand voice," "brand identity," "brand guidelines," "brand purpose," "brand values," "origin story," "brand narrative," "brand personality," or "brand archetype."
metadata:
  version: 1.0.0
---

# Strategies: Branding

Guides brand strategy: purpose, values, positioning, storytelling, voice, and visual identity. Companies with consistent branding see 23–33% revenue lift; people remember stories ~22× more than facts alone. Use this skill when defining a new brand, auditing consistency, or aligning messaging across touchpoints.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Brand strategy**: Purpose, values, positioning, differentiation, target audience
- **Brand storytelling**: Origin story, hero's journey, narrative arc, brand archetypes
- **Brand voice & tone**: Voice, tone, avoid terms, preferred wording
- **Brand visual identity**: Colors, typography, logo rules—strategy layer; implementation in **brand-visual-generator**, **logo-generator**

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read Sections 2 (Positioning), 3 (Value Proposition), 8 (Brand & Voice), 12 (Visual Identity).

Identify:
1. **Scope**: New brand, audit, or alignment
2. **Touchpoints**: Website, social, product UI, directories, content
3. **Existing assets**: Brand guide, logo, style guide

## Brand Strategy Pillars

| Pillar | Purpose |
|--------|---------|
| **Brand purpose** | Why the brand exists beyond profit; one sentence |
| **Brand values** | 4–5 core values; what you stand for; differentiators |
| **Target audience** | Who you serve; ICP; jobs to be done |
| **Positioning** | For [customer] who [need], our [product] is a [category] that [benefit]. Unlike [competitor], we [differentiator] because [reasons] |
| **Differentiation** | Why you, not alternatives; concrete, not vague |

## Brand Storytelling

### Origin Story

- **What**: Journey, founding, milestones, personal experiences that shaped the company
- **Why**: Emotional connection; 58% of customers buy based on company values
- **Elements**: Who founded it; why created; challenges overcome; vision; how it evolved

### Hero's Journey (Customer as Hero)

| Element | Content |
|---------|---------|
| **Hero** | Your customer; their needs, wants, context |
| **Problem** | What they face; how they solve it now |
| **Inciting insight** | Reframing that creates urgency |
| **Brand's role** | Guide, tool, or partner—not hero; how you enable resolution |
| **Transformation** | What better future looks like; proof (case studies, testimonials) |

### Brand Narrative Arc

- **Protagonist**: Customer facing a challenge
- **Stakes**: What happens if nothing changes
- **Proof**: Data, case studies, testimonials
- **CTA**: Place call to action in the story; provoke action

### Brand Archetypes (12 Types)

| Archetype | Tone | Example |
|-----------|------|---------|
| **Creator** | Innovative, imaginative | Adobe |
| **Caregiver** | Nurturing, supportive | Johnson & Johnson |
| **Ruler** | Authoritative, premium | Mercedes-Benz |
| **Innocent** | Simple, optimistic | Coca-Cola |
| **Sage** | Wise, knowledgeable | Google |
| **Explorer** | Adventurous, independent | Patagonia |
| **Outlaw** | Rebellious, disruptive | Harley-Davidson |
| **Magician** | Transformative, visionary | Disney |
| **Hero** | Courageous, determined | Nike |
| **Lover** | Passionate, sensual | Chanel |
| **Jester** | Playful, fun | M&M's |
| **Everyman** | Relatable, down-to-earth | IKEA |

Align archetype to customer personality; strengthens storytelling.

## Brand Voice & Tone

| Element | Definition | Example |
|---------|------------|---------|
| **Voice** | Brand personality; consistent across touchpoints | Professional / Friendly / Technical / Bold |
| **Tone** | How you say it; adapts to context | Confident but not arrogant; helpful; concise |
| **Avoid** | Buzzwords, terms to never use | "streamline," "revolutionize," "synergy" |
| **Preferred** | Terms to use consistently | "audit" not "analysis"; "customer" not "user" |

**Product marketing context Section 8**: Document voice, tone, avoid, preferred terms. See **project-context** template.

## Brand Visual Identity (Strategy Layer)

| Element | Strategy | Implementation |
|---------|----------|-----------------|
| **Colors** | Primary, secondary, CTA; industry mapping | **brand-visual-generator** |
| **Typography** | Display + body; hierarchy; pairing | **brand-visual-generator** |
| **Logo** | Variants, clear space, minimum size | **logo-generator** |
| **Imagery** | Tone, subject matter, visual mood | Brand guidelines |
| **Consistency** | Same identity across web, social, product | All touchpoints |

For full visual specs (fonts, HEX, spacing), see **brand-visual-generator**. For logo placement and implementation, see **logo-generator**.

## Brand Guidelines Structure

Single source of truth. Include:

- **Purpose & values**: Why you exist; what you stand for
- **Positioning**: One-liner; differentiation
- **Story**: Origin story; hero's journey summary
- **Voice & tone**: Voice, tone, avoid, preferred
- **Logo**: Usage rules, clear space, variants (light/dark)
- **Colors**: Primary, secondary, CTA (HEX, RGB, CMYK)
- **Typography**: Font families, hierarchy, sizing
- **Imagery**: Photography tone; iconography style

## Output Format

- **Brand strategy** (purpose, values, positioning, differentiation)
- **Story** (origin story, hero's journey, narrative arc)
- **Voice & tone** (voice, tone, avoid, preferred)
- **Archetype** (if applicable)
- **Visual** (high-level; defer to brand-visual-generator for specs)
- **Context template** for project-context Sections 8, 12

## Related Skills

- **about-page-generator**: About page implements brand story, mission, values
- **homepage-generator**: Homepage implements value prop, differentiation, brand voice
- **logo-generator**: Logo placement, implementation; branding defines logo rules
- **brand-visual-generator**: Typography, colors, spacing; branding defines visual strategy
- **media-kit-page-generator**: Media kit hosts brand guidelines
- **directory-submission**: Directory copy uses brand voice; Section 8 Brand & Voice
- **title-tag, meta-description**: Metadata uses brand voice
- **integrated-marketing**: Brand awareness across PESO
- **domain-selection**: Domain choice (Brand/PMD/EMD, TLD); do before or with branding when choosing domain
- **domain-architecture**: Domain structure implements brand architecture (Branded House vs House of Brands)
- **rebranding-strategy**: Rebrand execution; domain change, 301, announcement
