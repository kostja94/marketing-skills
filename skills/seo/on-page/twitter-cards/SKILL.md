---
name: seo-on-page-twitter-cards
description: When the user wants to add or optimize Twitter Card metadata for X (Twitter) link previews. Also use when the user mentions "Twitter Card," "twitter:card," "twitter:image," "X preview," or "tweet preview."
metadata:
  version: 1.0.0
---

# SEO On-Page: Twitter Cards

Guides implementation of Twitter Card meta tags for X (Twitter) link previews. Twitter falls back to Open Graph if Twitter-specific tags are missing; add both for best results.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Social Sharing)

- **Twitter Cards**: X-specific meta tags; control how links appear when shared on X/Twitter

## Card Types

| Type | Use case |
|------|----------|
| **summary** | Small card with thumbnail |
| **summary_large_image** | Large prominent image (recommended; 1200×675px) |
| **app** | Mobile app promotion |
| **player** | Video/audio content |

## Recommended Tags (summary_large_image)

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Your Title">
<meta name="twitter:description" content="Your description">
<meta name="twitter:image" content="https://example.com/image.jpg">
<meta name="twitter:site" content="@yourusername">
<meta name="twitter:creator" content="@authorusername">
<meta name="twitter:image:alt" content="Alt text for image">
```

| Tag | Guideline |
|-----|-----------|
| **twitter:card** | Required; `summary_large_image` for most pages |
| **twitter:title** | Max 70 chars; concise title |
| **twitter:description** | Max 200 chars; summary |
| **twitter:image** | Absolute URL; unique per page |
| **twitter:site** | @username of website |
| **twitter:creator** | @username of content creator |
| **twitter:image:alt** | Alt text; max 420 chars; accessibility |

## Image Requirements

| Item | Guideline |
|------|-----------|
| **Aspect ratio** | 2:1 |
| **Minimum** | 300×157 px |
| **Recommended** | 1200×675 px |
| **Max** | 4096×4096 px |
| **File size** | Under 5MB |
| **Formats** | JPG, PNG, WebP, GIF (first frame only); SVG not supported |

## Common Mistakes

- Missing Twitter Card tags (Twitter won't display images properly without them)
- Using relative image URLs instead of absolute https://
- Images too small or wrong aspect ratio
- Title/description too long (gets truncated)

## Implementation

### Next.js (App Router)

```tsx
export const metadata = {
  twitter: {
    card: 'summary_large_image',
    title: '...',
    description: '...',
    images: ['https://example.com/twitter.jpg'],
    site: '@yourusername',
    creator: '@authorusername',
  },
};
```

### HTML (generic)

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Your Title">
<meta name="twitter:description" content="Your description">
<meta name="twitter:image" content="https://example.com/image.jpg">
<meta name="twitter:site" content="@yourusername">
<meta name="twitter:image:alt" content="Alt text">
```

## Testing

- **X (Twitter)**: [Card Validator](https://cards-dev.twitter.com/validator)

## Related Skills

- **components-social-share**: Share buttons use Twitter Cards for X previews when users share; Cards must be set for share buttons to show proper previews
- **seo-on-page-open-graph**: OG tags; Twitter falls back to OG if Twitter tags missing
- **seo-on-page-title**: Title tag often mirrors twitter:title
- **seo-on-page-description**: Meta description often mirrors twitter:description
- **seo-on-page-metadata**: Hreflang, other meta tags
- **platforms-x**: X post copy and engagement (different from link previews)
