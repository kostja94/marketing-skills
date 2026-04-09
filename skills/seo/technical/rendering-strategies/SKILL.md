---
name: rendering-strategies
description: When the user wants to choose or optimize rendering strategy for SEO. Also use when the user mentions "SSR," "SSG," "CSR," "ISR," "static rendering," "dynamic rendering," "server-side rendering," "client-side rendering," "JavaScript rendering," "pre-rendering," "prerender," "content in initial HTML," or "crawler visibility." For crawl issues, use site-crawlability.
metadata:
  version: 1.0.2
---

# SEO Technical: Rendering Strategies

Guides rendering strategy selection and optimization for search engine and AI crawler visibility. **Golden rule**: Page data and metadata must be available on page load without JavaScript execution for optimal SEO.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **Static vs dynamic**: SSG, SSR, ISR, CSR; when to use each
- **Crawler behavior**: Googlebot renders JS (with delays); AI crawlers do not
- **Component-level**: Content in initial HTML; tabs, carousels, nav
- **Dynamic rendering**: Prerender for bots when full SSR/SSG is not feasible

## Rendering Methods

| Method | When HTML generated | SEO | Best for |
|--------|---------------------|-----|----------|
| **SSG** (Static Site Generation) | Build time | ✅ Best | Blog, docs, marketing pages; content rarely changes |
| **SSR** (Server-Side Rendering) | Request time | ✅ Good | News, product pages; dynamic, personalized content |
| **ISR** (Incremental Static Regeneration) | Build + revalidate | ✅ Good | Large sites; static with periodic updates |
| **CSR** (Client-Side Rendering) | Browser (after JS) | ❌ Poor | Dashboards, account pages; no SEO needed |
| **Dynamic rendering** | On-demand for bots | ✅ Fallback | SPAs; prerender for crawlers, SPA for users |

### SSG (Static Site Generation)

HTML generated at build time; same HTML for every request. **Best for SEO**: crawlers receive full HTML immediately; optimal performance.

- **Use when**: Blog, docs, marketing pages, content that doesn't change frequently
- **Framework**: Next.js `getStaticProps`, Astro, Gatsby

### SSR (Server-Side Rendering)

HTML generated on each request. **Good for SEO**: crawlers receive complete HTML; supports dynamic, personalized content.

- **Use when**: News, product pages, user-specific content
- **Tradeoff**: Higher server load; slower TTFB than SSG
- **Framework**: Next.js `getServerSideProps`, Remix

### ISR (Incremental Static Regeneration)

Static at build; pages can revalidate after a period. **Good for SEO**: combines static performance with freshness.

- **Use when**: Large sites (millions of pages); content updates periodically
- **Framework**: Next.js `revalidate` in `getStaticProps`

### CSR (Client-Side Rendering)

Server sends minimal HTML shell; content renders in browser after JS loads. **Not for SEO**: crawlers may see empty content; indexing delays or failures.

- **Use when**: Dashboards, account pages, internal tools—no search visibility needed
- **Avoid for**: Public content, marketing pages, blog

### Dynamic Rendering

Serve prerendered HTML to crawlers; serve SPA to users. **Fallback** when full SSR/SSG is not feasible (e.g. legacy SPA migration).

- **How**: Detect crawler user-agent; route to prerender service (e.g. Prerender.io) or headless render
- **When**: JavaScript-heavy sites; migration period; product/docs with CSR
- **Note**: Google permits this; prerendered content should match user experience

## Crawler Behavior

| Crawler | JavaScript | Content in initial HTML |
|---------|------------|-------------------------|
| **Googlebot** | Renders JS (Chrome); may have multi-day queue | Full weight; SSR/SSG preferred |
| **AI crawlers** (GPTBot, ClaudeBot, PerplexityBot) | Do **not** execute JS | **Required**—CSR content invisible |
| **Bingbot** | Renders JS | Same as Googlebot |

**AI crawlers**: ~28% of Googlebot's crawl volume. Critical content (articles, meta, nav) must be in initial HTML. See **site-crawlability** for AI crawler optimization; **generative-engine-optimization** for GEO.

## Component-Level: Content in Initial HTML

Google does **not** simulate user clicks (tabs, carousels, "Load more"). Content loaded via AJAX or on interaction is not discoverable.

| Component | Requirement | Implementation |
|------------|-------------|----------------|
| **Tabs / Accordion** | All tab content in DOM at load | Server-render; use `<details>`/`<summary>` or CSS show/hide |
| **Carousel** | All slides in initial HTML | Server-render; CSS/JS for show/hide only |
| **Hero** | Headline, CTA, LCP image in HTML | No JS-only rendering |
| **Navigation** | All nav links in first paint | No JS-injected menus for critical links |

**Recommendation**: Server-render (SSR/SSG) all critical content; use JS only for interaction (show/hide, animation). Content loaded on click = not indexed.

## Decision Guide

| Content type | Rendering | Reason |
|--------------|-----------|--------|
| Blog, docs, marketing | SSG or ISR | Best SEO; fast; static |
| Product, news, dynamic | SSR | Fresh content; crawler-ready |
| Dashboard, account | CSR | No SEO; auth required |
| Legacy SPA | Dynamic rendering | Bridge until SSR/SSG migration |

## Output Format

- **Current setup**: SSG, SSR, CSR, or hybrid
- **Recommendation**: By page type
- **Component checks**: Tabs, carousel, nav—content in initial HTML?
- **References**: [Next.js Rendering](https://nextjs.org/learn/seo/rendering-strategies), [Vercel SSR vs SSG](https://vercel.com/blog/nextjs-server-side-rendering-vs-static-generation)

## Related Skills

- **site-crawlability**: AI crawler optimization; SSR for critical content; URL management
- **generative-engine-optimization**: GEO; AI crawlers don't execute JS
- **core-web-vitals**: LCP; SSR/SSG for above-fold; client-side hurts LCP
- **mobile-friendly**: Mobile-first indexing; content parity
- **tab-accordion**: Content in DOM at load; server-render tabs
- **carousel**: Content in initial HTML; server-render slides
- **hero-generator**: Hero in initial HTML; avoid JS-only
- **navigation-menu-generator**: Nav in first paint; no JS-only menus
