---
name: video-optimization
description: When the user wants to optimize videos for Google Search, video sitemap, VideoObject schema, or video SEO on websites. Also use when the user mentions "video SEO," "video sitemap," "VideoObject," "video thumbnail," "video indexing," "video preview," "key moments," "Clip schema," or "embedded video optimization."
metadata:
  version: 1.0.0
---

# SEO On-Page: Video Optimization

Guides video optimization for Google Search (main results, video mode, Google Images, Discover), video sitemap, VideoObject schema, and indexing. **Note**: Google now prioritizes YouTube video results in search; YouTube + Reddit comprise ~78% of social media citations in AI Overviews. For YouTube-specific optimization, see **youtube-seo**; for GEO distribution via YouTube, see **generative-engine-optimization**. References: [Google Video SEO](https://developers.google.com/search/docs/appearance/video), [Semrush YouTube SEO](https://www.semrush.com/blog/youtube-seo/).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Discovery & indexing**: HTML embed elements, video sitemap
- **Metadata**: Title, description, thumbnail; stable URLs
- **Structured data**: VideoObject schema
- **Features**: Video preview, key moments (Clip, SeekToAction), LIVE badge
- **YouTube prioritization**: Google favors YouTube in search; embed or host on YouTube for GEO citation

## YouTube in Google Search (2025+)

**Google prioritizes YouTube video results** across search. YouTube receives 48.6B monthly visits (second to Google.com) and is treated as core search infrastructure for AI-driven discovery. [Search Engine Land](https://searchengineland.com/youtube-seo-ai-overviews-467253)

| Context | Implication |
|---------|-------------|
| **AI Overviews** | YouTube citations surged 25.21% since Jan 2025; instructional (+35.6%), visual demos (+32.5%); long-form dominates (94%) |
| **GEO** | YouTube + Reddit = ~78% of social media citations; Perplexity (38.7%) and Google AI Overviews (36.6%) drive most YouTube citations |
| **Strategy** | Embed YouTube on site pages for dual indexing; or host on YouTube for GEO citation. See **youtube-seo**, **generative-engine-optimization** |

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for brand and page context.

Identify:
1. **Hosting**: Self-hosted vs YouTube/Vimeo embed
2. **Page type**: Dedicated watch page vs supplementary (e.g. blog with embedded video)
3. **Features needed**: Preview, key moments, LIVE badge

---

## 1. Discovery & Indexing

### Use Standard HTML Embed Elements

Google finds videos in `<video>`, `<embed>`, `<iframe>`, or `<object>`. **Do not** use fragment identifiers to load video; avoid requiring user interaction (click, swipe) to load.

| Do | Don't |
|----|-------|
| `<video><source src="...mp4"/></video>` | Fragment-only load; JS-injected without fallback |
| `<iframe src="https://youtube.com/embed/...">` | Hide video behind paywall without paywall structured data |

**JavaScript injection**: If video is injected via JS, ensure it appears in rendered HTML; use URL Inspection in Search Console. If using Media Source API, inject HTML video container even when API fails so Google can find metadata.

### Video Sitemap

Submit a [video sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps) to help Google discover videos. Use `<video:video>` extension; `<loc>` = watch page URL.

**Structure** (from Google):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
  <url>
    <loc>https://example.com/videos/watch-page.html</loc>
    <video:video>
      <video:thumbnail_loc>https://example.com/thumbs/123.jpg</video:thumbnail_loc>
      <video:title>Grilling steaks for summer</video:title>
      <video:description>Bob shows you how to grill steaks perfectly.</video:description>
      <video:player_loc>https://example.com/player?video=123</video:player_loc>
    </video:video>
  </url>
</urlset>
```

See **xml-sitemap** for sitemap index. Video sitemap is an extension; can be standalone or combined.

### Indexing Requirements

- **Watch page** must be indexed and perform well in search
- **Video embedded** on watch page; not hidden behind elements
- **Thumbnail**: Valid, stable URL; ≥60×30 px; ≥80% alpha >250 (no heavy transparency)
- **Supported formats**: 3GP, 3G2, ASF, AVI, DivX, M2V, M3U, M3U8, M4V, MKV, MOV, MP4, MPEG, OGV, WebM, WMV, etc. **Data URLs not supported.**

### Dedicated Watch Page

For video features (main results, video mode, key moments, LIVE badge), create a **dedicated watch page** per video—page whose primary purpose is to display that video. Examples: video landing page, episode player page, news video page. **Not** watch pages: blog with embedded video, product page with 360° video, category page with multiple videos.

---

## 2. Stable URLs

- **Thumbnail**: Stable URL; CDNs with fast-expiring URLs can prevent indexing
- **Content URL**: Stable for video preview and key moments; use `contentUrl` in VideoObject
- **Player URL**: Stable for `embedUrl` / `player_loc`

---

## 3. Thumbnail & Metadata

### Thumbnail Sources (in priority order)

| Source | How |
|--------|-----|
| `<video>` poster | `poster` attribute |
| Video sitemap | `<video:thumbnail_loc>` |
| VideoObject | `thumbnailUrl` |
| OGP | `og:video:image` |

Use **same thumbnail URL** across all metadata sources.

### Thumbnail Specs

| Spec | Requirement |
|------|-------------|
| Formats | BMP, GIF, JPEG, PNG, WebP, SVG, AVIF |
| Size | Min 60×30 px; larger preferred |
| Transparency | ≥80% of pixels with alpha >250 |
| Access | Must be crawlable (no robots.txt block, no login) |

### Unique Metadata per Video

Provide **unique** `thumbnailUrl`, `name`, and `description` for each video in structured data and sitemap. Consistency with visible content is required.

---

## 4. VideoObject Schema

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Grilling steaks for summer",
  "description": "Bob shows you how to grill steaks perfectly every time.",
  "thumbnailUrl": "https://example.com/thumbs/123.jpg",
  "uploadDate": "2025-01-15T08:00:00Z",
  "contentUrl": "https://example.com/video/123.mp4",
  "embedUrl": "https://example.com/player?video=123"
}
```

**Required for rich results**: `thumbnailUrl`, `name`, `description`. Add `contentUrl` for video preview and key moments. See **schema-markup** for full VideoObject; **serp-features** for Video SERP feature.

---

## 5. Video Features

### Video Preview

Google selects short clips as dynamic previews. Allow Google to fetch video file; use `max-video-preview` robots meta to limit duration.

### Key Moments (Chapters)

| Method | Use |
|--------|-----|
| **Clip** | Exact start/end + label per segment; all languages |
| **SeekToAction** | Tell Google where timestamps live in URL; auto-detect; supported languages: en, es, pt, it, zh, fr, ja, de, tr, ko, nl, ru |
| **YouTube** | Timestamps in description; see **youtube-seo** |

Disable key moments: `nosnippet` meta.

### LIVE Badge

Use `BroadcastEvent` schema for live streams to show "LIVE" in results.

---

## 6. Allow Google to Fetch Video File

For **video preview** and **key moments**, Google must fetch the actual video bytes. Do not block `contentUrl` with noindex or robots.txt. Use stable URLs; ensure both watch page host and video/CDN host have sufficient capacity for crawling.

---

## 7. Third-Party Embeds (YouTube, Vimeo)

Google may index both your page and the platform's page. For your watch page: still add VideoObject and optionally video sitemap. For more features (preview, key moments), confirm the platform allows Google to fetch video files.

---

## 8. Removal & Restrictions

- **Remove**: 404 on watch page, or `noindex`; or set `expires` in schema / `<video:expiration_date>` in sitemap
- **Geo-restrict**: `regionsAllowed` or `ineligibleRegion` in VideoObject; `<video:restriction>` in sitemap

---

## 9. SafeSearch & Monitoring

- Mark pages appropriately for SafeSearch if content is adult. See [Google SafeSearch](https://developers.google.com/search/docs/appearance/safesearch).
- **Search Console**: Video indexing report; Video rich results report; Performance filtered by "Video" search appearance.

---

## Specs by Context

| Context | Priority | Notes |
|---------|----------|-------|
| **Website video** | VideoObject, sitemap, thumbnail | This skill |
| **YouTube** | Title, description, chapters, thumbnail | See **youtube-seo** |
| **GEO / AI citation** | YouTube distribution; long-form | See **generative-engine-optimization** |
| **Featured Snippet (video)** | Video schema; timestamps | See **featured-snippet** |

---

## Related Skills

- **youtube-seo**: YouTube titles, descriptions, thumbnails, chapters
- **schema-markup**: VideoObject, BroadcastEvent; rich results
- **serp-features**: Video SERP feature; rich results
- **featured-snippet**: Video snippet format
- **xml-sitemap**: Video sitemap extension
- **google-search-console**: Video indexing report; Video rich results
