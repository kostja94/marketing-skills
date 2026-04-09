---
name: tools-page-generator
description: When the user wants to create, optimize, or audit free tools pages. Also use when the user mentions "free tools," "tools page," "toolkit," "free [X] tool," "free [X] calculator," "free [X] checker," "lead magnet tool," "programmatic tools," or "tools hub." For content strategy, use content-strategy.
metadata:
  version: 1.0.2
---

# Pages: Tools (Free Tools)

Guides free tools pages that drive traffic and lead generation for the main product. **Tools are free, standalone utilities** — not the primary monetization. They serve the same ICP as the paid product, are often extracted mini-features from the full product (low dev effort), and typically scale via programmatic SEO. Distinct from features (paid capabilities) and resources (content hub).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, ICP, and conversion goals.

Identify:
1. **Tool types**: Calculators, checkers, converters, generators (see Tool Types below)
2. **ICP alignment**: Same audience as paid product; tools solve related problems
3. **Format**: Single tool page vs. toolkit hub + per-tool pages
4. **Gate strategy**: No signup (max traffic) vs. email gate (lead capture) vs. usage limits (taste → upgrade)
5. **Tech**: Often SPA (single-page application); lightweight, fast load

## Tools vs Features

| Dimension | Tools | Features |
|----------|-------|----------|
| **Monetization** | Free; not primary revenue | Paid product capabilities |
| **Purpose** | Lead gen, traffic, trust | Conversion, evaluation |
| **Content** | Standalone utility; excerpt from product | Full product capability list |
| **Scale** | Many tools; programmatic keywords | Fewer, curated |
| **Format** | Often SPA; toolkit hub | Benefit-led grid/list |
| **User intent** | "I need to do X now" (task) | "What can this product do?" (evaluation) |

## Tool Page Structure

| Section | Purpose |
|---------|---------|
| **Headline** | Task-focused; "Free [X] Checker" or "Calculate [Y] in Seconds" |
| **Tool UI** | Input → process → output; minimal friction |
| **Instructions** | 1–3 steps; "Enter URL → Click Analyze → Get Results" |
| **Tool description** | What it does, who it's for; SEO content |
| **FAQ** | Tool-specific: "What is [X]?", "How is [Y] calculated?" |
| **CTA** | "Get full access" / "Try [Product] free" — link to main product |
| **Related tools** | Internal links to other tools in toolkit |

## Toolkit Hub Page Structure

| Section | Purpose |
|---------|---------|
| **Headline** | "Free [Category] Tools" or "Free Tools to [Outcome]" |
| **Category tabs/sections** | e.g., SEO Tools, AI Writing Tools, Local SEO (Semrush pattern) |
| **Tool cards** | Name, one-line benefit, CTA to tool page |
| **How to use** | Short ordered procedure (often 3 steps for hubs); e.g. Choose tool → Enter info → Get results. Section **H2** per **howto-section-generator**—prefer outcome/tool-led (“How to use these tools”) or “In *N* steps …” **only** when *N* matches the visible steps |
| **CTA** | "Access 50+ tools with free account" |
| **Social proof** | Logos, "Trusted by X brands" |

## Tool Types (Common Patterns)

| Type | Examples | Programmatic potential |
|------|----------|-------------------------|
| **Calculators** | ROI, LTV, loan, salary, carbon footprint | "[X] calculator" keywords |
| **Checkers** | SEO, backlink, plagiarism, grammar, keyword rank | "[X] checker" keywords |
| **Converters** | Unit, currency, file format, encoding | "[X] to [Y] converter" |
| **Generators** | Sitemap, meta tags, FAQ schema, titles | "[X] generator" keywords |
| **Analyzers** | Content, readability, sentiment | "[X] analyzer" keywords |

## Best Practices

### Lead Gen Focus

- **Taste of product**: Tool delivers instant value; CTA offers "more" (full product, higher limits)
- **No signup preferred** for top-of-funnel; email gate or limits for bottom-of-funnel tools
- **Usage limits**: e.g., 3 checks/day free → upgrade for unlimited (Semrush, Ahrefs pattern)

### Same ICP, Lower Friction

- **Extract from product**: One capability from full product; low dev cost
- **Same keywords**: Tools rank for "[X] tool" while product ranks for "[X] software"
- **Bridge**: Tool users → trial signup when they hit limits or need more

### Programmatic SEO

- **Keyword patterns**: "[keyword] checker," "[city] [tool]," "[X] calculator" — template + data
- **Scale**: Many tools; each targets long-tail; see **programmatic-seo**
- **Template**: Same structure per tool; unique input/output, FAQ, meta

### Technical

- **SPA-friendly**: Single page, client-side processing; fast load
- **Schema**: SoftwareApplication, HowTo for tool pages
- **Mobile-first**: Tools often used on-the-go

## URL Structure

| Pattern | Example |
|---------|---------|
| **Hub** | /tools, /free-tools |
| **Category** | /free-tools/seo, /tools/calculators |
| **Per tool** | /free-tools/seo-checker, /tools/roi-calculator |

## SEO

- **Intent**: Informational + Transactional (task completion)
- **Title**: "Free [X] Tool \| [Product]" or "[X] Checker — No Signup"
- **Programmatic**: Template + keyword/data; avoid thin content; each tool adds unique value

## Output Format

- **Tool list** (types, names, keywords)
- **Toolkit hub structure** (if multiple tools)
- **Per-tool page structure** (sections, CTA placement)
- **Gate strategy** (no signup vs email vs limits)
- **Internal linking** (hub ↔ tools, tools ↔ product)
- **Programmatic template** (if scaling)
- **SEO** metadata

## Related Skills

- **card**: Tool card structure; name, benefit, CTA; grid layout for toolkit hub
- **grid**: Toolkit hub grid layout; responsive columns
- **features-page-generator**: Tools ≠ features; tools are free lead gen; features are paid capabilities; link from tools to product/features
- **programmatic-seo**: Tools at scale; template + data; keyword patterns
- **resources-page-generator**: Tools can be a section in resources; or standalone /tools
- **landing-page-generator**: Tool page as lead-capture LP when gated
- **schema-markup**: SoftwareApplication, HowTo for tool pages
- **howto-section-generator**: "How to use" step section; HowTo JSON-LD with tool usage copy
