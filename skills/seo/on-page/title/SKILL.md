---
name: title-tag
description: When the user wants to write, audit, or optimize an HTML title tag, SEO title, page title, SERP title, browser-tab title, duplicate title, or title rewrite issue. For a sitewide metadata lifecycle including implementation and production validation, use page-metadata.
metadata:
  version: 2.0.0
---

# SEO On-Page: Title Tag

Owns writing and review rules for the HTML `<title>` element. **page-metadata** owns discovery, implementation, and release verification.

## Inputs

Read root `contextus.md` when present. Confirm page type, unique page job, primary search intent, locale, current title and H1, verified differentiators, sibling-page titles, and whether a template automatically appends the brand.

## Rules

- Write a descriptive, concise, page-specific title that accurately represents the page.
- Put the primary search concept early when natural; do not keyword-stuff.
- Treat about 60 Latin characters for the title body as a default warning, not a hard limit. Pixel width, script, device, and query context affect display.
- A delimiter plus brand suffix such as `| Brand` is outside that title-body target. It may be truncated or rewritten; include it only when useful and never duplicate a template suffix.
- For CJK, RTL, or other scripts, review rendered width and natural language instead of applying a translated character formula.
- Title and H1 must serve the same page intent and promise, but need not use identical wording. Example: title `AI Image Generator`; H1 `Generate Images with AI`.
- Include only claims supported by the page. Do not add a year, number, superlative, or feature merely for click appeal.
- Apply the **Swap Test**: if the title fits a sibling page unchanged, add a verified page-specific fact or sharpen its task.
- Google may generate a different title link from the `<title>`, main visual title, headings, prominent text, anchors, `og:title`, or other signals. Optimize consistency of page identity, not control of the exact displayed string.

## Cannibalization

When multiple URLs target the same primary intent, report the affected URLs, overlap, and evidence. Do not merge pages, reassign keywords, change page roles, or alter information architecture.

## Output

- Recommended title, with the title body and optional brand suffix shown separately.
- A length or width warning when relevant, never a mechanical pass/fail.
- Brief rationale tied to intent and unique page facts.
- H1 semantic-alignment result; actual H1 edits route to **heading-structure**.
- Cannibalization warning when applicable.

## Primary reference

- [Google: influencing title links](https://developers.google.com/search/docs/appearance/title-link)

## Related Skills

- **page-metadata**, **meta-description**, **heading-structure**
- **localization-strategy**, **translation**, **google-search-console**
