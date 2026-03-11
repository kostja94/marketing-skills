# Reference Rules for Marketing Skills

Standardization for internal (skill-to-skill) and external (standalone sites) references. Aligns with [Google developer documentation style](https://developers.google.com/style/cross-references), [MDN Markdown guidelines](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Howto/Markdown_in_MDN), and [skill-authoring §4](skill-authoring.md#4-body-content-markdown-body).

**Quick reference**: Internal → `see **skill-name**` (bold, lowercase). External → `[Descriptive text](URL)`; no "click here." Product examples → ≤5 per category; add disclosure when 3+; prefer generic terms. Section order → content → References → Related Skills. Related Skills optimization → §7 below.

---

## 1. Internal References (Other Skills)

### 1.1 Format

| Context | Format | Example |
|---------|--------|---------|
| **Inline (body)** | `see **skill-name**` or `See **skill-name**` | see **keyword-research** for discovery |
| **With purpose** | `see **skill-name** for [purpose]` | See **site-crawlability** for technical detection |
| **Multiple** | `see **skill-a** and **skill-b**` | see **article-page-generator** and **generative-engine-optimization** |

### 1.2 Rules

- **Bold** the skill name: `**skill-name`** (lowercase, hyphens)
- **Lowercase** skill name; capitalize "See" at sentence start
- **Purpose clause**: Add "for X" when the link text doesn't indicate why the reader is referred
- **Avoid**: "click here," "this skill," "the X skill" — use the skill name directly

### 1.3 Related Skills Section

```markdown
## Related Skills

- **skill-name**: Brief purpose; when to use
- **other-skill**: Alternative or complementary; scope boundary
```

- One line per skill: `**name**: purpose`
- Order: Most relevant first; group by category if many
- Purpose: What the reader gets; when to use vs. current skill
- **Optimization**: Count limits, avoid cascading, when to include — see §7 below

---

## 2. External References (Standalone Sites)

### 2.1 Format

| Type | Format | Example |
|------|--------|---------|
| **Inline link** | `[Descriptive text](URL)` | [Google Rich Results Test](https://search.google.com/test/rich-results) |
| **With intro** | `For more information, see [Link text](URL).` | For more information, see [Schema.org](https://schema.org/). |
| **References block** | Bullet list at section end | See §2.3 |

### 2.2 Link Text Best Practices

| Do | Don't |
|----|-------|
| Use page title or descriptive phrase | "click here," "this link," "here" |
| Keep link text short (2–6 words typical) | Use raw URL as link text |
| Place important words first | Repeat same link text for different targets |
| Match destination content | Vague: "this document," "more info" |

**Examples:**

| Recommended | Not recommended |
|-------------|-----------------|
| [Google URL guidelines](https://developers.google.com/search/docs/crawling-indexing/url-structure) | [click here](url) |
| [Schema Markup Validator](https://validator.schema.org/) | [validator.schema.org](url) |
| [Alignify directory guide](https://alignify.co/zh/insights/directory-submission-sites) | [Alignify](url) (too vague) |

### 2.3 References Section

Place external references in a **References** or **References / Citations** block at the end of the skill (before Related Skills if both exist).

**Format:**

```markdown
## References

- [Page title or description](URL) — Brief note (optional)
- [Another resource](URL) — When to use
```

**Grouping (optional):**

```markdown
## References

**Official / Spec:**
- [Schema.org](https://schema.org/)
- [Google Structured Data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)

**Tools:**
- [Rich Results Test](https://search.google.com/test/rich-results)
- [Schema Markup Validator](https://validator.schema.org/)

**Third-party guides (optional):**
- [Alignify URL optimization](https://alignify.co/zh/seo/url-optimization) — URL best practices
```

### 2.4 External Reference Categories

| Category | Examples | When to include |
|----------|----------|-----------------|
| **Official / spec** | Google docs, Bing, Schema.org, sitemaps.org | Required for technical accuracy |
| **Validation tools** | Rich Results Test, Card Validator | When skill involves validation |
| **Third-party guides** | Alignify, industry blogs | Optional; one authoritative source per topic |
| **Platform docs** | Grokipedia, Product Hunt | When skill targets that platform |

### 2.5 Source Authority

External references must be **authoritative** or **directly relevant**. Exclude non-authoritative sources.

**Include:**

| Type | Examples |
|------|----------|
| **Official / spec** | Google, Bing, Schema.org, sitemaps.org, platform docs |
| **Validation tools** | Rich Results Test, Schema Validator, Card Validator |
| **Platform docs** | When skill targets that platform (e.g. Grokipedia) |
| **Project / meta docs** | Keep a Changelog, MDN, agentskills.io, skills.sh, GitHub (project repo) |
| **Media** | When relevant for context (e.g. The Verge for Grokipedia citation) |

**Exclude:**

| Type | Examples |
|------|----------|
| **Marketing / growth blogs** | Litmus, Mailchimp, indie-hacker guides, third-party campaign guides |
| **Design / consulting blogs** | Commercial design agencies, A/B test vendors |
| **Cross-domain skills** | Alexa skill docs when writing for AI agent skills |
| **Personal blogs** | Medium, Substack, etc., unless widely recognized |

- Prefer official docs over third-party summaries
- When removing a citation, rephrase to keep the insight without attributing to a non-authoritative source

### 2.6 Avoid Duplicate Links

- Link once per destination per skill; prefer the most relevant location
- Exception: Long skills (>200 lines) may repeat a link in a different section
- References section consolidates links; inline links for immediate context

---

## 3. Section Order

Recommended order for skill body:

1. Scope / Initial Assessment
2. Main content (methods, best practices, etc.)
3. Output Format
4. **References** (external links)
5. **Related Skills** (internal)

---

## 4. Alignify References

Alignify is referenced in several skills. Standardize as:

| Topic | URL | Link text |
|-------|-----|-----------|
| Directory submission | alignify.co/zh/insights/directory-submission-sites | Alignify directory guide |
| URL optimization | alignify.co/zh/seo/url-optimization | Alignify URL optimization |
| Blog placement | alignify.co/zh/seo/create-blog | Alignify subdomain vs subdirectory guide |
| AI logo design | alignify.co/insights/ai-logo-design | Alignify AI Logo Guide |

- Use full URL with `https://`
- Prefer descriptive link text over "Alignify" alone

---

## 5. Google / Bing References

| Resource | Standard link text |
|----------|-------------------|
| developers.google.com | "Google [topic]" or "[Topic] (Google)" |
| Google Rich Results Test | Rich Results Test |
| Bing Webmaster | Bing Webmaster docs |
| Schema.org | Schema.org |

---

## 6. Product and Website Examples

When skills mention third-party products, tools, or websites as examples (e.g. Rewardful, Taaft, Product Hunt), follow these rules. Aligns with [Google excessive claims](https://developers.google.com/style/excessive-claims), [Splunk third-party references](https://docs.splunk.com/Documentation/StyleGuide/current/StyleGuide/Third-partyrefs), and FTC disclosure principles.

### 6.1 Quantity Limit

| Context | Limit | Rationale |
|---------|-------|-----------|
| **Per table/category** | 2–5 examples max | Avoid overwhelming; reader can search for alternatives |
| **Per skill** | Prefer generic terms first; examples only when necessary | "Affiliate tracking tools" before "Rewardful, Tolt, Tapfiliate" |
| **Platform lists** | 3–5 per tier/type | Enough to illustrate; not a directory |

- Prefer **generic descriptors** (e.g. "affiliate tracking platform," "AI tool directory") when the concept is clear
- Add **concrete examples** only when they help the reader find or evaluate options

### 6.2 No Promotional Intent — Disclosure

Skills are educational; product mentions are illustrative, not endorsements. Include a disclosure when a skill lists 3+ product/website examples.

**Standard disclosure** (place in skill metadata or at end of first product-example section):

```markdown
*Product and website examples are illustrative only. No affiliation, partnership, or endorsement implied.*
```

**Shorter variant** (for skills with few examples):

```markdown
*Examples are illustrative; no endorsement implied.*
```

- Place once per skill, near the first product-example block
- Optional in README, skill-authoring, or project-level docs as a general note

### 6.3 Neutral, Factual Language

| Do | Don't |
|----|-------|
| Use factual, verifiable statements | "Best," "fastest," "simplest," "recommended" (unless citing a source) |
| Describe function or category | Subjective comparisons ("X is better than Y") |
| "Tools such as X, Y" or "e.g. X, Y" | Imply exclusivity ("Use X" without alternatives) |
| Official spelling and capitalization | Trademark symbols (™, ®) in body text |

- Per [Google style](https://developers.google.com/style/excessive-claims): avoid superlatives; use "helps with" rather than "prevents" for security/performance
- Per Splunk: spell product names as the company does; no unapproved abbreviations

### 6.4 When to Name Products

| Use product names when | Prefer generic when |
|------------------------|---------------------|
| Skill targets that platform (e.g. Grokipedia, Product Hunt) | Concept is universal (e.g. "affiliate tracking") |
| Reader needs to find a tool (e.g. "Rich Results Test") | Many alternatives exist and list would be long |
| Platform-specific workflow (e.g. "Taaft requires…") | Example would date quickly or imply endorsement |

### 6.5 Validation Checklist (Product Examples)

- [ ] ≤5 examples per table/category
- [ ] Disclosure present when 3+ product examples
- [ ] No superlatives or unverifiable claims
- [ ] Generic terms used where possible; examples only when helpful

---

## 7. Related Skills Optimization

**Count limits**: Most skills: **6–8** Related Skills; hub skills (e.g. serp-features, schema-markup): **8–10**; page skills with grouped entries: **≤12**.

**Rules**:
- **Direct dependency only** — Prefer skills the current skill directly depends on; avoid "nice to have"
- **Reference hierarchy** — A skill does not need to list every skill that references it. If **entity-seo** is referenced by article-page, faq-page, alternatives-page, **entity-seo**'s Related Skills should not list those four
- **Avoid consumer references** — Do not list skills that consume the current skill (e.g. page skills that use entity-seo)
- **Prefer in-page context** — When 1–2 sentences suffice, write inline instead of linking
- **No duplicate references** — Reference each skill once per document; avoid redundant body + Related Skills

**Format** (from §1.3):

```markdown
## Related Skills

- **skill-name**: Brief purpose; when to use
- **other-skill**: Alternative or complementary; scope boundary
```

**Validation**: ≤8 for most; ≤10 for hub; ≤12 for page skills with groups; no consumer refs; each entry has clear purpose.

---

## 8. Validation Checklist & Migration

**Before publishing a skill:**

- [ ] Internal refs use `**skill-name**` (bold, lowercase)
- [ ] External refs use descriptive link text, not "click here" or raw URL
- [ ] External refs are authoritative (official, tools, platform docs) or explicitly allowed (project/meta, media) — see §2.5
- [ ] Product/website examples: ≤5 per category; disclosure when 3+; neutral language — see §6
- [ ] References section exists when 2+ external links
- [ ] No duplicate links to same destination (unless long doc)
- [ ] Related Skills lists purpose for each skill
- [ ] Section order: content → References → Related Skills
- [ ] Related Skills: count limits per §7; no consumer refs

**When applying rules to existing skills:**

1. **Internal refs**: Change `see skill-name` → `see **skill-name**`; add "for X" when needed
2. **External refs**: Replace vague link text with descriptive phrases
3. **Source authority**: Remove non-authoritative sources; rephrase to keep insight without citation when needed — see §2.5
4. **Product examples**: Add disclosure when 3+; trim to ≤5 per category; prefer generic terms — see §6
5. **References block**: Move scattered links into a References section where appropriate
6. **Alignify**: Use standardized link text per §4
7. **Related Skills**: Apply count limits; remove consumer references per §7
