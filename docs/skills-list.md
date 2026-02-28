# Full Skills List

Complete list of all 83 skills with descriptions. See [README](../README.md) for overview.

## SEO

### Technical

| Skill | Description |
|-------|-------------|
| [robots-txt](../skills/seo/technical/robots/) | Configure and audit robots.txt, AI crawler rules |
| [xml-sitemap](../skills/seo/technical/sitemap/) | Create, audit, and optimize sitemap.xml |
| [canonical-tag](../skills/seo/technical/canonical/) | Configure canonical URLs, fix duplicate content |
| [indexing](../skills/seo/technical/indexing/) | Fix indexing issues, noindex, Search Console |
| [indexnow](../skills/seo/technical/indexnow/) | Implement IndexNow for faster Bing indexing |
| [site-crawlability](../skills/seo/technical/crawlability/) | Redirect chains, broken links, site structure, orphan pages, pagination |

### On-Page

| Skill | Description |
|-------|-------------|
| [title-tag](../skills/seo/on-page/title/) | Title tag optimization for SERP |
| [meta-description](../skills/seo/on-page/description/) | Meta description optimization for SERP |
| [page-metadata](../skills/seo/on-page/metadata/) | Hreflang, meta robots, viewport, charset |
| [open-graph](../skills/seo/on-page/open-graph/) | Open Graph tags for social sharing |
| [twitter-cards](../skills/seo/on-page/twitter-cards/) | Twitter Card tags for X previews |
| [schema-markup](../skills/seo/on-page/schema/) | Structured data (Schema.org, JSON-LD) |
| [internal-links](../skills/seo/on-page/internal-links/) | Internal linking, link equity, orphan pages |
| [url-structure](../skills/seo/on-page/url-structure/) | URL optimization, hierarchy, slugs |
| [heading-structure](../skills/seo/on-page/heading/) | Heading structure (H1–H6), content outline |

### Off-Page

| Skill | Description |
|-------|-------------|
| [link-building](../skills/seo/off-page/link-building/) | Link building, outreach, link acquisition |
| [backlink-analysis](../skills/seo/off-page/backlink-analysis/) | Backlink audit, toxic links, competitive analysis |

### Content

| Skill | Description |
|-------|-------------|
| [keyword-research](../skills/seo/content/keyword-research/) | Keyword research, search intent, difficulty |
| [content-strategy](../skills/seo/content/content-strategy/) | Content clusters, pillar pages, editorial calendar |
| [content-optimization](../skills/seo/content/content-optimization/) | Word count, H2 keywords, keyword density, tables, lists, multimedia |

## Pages

Page classification framework for navigation design, sitemaps, content strategy, and SEO. Paths: `skills/pages/{brand,content,marketing,legal,utility}/`.

### Classification Dimensions

| Purpose | Goal | Key Metrics |
|---------|------|-------------|
| **Brand** | Build awareness, trust, identity | Brand search, dwell time, trust signals |
| **SEO** | Organic traffic, educate users, topical authority | Organic rankings, traffic, backlinks |
| **Marketing** | Conversion, acquisition, partnership recruitment | Conversion rate, CAC, signups/purchases |
| **Legal** | Compliance, transparency, risk control | Compliance, accessibility |
| **Utility** | Navigation support, UX, system functions | Usability, error recovery |

| Intent | User Stage | Typical Pages |
|--------|------------|---------------|
| **Navigational** | Finding brand/website | Homepage, brand pages |
| **Informational** | Learning, understanding | Blog, guides, glossary, FAQ |
| **Commercial** | Comparing, evaluating | Features, pricing, services, case studies |
| **Transactional** | Buying, signing up, taking action | Product pages, pricing, landing pages |

### Page Mapping

| Purpose | Page | Skill | Intent | Funnel |
|---------|------|-------|--------|--------|
| Brand | Home | [homepage-generator](../skills/pages/brand/home/) | Navigational | Awareness |
| Brand | About | [about-page-generator](../skills/pages/brand/about/) | Navigational | Awareness |
| Brand | Contact | [contact-page-generator](../skills/pages/brand/contact/) | Navigational | Support |
| SEO | Features | [features-page-generator](../skills/pages/content/features/) | Commercial | Consideration |
| SEO | Glossary | [glossary-page-generator](../skills/pages/content/glossary/) | Informational | Awareness |
| SEO | Blog | [blog-page-generator](../skills/pages/content/blog/) | Informational | Awareness |
| SEO | Article | [article-page-generator](../skills/pages/content/article/) | Informational | Awareness |
| SEO | Resources | [resources-page-generator](../skills/pages/content/resources/) | Informational | Awareness |
| SEO | FAQ | [faq-page-generator](../skills/pages/content/faq/) | Informational | Consideration |
| SEO | API | [api-page-generator](../skills/pages/content/api/) | Informational | Consideration |
| Marketing | Pricing | [pricing-page-generator](../skills/pages/marketing/pricing/) | Transactional | Decision |
| Marketing | Products | [products-page-generator](../skills/pages/marketing/products/) | Transactional | Decision |
| Marketing | Services | [services-page-generator](../skills/pages/marketing/services/) | Commercial | Consideration |
| Marketing | Category pages | [category-page-generator](../skills/pages/marketing/category-pages/) | Commercial | Consideration |
| Marketing | Customer stories | [customer-stories-page-generator](../skills/pages/marketing/customer-stories/) | Commercial | Consideration |
| Marketing | Affiliate program | [affiliate-page-generator](../skills/pages/marketing/affiliate-program/) | Transactional | Decision |
| Marketing | Media kit | [media-kit-page-generator](../skills/pages/marketing/media-kit/) | Commercial | Consideration |
| Legal | Privacy | [privacy-page-generator](../skills/pages/legal/privacy/) | — | Support |
| Legal | Terms | [terms-page-generator](../skills/pages/legal/terms/) | — | Support |
| Legal | Cookie policy | [cookie-policy-page-generator](../skills/pages/legal/cookie-policy/) | — | Support |
| Legal | Legal | [legal-page-generator](../skills/pages/legal/legal/) | — | Support |
| Legal | Refund | [refund-page-generator](../skills/pages/legal/refund/) | — | Support |
| Legal | Shipping | [shipping-page-generator](../skills/pages/legal/shipping/) | — | Support |
| Utility | 404 | [404-page-generator](../skills/pages/utility/404/) | — | — |
| Utility | Careers | [careers-page-generator](../skills/pages/utility/careers/) | Commercial | Consideration |

### Best Practices

- **Match intent to page type**: Informational → blog, FAQ, glossary; Commercial → features, pricing, case studies; Transactional → products, pricing.
- **Avoid intent mismatch**: One clear primary goal per page.
- **Internal linking**: Brand → conversion paths; SEO → commercial/transactional; Legal in footer.
- **Indexing**: Brand, SEO, marketing: index; Legal: index but not keyword-optimized; System pages: noindex.
- **Navigation**: Primary nav = brand + core marketing; Secondary = blog, resources, glossary; Footer = legal, contact, utility.

## Components

| Skill | Description |
|-------|-------------|
| [top-banner-generator](../skills/components/top-banner/) | Announcement bar, sticky banner, promo bar |
| [sidebar-generator](../skills/components/sidebar/) | Sidebar for blogs, docs; nav, CTA, related content |
| [popup-generator](../skills/components/popup/) | Popup, modal, lightbox; lead capture, offers |
| [navigation-menu-generator](../skills/components/navigation-menu/) | Navigation menu design, SEO, UX, accessibility |
| [breadcrumb-generator](../skills/components/breadcrumb/) | Breadcrumb navigation, BreadcrumbList schema |
| [social-share-generator](../skills/components/social-share/) | Share buttons (X, LinkedIn, Facebook), placement, intent URLs |
| [footer-generator](../skills/components/footer/) | Footer design, links, SEO, newsletter placement |
| [toc-generator](../skills/components/toc/) | Table of contents for long-form content |
| [hero-generator](../skills/components/hero/) | Hero section design, conversion |
| [logo-generator](../skills/components/logo/) | Logo placement, linking, brand recall |
| [favicon-generator](../skills/components/favicon/) | Favicon, app icons, PWA icons |
| [brand-visual-generator](../skills/components/brand-visual/) | Visual identity, typography, colors, spacing |
| [trust-badges-generator](../skills/components/trust-badges/) | Trust badges, "Trusted by" logos |
| [testimonials-generator](../skills/components/testimonials/) | Testimonials, reviews, customer quotes |
| [cta-generator](../skills/components/cta/) | Call-to-action button design |
| [newsletter-signup-generator](../skills/components/newsletter-signup/) | Newsletter signup form |
| [url-slug-generator](../skills/components/url-slug/) | URL slug creation for content; 3–5 words, SEO-friendly |

## Channels

| Skill | Description |
|-------|-------------|
| [affiliate-marketing](../skills/channels/affiliate/) | Affiliate marketing strategy, CPS model |
| [email-marketing](../skills/channels/email-marketing/) | EDM, newsletter, deliverability, SEO synergy |
| [employee-generated-content](../skills/channels/egc/) | Employee-generated content, employee advocacy |
| [influencer-marketing](../skills/channels/influencer/) | Influencer marketing, KOL, creator partnership |
| [referral-program](../skills/channels/referral/) | Referral program strategy |
| [creator-program](../skills/channels/creator-program/) | Creator program strategy |
| [community-forum](../skills/channels/community-forum/) | Forum promotion, community invitation, Indie Hacker, HN |
| [directory-submission](../skills/channels/directories/) | Directory submission (Taaft, Product Hunt, etc.) |

## Platforms

| Skill | Description |
|-------|-------------|
| [twitter-x-posts](../skills/platforms/x/) | X (Twitter) post copy, threads, image specs |
| [reddit-posts](../skills/platforms/reddit/) | Reddit post copy, subreddit rules |
| [linkedin-posts](../skills/platforms/linkedin/) | LinkedIn post copy, professional content |
| [tiktok-captions](../skills/platforms/tiktok/) | TikTok caption, video specs, script |
| [grokipedia-recommendations](../skills/platforms/grokipedia/) | Grokipedia recommendations, parasite SEO, GEO |

## Strategies

| Skill | Description |
|-------|-------------|
| [generative-engine-optimization](../skills/strategies/geo/) | GEO/AEO for AI search visibility |
| [integrated-marketing](../skills/strategies/integrated-marketing/) | IMC, PESO, program vs channel vs campaign |
| [localization-strategy](../skills/strategies/localization/) | Localization strategy, i18n, multilingual |

## Analytics

| Skill | Description |
|-------|-------------|
| [traffic-analysis](../skills/analytics/traffic/) | Traffic sources, dark traffic, UTM attribution |
| [analytics-tracking](../skills/analytics/tracking/) | GA4, event tracking, conversions |
| [seo-monitoring](../skills/analytics/seo-monitoring/) | SEO data analysis, benchmark, article database |
| [ai-traffic-tracking](../skills/analytics/ai-traffic/) | Track AI search traffic in GA4 and GSC |
| [google-search-console](../skills/analytics/google-search-console/) | GSC analysis, indexing, Core Web Vitals |
