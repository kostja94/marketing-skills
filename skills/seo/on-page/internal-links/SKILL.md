---
name: internal-links
description: Audits and designs internal links for a site, page family or article. Use for orphan pages, link equity, click depth, hubs, anchor text, old-post backfill and product navigation.
metadata:
  version: 2.0.0
---

# Internal links

## Scope and evidence

State the intended outcome: discovery, access to priority pages, semantic hierarchy, a reading path, product conversion, or diagnosis of missing or overlapping pages. Read the relevant project context from root `{project}.md` when available; otherwise use supplied material. Declare included hosts, locales and surfaces (Blog, Docs, Help Center, app).

Classify clickable destinations by ownership: same-host page, same registered domain on another subdomain (ecosystem), another owned domain, owned social/community channel, third party, or same-page fragment. Report these separately. Canonicals, hreflang, redirects, sitemap and Schema URLs can corroborate findings but do not count as clickable edges. For third-party links in Blog articles use outbound-links.

Establish live nodes from the rendered site and existing page inventory. Use [site-structure-inventory](https://github.com/kostja94/vibe-coding/tree/main/skills/site-structure-inventory) if discovery is needed. Cross-check robots, sitemap, CMS, routes, search console, analytics or logs as available. Label disagreements with source and date: a deployment repository can lag production or contain future work. Record crawl exclusions, sampling and unknowns before calling a page an orphan.

## Compare observed and intended links

1. Crawl reachable in-scope pages and extract rendered links. Distinguish navigation, footer, breadcrumb, body, card, CTA, recommendation and fragment. For large inventories, summarize by page family and URL pattern with examples.
2. For each important page, identify its parent, children, justified peers, useful incoming entrances and next user action. Select the [landing-page workflow](references/landing-pages.md) for product, proof and conversion, or the [Blog workflow](references/blog.md) for education and continued reading. For mixed pages, select the primary role, then inspect the bridge to the other family.
3. Compare observed edges with these candidates. Flag missing nodes separately from missing edges: if the intended destination does not exist, report the gap. For each issue give the observed evidence, impact, proposed source/target, placement or anchor change, and a verification method. Separate responsibility conflicts from link fixes.
4. Prioritize broken, wrong or noncanonical targets; important orphans; broken hub/detail relationships; navigation, breadcrumbs and main product paths; strong contextual gaps; cross-cluster bridges; then wording. Counts, density and click depth are diagnostics or project-specific thresholds. Choose natural, descriptive anchor text that predicts the destination; use a keyword only where it helps the reader.

## Deliver at the scale of the site

- Small site: add the key relationships and serious reachability gaps to the existing site-structure inventory.
- Curated site: use a project internal-linking plan for intended relationships, priority destinations, hubs, subdomain rules and exceptions.
- Large or programmatic site: additionally generate a dated observed graph in CSV, JSON or a database. Store evidence separately from proposals; a proposed edge contributes zero observed inlinks.

For an observed edge preserve the literal source and target, the roles of both pages, placement, actual anchor (or image/control), and discovery time separately from recheck time. Record the verified canonical target alongside the original URL; leave unverified values unknown. Support the status with evidence for existence, crawlability, destination availability and contextual relevance separately.

After authorized changes, recrawl the affected paths. Verify important destinations have relevant crawlable entrances, anchors resolve to the intended canonical and locale, and the new observations and project plan agree. For draft-only work report the verified artifact and any outstanding live checks.

## Related skills

Use website-structure or url-structure for architecture decisions, site-crawlability for technical access, breadcrumb-generator for breadcrumb implementation, and content-strategy for cluster planning.
