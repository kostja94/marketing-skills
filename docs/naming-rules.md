# Skill Naming Rules

Full naming specification for marketing skills. See [SKILLS_GUIDE §7](../SKILLS_GUIDE.md#7-naming-and-categorization) for the summary.

---

## Core Principles (Highest Priority)

All naming decisions must satisfy these two principles first.

### Principle 1: Content / Function / Skills Consistency

The name must accurately reflect what the skill does and covers.

| Check | Example |
|-------|---------|
| Matches scope | A skill that optimizes title tags → `title-tag`, not `seo-tags` |
| Matches output | A skill that generates pricing page content → `pricing-page-generator` |
| No scope creep | Don't name for adjacent topics; use Related Skills for cross-links |
| Aligns with description | Name should match the primary trigger keywords in the description |

### Principle 2: High Search Volume, Most Generic Keywords

Use the most common, high-search-volume terms for SEO and skills.sh discoverability.

| Check | Example |
|-------|---------|
| User search intent | "schema markup" (high) > "structured data" (more technical) → `schema-markup` |
| Generic over niche | "link building" (generic) > "off-page SEO" (jargon) → `link-building` |
| Industry standard | "canonical tag" (Moz, Google docs) > "canonical URL" → `canonical-tag` |
| Competitor validation | Skills with high installs confirm search demand |

**When in conflict**: Principle 1 (content match) takes precedence. A name that misrepresents the skill harms trust.

---

## Naming Rules

### Spec Compliance

- Lowercase letters, numbers, hyphens only
- 1–64 characters
- No leading/trailing hyphen, no consecutive hyphens `--`
- For nested structure, `name` may differ from directory path for search discoverability

### Category Patterns

| Category | Pattern | Example |
|----------|---------|---------|
| **Pages** | `[type]-page-generator` | pricing-page-generator, homepage-generator |
| **Components** | `[component]-generator` | trust-badges-generator, newsletter-signup-generator |
| **SEO** | Industry term (noun phrase) | schema-markup, title-tag, canonical-tag, link-building |
| **Channels** | `[channel]-[noun]` | referral-program, affiliate-marketing, employee-generated-content |
| **Platforms** | `[platform]-[suffix]` | twitter-x-posts, reddit-posts, tiktok-captions |
| **Strategies** | Full name, no abbreviation | generative-engine-optimization (not geo) |
| **Analytics** | `[metric]-[action]` or tool name | traffic-analysis, google-search-console |

### Platform Suffix

Platform names must be followed by a clarifying word: posts, captions, recommendations.

| Pattern | Example |
|---------|---------|
| [platform]-posts | twitter-x-posts, reddit-posts, linkedin-posts |
| [platform]-captions | tiktok-captions |
| [platform]-recommendations | grokipedia-recommendations |

### No Abbreviations for Strategies

Use full names: `generative-engine-optimization` (not `geo`), `employee-generated-content` (not `egc`).

### Prefer 2+ Words

Avoid single-word names when possible. Exceptions: product names (indexnow), established terms (indexing).

---

## Names to Avoid

- Too generic: `helper`, `utils`, `tools`
- Vague: `seo` (prefer specific, e.g. `schema-markup`)
- Abbreviations unclear to new users: `egc`, `geo`
