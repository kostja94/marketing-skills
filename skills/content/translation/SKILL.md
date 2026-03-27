---
name: translation
description: When the user wants to translate content, create translation workflows, manage terminology, or optimize translation quality. Also use when the user mentions "translate," "translation," "localization copy," "glossary," "terminology," "style guide translation," "machine translation," "human translation," "TMS," or "multilingual content." For strategy, use localization-strategy.
metadata:
  version: 1.0.1
---

# Content: Translation

Guides translation workflow, terminology, style, and quality for multilingual content. Covers when to use human vs machine translation, glossary and style guide creation, and SEO considerations. For i18n implementation, hreflang, and URL structure, see **localization-strategy**.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **Workflow**: Brief → translate → review
- **Terminology**: Glossary creation and management
- **Style guide**: Voice, tone, formatting per language
- **Human vs MT**: When to use each; post-editing
- **Quality**: QA, consistency, SEO
- **Market-specific**: Terminology by region

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for brand voice, target markets, and product terminology.

Identify:
1. **Content type**: Product UI, marketing copy, blog, landing page, docs
2. **Target language(s)**: Priority locales
3. **Existing assets**: Glossary, style guide, translation memory (TM)

---

## 1. Translation Workflow

### Brief → Translate → Review

| Phase | Purpose | Output |
|-------|---------|--------|
| **Brief** | Context, audience, tone, glossary reference, style guide | Translator brief document |
| **Translate** | First pass; use glossary + TM when available | Draft translation |
| **Review** | Native speaker review; consistency, brand voice, SEO | Final translation |

### Translator Brief

Include in every project:
- **Context**: What the content is for (landing page, product UI, blog)
- **Audience**: Target market, user persona
- **Tone**: Formal, casual, technical
- **Glossary**: Link or attach; mandatory terms
- **Style guide**: Reference or key rules
- **Constraints**: Character limits (UI), SEO keywords to include naturally

### Content-Type Workflow

| Content Type | Approach | Notes |
|--------------|----------|-------|
| **Product UI** | Glossary-critical; short strings; consistency | Use TM; avoid machine translation |
| **Marketing copy** | Brand voice; cultural adaptation | Human translation; see terminology |
| **Blog / Article** | SEO; natural keyword placement | Re-research keywords in target language; don't translate keyword lists |
| **Landing page** | Conversion-focused; CTA clarity | Human; test localized CTAs |
| **Technical docs** | Precision; glossary | TM + glossary; consider MT + post-edit for high volume |

---

## 2. Glossary & Terminology

### Glossary Purpose

- **Consistency**: Same term translated the same way across all content
- **Brand**: Product names, feature names, approved phrasing
- **Compliance**: Safety, legal, regulated terms
- **Cost**: Reduces rework; accelerates review

### Glossary Structure

| Field | Purpose |
|-------|---------|
| **Source term** | Original (e.g., English) |
| **Target term** | Approved translation |
| **Context** | Where it appears; usage note |
| **Do not translate** | Brand names, product names (when applicable) |

### Market-Specific Terminology

| Term | English | Chinese | Notes |
|------|---------|---------|------|
| **Generative AI** | Generative AI, GenAI | AIGC (人工智能生成内容) | Use "AIGC" for China; "Generative AI" for English |
| **Influencer** | Influencer | KOL (关键意见领袖) | "KOL" common in Chinese marketing |
| **User** | User | 用户 | Context-dependent |
| **Dashboard** | Dashboard | 控制台, 仪表盘 | Choose one; document in glossary |

**Principle**: Don't translate terminology lists; research how target market searches and speaks. See **keyword-research** for multi-language keyword research.

---

## 3. Style Guide (Translation)

### Elements to Define

| Element | Purpose |
|---------|---------|
| **Voice** | Brand personality; formal vs casual |
| **Tone** | Varies by content type (support = helpful; marketing = persuasive) |
| **Register** | Formal (您) vs informal (你) in languages that distinguish |
| **Punctuation** | Quotation marks, spacing (e.g., no space before colon in French) |
| **Formatting** | Dates, numbers, units; locale-specific |
| **Forbidden** | Terms or phrases to avoid |

### Per-Language Considerations

- **Chinese**: Simplified vs Traditional; measure word usage
- **German**: Formal (Sie) vs informal (du); compound nouns
- **Japanese**: Honorifics; keigo for formal contexts
- **Arabic**: RTL; formal vs dialect

---

## 4. Human vs Machine Translation

### When to Use Human Translation

| Scenario | Reason |
|----------|--------|
| **Product UI** | Terminology, UX clarity, brand |
| **Marketing copy** | Persuasion, cultural nuance, CTAs |
| **Landing pages** | Conversion; tested copy |
| **Legal, compliance** | Accuracy, liability |
| **Brand-critical** | Taglines, campaign copy |

### When Machine Translation (MT) May Be Acceptable

| Scenario | Condition |
|----------|-----------|
| **High-volume, low-stakes** | Internal docs, user-generated content |
| **Draft / triage** | MT + human post-edit (MTPE) |
| **Real-time** | Chat, support; with disclaimer |

### Avoid

- **Raw MT for product/marketing**: Terminology errors, cultural misfires, poor SEO
- **MT without post-edit** for customer-facing content
- **Translating keyword lists** instead of re-researching in target language

---

## 5. Translation Memory (TM) & TMS

### Translation Memory

- **What**: Stores approved source↔target sentence pairs
- **Benefit**: Consistency; reuse; lower cost per word; faster turnaround
- **Best practice**: Maintain TM; clean duplicates; align with glossary

### Translation Management System (TMS)

- **Use for**: Centralized workflow; glossary + TM integration; vendor management
- **When**: Multiple languages; ongoing translation; team collaboration

---

## 6. Quality & SEO

### Quality Checklist

- [ ] Glossary terms used correctly
- [ ] Style guide followed
- [ ] No untranslated strings
- [ ] Numbers, dates, units localized
- [ ] Character limits respected (UI)
- [ ] Native speaker review completed

### SEO for Translated Content

- **Keywords**: Re-research in target language; don't translate from source
- **Metadata**: Title, description translated; see **title-tag**, **meta-description**
- **Hreflang**: Technical implementation in **localization-strategy**; translation produces the content
- **Thin content**: Avoid publishing many low-quality translated pages at once; can trigger penalties. See **localization-strategy** Multilingual Risks.

---

## 7. Integration with Localization

| Topic | Skill |
|-------|-------|
| **i18n implementation** | localization-strategy |
| **URL structure, hreflang** | localization-strategy |
| **Translation workflow, glossary, style** | This skill (translation) |
| **Keyword research by market** | keyword-research; localization-strategy |

When adding a new locale: create glossary, style guide, then translate. See **localization-strategy** for technical checklist (hreflang, sitemap, metadata).

---

## Output Format

- **Translator brief** (context, audience, glossary, style)
- **Glossary** additions or updates
- **Style guide** notes for target language
- **Human vs MT** recommendation
- **Quality** checklist

## Related Skills

### Strategy & Technical

- **localization-strategy**: i18n, hreflang, URL structure, pricing by market; translation produces content for localized pages
- **content-strategy**: Multilingual content planning; avoid thin translations
- **content-marketing**: Content types and formats; translation as one channel adaptation

### SEO & Content

- **keyword-research**: Multi-language keyword research; don't translate keyword lists
- **page-metadata**: Hreflang implementation
- **title-tag, meta-description**: Translate metadata per locale
- **copywriting**: Source copy to translate; brand voice
- **image-optimization**: Localize image filenames for translated pages

### Pages

- **article-page-generator**: Article structure; translate with SEO in mind
- **landing-page-generator**: Landing page copy; human translation for conversion
