---
name: canonical-tag
description: Audit and fix duplicate-page canonicalization across protocol, host, slash, default-document, extension, case, and tracking-parameter URL variants. Use for canonical URLs, duplicate content, preferred URLs, URL consolidation, or conflicting canonical signals. For URL naming and hierarchy design, use url-structure.
metadata:
  version: 1.1.0
---

# SEO Technical: Canonicalization

Determine the preferred URL for each page identity, consolidate duplicate variants, and verify that redirects, canonical annotations, internal links, sitemaps, and localization signals agree.

## Scope

Treat these as one duplicate-page canonicalization problem when they expose the same or substantially similar primary content:

- HTTP and HTTPS;
- www and non-www hosts, including combined protocol/host variants;
- trailing-slash and non-trailing-slash paths;
- repeated path slashes such as `/docs//guide`;
- directory defaults such as `/docs/` and `/docs/index.html`;
- historical extensions such as `/guide.html` and `/guide`;
- case variants such as `/Guide` and `/guide`;
- UTM and other tracking parameters that do not change primary content.

Do not assume that similar-looking URLs are duplicates. Case, parameters, extensions, and slash behavior can identify different resources. Compare response behavior, primary content, and project intent before consolidating.

## Inputs and Context

Read root `contextus.md` when present and only the modules relevant to the task. Otherwise use project configuration, routing code, deployment rules, sitemaps, and user-provided facts. Establish:

1. preferred scheme and host;
2. preferred path conventions;
3. which parameters change content versus only attribution or presentation;
4. framework, origin server, CDN, and redirect ownership;
5. existing indexed URLs, backlinks, migrations, and localization rules when relevant.

Ask only for missing information that would change the preferred URL or make a redirect unsafe.

## Decision Rules

| Situation | Primary action |
|---|---|
| Duplicate URL should no longer remain accessible | Permanent server-side redirect to the final preferred URL |
| Duplicate or near-duplicate must remain accessible | `rel="canonical"` to the preferred URL |
| Canonical HTML page | Self-referencing canonical |
| Non-HTML duplicate such as a PDF | Canonical HTTP `Link` header when supported |
| Tracking parameter that must reach analytics | Keep the landing request if needed; canonical to the content URL without tracking parameters |
| Parameter changes primary content or search intent | Evaluate as a separate page; do not strip or canonicalize mechanically |
| Pagination | Give each page a crawlable URL and evaluate it as distinct content; do not canonicalize every page to page 1 |
| Language or regional variant | Canonical within the appropriate language identity and coordinate with `hreflang` |

Use redirects to retire duplicate access paths. Use canonical annotations when access must remain. Do not use `robots.txt`, the removal tool, or `noindex` as substitutes for canonicalization.

## Variant Audit Matrix

Generate applicable test cases from the real site rather than testing one example only.

| Dimension | Variants to test | Expected invariant |
|---|---|---|
| Scheme | `http`, `https` | Non-preferred scheme reaches preferred HTTPS URL |
| Host | `www`, apex, known aliases | Non-preferred hosts reach one preferred host |
| Scheme + host | all supported combinations | Each duplicate reaches the same final URL without a redirect chain |
| Trailing slash | `/page`, `/page/` | One convention for the same page identity |
| Repeated slash | `/a//b`, `/a/b` | Duplicate path normalizes without corrupting `://` |
| Default document | `/`, `/index.html`; `/docs/`, `/docs/index.html` | Default-document aliases converge when content is equivalent |
| Extension | `/guide.html`, `/guide` | Historical alias maps to the corresponding page, not the homepage |
| Case | `/Guide`, `/guide` | Equivalent paths converge; genuinely case-distinct resources remain distinct |
| Tracking | base URL plus `utm_*`, `gclid`, or project tracking keys | Attribution works as required; content identity remains the clean URL |
| Combinations | case + extension + tracking + host/scheme variants | Normalize directly to one destination where safe |

Do not invent routes or send mutation requests during an audit. Use read-only requests unless the user asks to implement fixes.

## Signal Consistency

For every preferred URL, verify:

- redirect targets, HTML canonical or canonical HTTP header;
- internal navigation and content links;
- XML sitemap entries;
- `hreflang` URLs and return links when applicable;
- structured-data URLs and feeds when they identify the page;
- framework-generated metadata and client-side code do not overwrite the source canonical.

Canonical targets must be absolute, fetchable, indexable, and appropriate for the same content identity. Avoid canonical chains and conflicting targets across methods.

## Verification

Record evidence for representative URLs and high-risk templates:

1. requested URL;
2. HTTP status and each redirect hop;
3. final URL;
4. source canonical target;
5. indexability and content-equivalence result;
6. sitemap, internal-link, and `hreflang` consistency;
7. pass, fail, or needs-decision status.

Confirm that retired variants reach their corresponding preferred page in one hop where infrastructure permits. A final `200` alone is insufficient: the final URL and canonical must also be correct. For Google-specific diagnosis, compare the user-declared and Google-selected canonicals in URL Inspection when access is available.

## Implementation Boundaries

Implement in the layer that owns the behavior: CDN or reverse proxy for host/scheme normalization, server/router for paths, and page metadata for canonical annotations. Preserve query parameters needed for attribution or product behavior; remove only parameters confirmed not to affect the destination.

When changing live URLs, provide a mapping and rollback-aware implementation plan. Do not apply redirects to production, alter DNS, or change indexing controls without the user's authorization.

## Output

Return:

- the preferred scheme, host, and path conventions;
- duplicate clusters and the evidence that they represent the same page;
- a variant matrix with current and expected behavior;
- the selected method for each cluster: redirect, canonical, separate page, or needs decision;
- implementation location and exact proposed change when requested;
- verification results and unresolved risks.

References: [Google canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization), [canonical methods](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), [redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects), and [URL structure](https://developers.google.com/search/docs/crawling-indexing/url-structure).

## Related Skills

- **url-structure**: Design readable hierarchy and format for new canonical URLs.
- **localization-strategy**: Coordinate canonical and `hreflang` for localized pages.
- **xml-sitemap**: Publish only canonical indexable URLs.
- **indexing**: Diagnose indexability and selected-canonical issues.
- **site-crawlability**: Inspect crawl waste, redirect chains, and response behavior.
- **google-search-console**: Inspect Google-selected canonicals when property access exists.
