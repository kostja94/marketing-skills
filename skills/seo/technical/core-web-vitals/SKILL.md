---
name: core-web-vitals
description: When the user wants to optimize Core Web Vitals, fix LCP, INP, or CLS issues. Also use when the user mentions "Core Web Vitals," "CWV," "LCP," "INP," "CLS," "FID," "page speed," "page performance," "Largest Contentful Paint," "Interaction to Next Paint," "Cumulative Layout Shift," or "Page Experience."
metadata:
  version: 1.0.0
---

# SEO Technical: Core Web Vitals

Guides optimization of Core Web Vitals (CWV)—Google's user experience metrics that affect search ranking. CWV are confirmed ranking factors for mobile and desktop.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **LCP** (Largest Contentful Paint): Loading performance; time to render largest content element
- **INP** (Interaction to Next Paint): Responsiveness; replaced FID in March 2024
- **CLS** (Cumulative Layout Shift): Visual stability; unexpected layout shifts

## Target Thresholds (75th percentile, field data)

| Metric | Target | Good | Needs Improvement | Poor |
|--------|--------|------|-------------------|------|
| **LCP** | ≤2.5s | ≤2.5s | 2.5–4.0s | >4.0s |
| **INP** | ≤200ms | ≤200ms | 200–500ms | >500ms |
| **CLS** | <0.1 | ≤0.1 | 0.1–0.25 | >0.25 |

**Source**: [Google Page Experience](https://developers.google.com/search/docs/appearance/page-experience)

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for site URL.

Identify:
1. **Tools**: GSC Core Web Vitals report, PageSpeed Insights, Chrome DevTools
2. **Metrics**: Which metric is failing (LCP, INP, CLS)
3. **Page type**: Hero, article, product, list—LCP candidate differs

## LCP Optimization

LCP measures the time until the largest content element (image, video, or text block) is visible.

| Cause | Fix |
|-------|-----|
| **Slow server response** | Reduce TTFB; use CDN; optimize server |
| **Render-blocking resources** | Defer non-critical CSS/JS; inline critical CSS |
| **Large images** | WebP/AVIF; compress; `width`/`height` to prevent CLS; see **image-optimization** |
| **Client-side rendering** | SSR/SSG for above-fold content; see **rendering-strategies** |
| **Third-party scripts** | Load async; defer non-critical |

**LCP candidates**: Hero image, large text block, video poster. Ensure above-fold images use `loading="eager"` (default); never lazy-load LCP.

## INP Optimization

INP measures responsiveness—time from user interaction to next paint. Replaced FID in March 2024.

| Cause | Fix |
|-------|-----|
| **Long-running JS** | Break tasks >50ms; use `requestIdleCallback`; Web Workers |
| **Heavy event handlers** | Debounce/throttle; defer non-critical work |
| **Main thread blocking** | Reduce third-party scripts; defer non-critical JS |
| **Layout thrashing** | Batch DOM reads/writes; avoid forced reflows |

## CLS Optimization

CLS measures unexpected layout shifts.

| Cause | Fix |
|-------|-----|
| **Images without dimensions** | Always set `width` and `height` attributes |
| **Dynamic content** | Reserve space for ads, embeds; use `min-height` |
| **Web fonts** | `font-display: optional` or `swap`; preload critical fonts |
| **Animations** | Use `transform` instead of `top`/`left`/`width` |

**Reserve space**: For images, ads, embeds—define dimensions before load. Avoid inserting content above existing content without reserved space.

## Tools & Monitoring

| Tool | Use |
|------|-----|
| **GSC** | Core Web Vitals report; URL grouping; field data |
| **PageSpeed Insights** | Lab + field data; mobile + desktop |
| **Chrome DevTools** | Performance panel; LCP element; layout shift overlay |

## Output Format

- **Current state**: Which metrics fail (LCP, INP, CLS)
- **Prioritized fixes**: By impact
- **References**: [Web Vitals](https://web.dev/vitals/), [Page Experience](https://developers.google.com/search/docs/appearance/page-experience)

## Related Skills

- **image-optimization**: LCP image optimization; WebP; lazy loading (below-fold only)
- **google-search-console**: CWV report; field data monitoring
- **mobile-friendly**: Mobile-first indexing; mobile CWV targets
- **rendering-strategies**: SSR/SSG for LCP; content in initial HTML
- **site-crawlability**: Redirect chains waste crawl; fix for performance
