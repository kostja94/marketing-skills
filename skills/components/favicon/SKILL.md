---
name: favicon-generator
description: When the user wants to implement, optimize, or audit favicon and app icons. Also use when the user mentions "favicon," "app icon," "browser icon," "touch icon," or "PWA icon."
metadata:
  version: 1.0.0
---

# Components: Favicon

Guides favicon and app icon implementation for brand consistency across browser tabs, bookmarks, mobile home screens, and **Google Search results**. Favicons help users identify sites; missing or incorrect icons hurt trust.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for brand and visual identity.

Identify:
1. **Tech stack**: Next.js, WordPress, static HTML, etc.
2. **PWA**: Is the site a PWA or planning to be?
3. **Existing assets**: Logo, icon files

## Required Sizes (Best Practices 2025)

| Size | Use |
|------|-----|
| **16x16** | Browser tabs, standard displays |
| **32x32** | Retina/HiDPI browser tabs |
| **180x180** | Apple Touch Icon (iOS home screen); no transparency |
| **192x192** | Android Chrome home screen, PWA launcher |
| **512x512** | PWA splash screens, adaptive icons |

**Optional**: 48x48, 96x96, 120x120, 152x152, 167x167, 256x256 for broader coverage.

## Formats

| Format | Use |
|--------|-----|
| **SVG** | Modern browsers; scalable; supports dark mode via media queries; lightweight |
| **PNG** | High-DPI; explicit sizes; easy to generate; required for Apple Touch Icon |
| **ICO** | Legacy; bundles multiple sizes; fallback for older browsers |

**Recommended**: Provide SVG + PNG fallbacks. Never skip Apple Touch Icon (180x180); iOS shows a generic screenshot without it.

## Google Search (SERP Display)

Favicons can appear in Google Search results next to your site's listings. [Google Search Central](https://developers.google.com/search/docs/appearance/favicon-in-search) requirements:

| Requirement | Guideline |
|-------------|-----------|
| **Placement** | Add `<link rel="icon" href="/path/to/favicon.ico">` to **homepage** header |
| **One per hostname** | One favicon per hostname; `example.com` and `code.example.com` are separate; `example.com/sub-site` shares the same favicon |
| **Crawlability** | Googlebot-Image must crawl favicon; Googlebot must crawl homepage; do not block either in robots.txt |
| **Shape** | Square (1:1 aspect ratio); minimum 8x8px; **preferably >48x48px** for quality across platforms |
| **Stable URL** | Do not change favicon URL frequently |
| **Appropriate** | No inappropriate content (pornography, hate symbols); Google may replace with default icon |
| **Timing** | Crawling can take days to weeks; use Search Console URL Inspection to request indexing |

**Supported rel values**: `icon`, `shortcut icon`, `apple-touch-icon`, `apple-touch-icon-precomposed`. **href** can be relative (`/favicon.ico`) or absolute; favicon can be hosted on CDN.

## Implementation

### HTML Link Tags

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
```

### Next.js

Place in `/app`: `favicon.ico`, `icon.png`, `apple-icon.png`. Next.js auto-generates tags.

### PWA Manifest

Include `icons` array in `manifest.json` with 192x192 and 512x512 for maskable icons.

## Best Practices

- **Simplicity**: At 16x16, complex details are illegible; use simplified logo mark; design for brand recognition in SERPs
- **Consistency**: Favicon should match logo/brand (logo-generator, brand-visual-generator)
- **Cache**: Use long cache; version for updates (e.g. `/favicon.ico?v=2`)
- **Tools**: RealFaviconGenerator, favicon.io, or favicons npm package for automation
- **Test**: Check across browsers, dark mode, and Search Console (favicon may take days to weeks to appear)

## Output Format

- **Size** checklist (16, 32, 180, 192, 512; >48x48 for Google Search)
- **Format** recommendations (SVG, PNG, ICO)
- **Implementation** notes per tech stack (homepage header placement)
- **Google Search** checklist (crawlability, stable URL, appropriate content)
- **Manifest** (if PWA)

## Related Skills

- **logo-generator**: Favicon typically derived from logo; consistent branding
- **media-kit-page-generator**: Media kit should include favicon or link to brand assets
- **brand-visual-generator**: Visual identity; favicon aligns with brand colors and mark
- **indexing**: Favicon requires crawlable homepage; URL Inspection for indexing
