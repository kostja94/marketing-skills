---
name: tab-accordion
description: When the user wants to add or optimize tab or accordion components for content organization. Also use when the user mentions "tab component," "accordion," "expandable content," "collapsible sections," "tabbed content," "FAQ accordion," "how-to tabs," "horizontal tabs," "vertical accordion," "content in tabs," "hidden content SEO," "details summary," or "disclosure widget." For FAQ content, use faq-page-generator.
metadata:
  version: 1.1.1
---

# Components: Tab & Accordion

Guides tab and accordion implementation for organizing content without excessive vertical space. Two layout patterns: **vertical accordion** (FAQ-style, stacked) and **horizontal tabs** (how-to style, side-by-side). Both improve UX by reducing scroll; SEO impact depends on implementation and content placement.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Layout Patterns

| Pattern | Layout | Best for | Example |
|---------|--------|----------|---------|
| **Vertical accordion** | Stacked; expand/collapse one at a time | FAQ, Q&A, long lists, objection handling | "How do I return?" → answer below |
| **Horizontal tabs** | Side-by-side labels; one panel visible | How-to steps, product specs, pricing tiers, comparisons | "Step 1 \| Step 2 \| Step 3" |

**Mobile**: Vertical accordion works well on small screens (natural scroll). Horizontal tabs can feel cramped—consider accordion, dropdown, or full-width tab bar that scrolls.

## SEO: Is It Friendly?

**Google's position**: Google indexes and ranks content inside tabs and accordions fully; hidden content receives full weight (confirmed since 2016 mobile-first indexing). Gary Illyes: "we index the content, its weight is fully considered for ranking."

**Practical nuance**: Some tests show always-visible content outperforms hidden content in rankings. Reserve tabs/accordions for **secondary** content; place primary, keyword-critical content in visible areas.

| Content type | Placement |
|--------------|-----------|
| **Primary / ranking-focused** | Visible above fold; not hidden |
| **Secondary / supporting** | Tabs, accordions acceptable |
| **FAQ answers** | Accordion OK; first item expanded by default; see **faq-page-generator** |

### Indexing Requirements

**Content must be in the DOM on page load.** Google does not simulate user clicks; it cannot "click" tabs to discover content.

| Implementation | Indexed? |
|----------------|----------|
| All tab content in HTML at load | ✅ Yes |
| Content loaded via AJAX on tab click | ❌ No |

**Recommendation**: Server-render all tab content in the initial HTML; use CSS/JS only to show/hide. Prefer `<details>`/`<summary>` or equivalent server-rendered markup. See **rendering-strategies** for SSR, SSG, CSR and crawler visibility.

### Horizontal Tabs: More Tabs, More Content?

**Technically**: Yes—if all content is in the DOM at load, more tabs = more indexable content. Mobile-first indexing gives full weight to tabbed content in HTML.

**Strategically**: Not always. **Signal dilution** occurs when many tabs = many different topics on one page. Google may struggle to understand which query the page should rank for; topical authority and keyword focus get spread thin.

| Scenario | Use tabs? | Alternative |
|----------|-----------|-------------|
| **Same topic** (How-to Step 1/2/3; product specs: dimensions, materials, shipping) | ✅ Yes | — |
| **Different topics** (Service A, Service B, Portfolio, Blog) | ❌ No | Separate URLs per topic; see **content-strategy** for pillar/cluster |

**When many horizontal tabs work**: All tabs semantically related to one query (e.g., one how-to, one product). **When to use separate pages**: Each tab is a distinct topic deserving its own URL, crawl, and ranking opportunity.

## Implementation

### Native HTML (Recommended)

Use `<details>` and `<summary>`—no JavaScript required; accessible; crawlable.

```html
<details open>
  <summary>First question (expanded by default)</summary>
  <p>Answer content here.</p>
</details>
<details>
  <summary>Second question</summary>
  <p>Answer content here.</p>
</details>
```

- **First tab/accordion**: Add `open` attribute so it's expanded by default
- **`<summary>`**: Must be first child of `<details>`; acts as toggle
- **Progressive enhancement**: Style with CSS; add JS only if needed (e.g., close others when one opens)

### JavaScript-Dependent Tabs

If using JS-only tabs: **ensure all tab content is in the DOM at page load**, not loaded via AJAX on click. Google does not simulate tab clicks. Prefer `<details>`/`<summary>` or server-rendered HTML. See **rendering-strategies**.

### Avoid

- Content loaded only after user click (AJAX, lazy-loaded via fetch)—crawlers will not index it
- `display: none` or `visibility: hidden` for primary content—Google may treat differently
- Many tabs with unrelated topics on one page—causes signal dilution; use separate URLs instead

## Content Best Practices

| Practice | Purpose |
|----------|---------|
| **First item expanded** | Ensures primary content visible on load; better for SEO and UX |
| **Descriptive headers** | `<summary>` / tab labels should clearly describe content; include keywords naturally |
| **Logical structure** | H2/H3 for sections; supports snippet extraction; see **featured-snippet** |
| **Answer-first** | For FAQ: 40–60 words direct answer; then detail; see **faq-page-generator** |

## Use Cases

| Use case | Format | Layout | Notes |
|----------|--------|--------|-------|
| **FAQ** | Accordion | Vertical | FAQPage schema; first Q expanded; see **faq-page-generator** |
| **How-to steps** | Tabs | Horizontal | Step 1, Step 2, Step 3; sequential flow |
| **Product specs** | Tabs | Horizontal | Dimensions, materials, shipping—secondary to hero |
| **Long guides** | Accordion | Vertical | Collapsible sections; see **toc-generator** |
| **Pricing tiers** | Tabs | Horizontal | Compare plans; primary CTA visible |
| **Objection handling** | Accordion | Vertical | "What about X?"—supporting conversion |

## Schema & Rich Results

- **FAQ (vertical accordion)**: FAQPage JSON-LD; schema must match on-page content exactly; see **schema-markup**, **faq-page-generator**
- **How-to (horizontal tabs)**: HowTo schema for step-by-step content; see **schema-markup**, **featured-snippet**
- **Other tabs**: No specific schema; ensure semantic HTML (headings, structure)

## UX & Accessibility

- **Visual indicator**: Arrow, plus/minus, or chevron to show expand/collapse state
- **Keyboard**: `<details>`/`<summary>` natively keyboard-accessible
- **Core Web Vitals**: Avoid layout shift (CLS) when expanding; reserve space or animate smoothly
- **Mobile**: Touch targets ≥44×44px; vertical accordion often better than horizontal tabs on small screens (tabs can be cramped; accordion scrolls naturally)

## Pre-Implementation Checklist

- [ ] All tab/accordion content in DOM at page load (no AJAX on click)
- [ ] Primary ranking content visible, not hidden
- [ ] First tab/accordion expanded by default
- [ ] Using `<details>`/`<summary>` or equivalent server-rendered HTML
- [ ] Headers descriptive; keywords natural
- [ ] Tabs share one topic (avoid signal dilution); if different topics, consider separate pages
- [ ] For FAQ: FAQPage schema matches content

## Related Skills

- **faq-page-generator**: FAQ structure, answer length, schema; accordion is common FAQ UI
- **featured-snippet**: Answer-first, H2/H3; content in accordions can be extracted
- **schema-markup**: FAQPage for FAQ accordions; HowTo for step-by-step tabs
- **content-strategy**: Pillar/cluster architecture; when to use separate pages vs tabs
- **toc-generator**: Collapsible TOC; similar disclosure pattern
- **content-optimization**: Word count, structure, multimedia in expandable sections
- **rendering-strategies**: SSR, SSG, CSR; content in initial HTML for crawlers
