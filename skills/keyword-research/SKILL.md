---
name: keyword-research
description: Coordinates keyword research from a seed or existing keyword data through discovery, intent clustering, opportunity assessment and page mapping.
metadata:
  version: 2.3.0
---

# Keyword Research

For a market or category, start with [category research](references/category-research.md) to identify demand branches and seeds. For an existing website, start with its URL inventory and check indexability before diagnosing weak keyword performance. For a single seed, begin directly with the workflow below. Establish the decision, product capabilities, market, language and channel. Reuse relevant project context (including contextus.md when available), existing queries, URLs and CSV exports. State reasonable assumptions. A single seed is enough. When exploring several seeds one at a time, complete the current one before continuing.

Read the relevant sibling skills by name from the installed collection or local repository. Start at the earliest missing input and stop at the requested deliverable.

| Request | Skill | Handoff |
|---|---|---|
| Find demand or long-tail expressions | keyword-discovery | Candidate queries with provenance |
| Decide whether queries serve one page | keyword-clustering | Task, same-page variants, separate or uncertain branches |
| Choose what to pursue first | keyword-opportunity | Priorities, reasons and evidence gaps |
| Decide where validated demand belongs | keyword-mapping | Existing asset or proposed action per cluster |

By default, skip US search volume and keyword prioritization. Run keyword-opportunity for US rankings only when requested and suitable third-party data is available. Otherwise pass clusters directly to mapping. For a full study, pass these outputs forward in order. Return to discovery for a specific unresolved branch. If a sibling skill is unavailable, identify the missing step and use the handoff above to provide a bounded result. Keep source observations distinguishable from hypotheses throughout. For ads or product research, stop at the requested demand or opportunity decision. Hand content architecture and scheduling to content-strategy.

Default to concise findings, decision-relevant clusters and outstanding checks in the conversation. Produce full inventories or files on request. Stop when additional sources yield no material new tasks or variants, or at the agreed scope limit.

In a full report, show the base expression family before modifier clusters. Carry each material action, process and tool form into the page map or explain its pending placement. Report the concrete keyword strings, and mark observed versus inferred wording.

For a general keyword research request, deliver a decision report even if site inventory is missing. Lead with the main search task and proposed destination. Provide one row per candidate page cluster with a primary term, same-page variants, intent, landing page / blog / other type, proposed URL, decision and evidence or gap. Distinguish proposed paths from existing URLs. Separate confirmed observations from inferred expansions and show pending clusters. Respect a discovery-only request.

## Completion check for a full study

Before delivery, account for each research node as observed, inferred, blocked or outside the requested scope. A blocked source is an evidence gap. Resume at the first unresolved decision when more evidence becomes available.

1. Establish the seed, market, audience and product task. Identify useful parents while preserving the seed.
2. Run discovery across base word forms and task branches. Record competitor URLs and the status of Autocomplete, People Also Ask and related searches separately. Preserve provenance when deduplicating.
3. Hand discovery evidence to clustering. Resolve same-page variants, separate tasks and uncertain relationships against user goals, product capability and available search results. Send ambiguous high-impact branches back for targeted research.
4. Check product fit and evidence at cluster level. Apply the optional prioritization rule above. Label unknown metrics and unsupported capabilities explicitly.
5. Map each actionable cluster to a current or provisional destination, page type and reason. Distinguish an independent intent from a decision to create a new URL.
6. Deliver findings, cluster decisions, open checks and any explicitly requested, data-backed priorities. If a missing step prevents a decision, label that part provisional. For a narrower request, stop at its agreed node.

For authenticated sources use the configured credential provider. In an environment configured for 1Password, retrieve credentials through that integration and keep secret values out of files, logs and reports.
