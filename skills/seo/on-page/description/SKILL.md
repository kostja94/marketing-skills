---
name: meta-description
description: When the user wants to write, audit, or optimize a meta description, SEO description, SERP snippet candidate, duplicate description, description length, or description rewrite issue. For a sitewide metadata lifecycle including implementation and production validation, use page-metadata.
metadata:
  version: 2.0.0
---

# SEO On-Page: Meta Description

Owns writing and review rules for `<meta name="description">`. It is a candidate source for search snippets, not a guarantee of the text Google will display.

## Inputs

Read root `contextus.md` when present. Confirm page type, primary search intent, locale, verified page-specific facts, current description, body coverage, sibling-page descriptions, and the intended next action when one exists.

## Rules

- Write an accurate, useful summary or pitch for the specific page.
- Lead with information that distinguishes this page from sibling pages.
- Use query-relevant language naturally, without a keyword list.
- Length is a warning, not a hard gate. Google has no fixed meta-description length limit and truncates snippets as needed for the device and result context.
- A description may exceed traditional character guidance when it remains concise and useful. Flag descriptions too short to explain value or too long because of filler, repetition, or boilerplate.
- Use a CTA only when it suits the page task. Do not force marketing CTAs into legal, documentation, status, or informational pages.
- Include price, author, date, availability, or compatibility only when present and current on the page.
- Apply the **Swap Test**: if a description can move unchanged to a sibling page, it is not specific enough.
- Localize from the target market's query language and intent; do not translate and truncate.
- Google primarily creates snippets from page content and may show different text for different queries. Ensure the H2/body can substantiate the description's promise.
- Do not claim a fixed CTR, ranking, or traffic increase. A meta description is not a direct ranking control.

## Output

- Recommended description and a non-binding length warning when useful.
- Brief rationale tied to intent and page-specific facts.
- Body-coverage warning if the page cannot substantiate the proposed description.
- Sibling duplication or cannibalization warning when applicable; do not restructure pages.

## Primary reference

- [Google: snippets and meta descriptions](https://developers.google.com/search/docs/appearance/snippet)

## Related Skills

- **page-metadata**, **title-tag**, **heading-structure**
- **localization-strategy**, **translation**, **google-search-console**
