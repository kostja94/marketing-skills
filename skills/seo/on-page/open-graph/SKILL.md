---
name: open-graph
description: When the user wants to add, audit, implement, or optimize Open Graph metadata for social sharing, including og:title, og:description, og:image, og:url, Facebook previews, LinkedIn previews, or social share previews. For a full metadata lifecycle use page-metadata; for X-specific previews use twitter-cards.
metadata:
  version: 2.0.0
---

# SEO On-Page: Open Graph

Owns Open Graph writing and implementation rules for social previews. **page-metadata** owns the full-page lifecycle and release verification.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Social Sharing)

- **Open Graph**: Facebook-originated protocol; controls preview card when links are shared on social platforms

## The 4 Essential Tags

Every shareable page requires these minimum tags:

```html
<meta property="og:title" content="Your Page Title">
<meta property="og:description" content="Your description">
<meta property="og:image" content="https://yourdomain.com/image.png">
<meta property="og:url" content="https://yourdomain.com/page">
```

| Tag | Guideline |
|-----|-----------|
| **og:title** | Concise and useful in a sharing context; same page identity as SEO title, not necessarily identical text |
| **og:description** | Accurate social summary; may differ from the meta description without changing the promise |
| **og:image** | Absolute HTTPS URL; representative of the page; include dimensions when known |
| **og:url** | Stable public page identity; normally the same URL declared canonical |

## Recommended Additional Tags

| Tag | Purpose |
|-----|---------|
| **og:type** | Content type: `website`, `article`, `video`, `product` |
| **og:site_name** | Website name; displayed separately from title |
| **og:image:width** / **og:image:height** | Image dimensions (1200×630px) |
| **og:image:alt** | Alt text for accessibility |
| **og:locale** | Language/territory (e.g., `en_US`); for multilingual sites |

## Image Best Practices

| Item | Guideline |
|------|-----------|
| **Size** | Use a high-resolution image and verify the target platforms' current requirements; 1200×630 is a common cross-platform starting point |
| **Format** | Use a platform-supported web image format and verify the deployed response |
| **URL** | Absolute URL with https://; no relative paths |
| **Unique** | One unique image per page when possible |

## Common Mistakes

- Using relative image URLs instead of absolute https://
- Images too small or wrong aspect ratio
- Empty or placeholder values
- Missing og:url (canonical)
- Reusing a generic logo or unrelated image when a representative page image is available
- Copying SEO title/description mechanically when the share context needs different wording

## Implementation

### Next.js (App Router)

```tsx
export const metadata = {
  openGraph: {
    title: '...',
    description: '...',
    url: 'https://example.com/page',
    siteName: 'Example',
    images: [{ url: 'https://example.com/og.jpg', width: 1200, height: 630, alt: '...' }],
    locale: 'en_US',
    type: 'website',
  },
};
```

### HTML (generic)

```html
<meta property="og:title" content="Your Title">
<meta property="og:description" content="Your description">
<meta property="og:image" content="https://example.com/og.jpg">
<meta property="og:url" content="https://example.com/page">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Your Site">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Alt text">
```

## Testing

- **Facebook**: [Sharing Debugger](https://developers.facebook.com/tools/debug/)
- **LinkedIn**: [Post Inspector](https://www.linkedin.com/post-inspector/)

Preview services cache metadata. Test the deployed absolute URL and refresh the cache when supported. Also inspect the raw initial HTML; a client-only tag insertion may not be available to every scraper.

## Consistency boundary

Open Graph and SEO metadata may use different copy because search and social feeds are different contexts. They must still identify the same page, describe the same product or content, and avoid unsupported claims. Do not require string equality.

## Related Skills

- **social-share-generator**: Share buttons use OG tags for rich previews when users share; OG must be set for share buttons to show proper cards
- **article-page-generator**: Use og:type `article` for article/post pages; article-specific tags (published_time, author)
- **page-metadata**: Full lifecycle, source-of-truth implementation, and production validation
- **title-tag**, **meta-description**: Search copy; may differ while preserving page identity
- **twitter-cards**: Twitter uses OG as fallback; add Twitter-specific tags for best results
- **canonical-tag**: og:url should match canonical URL
- **og-image-generator**: Programmatic OG image generation — 6 visual styles (Terminal/CLI, Magazine Editorial, Swiss Minimal, Pixel Retro, Brutalist, Newspaper), Satori+resvg, Puppeteer, AI image generation tools, and Agent-Native content-aware workflow. This skill covers how to SET the image tag; og-image-generator covers how to CREATE the image.
