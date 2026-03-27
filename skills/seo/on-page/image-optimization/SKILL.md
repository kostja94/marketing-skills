---
name: image-optimization
description: When the user wants to optimize images for search engines and performance. Also use when the user mentions "image SEO," "alt text," "image captions," "figcaption," "image optimization," "WebP," "lazy loading," "LCP," "image sitemap," "responsive images," "srcset," "image format," or "hero image optimization." For CWV, use core-web-vitals.
metadata:
  version: 1.2.1
---

# SEO On-Page: Image Optimization

Guides image optimization for Google Search (text results, Image Pack, Google Images, Discover), Core Web Vitals (LCP), and accessibility. Consolidates image-related best practices from components (hero, trust-badges) and pages (landing-page). References: [Google Image SEO](https://developers.google.com/search/docs/appearance/google-images), [Semrush Image SEO](https://www.semrush.com/blog/image-seo/).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Discovery & indexing**: HTML img elements, image sitemap
- **Format & performance**: WebP, responsive images, lazy loading, LCP; full CWV optimization in **core-web-vitals**
- **Metadata**: Alt text, file names, captions
- **Preferred image**: primaryImageOfPage, og:image; thumbnail next to title/description in search results
- **Structured data**: ImageObject, image in Article/Product/etc.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for brand and page context.

Identify:
1. **Context**: Hero, content page, product, trust badge, social preview
2. **Above vs below fold**: LCP candidate (hero) vs lazy-loadable
3. **Image count**: Single hero vs gallery, programmatic pages

---

## 1. Discovery & Indexing

### Use HTML Image Elements

Google finds images in the `src` attribute of `<img>` (including inside `<picture>`). **CSS background images are not indexed.**

| Do | Don't |
|----|-------|
| `<img src="puppy.jpg" alt="Golden retriever puppy" />` | `<div style="background-image:url(puppy.jpg)">` |

### Image Sitemap

Submit an [image sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps) to help Google discover images it might otherwise miss. Image sitemaps can include URLs from CDNs (other domains); verify CDN domain in Search Console for crawl error reporting.

**Structure** (from Google):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://example.com/page</loc>
    <image:image>
      <image:loc>https://example.com/image.jpg</image:loc>
    </image:image>
  </url>
</urlset>
```

See **xml-sitemap** for sitemap index and submission. Image sitemap is an extension; can be standalone or combined with page sitemap.

---

## 2. Format & Performance

### Supported Formats

Google supports: **BMP, GIF, JPEG, PNG, WebP, SVG, AVIF**. Match filename extension to format.

| Format | Best for | Notes |
|--------|----------|-------|
| **WebP** | Photos, graphics | Smaller files, faster load; lossy + lossless; transparency, animation |
| **AVIF** | Modern browsers | Even smaller than WebP; check support |
| **JPEG** | Standard photos | Fallback; widely supported |
| **PNG** | Transparency, detail | Larger; use when needed |
| **SVG** | Icons, logos | Scalable; use `<title>` for inline SVG alt |
| **GIF** | Simple animation | First frame only for preview |

### Responsive Images

Use `<picture>` or `srcset` for different screen sizes. **Always provide fallback `src`**—some crawlers don't understand srcset.

```html
<img
  srcset="image-320w.jpg 320w, image-480w.jpg 480w, image-800w.jpg 800w"
  sizes="(max-width: 320px) 280px, (max-width: 480px) 440px, 800px"
  src="image-800w.jpg"
  alt="Descriptive alt text">
```

**Picture element** (format fallback, e.g. WebP → PNG):

```html
<picture>
  <source type="image/webp" srcset="image.webp">
  <img src="image.png" alt="Descriptive alt text">
</picture>
```

### Data URI (Inline Images)

Base64 data URIs (`data:image/...;base64,...`) reduce HTTP requests but increase HTML size. Use sparingly for small icons; avoid for large images. See [web.dev](https://web.dev/articles/embedding-images-and-video#data_uris).

### Resize & Compress

- **Max width**: Generally ≤2,500px; match container max-width
- **Compression**: WebP preferred; quality 75–85 for lossy; 72dpi for web
- **LCP**: Hero/above-fold images are LCP candidates; optimize aggressively

### Lazy Loading

Use `loading="lazy"` **only for below-fold images**. Above-fold images (hero) must load immediately—lazy loading them hurts LCP.

```html
<img src="hero.jpg" alt="..." loading="eager">
<img src="below-fold.jpg" alt="..." loading="lazy">
```

---

## 3. Alt Text

Alt text improves **accessibility** (screen readers, low bandwidth) and **SEO** (Google uses it with computer vision to understand images). It also serves as anchor text if the image is a link.

### Best Practices

| Do | Don't |
|----|-------|
| Useful, information-rich description | Keyword stuffing |
| Context of page content | "image of" or "photo of" (redundant) |
| Max ~125 characters (some assistive tech truncates) | Empty alt on meaningful images |
| Descriptive for functional images | Alt on purely decorative images (use `alt=""`) |

**Examples** (from Google):

- ❌ Missing: `<img src="puppy.jpg"/>`
- ❌ Stuffing: `alt="puppy dog baby dog pup pups puppies..."`
- ✅ Better: `alt="puppy"`
- ✅ Best: `alt="Dalmatian puppy playing fetch"`

### Captions

Google extracts image context from captions and nearby text. Use `<figcaption>` or descriptive text near the image.

| Use | Purpose |
|-----|---------|
| **Topic relevance** | Caption describes image subject; supports indexing |
| **Featured Snippets** | Images near answers with captions can capture thumbnail slots; see **featured-snippet** |
| **Image Pack** | Alt + caption + file name help Image Pack display; see **serp-features** |

### Inline SVG

Use `<title>` inside SVG for accessibility:

```html
<svg aria-labelledby="svgtitle1">
  <title id="svgtitle1">Descriptive text for the SVG</title>
</svg>
```

---

## 4. File Names

Descriptive filenames give Google light clues about subject matter.

| Do | Don't |
|----|-------|
| `apple-iphone-15-pink-side-view.jpg` | `IMG00353.jpg` |
| Short, hyphen-separated | Generic: `image1.jpg`, `pic.gif` |
| Localize filenames for translated pages | Overly long filenames |

---

## 5. Preferred Image (SERP Thumbnail & Discover)

When users search for keywords, optimized images can appear as **thumbnails next to the page title and description** in search results—enhancing visibility and CTR. Google also uses these images for Google Discover. [Search Engine Land](https://searchengineland.com/google-uses-both-schema-org-markup-and-ogimage-meta-tag-for-thumbnails-in-google-search-and-discover-470598)

Google selects thumbnails automatically from multiple sources. Influence selection via:

### Schema: primaryImageOfPage

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "url": "https://example.com/page",
  "primaryImageOfPage": "https://example.com/images/cat.png"
}
```

Or attach `image` to main entity (e.g. BlogPosting, Article) via `mainEntity` or `mainEntityOfPage`.

### Open Graph

```html
<meta property="og:image" content="https://example.com/images/cat.png">
```

**Preferred image rules**: Relevant, representative; avoid generic (e.g. logo) or text-heavy images; avoid extreme aspect ratios; high resolution. See **open-graph**, **twitter-cards** for social specs.

**Google Discover** (if targeting Discover): ≥1200px wide; ≥300KB; 16:9 aspect ratio preferred; important content visible in landscape crop.

---

## 6. Page Context

- **Title & meta description**: Google uses page title and meta for image result snippets. See **title-tag**, **meta-description**.
- **Placement**: Put images near relevant text; page subject matter influences image indexing.
- **Same URL**: Reference the same image with the same URL across pages for cache efficiency and crawl budget.

---

## 7. Structured Data

Add structured data for rich results in Google Images (badges, extra info). Image attribute is required for eligibility. See **schema-markup** for ImageObject, Article, Product, Recipe, etc.

---

## 8. Specs by Context

| Context | Priority | Notes |
|---------|----------|-------|
| **Hero** | LCP, alt, no lazy | See **hero-generator**; above-fold, fast load |
| **Article / Blog hero** | 1200–1600px wide; proportional height; 1200×630 for og:image | Same image for Schema, Open Graph, Twitter Cards; under 200 KB; WebP preferred; descriptive alt; set width/height to prevent CLS; use srcset/sizes for responsive; articles with relevant images get ~94% more views |
| **Trust badges** | Alt text | See **trust-badges-generator**; e.g. "Norton Secured" |
| **Landing page** | All above | See **landing-page-generator** Pre-Delivery Checklist |
| **OG / Twitter** | 1200×630, 1200×675 | See **open-graph**, **twitter-cards** |
| **Platforms** | Per-platform | X, LinkedIn, Pinterest—see platform skills |

---

## 9. Opt-Out & SafeSearch

- **Inline linking opt-out**: Prevent full-sized image display in Google Images via HTTP referrer check (200 or 204). See [Google docs](https://developers.google.com/search/docs/appearance/google-images#opt-out).
- **SafeSearch**: Label pages for explicit content if applicable.

---

## Output Format

- **Alt text** suggestions per image
- **Captions** (if applicable; snippet/Image Pack context)
- **File name** recommendations
- **Format** (WebP, fallback)
- **Responsive** (srcset/sizes or picture)
- **Lazy loading** (above-fold vs below-fold)
- **Image sitemap** (if many images)
- **Preferred image** (schema, og:image) for key pages

## Related Skills

- **core-web-vitals**: LCP, INP, CLS; image optimization supports LCP
- **xml-sitemap**: Sitemap structure; image sitemap extension
- **open-graph, twitter-cards**: og:image, twitter:image; social preview
- **schema-markup**: ImageObject, Article/Product image
- **content-optimization**: Multimedia in content; defers image SEO to this skill
- **featured-snippet**: Images near answers + captions; snippet thumbnail
- **serp-features**: Image Pack; alt, captions, file names
- **visual-content**: Visual content for social, infographics; website images use this skill
