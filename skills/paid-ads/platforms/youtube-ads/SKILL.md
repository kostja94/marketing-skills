---
name: youtube-ads
description: When the user wants to run YouTube ads, set up TrueView or Bumper campaigns, or optimize video ad creative. Also use when the user mentions "YouTube ads," "TrueView," "Bumper ads," "YouTube Discovery," "video ads," "YouTube campaign," or "in-feed ads."
metadata:
  version: 1.0.0
---

# Paid Ads: YouTube Ads

Guides YouTube advertising: TrueView, Bumper, and Discovery (in-feed) formats. Use this skill when planning or optimizing YouTube ad campaigns. For Google Search/Display/PMax, see **google-ads**. For organic YouTube optimization, see **youtube-seo**.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read Sections 3 (Value Proposition), 4 (Audience).

Identify:
1. **Goal**: Awareness, consideration, conversion
2. **Budget**: Bumper cheaper; TrueView for scale
3. **Creative**: Existing video or net-new

## Ad Formats

| Format | Length | Skippable | Best For |
|--------|--------|-----------|----------|
| **TrueView Skippable** | 12 sec+ | After 5 sec | Reach; large audiences |
| **TrueView Non-skippable** | 15–20 sec | No | Full message; guaranteed view |
| **TrueView for Action** | — | — | Conversions; CTA-focused |
| **Bumper** | 6 sec or less | No | Brand awareness; memorable; lower cost |
| **Discovery (In-Feed)** | Thumbnail + text | — | Search, related videos, homepage; interest targeting |

## Format Selection

| Goal | Format |
|------|--------|
| **Brand awareness** | Bumper |
| **Website traffic** | TrueView |
| **Conversions** | TrueView for Action |
| **Interested audiences** | Discovery |

## Creative Guidelines

- **Bumper**: Quick, memorable; brand message in 6 sec
- **TrueView**: Hook in first 5 sec (skippable); deliver value before skip
- **Discovery**: Thumbnail + headline; appears like organic video

## Output Format

- **Format** recommendation
- **Creative** specs (length, hook, CTA)
- **Targeting** notes
- **Pre-launch** checklist

## Related Skills

- **google-ads**: Google Ads platform; YouTube runs through Google Ads
- **youtube-seo**: Organic YouTube; video optimization
- **video-marketing**: Video script, hook structure
- **paid-ads-strategy**: When to use video ads; channel selection
