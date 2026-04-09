---
name: mobile-friendly
description: When the user wants to optimize for mobile-first indexing or fix mobile usability. Also use when the user mentions "mobile-friendly," "mobile-first indexing," "mobile SEO," "responsive design," "mobile adaptation," "mobile viewport," "viewport meta," "touch targets," "font size mobile," "AMP," or "Accelerated Mobile Pages." For viewport meta, use page-metadata.
metadata:
  version: 1.1.2
---

# SEO Technical: Mobile-Friendly

Guides mobile-first indexing optimization and mobile usability. Google uses the mobile version of pages for indexing and ranking; mobile-friendliness is a ranking factor.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **Mobile-first indexing**: Google primarily crawls and indexes mobile version
- **Mobile adaptation**: Responsive design, viewport, breakpoints
- **Content parity**: Mobile and desktop content should match (or mobile preferred)
- **Mobile usability**: Viewport, font size, touch targets, no intrusive interstitials
- **AMP**: Accelerated Mobile Pages—status and when to consider

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for site URL.

Identify:
1. **Site type**: Responsive, separate AMP, dynamic serving
2. **Content parity**: Does mobile show same content as desktop?
3. **Tools**: GSC Mobile Usability report; [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)

## Mobile-First Indexing Requirements

| Requirement | Action |
|-------------|--------|
| **Content parity** | Mobile version must include same primary content as desktop; avoid hiding key content on mobile |
| **Structured data** | Same schema on mobile and desktop; ensure mobile URLs in schema |
| **Metadata** | Same title, meta description on mobile |
| **Media** | Images should be crawlable; avoid lazy-loading above-fold images |

## Responsive Design & Mobile Adaptation

**Responsive design** = Single HTML; CSS media queries adapt layout to screen size. **Preferred** for SEO: one URL, no duplicate content.

| Principle | Practice |
|-----------|----------|
| **Mobile-first** | Design for mobile first; enhance for desktop |
| **Fluid layout** | Use `%`, `vw`, `flex`, `grid`; avoid fixed pixel widths |
| **Breakpoints** | Common: 320px, 768px, 1024px, 1280px; match device widths |
| **Images** | Responsive images (`srcset`, `sizes`); see **image-optimization** |

## Viewport

The viewport meta tag tells browsers how to scale and size the page on mobile. **Required** for mobile-friendly pages.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

| Attribute | Purpose |
|-----------|---------|
| `width=device-width` | Match viewport to device screen width |
| `initial-scale=1` | 1:1 scale on load; prevents zoom |
| `maximum-scale` | Avoid disabling zoom (accessibility) |
| `user-scalable=no` | **Avoid**—hurts accessibility |

**Without viewport**: Desktop layout shrunk; horizontal scroll; fails Mobile-Friendly Test. See **page-metadata**.

## Mobile Usability Checklist

| Element | Guideline |
|---------|-----------|
| **Viewport** | See above; required for mobile-friendly |
| **Font size** | 16px minimum for body text; avoid zooming to read |
| **Touch targets** | Buttons/links ≥48×48px; adequate spacing between taps |
| **Content width** | No horizontal scrolling; content fits viewport |
| **Intrusive interstitials** | Avoid popups that block main content on mobile |

## Common Issues

| Issue | Fix |
|-------|-----|
| **Content hidden on mobile** | Show critical content; avoid accordion/tabs for primary content |
| **Flash / unsupported** | Replace with HTML5 alternatives |
| **Text too small** | Use base font ≥16px; avoid `font-size` in px <12 |
| **Links too close** | Increase tap target size; add padding |

## Responsive vs. Separate URLs

| Approach | When | Note |
|----------|------|-----|
| **Responsive** | Preferred | Single URL; same HTML, CSS media queries |
| **Dynamic serving** | Same URL, different HTML by user-agent | Ensure mobile content parity |
| **Separate URLs** | m.example.com | Use canonical + hreflang; see **canonical-tag**, **page-metadata** |

## Accelerated Mobile Pages (AMP)

AMP is a web component framework for fast-loading pages. **Status (2024–2025)**: Still supported; no longer required for Top Stories or ranking.

| Aspect | Note |
|--------|------|
| **Ranking** | No ranking advantage over well-optimized responsive pages |
| **Top Stories** | AMP no longer required since 2021; Core Web Vitals suffice |
| **When to consider** | News sites, ad-heavy pages, very slow hosting—but responsive + CWV usually better |
| **Alternative** | Responsive design + **core-web-vitals** optimization; SSR/SSG; see **rendering-strategies** |

**Recommendation**: For most sites, prioritize responsive design and Core Web Vitals over AMP. AMP adds maintenance (separate AMP HTML); modern optimization offers similar performance with more flexibility.

## Output Format

- **Mobile Usability status**: Pass/fail from GSC or Mobile-Friendly Test
- **Responsive / viewport**: Check viewport meta; breakpoints; fluid layout
- **Content parity**: Mobile vs desktop content check
- **AMP**: Only if legacy or specific use case
- **Fixes**: Prioritized by impact

## Related Skills

- **page-metadata**: Viewport meta tag; required for mobile
- **core-web-vitals**: CWV measured on mobile; replaces AMP for Top Stories; LCP, INP, CLS
- **canonical-tag**: Separate mobile URLs; hreflang for mobile
- **image-optimization**: Responsive images; mobile LCP
- **rendering-strategies**: SSR/SSG for fast mobile load
- **google-search-console**: Mobile Usability report
