---
name: seo-on-page-schema
description: When the user wants to add or optimize structured data (Schema.org, JSON-LD). Also use when the user mentions "schema," "structured data," "JSON-LD," "rich snippets," "FAQ schema," "Article schema," "Organization schema," "JobPosting," "HowTo," "Event," "SoftwareApplication," "BreadcrumbList," "WebSite," "Recipe," "Product," "Dataset," or "GEO."
metadata:
  version: 1.0.0
---

# SEO On-Page: Schema / Structured Data

Guides implementation of Schema.org structured data (JSON-LD) for rich snippets, enhanced search results, and Generative Engine Optimization (GEO).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (On-Page SEO)

- **Schema markup**: Schema.org types for rich results, AI search visibility, and machine-readable content
- **Schema.org vs. search engines**: Schema.org defines 800+ types; each search engine supports only a subset for rich results

## Schema.org vs. Search Engine Support

**Schema.org and Google Structured Data are not fully aligned.** Schema.org is an open vocabulary (800+ types); Google, Bing, and other engines each support only a curated subset for rich results.

| Engine | Support | Notes |
|--------|---------|-------|
| **Google** | Subset only | Only types in [Google's search gallery](https://developers.google.com/search/docs/guides/search-gallery) generate rich results. Valid Schema.org markup not in Google's list won't produce enhanced snippets—even if technically correct. |
| **Bing** | Subset; different | Supports JSON-LD, Microdata, RDFa, Open Graph. Some types (e.g., Product, Offer) have format-specific support. Check [Bing Webmaster docs](https://www.bing.com/webmasters/help/marking-up-your-site-with-structured-data-3a93e731). |
| **Other engines** | Varies | Yandex, DuckDuckGo, AI search tools (Perplexity, etc.) may use Schema.org for understanding even when they don't display rich results. |

**Practical implication**: Implement Schema.org markup for your content type. If Google doesn't show rich results for that type, Bing or AI systems may still use it. Always verify against [Google's developer docs](https://developers.google.com/search/docs) for Google-specific rich result eligibility.

## Generative Engine Optimization (GEO)

**GEO** = optimizing content so AI systems (Google AI Overviews, Perplexity, ChatGPT, Gemini) choose, cite, and quote your content in generated answers.

**Why Schema matters for GEO:**
- Structured data makes content **machine-readable**; AI engines extract and cite information more accurately
- Without schema, AI must infer context; with it, you guide extraction directly
- [Search Engine Land study](https://searchengineland.com/schema-ai-overviews-structured-data-visibility-462353): In controlled tests, **only pages with well-implemented schema appeared in AI Overviews** and achieved best organic ranking. Schema quality—not just presence—matters
- [SEMrush analysis](https://www.semrush.com/blog/technical-seo-impact-on-ai-search-study/) of 5M cited URLs: **Organization, Article, BreadcrumbList** appear most frequently on pages cited by Google AI Mode
- Pages with schema show ~40% higher CTR; GEO tactics can increase AI visibility by up to 40%

**Key Schema types for GEO:** Organization, Person/Author, WebSite, WebPage, FAQPage, HowTo, Article, Product, AggregateRating. Focus on authority (Organization, Person), content structure (Article, FAQPage), and completeness (required properties, correct format).

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product type and content.

Identify:
1. **Page type**: Article, Product, FAQ, Organization, JobPosting, Event, etc.
2. **Content**: What entities to describe
3. **Goal**: Rich snippets, AI Overview visibility, Knowledge Panel

## Schema Type Classification

### Core Types (General Use)

| Type | Use case |
|------|----------|
| **Organization** | Site-wide; company info, logo, sameAs |
| **WebSite** | Site-wide; search action, site name |
| **Article** | Blog posts, news, tool intros |
| **BreadcrumbList** | Breadcrumb navigation |
| **FAQPage** | FAQ sections; triggers PAA-style results |
| **Person** | Author info; pairs with Article |
| **ImageObject** | Image metadata for rich results |
| **HowTo** | Tutorials, step-by-step guides. **Note**: Google may have deprecated HowTo rich results (2023–2024); Schema.org still supports it; Bing/AI may use it |

### Exclusive Types (Specific Scenarios)

| Type | Use case |
|------|----------|
| **JobPosting** | Recruitment sites, AI Job Matching |
| **Product** | E-commerce product pages |
| **Event** | Event pages, ticketing (not general blogs) |
| **SoftwareApplication** | App pages, tool pages |
| **LocalBusiness** | Local business pages |
| **Dataset** | Data platforms, datasets |
| **DiscussionForumPosting** | Forums, community posts |
| **Quiz** | Education, flashcards |
| **MathSolver** | Math tools |
| **CaseStudy** | Case study pages |
| **Recipe** | Recipes, meal plans, cooking instructions |

**Rule**: Use core types for most sites. Use exclusive types only when page content matches (e.g., don't use Event on a blog; don't use JobPosting on a product page).

## Action: Website/Product Type → Schema Mapping

**Use this table to recommend which exclusive schema types fit a site.** Match the site's content and product type to the most relevant schema. When in doubt, start with core types (Organization, WebSite, Article); add exclusive types only when content clearly matches.

| Website / Product type | Recommended exclusive schema | Why |
|------------------------|------------------------------|-----|
| **AI meal planner, recipe site, food blog, cooking app** | **Recipe** | Ingredients, instructions, cook time, servings—highly relevant for food/meal content. Google supports Recipe rich results. |
| **Job board, recruitment site, careers page** | **JobPosting** | Title, company, location, salary, employment type. Required for Google Jobs. |
| **Event platform, ticketing, webinar, conference** | **Event** | Date, location, price. Use only on actual event pages. |
| **SaaS, app, Chrome extension, tool, software product page** | **SoftwareApplication** | App name, category, rating, price, OS. Fits product/feature pages. |
| **E-commerce product page** | **Product** | Price, availability, brand, reviews. Use with Offer, AggregateRating. |
| **Forum, community, Reddit-style, Q&A** | **DiscussionForumPosting** | Post content, author, comments. For user-generated discussion. |
| **Data platform, dataset repository, Scale AI / Surge AI** | **Dataset** | Dataset name, creator, license, distribution format. For data catalog pages. |
| **Education site, flashcards, Quizlet-style** | **Quiz** | Question-answer pairs. For educational Q&A content. |
| **Math solver, calculator, equation tool** | **MathSolver** | Math problem input, solution output. For math tools. |
| **Restaurant, local service, store locator** | **LocalBusiness** | Address, hours, NAP. For local SEO. |
| **Case study, customer story page** | **CaseStudy** | Client, outcome, methodology. For B2B case studies. |
| **FAQ page, product FAQ, support FAQ** | **FAQPage** | Question + acceptedAnswer pairs. Triggers PAA-style results. |
| **Tutorial, how-to guide, step-by-step** | **HowTo** | Steps, tools, time. Note: Google may have deprecated rich results; Bing/AI may still use. |
| **News article, press release** | **NewsArticle** | Use instead of Article for news. |
| **Video page, podcast episode** | **VideoObject** / **PodcastEpisode** | For video/audio content. |

**Examples:**
- **AI meal planner** (e.g., generates weekly meal plans with recipes) → Add **Recipe** schema to each recipe/meal page; **Article** or **WebPage** for landing pages
- **AI writing tool** → **SoftwareApplication** on product page; **Article** on blog
- **Recruitment SaaS** → **JobPosting** on job listing pages; **SoftwareApplication** on product page
- **Recipe blog** → **Recipe** on each recipe post; **Article** for non-recipe posts

**Output**: When recommending schema, state: (1) which exclusive types fit the site/product, (2) which page types get which schema, (3) core types to add site-wide (Organization, WebSite, BreadcrumbList).

## Best Practices

| Principle | Guideline |
|-----------|-----------|
| **Accuracy** | Data must match visible page content; never add invisible or misleading data |
| **Completeness** | Include all required properties per type |
| **Most specific type** | Use NewsArticle over Article when applicable |
| **JSON-LD** | Preferred format; place in `<script type="application/ld+json">` |
| **@id for entities** | Use @id for Organization, Person to enable entity linking across pages |
| **Phased implementation** | Add required properties first; then optional for optimization |
| **Validation** | Test with Rich Results Test and Schema Markup Validator |

## Implementation Workflow

1. **Analyze** page type and content; choose matching Schema type
2. **Select format** — JSON-LD recommended (Google, Bing, AI tools support it)
3. **Write** structured data; start with required properties
4. **Validate** with [Rich Results Test](https://search.google.com/test/rich-results), [Schema Markup Validator](https://validator.schema.org/)
5. **Deploy and monitor** via Search Console enhanced reports

## Common Errors and Fixes

| Error | Fix |
|-------|-----|
| **Data doesn't match visible content** | Schema must describe only what users see |
| **Missing required properties** | Check Google/Schema.org docs for each type |
| **Wrong type for page** | Don't use Event on non-event pages; don't use JobPosting on product pages |
| **Format/syntax errors** | Validate JSON-LD; check quotes, brackets, commas |
| **Over-markup** | Mark only relevant content; avoid stuffing unrelated types |

## Implementation

### Next.js (metadata)

```tsx
export const metadata = {
  other: {
    'script:ld+json': JSON.stringify({
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "...",
      "description": "...",
      "image": "https://example.com/image.jpg",
      "datePublished": "2024-01-01T00:00:00Z",
      "dateModified": "2024-01-15T00:00:00Z",
      "author": { "@type": "Person", "name": "..." },
      "publisher": { "@type": "Organization", "name": "...", "logo": { "@type": "ImageObject", "url": "..." } }
    }),
  },
};
```

### HTML (generic)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "...",
  "description": "...",
  "author": { "@type": "Person", "name": "..." },
  "publisher": { "@type": "Organization", "name": "...", "logo": { "@type": "ImageObject", "url": "..." } }
}
</script>
```

## Validation Tools

| Tool | Purpose |
|------|---------|
| [Google Rich Results Test](https://search.google.com/test/rich-results) | Check if Google can generate rich results |
| [Schema Markup Validator](https://validator.schema.org/) | Validate against Schema.org spec |
| Search Console | Enhanced reports; monitor validity over time |

## Output Format

- **Action first**: Use the Website/Product Type → Schema Mapping table to recommend which exclusive schema fits the site (e.g., AI meal planner → Recipe; SaaS tool → SoftwareApplication)
- **Schema type** recommendation (core vs. exclusive)
- **Page-level mapping**: Which pages get which schema
- **JSON-LD** structure with required properties
- **Validation** steps
- **References**: [Schema.org](https://schema.org/), [Google Structured Data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data), [Bing Markup](https://www.bing.com/webmasters/help/marking-up-your-site-with-structured-data-3a93e731)

## Related Skills

- **pages-article**: Article page structure; Article/BlogPosting/NewsArticle schema implementation
- **seo-on-page-title, seo-on-page-description, seo-on-page-metadata**: Metadata complements schema
- **seo-on-page-heading**: Article schema uses headline (often H1)
- **seo-technical-indexing**: Google Indexing API for JobPosting, BroadcastEvent
- **strategies-geo**: GEO strategy and AI search visibility
- **components-breadcrumb**: BreadcrumbList schema implementation
