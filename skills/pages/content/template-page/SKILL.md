---
name: template-page-generator
description: When the user wants to design template pages—aggregation (gallery/hub) or detail (individual template). Also use when the user mentions "template page," "template gallery," "template hub," "template detail page," "template marketplace," "programmatic template," "CMS templates," "design templates," "vibe coding templates," "UI templates," "template for users to use," or "template + data pages." For SEO-at-scale strategy (data-driven URL sets), use programmatic-seo.
metadata:
  version: 1.2.0
---

# Pages: Template Page

Guides template page design for two distinct use cases: **(1) Programmatic SEO** — template + data = scale; **(2) User-facing templates** — users browse, select, and use templates to generate their own content (CMS, images, websites, vibe coding). See **programmatic-seo** for the scale framework. This skill covers **template aggregation pages** (gallery, hub) and **template detail pages** (individual template with "use" flow).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

---

## Two Template Page Types

| Type | Purpose | Examples |
|------|---------|----------|
| **Template aggregation page** | Gallery, hub, category; list templates for browse and filter | Canva /templates, Figma templates, VibeCatalog /templates, uitovibe theme gallery |
| **Template detail page** | Individual template; preview, description, **"Use this template"** CTA | Single template page; user clicks to copy, customize, or open in editor |

---

## Core Function: Users Use Templates to Generate Content

Beyond SEO, template pages enable **direct use**: users select a template and generate their own content. Common patterns:

| Domain | Flow | Examples |
|--------|------|----------|
| **CMS** | Browse templates → Select → Create page/post from template | WordPress themes, Webflow templates, Notion templates |
| **Design / Images** | Browse → Preview → Customize in editor | Canva (Customize this template), Figma (Duplicate to your drafts) |
| **Website builders** | Browse → Select → Customize (colors, fonts, content) → Deploy | VibeCatalog, Lovable, Bolt.new, v0; dashboard, landing page, SaaS templates |
| **Vibe coding** | Browse UI themes → Copy style instructions → Add to AI prompt → Generate | uitovibe (copy instructions, paste into Bolt/Lovable/Cursor prompt) |

**Key CTA**: "Use this template," "Customize this template," "Copy to editor," "Get this template," "Start with this."

---

## Template Aggregation Page (Gallery / Hub)

| Section | Purpose |
|---------|---------|
| **Headline** | "Templates for [category]" or "Browse [X] templates" |
| **Filters / Categories** | By type (dashboard, landing page, resume), platform (Bolt, Lovable, Next.js), use case |
| **Template cards** | Thumbnail, name, short description, "Use" or "Preview" CTA; grid or list |
| **Search** | By keyword, tag |
| **Social proof** | "X templates," "Used by Y users," ratings |
| **CTA** | Primary action (Browse, Get started, Sign up to use) |

**Reference**: Canva organizes by 50+ design types (Docs, Presentations, Logos, Instagram Posts, etc.); Figma offers 300+ templates; VibeCatalog by project type (dashboards, landing pages). See **card** for template card structure and grid layout.

---

## Template Detail Page (Individual Template)

| Section | Purpose |
|---------|---------|
| **Hero** | Template name, one-line benefit; **primary CTA: "Use this template" / "Customize" / "Copy"** |
| **Preview** | Live preview, screenshot, or interactive demo; multiple views (desktop, mobile) |
| **Description** | What it does, who it's for, what's included |
| **Features / What's included** | Components, sections, customization options (colors, fonts, layouts) |
| **How to use** | Steps: Copy → Paste in editor / Open in [tool] → Customize |
| **Platform compatibility** | Bolt, Lovable, v0, Next.js, React, etc. |
| **FAQ** | "Can I use commercially?", "Do I get source code?", "How do I customize?" |
| **Related templates** | Internal links to similar templates |

**Vibe coding pattern** (uitovibe, VibeCatalog): Template = style instructions or full code; user copies instructions into AI prompt or downloads/clones to customize. CTA: "Copy instructions," "Add to prompt," "Get template."

---

## Template + Programmatic SEO

When templates are **generated at scale** from data (location pages, integration pages, comparison pages), use **programmatic-seo** framework:

| Section | Purpose | Data Slot |
|---------|---------|-----------|
| **Intro** | H1, intro; matches intent | `{entity_name}`, `{context}` |
| **Evidence block** | Tables, lists, verified data; avoids thin content | `{data_table}`, `{list_items}` |
| **Decision** | Recommendation, next steps | `{recommendation}` |
| **FAQ** | Schema-friendly Q&A | `{faq_items}` |
| **CTA** | Conversion | `{cta_destination}` |

See **programmatic-seo** for data, automation, pitfalls. When programmatic pages have conversion goals, apply **landing-page-generator** principles.

---

## Template + Landing Page (Conversion-Focused Programmatic)

When programmatic pages drive signup/lead capture (e.g., "[Product] for [City]" LPs), apply landing page structure to the template: Stop the scroll → Earn trust → Explain value → Remove doubt → Make the ask. See **landing-page-generator**.

---

## Common Template Patterns by Domain

| Domain | Aggregation | Detail | Use Flow |
|--------|-------------|--------|---------|
| **Design (Canva, Figma)** | Category browse, filters | Preview, "Customize" | Open in editor, drag-and-drop |
| **Vibe coding (uitovibe, VibeCatalog)** | Theme gallery, by style | Copy instructions, "Add to prompt" | Paste into Bolt/Lovable/Cursor |
| **Website (Lovable, Bolt, v0)** | By project type | Live demo, "Use template" | Clone, customize, deploy |
| **CMS** | By content type | Preview, "Create from template" | New page/post from template |
| **Programmatic SEO** | N/A (data-driven) | Output pages from template + data | Informational; CTA to product |

---

## Output Format

- **Page type** (aggregation vs detail)
- **Sections** (per type above)
- **Primary CTA** ("Use this template," "Customize," "Copy instructions")
- **User flow** (browse → preview → use → customize)
- **Programmatic alignment** (if template + data scale)
- **Schema** (ItemList for aggregation; CreativeWork, SoftwareApplication for detail)

## Related Skills

- **card**: Template card structure; thumbnail, name, description, CTA; grid layout
- **grid**: Template grid layout; responsive columns
- **programmatic-seo**: Template + data = scale; use cases, data requirements, pitfalls
- **landing-page-generator**: Conversion structure; programmatic landing pages
- **tools-page-generator**: Tool pages at scale; toolkit hub
- **alternatives-page-generator**: Alternatives/comparison at scale
- **category-page-generator**: Category structure; similar to template aggregation
- **schema-markup**: ItemList, CreativeWork, SoftwareApplication
- **url-structure**: /templates, /templates/[slug] hierarchy
