---
name: open-graph
description: When the user wants to add or optimize Open Graph metadata for social sharing. Also use when the user mentions "Open Graph," "og:tags," "og:title," "og:image," "og:description," "Facebook preview," "LinkedIn preview," or "social share preview."
metadata:
  version: 1.0.0
---

# SEO On-Page: Open Graph

Guides implementation of Open Graph meta tags for social media previews (Facebook, LinkedIn, Slack, Discord, etc.). Pages with proper OG tags get 2–3× more clicks than bare URL links.

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
| **og:title** | Keep under 60 chars; compelling; match page content |
| **og:description** | 150–200 chars; conversion-focused |
| **og:image** | Absolute URL (https://); 1200×630px recommended |
| **og:url** | Canonical URL; deduplicates shares |

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
| **Size** | 1200×630px (1.91:1 ratio) for Facebook, LinkedIn, WhatsApp |
| **Format** | JPG, PNG, WebP; under 5MB |
| **URL** | Absolute URL with https://; no relative paths |
| **Unique** | One unique image per page when possible |

## Common Mistakes

- Using relative image URLs instead of absolute https://
- Images too small or wrong aspect ratio
- Empty or placeholder values
- Missing og:url (canonical)

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

## Related Skills

- **social-share-generator**: Share buttons use OG tags for rich previews when users share; OG must be set for share buttons to show proper cards
- **article-page-generator**: Use og:type `article` for article/post pages; article-specific tags (published_time, author)
- **page-metadata**: Hreflang, other meta tags
- **title-tag**: Title tag often mirrors og:title
- **meta-description**: Meta description often mirrors og:description
- **twitter-cards**: Twitter uses OG as fallback; add Twitter-specific tags for best results
- **canonical-tag**: og:url should match canonical URL
