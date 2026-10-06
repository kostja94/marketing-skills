---
name: translation
description: Translate, transcreate, review, or maintain multilingual product and marketing content, including source locking, glossary decisions, language style, machine-assisted workflows, legal-content safeguards, QA, and source-change synchronization. Use localization-strategy for market scope, locale architecture, rollout, and production release planning.
metadata:
  version: 2.0.0
---

# Translation

Own the language-production lifecycle. Deliver natural, accurate target-language content without changing product facts, inventing market claims, or treating translated words as proof that a locale is ready to launch.

## Boundaries

- This skill owns translation, transcreation, terminology, style, linguistic review, and keeping translations current.
- **localization-strategy** owns locale selection, page coverage, URL architecture, routing, rollout, and release verification.
- **keyword-research** owns target-market queries. Never translate a source keyword list and call it localized research.
- Project positioning, feature availability, legal facts, and approved terminology remain in their project SSOTs.

## Prepare the Source

Read root `contextus.md` when present. Before translating, establish:

- source version and owner;
- content type and target locale or market;
- user task, audience, tone, and channel;
- product facts and claims that must remain unchanged;
- approved terminology, forbidden terms, and terms intentionally left untranslated;
- layout, UI, metadata, structured-data, or character constraints;
- review level required by business, legal, safety, or conversion risk.

If the source is unstable or contradictory, report the conflict before producing many dependent translations.

## Choose the Right Treatment

| Treatment | Use when | Main risk |
|---|---|---|
| Direct translation | Meaning and context transfer cleanly | Literal but unnatural phrasing |
| Localization | Formats, examples, terminology, or market facts differ | Unverified adaptation |
| Transcreation | Taglines, campaigns, landing-page persuasion, or cultural framing must change | Drifting from the product promise |
| Machine-assisted translation with review | Volume is high and risk is controlled | Fluent factual or terminology errors |
| Specialist translation | Legal, regulated, safety-critical, or technically exact material | Liability from semantic change |

Machine translation is a production method, not an automatic quality verdict. Match review depth to risk and page importance. Do not publish raw machine output merely because it reads fluently.

## Maintain Terminology

Use one project termbase or glossary rather than embedding competing lists in multiple plans. Useful fields include:

- source term and approved target term;
- definition or product context;
- allowed variants and forbidden translations;
- keep-untranslated decision;
- locale or market scope;
- owner and approval status.

Distinguish brand names, registered entities, product features, technical standards, generic category terms, UI labels, and search-language variants. A search phrase may differ from the UI term; document the role rather than forcing one string everywhere.

## Translate by Content Type

### Product UI

- preserve action, state, and error meaning;
- check interpolation variables, plurals, gender, truncation, line wrapping, and RTL behavior;
- review strings in screen context, not only in a spreadsheet;
- keep the same concept named consistently across navigation, onboarding, billing, and help.

### Marketing and Landing Pages

- preserve the page's audience, product promise, evidence, and desired action;
- use natural target-market phrasing and approved query language without keyword stuffing;
- adapt examples, proof, CTA, and objection handling only when the market facts support the change;
- keep Title, H1, description, body, and social copy semantically aligned without requiring identical strings.

### Articles and Documentation

- preserve technical meaning, examples, code, citations, and internal-link intent;
- localize headings and anchors only when the publishing system supports the resulting links;
- keep source and localized update states visible so stale versions can be found.

### Legal and Regulated Content

- preserve section correspondence, parties, defined terms, numbers, dates, rights, obligations, prohibitions, governing law, and dispute terms;
- do not add a “source language prevails” clause or change legal effect without authorized legal direction;
- record unresolved ambiguity for counsel rather than silently choosing a convenient interpretation;
- require specialist review before release.

## Production Workflow

1. Lock the source version and collect context.
2. Load the project glossary and style guidance.
3. Produce a first pass using the selected treatment.
4. Run terminology, factual, completeness, and formatting checks.
5. Review in the rendered product or page context.
6. Complete native or specialist review at the required risk level.
7. Mark the content ready and record its source version.
8. When the source changes, calculate affected strings or sections, move the translation to `outdated`, and review only after understanding the semantic change.

Suggested lifecycle states are `translation-draft`, `review`, `localized-ready`, `outdated`, and `not-applicable`. Use the project's existing state model when one exists.

## Quality Gates

Check what matters for the artifact:

- no missing or accidentally untranslated user-facing content;
- approved terms and intentional untranslated terms are respected;
- claims, numbers, links, entities, prices, and feature availability match verified facts;
- grammar, register, punctuation, dates, numbers, units, and address formats suit the locale;
- UI variables, markup, links, and code remain valid;
- metadata and headings match the localized page intent;
- the rendered page has no clipping, mixed-language fallback, broken RTL, or inaccessible controls;
- the source version and approval state are traceable.

For large inventories, test every template and risk tier plus representative pages; do not pretend a small sample proves every page correct.

## Output

Return the requested translation or review result plus only the supporting artifacts needed, such as:

- translator brief;
- approved and unresolved terminology decisions;
- translated or transcreated copy;
- issues requiring product, legal, or market decisions;
- QA and rendered-context findings;
- source-version and update-status notes.

Do not create a new translation-plan document when an existing project context, glossary, CMS workflow, or Skill should be updated.

## Related Skills

- **localization-strategy**: locale scope, architecture, migration, rollout, and production validation
- **keyword-research**: target-market queries and search intent
- **page-metadata**, **title-tag**, **meta-description**, **heading-structure**: localized search and page copy
- **copywriting**, **content-optimization**: source and target copy quality
