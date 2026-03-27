---
name: download-page-generator
description: When the user wants to create, optimize, or audit a download page for desktop or mobile app. Also use when the user mentions "download page," "app download," "desktop download," "mobile app download," "App Store," "Play Store," "get the app," "install app," or "download CTA." For app install ads, use app-ads.
metadata:
  version: 1.0.1
---

# Pages: Download Page

Guides download page structure and optimization for desktop and mobile app downloads. Purpose: convert visitors into installers by clearly presenting value, platform options, and trust signals.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product, audience, and value proposition.

Identify:
1. **App type**: Desktop (Windows, macOS, Linux) or mobile (iOS, Android, both)
2. **Traffic source**: Organic, paid, email, referral
3. **Distribution**: App Store / Play Store only, direct download, or both

## Page Purpose

| Purpose | Goal |
|---------|------|
| **Download** | Guide users to install desktop or mobile app |
| **Trust** | Build confidence before download (security, privacy, reviews) |
| **Conversion** | Maximize download rate, store visits, install conversion |

## Download Page Structure

| Step | Purpose | Elements |
|------|---------|----------|
| **1. Value proposition** | Why download | Headline, benefit-focused copy, key features |
| **2. Platform selection** | Clear path | Desktop: OS detection or manual pick; Mobile: App Store / Play Store buttons |
| **3. Trust signals** | Reduce friction | Ratings, download count, security badges, privacy note |
| **4. Visual proof** | Show the app | Screenshots, app previews, video |
| **5. CTA** | Primary action | Single, prominent download button |

## Platform-Specific Layout

### Desktop App

- **OS detection**: Auto-detect OS or show "Download for Windows / macOS / Linux"
- **Direct download**: One-click .exe / .dmg / .deb etc.
- **Alternatives**: Optional "Other platforms" or "Command line" for power users

### Mobile App

- **Dual store**: App Store + Play Store buttons side by side
- **Smart redirect**: Detect device and show relevant store first; still show both
- **QR code**: Optional for desktop visitors to scan and install on phone

## Optimization Best Practices

### Performance

- **Load time**: Under 3 seconds; each extra second can cost ~7% conversion
- **Mobile-first**: Most app download traffic is mobile; responsive, thumb-reachable CTAs
- **Image optimization**: WebP, lazy loading, compression (e.g. TinyPNG, ImageOptim)

### Conversion

- **Single primary CTA**: "Download Free Now," "Get on App Store," "Get for Windows"
- **Above the fold**: CTA visible without scrolling
- **Repeat CTA**: On longer pages, repeat at logical points
- **A/B test**: CTA color, size, copy, placement

### Trust & Social Proof

- **Star ratings**: Show App Store / Play Store ratings
- **Download count**: "10M+ downloads," "Trusted by X users"
- **Testimonials**: User quotes, media logos
- **Security**: Security badges if collecting sensitive info

### Content

- **Top 3–5 features**: Benefit-focused, scannable bullet points
- **Screenshots**: High-quality, show app in action
- **Video**: App preview or demo video

### Alignment with Traffic

- **Ads**: If from PPC, ensure message matches ad (offer, platform); see **paid-ads-strategy**
- **Email**: Match campaign message and CTA

## Output Format

- **Headline** and subheadline
- **Structure** (5-step flow sections)
- **Platform layout** (desktop vs mobile)
- **CTA** copy and placement
- **Trust signals** placement
- **SEO** metadata (if page is indexed)

## Related Skills

### Pages

- **landing-page-generator**: Download page is a type of landing page; apply LP principles
- **homepage-generator**: Homepage often links to download page
- **features-page-generator**: Feature copy for "Explain value" section

### Components

- **hero-generator**: Hero section (value proposition)
- **cta-generator**: Download button design
- **trust-badges-generator**: Social proof, ratings
- **testimonials-generator**: User testimonials

### SEO

- **title-tag, meta-description, page-metadata**: Download page metadata
