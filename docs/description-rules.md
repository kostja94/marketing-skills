# Skill Description Rules

Optimization guidelines for `description` field in SKILL.md. Aligns with [naming-rules.md](naming-rules.md) and [SKILLS_GUIDE §3.3](../SKILLS_GUIDE.md#33-description-field-rules).

---

## Core Principles

### Principle 1: Name–Description Alignment

The description must reinforce the skill name. Primary trigger keywords should match or extend the name.

| Check | Example |
|-------|---------|
| Name in description | `schema-markup` → include "schema," "structured data," "JSON-LD" |
| No contradiction | Don't describe scope that differs from name |
| Consistent terminology | Use same industry terms as name (e.g. "link building" not "off-page SEO" in user-facing text) |

### Principle 2: Keyword Coverage (Discoverability)

Maximize trigger coverage with **keyword variants** and **long-tail phrases** users actually search or say.

| Type | Purpose | Example |
|------|---------|---------|
| **Primary** | Core intent, matches name | "schema markup," "structured data" |
| **Synonyms** | Alternative terms | "JSON-LD," "rich snippets," "Schema.org" |
| **Long-tail** | Specific intents | "add FAQ schema," "fix duplicate content," "optimize for AI search" |
| **Task verbs** | Action-oriented | "create," "optimize," "audit," "fix," "implement," "configure" |
| **Tool/product** | Platform-specific | "GA4," "GSC," "Product Hunt," "IndexNow" |

### Principle 3: WHAT + WHEN Structure

Every description must include:

1. **WHAT**: What the skill does (1–2 clauses)
2. **WHEN**: Trigger scenarios and keyword list

**Format**:
```
When the user wants to [primary actions]. Also use when the user mentions "[keyword1]," "[keyword2]," "[keyword3]," or "[long-tail phrase]."
```

---

## Best Practices (from Research)

### 1. Customer Perspective

- Lead with **value** and **utility**, not technical jargon
- First 1–2 clauses answer: "What can I do with this?"
- Avoid internal/developer-only terms unless they're common search terms

### 2. Keyword Density vs. Naturalness

- Include 5–12 trigger keywords; avoid stuffing
- Use natural phrasing; keywords should read as part of a sentence
- Prefer **high-search-volume** and **industry-standard** terms (same as naming Principle 2)

### 3. Length

- **Max 1024 chars** (SKILLS_GUIDE)
- Aim for **150–300 chars** for readability; extend with keywords only when needed
- Every phrase should add unique trigger value

### 4. Third Person

- Description is injected into system prompt
- ✅ "When the user wants to optimize..."
- ❌ "I can help you optimize..." or "Use this skill to..."

### 5. Avoid Redundancy

- Don't repeat the name verbatim unless it's a primary trigger
- Remove filler ("various," "etc.," "and more")
- Prefer specific over generic ("fix indexing issues" > "handle SEO")

---

## Keyword Expansion by Category

### SEO Skills

| Dimension | Include |
|-----------|---------|
| **Technical terms** | Industry standard (Schema.org, canonical, noindex, sitemap.xml) |
| **User intent** | "fix," "optimize," "implement," "audit," "configure" |
| **Tool names** | GSC, GA4, IndexNow, Bing |
| **Problem phrases** | "duplicate content," "not indexed," "Crawled - currently not indexed," "orphan pages" |

### Pages Skills

| Dimension | Include |
|-----------|---------|
| **Page type** | "homepage," "pricing page," "landing page," "404 page" |
| **Synonyms** | "about us," "company story," "contact form," "FAQ page" |
| **Intent** | "create," "optimize," "audit," "structure" |
| **Related concepts** | "conversion," "objection handling," "case studies" |

### Components Skills

| Dimension | Include |
|-----------|---------|
| **UI terms** | "hero section," "above the fold," "breadcrumb," "TOC" |
| **Technical** | "BreadcrumbList schema," "Open Graph," "og:image" |
| **Synonyms** | "announcement bar," "sticky banner," "popup," "modal" |

### Channels & Platforms

| Dimension | Include |
|-----------|---------|
| **Platform names** | Product Hunt, Taaft, Reddit, LinkedIn, X, TikTok |
| **Strategy terms** | "affiliate program," "referral program," "EDM," "creator partnership" |
| **Abbreviations** | EGC, KOL, CPS, IMC, PESO (with full form in body) |

### Strategies & Analytics

| Dimension | Include |
|-----------|---------|
| **Concept names** | GEO, AEO, "generative engine optimization," "AI search visibility" |
| **Metrics** | "traffic sources," "dark traffic," "UTM," "CTR," "impressions" |
| **Tool names** | GA4, GSC, Search Console |

---

## Anti-Patterns to Avoid

| Anti-pattern | Fix |
|-------------|-----|
| Too generic | "Helps with SEO" → specify: "optimize title tag, meta description, SERP snippet" |
| Missing triggers | Add 5+ keyword variants users might say |
| Jargon-only | Add user-friendly terms: "structured data" + "schema," "rich snippets" |
| First/second person | Use third person: "When the user wants to..." |
| Name not reflected | Ensure primary keyword from name appears in description |
| Overlong | Trim to 300 chars; move rare triggers to skill body |

---

## Validation Checklist

Before publishing a description:

- [ ] Name appears or is clearly implied (primary keyword)
- [ ] WHAT + WHEN structure present
- [ ] 5+ trigger keywords or phrases
- [ ] At least 1–2 long-tail / problem-specific phrases
- [ ] Third person throughout
- [ ] No contradiction with skill scope
- [ ] ≤ 1024 characters
- [ ] Industry terms match naming-rules (high search volume, generic over niche)

---

## References

- [SKILLS_GUIDE §3.3](../SKILLS_GUIDE.md#33-description-field-rules) — description field rules
- [naming-rules.md](naming-rules.md) — name optimization (description should align)
- [8 Tips for Effective Skill Description](https://developer.amazon.com/en-IN/blogs/alexa/alexa-skills-kit/2020/05/8-tip-for-effective-skill-description-and-metadata-writing) — Amazon Alexa
- [The SKILL.md Pattern](https://bibek-poudel.medium.com/the-skill-md-pattern-how-to-write-ai-agent-skills-that-actually-work-72a3169dd7ee) — AI agent skills
- Create-skill (Cursor): "Include both WHAT and WHEN; be specific and include trigger terms"
