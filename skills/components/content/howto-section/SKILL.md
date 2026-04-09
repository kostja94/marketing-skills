---
name: howto-section-generator
description: When the user wants to create, optimize, or audit a HowTo section block—an in-page block of ordered steps with optional Schema.org HowTo JSON-LD. Also use when the user mentions "HowTo section," "how-to section," "steps section," "quick start," "walkthrough," "tutorial block," "3 steps," "N steps," "simple steps," "tutorial steps," "step-by-step block," "HowTo schema," "HowTo JSON-LD," "instruction steps," "numbered steps SEO," "horizontal tabs for steps," or "procedure section." This skill is for a section inside a page, not a full page template—use article-page-generator, docs-page-generator, or tools-page-generator for page-level layout. For FAQ Q&A blocks, use faq-page-generator. For structured data details beyond HowTo, use schema-markup. For article body copy only, use article-content.
metadata:
  version: 1.0.3
---

# Components: HowTo Section

Guides **HowTo as an in-page section**: a block of **ordered steps** (and optional **HowTo** JSON-LD) embedded **inside** article, documentation, tool, or landing pages. **Not** a standalone page type—parent page structure and templates come from **article-page-generator**, **docs-page-generator**, **tools-page-generator**, **landing-page-generator**, etc. Distinct from **FAQ** (Q&A → FAQPage) and from **full article body** drafting alone (**article-content**). **schema-markup** remains the source for exhaustive Schema.org property rules and type-wide tables; this skill owns **section-level** placement, copy, HTML, and HowTo-vs-FAQ decisions.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## HowTo Section vs FAQ Section

| Dimension | HowTo section | FAQ section |
|-----------|---------------|-------------|
| **Intent** | User follows **ordered steps** to complete a task | User reads **Q&A pairs** for doubts |
| **Structure** | Steps (1→2→3), optional tools/time/supplies | Question → answer per item |
| **Schema** | **HowTo** (Schema.org) | **FAQPage** |
| **UI** | Often **horizontal tabs** for steps; or **numbered list** in flow | Often **vertical accordion** |
| **Skill** | **howto-section-generator** (this) | **faq-page-generator** |

Do not mark FAQ content as HowTo or vice versa; schema must match visible content.

## Placement Within the Parent Page

This section is always **part of** a larger page. Typical positions:

| Location | When |
|----------|------|
| **After intro (and optional TL;DR / Key Takeaways)** | Article: context first, then **solution = steps** |
| **As the main middle of the page** | Tutorial-heavy article where the HowTo block carries most of the value |
| **After product/tool context** | Tool or LP: short context → **How to use** steps → FAQ/CTA |

**Narrative**: Align with **PAS** for how-to articles—**Problem** in intro; **Agitation** in brief context; **Solution** = the HowTo section. **Answer-first** still applies **per step** (see below).

**Parent page vs URL split**: Whether the **parent** is one article URL or a separate doc/tool URL is decided by **content-strategy**, **article-page-generator**, **docs-page-generator**, or **tools-page-generator**. This skill only defines the **HowTo block**; if each tab were a **different ranking topic**, use **separate URLs** (pillar/cluster). If all steps are **one task**, keep **one page** with one HowTo section (or multiple sections only if clearly separated).

## Content Structure

### Headings and lists

#### Section title (H2)

Headings should **describe the topic or purpose** (WCAG 2.4.6)—not just decorate. Prefer one primary H2 for the procedure; match **page type** and **search intent**.

| Pattern | Best for | Examples |
|---------|----------|----------|
| **Outcome / task (default)** | Blog posts, guides, most informational “how to …” queries | “How to [verb] [outcome]”, “[Task] step by step” |
| **Product or tool** | Tool pages, LP blocks after hero | “How to use [Product]”, “Using [Tool]” |
| **Quick start / walkthrough** | Docs, onboarding | “Quick start”, “Walkthrough”, “Get started with [X]” |
| **Numbered hook** (“In 3 steps …”, “3 simple steps to …”) | Short LP/tool copy when **simplicity** is the message | Use **only** if the visible `<ol>` (and HowTo JSON-LD `step` list) has **exactly** that many steps |

**Rules**

- **Avoid** a bare **“Steps”** or **“Instructions”** as the only H2 text when you can name the outcome—screen reader and scan users lose context.
- **Count in the title**: If you use “3 steps” / “In 4 steps” in the H2, tabs, or subheads, the on-page list and **HowTo** schema must show the **same** number of steps (no extra steps only in JSON-LD).
- **Volatile UIs**: If step count may change with releases, prefer **non-count** titles (“How to …”) and put “three main steps” in body copy if needed.
- **Language**: Mirror the query (e.g. “How to …” for EN informational intent); localized pages: same intent in `inLanguage` as the visible heading.

- **Steps**: Use **semantic ordered list** `<ol>` with `<li>` per step; **bold** the step title inside the `<li>` if needed.
- **Sub-steps**: Nested `<ol>` or H3 under a step when the step is long.
- **Avoid**: Fake lists built only with `<div>`—hurts extraction and accessibility.

### Answer-first per step

- In each step (or immediately under each step heading), give a **direct answer in ~40–60 words**—what to do—then tools, screenshots, edge cases.
- Matches **featured-snippet** list patterns and **article-content** QAE (Question → short Answer → Evidence).

### Word count (article context)

- **Standard how-to articles** often land **~1,000–1,500 words** total for a single topic; the HowTo section is often the bulk of “actionable” depth. See **article-content** for full ranges by type.

## Featured Snippets & SERP

| Format | Role |
|--------|------|
| **List snippet** (~19% of snippet formats) | How-to, steps, options—use `<ol>` / `<ul>` |
| **Schema** | **FAQPage, HowTo, Article** support **identifying** extractable blocks; **not required** for Featured Snippets |
| **HowTo ↔ snippet** | **HowTo** maps to **list-style** position-zero; **desktop** support historically stronger; **mobile** may be limited |

See **featured-snippet**, **serp-features**.

## Schema.org: HowTo (JSON-LD)

**Use case**: Tutorials, procedural guides, **visible** step sequences **in this section**.

**Principles** (detail in **schema-markup**):

- **JSON-LD** in `<script type="application/ld+json">`; properties must **match visible content**—no hidden-only steps.
- **Google**: HowTo was **high-impact** for rich results on **desktop**; **mobile** support is **limited/context-dependent**. Google may have **deprecated or reduced HowTo rich results** (2023–2024); **Schema.org** still defines HowTo; **Bing and AI systems** may still consume it.
- **GEO**: HowTo is among types that help AI cite structured procedures (**generative-engine-optimization**).

**Where the section lives** (parent page type)

| Parent page type | Typical embedding |
|------------------|-------------------|
| **Blog / guide** | HowTo section inside the article body |
| **Documentation** | Guides/tutorials—often **TechArticle** + **HowTo** per **docs-page-generator** |
| **Free tool / calculator** | **SoftwareApplication** + **HowTo** for “how to use” per **tools-page-generator** |

**Multilingual**: `inLanguage` on HowTo (and related types) aligned with hreflang; localize step text in JSON-LD. See **schema-markup**.

**Validation**: [Rich Results Test](https://search.google.com/test/rich-results), [Schema.org Validator](https://validator.schema.org/).

## UI: Tabs, accordions, and crawlability

| Pattern | Guidance |
|---------|----------|
| **Horizontal tabs** | Good for **Step 1 \| Step 2 \| Step 3** when all steps are **one topic**; see **tab-accordion** |
| **DOM** | All step content must be in the **initial HTML**—no AJAX load on tab click |
| **Default open** | First tab or first step **visible by default** |
| **Primary vs secondary** | If the HowTo **is** the page’s main value, avoid burying **all** steps in low-priority hidden UI; crawlers index hidden content, but **primary** intent should be clear |

**Vertical accordion** for **steps** is less common than for FAQ; if used, same rules: **server-rendered**, first item expanded, content in DOM at load (**rendering-strategies**).

## GEO

- Clear **steps**, **self-contained** paragraphs per step, and **HowTo** JSON-LD help models cite procedures.
- Layer with **TL;DR / Key Takeaways** at article level when appropriate (**article-content**, **generative-engine-optimization**).

## Zero-click

- Informational queries (“how to …”) often **zero-click**; optimize for **citation** in AI Overviews as well as CTR (**serp-features**).

## Best Practices Checklist

- [ ] One primary **H2** (or clear section) for the procedure; wording matches page type (outcome vs quick start vs counted steps)
- [ ] If the title mentions a **step count**, it matches **`<ol>`** length and **HowTo** `step` items
- [ ] **`<ol>`** steps with concise, **answer-first** lines per step
- [ ] **HowTo** JSON-LD aligned with visible steps (and `totalTime` / `tool` / `supply` if shown on page)
- [ ] Not confused with **FAQPage** for Q&A lists
- [ ] Tabs/accordions: full content in DOM; first panel visible
- [ ] Validated with Rich Results Test / Schema.org Validator

## Output Format

- **Placement** of the section **within the parent page** (after intro, mid-body, before FAQ, etc.)
- **Outline**: H2 structure, ordered list, optional sub-steps
- **Section title rationale**: Why this H2 pattern (outcome vs quick start vs “In *N* steps”) fits the parent page and query
- **Copy notes**: answer-first per step; length targets
- **HowTo JSON-LD** outline (required properties for your case)
- **UI** note (tabs vs inline list) and **crawlability** requirements
- **Differentiation** from FAQ on the same page if both exist
- **Explicit**: This output is a **section block**, not a full page wireframe—defer page chrome to **article-page-generator** / **docs-page-generator** / **tools-page-generator** as appropriate

## Related Skills

- **schema-markup**: HowTo JSON-LD; properties; Google/Bing/AI notes; `inLanguage`
- **featured-snippet**: List snippets; H2/H3; 40–60 word patterns
- **serp-features**: HowTo in rich results; Featured Snippet vs rich results; zero-click
- **tab-accordion**: Horizontal tabs for steps; DOM; FAQ vs HowTo UI
- **heading-structure**: H2/H3 hierarchy for step titles and section outline
- **article-content**: How-to body copy, PAS, QAE, word counts, TL;DR
- **article-page-generator**: Single post **page** layout, metadata, Article schema alongside a HowTo **section**
- **landing-page-generator**: LP pages that embed a HowTo **section** before FAQ/CTA
- **faq-page-generator**: FAQ **sections**; FAQPage—do not mix with HowTo schema
- **docs-page-generator**: Documentation **site/page** structure; TechArticle + HowTo for guides
- **tools-page-generator**: Tool **page**; SoftwareApplication + HowTo for usage instructions
- **content-strategy**: Pillar/cluster; when to split topics to new URLs
- **content-optimization**: Lists, headings, keyword placement in longform
- **generative-engine-optimization**: GEO; citation strategy
- **rendering-strategies**: SSR/SSG; content in initial HTML
- **video-optimization**: If steps are primarily video-led

## References

- [Schema.org: HowTo](https://schema.org/HowTo)
- [Understanding 2.4.6 Headings and Labels (WCAG 2.2)](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html) (descriptive headings)
- [Google: Structured data intro](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) (verify current supported types in Search Gallery)
- [Featured snippets overview](https://developers.google.com/search/docs/appearance/featured-snippets) (content structure)
