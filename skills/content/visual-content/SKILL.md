---
name: visual-content
description: When the user wants to plan, create, or repurpose visual content (images, infographics, social post images) across channels. Also use when the user mentions "content images," "social media images," "infographic," "visual content," "post image," "image specs," "visual repurposing," "content visuals," or "image for social post."
metadata:
  version: 1.0.0
---

# Content: Visual Content

Guides visual content planning and creation across website, social media, email, and other channels. Images are needed not just for websites—social posts, infographics, and repurposed content all require visuals. Visual-first planning in content calendars improves engagement; cross-channel consistency and repurposing maximize ROI.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **When to use images**: By content type and format
- **Specs by context**: Website vs social vs email
- **Platform image specs**: X, LinkedIn, Pinterest, Instagram, Facebook, YouTube
- **Repurposing**: One visual → multiple formats and channels
- **Visual-first planning**: Content calendar with image planning

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read Section 12 (Visual Identity) for brand consistency.

Identify:
1. **Context**: Article, social post, infographic, email, landing page
2. **Channels**: Which platforms will use this visual
3. **Repurposing**: Will this visual be adapted for other formats?

---

## 1. When to Use Images

| Content Type | Visual Need | Notes |
|--------------|-------------|-------|
| **Article / Blog** | Hero image, in-article images, screenshots | See **image-optimization** for web (alt, WebP, LCP) |
| **Social post** | Single image, carousel, or link preview | Platform-specific specs below |
| **Infographic** | Primary format; data visualization | Repurpose to social (cropped), blog (full) |
| **Case study** | Customer photo, results chart, logo | Repurpose to LinkedIn carousel, blog |
| **Product update** | Screenshot, feature graphic | Changelog, email, social |
| **Email** | Header image, inline graphics | Keep lightweight; many clients block images |
| **Landing page** | Hero, trust badges, screenshots | See **hero-generator**, **image-optimization** |

---

## 2. Website vs Social vs Email

| Context | Priority | Skill |
|---------|----------|-------|
| **Website** | Alt text, WebP, LCP, responsive, lazy loading | **image-optimization** |
| **Social posts** | Platform dimensions, aspect ratio, file size | **Platform skills** (X, LinkedIn, Pinterest, etc.) |
| **OG / Twitter Cards** | 1200×630, 1200×675 for link previews | **open-graph**, **twitter-cards** |
| **Email** | Inline-friendly; avoid heavy images; alt for blocked | **email-marketing** |

---

## 3. Platform Image Specs (Social)

| Platform | Post Image | Stories / Reels | Profile | Notes |
|----------|------------|-----------------|---------|-------|
| **X (Twitter)** | 1200×675 (16:9), 800×800 | — | 400×400 | See **twitter-x-posts** |
| **LinkedIn** | 1200×627, 1200×1200; carousel up to 20 | — | 400×400 | See **linkedin-posts**; vertical preferred on mobile |
| **Pinterest** | 1000×1500 (2:3) | — | 165×165 | Alt text ~25% more impressions; see **pinterest-posts** |
| **Instagram** | 1080×1350 (4:5), 1080×1080 | 1080×1920 (9:16) | 320×320 | 4:5 outperforms square on feed |
| **Facebook** | 1200×630, 1080×1080 | 1080×1920 | 320×320 | |
| **YouTube** | Thumbnail 1280×720 | — | 800×800 | |

**General**: 1080px width works across most platforms; vertical (4:5, 9:16) outperforms square on mobile-first feeds. Keep critical elements (logo, text) in safe center—platforms may crop.

---

## 4. Visual Repurposing

**Principle**: One core visual → multiple crops/formats → multiple channels.

| Core Visual | Adaptations | Channels |
|-------------|-------------|----------|
| **Infographic** | Full (blog), cropped sections (Instagram, LinkedIn carousel), square (X) | Blog, LinkedIn, Instagram, X |
| **Case study graphic** | Hero (blog), single slide (LinkedIn), story (Instagram) | Blog, LinkedIn, Instagram |
| **Product screenshot** | Hero (landing), post (X, LinkedIn), email header | Website, social, email |
| **Quote graphic** | Square (X, LinkedIn), 4:5 (Instagram) | X, LinkedIn, Instagram |

**Workflow**: Design at largest needed size; export platform-specific crops. Use consistent colors, fonts, logo placement (see **brand-visual-generator**).

---

## 5. Visual-First Content Planning

- **Plan images in content calendar**: Don't add visuals as afterthought; visuals drive engagement
- **Batch by theme**: Create visuals for a topic cluster or campaign together for consistency
- **Repurposing column**: In calendar, note which core piece becomes which visual format for which channel
- **Asset library**: Organize by campaign/theme; tag for reuse

---

## 6. Format-Specific Notes

### Infographics

- **Dimensions**: 800–1200px width; height varies by content
- **Export**: PNG for web; PDF for download
- **Repurpose**: Slice into 3–5 slides for LinkedIn carousel; single stat for X/Instagram

### Social Post Images

- **Text overlay**: Keep minimal; many platforms deprecate text-heavy images
- **Branding**: Logo in corner; consistent with **brand-visual-generator**
- **Alt text**: Add for LinkedIn, Pinterest, X (accessibility + Pinterest SEO); see **image-optimization** for alt best practices

### Article / Blog Images

- **Hero**: Often LCP candidate; optimize per **image-optimization**
- **In-article**: Support narrative; alt text, captions per **image-optimization**
- **Screenshots**: Annotate when helpful; keep file size low

---

## Output Format

- **Visual plan** (what images for what content)
- **Specs** by context (platform dimensions, format)
- **Repurposing** map (one visual → multiple outputs)
- **References** to platform skills and image-optimization

## Related Skills

### Content & Strategy

- **content-marketing**: Content types, formats, repurposing; visual content is part of content mix
- **content-strategy**: SEO topic clusters; article visuals
- **copywriting**: Copy pairs with visuals; headlines for image posts

### Platform (Image Specs)

- **twitter-x-posts**: X post image specs
- **linkedin-posts**: LinkedIn image specs
- **pinterest-posts**: Pinterest Pin dimensions, alt text
- **reddit-posts**: Reddit image post context

### Website & SEO

- **image-optimization**: Web images (alt, captions, WebP, LCP, responsive); central skill for image SEO
- **open-graph, twitter-cards**: Link preview images
- **hero-generator**: Hero section visuals

### Other

- **brand-visual-generator**: Typography, colors, imagery tone; visual consistency
- **video-marketing**: Video thumbnails; video as visual format
- **video-optimization**: Video SEO; VideoObject; video sitemap; YouTube prioritization
