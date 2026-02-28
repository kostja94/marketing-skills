---
name: components-social-share
description: When the user wants to add, optimize, or audit social share buttons (share article to X, LinkedIn, Facebook, etc.). Also use when the user mentions "share buttons," "social share," "share to X," "share to LinkedIn," or "social sharing."
metadata:
  version: 1.0.0
---

# Components: Social Share Buttons

Guides implementation of **share buttons** that let users share the current page (article, post, product) to social platforms. Distinct from **social profile links** (footer links to your brand's X, LinkedIn, etc.) — share buttons share *this* content.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Share buttons**: Share current page URL to X, LinkedIn, Facebook, WhatsApp, etc.
- **Not** social profile links (e.g. "Follow us on X") — those live in footer/nav

## Why It Matters

- Websites with visible social share icons see **~158% increase in social engagement** ([NiftyButtons](https://www.niftybuttons.com/blog/ultimate-guide-adding-social-media-icons-website-2025))
- Share buttons amplify reach; Open Graph and Twitter Cards control preview — see **seo-on-page-open-graph**, **seo-on-page-twitter-cards**

## Placement (Article Pages)

**Fewer, better-placed buttons outperform scattered placement.** Research: removing 80% of buttons and repositioning the remaining 20% at high-emotion moments can **3× conversion** on share actions.

| Placement | Best For | Notes |
|-----------|----------|-------|
| **After first paragraph** | Most articles | Catches speed-readers; visible early |
| **Sticky sidebar** | Long-form (desktop) | Always visible; consider hiding on mobile |
| **Below title / hero** | Short posts | High visibility |
| **End of article** | All | Natural completion point; pair with CTA |
| **Mid-article** (after key insight) | Long content | Place at friction points (after surprising stat, before CTA) |

**Avoid**: Dozens of icons; every platform when audience uses 2–3. Choose 3–5 platforms that match your audience (e.g. B2B: X, LinkedIn; B2C: X, Facebook, WhatsApp).

## Share URLs (Intent Links)

Use platform share/intent URLs so users share with one click:

| Platform | Share URL pattern |
|----------|-------------------|
| **X (Twitter)** | `https://twitter.com/intent/tweet?url={url}&text={text}` |
| **LinkedIn** | `https://www.linkedin.com/sharing/share-offsite/?url={url}` |
| **Facebook** | `https://www.facebook.com/sharer/sharer.php?u={url}` |
| **WhatsApp** | `https://wa.me/?text={url}%20{text}` |
| **Telegram** | `https://t.me/share/url?url={url}&text={text}` |

Encode `url` and `text` with `encodeURIComponent()`. Use page title or a short pre-written message for `text` — **platform-specific prompts with pre-written messages perform ~4× better than generic icons**.

## Platform Brand Guidelines (Icons)

Use official brand assets. Minimum sizes and color rules:

| Platform | Min size | Colors | Notes |
|----------|----------|--------|-------|
| **Facebook** | 16px | Blue #1877F2 or monochrome | No rotation, animation without permission |
| **X (Twitter)** | 32px | Black or white only | Use current X logo, not deprecated bird |
| **LinkedIn** | 21px height | Blue #0A66C2 or monochrome | Use "in" bug for icons |
| **Instagram** | 29×29px | Black, white, or official gradient | Glyph for social icons |

Source icons from official brand resource centers. Outdated or non-compliant icons reduce perceived shareability.

## Design & Technical

| Item | Guideline |
|------|-----------|
| **Format** | SVG preferred (scalable, small); PNG/WebP with fallback |
| **Performance** | Lightweight; avoid heavy share plugins that slow LCP |
| **Accessibility** | `aria-label="Share on X"`; keyboard accessible |
| **Mobile** | Touch targets ≥44×44px; consider native share API (`navigator.share`) on mobile |

## Native Share API (Mobile)

On supported browsers, `navigator.share` lets users share via system dialog (includes more apps). Fallback to intent links when unsupported:

```javascript
if (navigator.share) {
  navigator.share({ title, url, text }).catch(() => {});
} else {
  window.open(shareUrl, '_blank', 'noopener');
}
```

## Output Format

- **Placement** recommendation for page type
- **Platforms** to include (3–5)
- **Share URL** examples with placeholders
- **Icon** guidelines (size, source)
- **Accessibility** checklist

## Related Skills

- **pages-article**: Share buttons on article pages; placement after intro, end of article
- **pages-blog**: Share buttons on blog index and post cards
- **seo-on-page-open-graph**: OG tags control share preview (og:image, og:title, etc.) — required for share buttons to show rich cards on Facebook, LinkedIn
- **seo-on-page-twitter-cards**: Twitter Cards control X preview — required for share buttons to show rich cards when shared to X
- **components-footer**: Footer has social *profile* links (Follow us); this skill is for *share* buttons (share this page)
