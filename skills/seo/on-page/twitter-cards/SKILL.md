---
name: twitter-cards
description: When the user wants to add, audit, implement, or optimize Twitter Card metadata for X link previews, including twitter:card, twitter:title, twitter:description, twitter:image, or X previews. For a full metadata lifecycle use page-metadata; for broader social previews use open-graph.
metadata:
  version: 2.0.0
---

# SEO On-Page: Twitter Cards

Owns X/Twitter Card writing and implementation rules. **page-metadata** owns the full-page lifecycle and release verification. Platforms may use Open Graph fallbacks, so define X-specific copy only when it adds value.

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
| **twitter:title** | Concise social title; same page identity as SEO/OG copy, not necessarily identical text |
| **twitter:description** | Accurate social summary without unsupported claims |
| **twitter:image** | Absolute URL; unique per page |
| **twitter:site** | @username of website |
| **twitter:creator** | @username of content creator |
| **twitter:image:alt** | Alt text; max 420 chars; accessibility |

## Image Requirements

| Item | Guideline |
|------|-----------|
| **Aspect ratio** | 2:1 |
| **Minimum** | 300×157 px |
| **Recommended** | Use a high-resolution image suited to the selected card and verify current platform behavior |
| **Delivery** | Absolute HTTPS URL with a successful image response |
| **Format and size** | Verify against current X documentation when implementation depends on exact limits |

## Common Mistakes

- Missing Twitter Card tags (Twitter won't display images properly without them)
- Using relative image URLs instead of absolute https://
- Images too small or wrong aspect ratio
- Title/description too long (gets truncated)
- Mechanically copying SEO copy when the share context needs different wording
- Changing the product identity or promise between SEO, OG, and X metadata

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

Inspect the deployed initial HTML and test an actual share/preview workflow available to the current X product. Do not depend on the retired public Card Validator as a release gate. Allow for cached previews.

## Related Skills

- **social-share-generator**: Share buttons use Twitter Cards for X previews when users share; Cards must be set for share buttons to show proper previews
- **open-graph**: OG tags; Twitter falls back to OG if Twitter tags missing
- **title-tag**, **meta-description**: Search copy; may differ while preserving page identity
- **page-metadata**: Full lifecycle, source-of-truth implementation, and production validation
- **twitter-x-posts**: X post copy and engagement (different from link previews)
- **twitter-card-image-generator**: Programmatic Twitter Card image generation — 1200×675px, 2:1 ratio, player card posters, dark mode adaptations for ~40% of X users, timeline-safe zone design for mobile 1:1 crop, all 6 visual styles from og-image-generator. This skill covers how to SET the twitter:image tag; twitter-card-image-generator covers how to CREATE the image.
