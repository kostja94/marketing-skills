---
name: comparison-table-generator
description: When the user wants to create, optimize, or audit a comparison table section—an in-page block (HTML table or responsive equivalent) comparing products, methods, or approaches, with optional supporting copy. Also use when the user mentions "comparison table," "compare table," "feature matrix," "vs table," "side-by-side comparison," "competitor comparison," "traditional vs modern," "manual vs automated," "before and after," "old way vs new way," "alternatives comparison block," or "comparison section on landing page or blog." This skill is for a section inside a page, not a full alternatives URL or blog post wireframe—use alternatives-page-generator for page-level layout, keywords, and PPC destination strategy. For full-page structured data rules, use schema-markup. For FAQ blocks paired with the table, use faq-page-generator.
metadata:
  version: 1.0.0
---

# Components: Comparison Table Section

Guides **comparison tables as an in-page section**: a **scannable matrix** (rows × columns) embedded **inside** landing pages, blog posts, pricing pages, homepages, or docs. **Not** a standalone page type—parent page structure, URLs, and "alternatives vs blog" decisions come from **alternatives-page-generator**, **landing-page-generator**, **article-page-generator**, **pricing-page-generator**, etc. Distinct from **FAQ** (Q&A → FAQPage) and from **HowTo** (procedure → HowTo). **schema-markup** remains the source for exhaustive Schema.org rules; this skill owns **section-level** criteria, copy, HTML/accessibility, fairness, and ad alignment.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Comparison Table Section vs Alternatives Page

| Dimension | Comparison table **section** (this skill) | Alternatives / compare **page** |
|-----------|-------------------------------------------|----------------------------------|
| **Scope** | One block: headings, table, footnotes, optional CTA line | Full page or article: headline, intro, verdict, listicles, FAQ, metadata |
| **URL / intent** | Chosen by parent; section supports **commercial** or **informational** parent | Owns **"X alternatives"**, **"X vs Y"**, PPC landing strategy |
| **PPC** | Align **copy and criteria** with ad and parent LP | Owns **where** paid traffic lands (dedicated LP vs blog) |
| **Skill** | **comparison-table-generator** (this) | **alternatives-page-generator** |

Use **both** when building an alternatives LP: **alternatives-page-generator** for page structure; **comparison-table-generator** for the **table** itself (criteria, rows, cells, fairness).

## Comparison Types (Same Component, Different Framing)

| Type | Rows / columns | Typical use |
|------|------------------|-------------|
| **Product vs product** | You vs 1–N competitors or tools | Alternatives LP, category pages, blog "best X" |
| **Traditional vs modern** | Old workflow vs your approach | Category creation, thought leadership, LP objection handling |
| **Manual vs automated** | Spreadsheets, agencies, DIY vs product | Mid-funnel LP, demo request pages |
| **Before / after** | State A vs State B (metrics allowed if true) | Outcome-focused LP, case studies |
| **Feature / capability matrix** | Features as rows; plans or products as columns | Pricing-adjacent, **features-page-generator** context |

**Column count**: Prefer **4–7 columns** including names; more columns hurt mobile—use **priority columns** above the fold and **expand** or **link** to full spec.

## Placement Within the Parent Page

| Location | When |
|----------|------|
| **After hero + short value prop** | LP: remove doubt early; **before** long prose |
| **After "problem" / "why switch"** | Alternatives or comparison article: user is ready for criteria |
| **Before FAQ** | Table answers "which is better for X?"; FAQ handles objections |
| **Mid-article** | Blog: after context; supports **featured-snippet** table patterns |

**Narrative**: Table should **answer** the promise of the H1/H2—do not bury the matrix below unrelated storytelling.

## Content Structure

### Section title (H2)

- **Default**: Outcome or task-oriented—"How [Product] compares to [Competitor]," "[Category] comparison at a glance," "Traditional vs [Your approach]."
- **Avoid**: Vague **"Comparison"** alone; match query language where relevant (**"vs"**, **alternatives**, **best for**).

### Intro (1–3 sentences)

- State **who** the table is for and **criteria** (e.g. "pricing as of [date]," "SMB-focused").
- **Transparency**: "We sell [Product]; we include [Competitor] because users search for both."

### The table

- **HTML `<table>`** with `<thead>`, `<th>` scope, **`<caption>`** (summary for screen readers).
- **Cells**: Short phrases, icons, or **Yes/No/Limited**—avoid marketing fluff in cells; **footnote** nuance.
- **Parity**: Compare on **dimensions competitors would accept**; cherry-picked rows erode trust and **GEO** citation.
- **Last updated**: Row or footnote—**pricing** and **limits** must be refreshable.

### Below the table

- **Optional**: One **"Best for"** line per column (if not already in table).
- **CTA**: Single primary CTA aligned with parent page (trial, demo, contact)—not one CTA per competitor cell unless design system allows.

## SEO

- **Intent**: Often **commercial**; align headings and intro with **"vs"**, **alternatives**, **best [category]** modifiers.
- **Snippets**: Semantic **table** + clear **headers** support **list/table** extraction; see **featured-snippet**.
- **Keywords**: Work **natural** competitor names into **caption**, **headings**, or intro—avoid stuffing; **alternatives-page-generator** owns keyword strategy for full URLs.

## GEO (AI Search)

- **Extractable facts**: Tables with **plain text** in cells are easier for models to cite than long paragraphs.
- **Fairness**: Acknowledge **where a competitor is strong**—overly biased matrices are less likely to be summarized neutrally in AI answers.
- **Entity clarity**: Use **consistent** product names (same spelling as in **entity-seo** / **Organization**).

## Paid Ads Alignment

- **Message match**: Table **criteria** and **headline** should reflect ad copy (e.g. "cheaper," "faster," "no code")—see **paid-ads-strategy**, **landing-page-generator**.
- **Landing**: Competitor brand campaigns → **dedicated LP** with comparison section; **alternatives-page-generator** + **google-ads** for policy.

## Accessibility & Mobile

- **Never** rely on **images only** for the matrix—use a real table; images can supplement.
- **Responsive**: Horizontal scroll with visible focus, or **card** layout per row on small screens (**tab-accordion** patterns only if content stays in DOM).
- **Color**: Don't encode meaning by color alone (WCAG contrast).

## Fairness, Legal, Trademark

- **Factual claims**: Prices, limits, **integrations**—cite **source** or "as of [date]"; no invented specs.
- **Trademark**: Use competitor names **accurately** for **comparison** (nominative use); avoid confusing logos without permission—follow legal review.
- **Tone**: **FUD** and **disparagement** hurt trust and SEO; **objective** tables win.

## Schema (High Level)

- **FAQ** below the table → **FAQPage** if Q&A pairs; see **faq-page-generator**.
- **Product** / **Offer** on product pages—see **schema-markup**; this skill does not duplicate schema tables.
- **No** fake **HowTo** for comparison tables.

## Anti-Patterns

- **Screenshot-only** comparison (no crawlable text).
- **Hidden columns** that only favor you (users and reviewers notice).
- **Stale pricing**—add refresh **owner** or **date** in content workflow.

## Best Practices Checklist

- [ ] **`<table>`** with `<caption>`, header cells, semantic structure
- [ ] Criteria **fair** and **parity** across columns
- [ ] **Intro** states bias (you are the vendor) and **evaluation** frame
- [ ] **Last updated** or **as-of** for volatile fields
- [ ] **Mobile** usable (scroll or card fallback)
- [ ] **PPC** / **H1** alignment if traffic is paid
- [ ] Paired **FAQ** or short copy for objections if parent page needs it

## Output Format

- **Placement** of the section within the parent page
- **Comparison type** (product vs product, traditional vs modern, etc.)
- **Column/row design** (criteria list; row labels)
- **Draft table** (HTML outline or Markdown grid with cell guidance)
- **Footnotes** for nuanced cells
- **Fairness** notes (what to acknowledge about competitors)
- **Ad alignment** notes (if PPC)
- **Explicit**: Section block only—defer full page wireframe to **alternatives-page-generator** / **landing-page-generator** / **article-page-generator**

## Related Skills

- **alternatives-page-generator**: Full alternatives/compare **page** or blog; keywords, PPC destination, URL strategy
- **landing-page-generator**: LP structure; when comparison sits on a paid LP
- **article-page-generator**: Blog posts with comparison **section**
- **pricing-page-generator**: Pricing grids and comparisons; **features-page-generator** for feature matrix context
- **faq-page-generator**: FAQ below or beside comparison table
- **featured-snippet**: Table/list snippet patterns
- **schema-markup**: Product, FAQPage, Article—full JSON-LD rules
- **entity-seo**: Entity naming and consistency for GEO
- **paid-ads-strategy**, **google-ads**: Competitor brand ads, message match
- **competitor-research**: Research inputs; **not** end-user copy
- **tab-accordion**: Optional mobile patterns; DOM visibility
- **content-optimization**: Headings and keyword placement in longform

## References

- [Comparison Page SEO: How to Rank for "X vs Y" Queries](https://vydera.com/en/lab/comparison-page-seo) (Vydera)—table centrality, snippet/AI citation
- [Effective Comparison Pages: Steps for Better Conversion](https://www.semrush.com/blog/effective-comparison-pages) (Semrush)—conversion, structure
- [Competitor comparison landing pages](https://www.wordtune.com/blog/competitor-comparison-landing-pages) (Wordtune)—tone, fairness
- [Understanding 1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html) (WCAG)—tables and semantics
