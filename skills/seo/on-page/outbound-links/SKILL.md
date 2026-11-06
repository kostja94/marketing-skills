---
name: outbound-links
description: Selects and audits third-party citations, action links and embeds in Blog articles. Use to verify claim attribution, editorial placement, source freshness, commercial disclosure and rendered link attributes.
metadata:
  version: 1.0.0
---

# Outbound links in Blog articles

## Scope

Review article bodies. Exclude Blog indexes, author and tag pages, site chrome, share buttons and fixed social destinations. Use internal-links for ownership classification when host alone is ambiguous. Marketing pages, Docs, Help Centers and tools require their own editorial policies. For acquisition or inbound profile audits use link-building or backlink-analysis.

## Decide what the reader needs

For each occurrence, identify the exact claim, original sample, necessary reader action or useful further reading. Place evidence for facts, data and direct quotations beside the relevant statement. Link to the specific supporting page. Publication rank, traffic and domain metrics cannot establish that a source supports a claim.

| Claim | Preferred evidence |
|---|---|
| Law or policy; technical standard | Applicable official legal text, regulator or responsible standards body; check version, scope and effective status. |
| Product behavior, price, compatibility | Current official documentation, pricing or release notes; verify on the review date. |
| Statistics and trends | Original study or dataset with inspectable method, sample and date. Label historical findings with their year. |
| Company event or partnership | Announcement by the parties involved; corroborating reporting where useful. |
| Expert judgment | Identifiable author with relevant expertise, quoted in context. |
| Creator example, user feedback or community claim | Original public post or video. It establishes what this account showed or reported. Wider claims about prevalence, capability or causation require independent evidence. |

Prefer the original source. Use reliable secondary material when the original is unavailable, the secondary account is itself under discussion, or it adds indispensable verification. Check attribution, public access, publication date or identifiable version, and whether the material says what the article claims. Reject anonymous or unverifiable aggregation, unsupported AI-generated copy, content farms, irrelevant home/search/tag pages and obsolete evidence presented as current. A rumor or anecdote may itself be the subject of analysis if labeled as such. Recheck key evidence on substantive article updates according to how quickly the fact changes; prefer a semantically equivalent successor from the same publisher if the source moves.

## Edit placement and quantity

These are the default Blog editorial rules for this workflow:

- Keep third-party links out of the TL;DR, FAQ, conclusion and final CTA. Move new evidence in the conclusion into the argument. In the first actual body paragraph after metadata, title and summary, allow an essential citation for a fact, figure or quotation; place action links and further reading later. Later introductory paragraphs are distinct from the first paragraph.
- Choose descriptive anchor text naming the source, material or reader action. Natural variants are fine. Avoid bare URLs, generic commands, isolated brand names, invented titles and keyword stuffing.
- Add an optional **References** section when a research piece, comparison, alternatives article or source-heavy guide benefits from centralized review, or the editor requests a bibliography. Use an ordinary H2 and list with descriptive titles and useful publisher, date or version details. Important inline sources may recur here; include only materials worth revisiting. This list cannot supply attribution missing from the body.
- Count distinct resolved third-party target URLs in the body. Exclude template links, repeated bibliography entries and duplicate embed fallbacks. Above five, review redundancies, consolidate claims supported by one source and move optional reading to References. Keep indispensable evidence even above the threshold. Repeat a URL inline only for a distinct necessary action; several URLs from the same domain may each support different claims. Avoid repeated brand exposure.

## Verify availability and rendering

Record the result for the actual destination. **Pass** when the reader reaches supporting material. **Normalize redirect** when it moves to equivalent content. **Manual verification** when automation returns 401/403, a challenge, geographic restriction or a JS shell; inspect in a browser if possible. **Broken or degraded** when verification confirms removal, irrelevant redirection (including to a homepage) or replaced content. Leave unresolved cases pending. A 200 response alone cannot establish semantic fit.

For an embed, explain what the original shows and provide an accessible fallback link to it. Check loading failure, lazy loading, consent, performance, mobile and accessibility. Private, deleted or region-restricted media cannot be the only support. In References, cite the original URL rather than embedding the widget again.

Apply the same link behavior to Markdown and HTML in the rendered article. This workflow defaults to opening third-party targets in a new tab with `noopener`; add `noreferrer` only for an explicit privacy need that outweighs referral reporting. For editorial citations use ordinary links. Add `sponsored` for paid placements, affiliate commissions, gifts or other compensation, `ugc` for user-submitted links, and `nofollow` for necessary links to untrusted targets; combine tokens when warranted. A partnership or integration alone does not establish compensation. Disclose a material commercial relationship in clear text before the reader first encounters the link.

Check that the publishing system supports per-link attributes, validates restricted placements and preserves fallbacks without counting them twice. Inspect final rendered targets, rel values and redirects, or report the stage actually verified when only draft or preview access is available.

## Audit output

Use one row per occurrence and claim/action, even when several rows share a URL. Group source metadata where useful. Record:

- article URL and page role; actual target and independently verified canonical URL;
- publisher, specific claim or action, placement, observed anchor and why the source is qualified;
- publication date separately from check date, actual rendered rel, HTTP and browser observations, decision, reason and proposed fix.

Mark unknown values explicitly. Distinguish the link decision from publication status. For batch work summarize distinct body targets separately from the number of occurrence-level findings.

## Related guidance

Use [Google's link practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) and [outbound link qualifications](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links) for crawler and relationship semantics, [MDN on noopener](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener) for browser behavior, and [W3C link purpose](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-link-only.html) for accessible link text.
