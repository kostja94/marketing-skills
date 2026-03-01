# Use Cases & Content Roadmap

This document describes target use cases for marketing-skills, content creation recommendations, and partnership opportunities.

---

## 1. Use Cases

### 1.1 Personal Developer — SEO-Friendly Personal Site

**Scenario**: Individual developers want to build a personal website (portfolio, blog, landing page) with SEO built in from the start.

**Why this works**:
- One-click install: `npx skills add kostja94/marketing-skills`
- No need to learn SEO from scratch — the agent applies best practices when you ask
- Skills cover technical SEO (robots, sitemap, canonical), on-page (title, meta, schema), and page types (homepage, about, contact, blog)

**Recommended skills subset**:
- Technical: `robots-txt`, `xml-sitemap`, `canonical-tag`, `indexing`
- On-page: `title-tag`, `meta-description`, `open-graph`, `twitter-cards`, `schema-markup`, `heading-structure`
- Pages: `homepage-generator`, `about-page-generator`, `contact-page-generator`, `blog-page-generator`
- Components: `hero-generator`, `footer-generator`, `cta-generator`

**Content creation**: [§ Personal Site Quick Start](#content-recommendation-1-personal-site-quick-start)

---

### 1.2 Product Website — SEO Growth with Frontend + Ops Split

**Scenario**: A product website wants to drive SEO growth. Frontend uses optimization techniques; operations can build marketing pages independently via rewrite without depending on engineering.

**Why this works**:
- **Frontend**: Technical and on-page skills ensure crawlability, indexing, and SERP optimization
- **Ops-driven marketing**: Marketing page skills (pricing, landing, use cases, customer stories) can be built as static/markdown and served via rewrite rules — no code deploy needed
- Clear separation: engineering owns core product pages; ops owns campaign/landing pages

**Recommended skills subset**:
- Technical + on-page (frontend team)
- Pages (marketing): `pricing-page-generator`, `landing-page-generator`, `use-cases-page-generator`, `customer-stories-page-generator`, `alternatives-page-generator`, `integrations-page-generator`
- Strategies: `seo-strategy`, `paid-ads-strategy`, `website-structure`

**Content creation**: [§ Product Website SEO Playbook](#content-recommendation-2-product-website-seo-playbook)

---

### 1.3 Vibe Coding Beginner — Learn SEO & Website Building Standalone

**Scenario**: Someone new to vibe coding (Bolt.new, v0, Lovable, etc.) wants to learn SEO and website construction without joining an existing project.

**Why this works**:
- Skills are markdown — install and read them as learning material
- Can use ChatGPT, Claude Web, or Gemini: paste a skill, ask questions, get explanations
- No project required: `npx skills add ... -g` for global install, or clone and browse `skills/*/SKILL.md`

**Recommended approach**:
- Start with `seo-strategy` for workflow overview
- Then technical: `robots-txt`, `xml-sitemap`, `title-tag`, `meta-description`
- Use [SKILLS_GUIDE](SKILLS_GUIDE.md) and [page-taxonomy](page-taxonomy.md) for structure

**Content creation**: [§ Vibe Coding SEO Learning Path](#content-recommendation-3-vibe-coding-seo-learning-path)

---

### 1.4 Vibe Coding Product — Built-in Skills as Templates

**Scenario**: Vibe coding platforms (Lovable, v0, Bolt.new, Medo, etc.) want to ship SEO-friendly outputs by default. Built-in skills act as templates so user-generated projects are more discoverable and conversion-ready.

**Why this works**:
- Skills follow the open [Agent Skills spec](https://agentskills.io/specification) — portable across agents
- Pre-baked SEO and page patterns reduce user friction
- Better default = better outcomes = higher retention

**Partnership**: If you build a vibe coding product and want to integrate these skills, [contact me](mailto:zyjstc@gmail.com) for collaboration.

**Content creation**: [§ Vibe Coding Integration Guide](#content-recommendation-4-vibe-coding-integration-guide)

---

### 1.5 Want to Build Your Own Skills — Fork & Adapt

**Scenario**: You want to create your own agent skills but don't know where to start.

**Why this works**:
- **Fork the repo** — you get a complete, working skill set with 100+ skills as reference
- **Modify and adapt** — change descriptions, add your domain knowledge, remove what you don't need
- **Learn from structure** — SKILL.md format, frontmatter, Related Skills, output patterns are all documented
- **Start small** — copy one skill folder, rename it, edit the content; no need to build from scratch

**How to start**:
1. Fork [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills)
2. Read [SKILLS_GUIDE](SKILLS_GUIDE.md) for format and authoring rules
3. Pick a skill similar to what you want (e.g. `pricing-page-generator` → your `custom-page-generator`)
4. Copy, rename, edit — then install with `npx skills add your-username/your-fork`

**Content creation**: [§ Skill Authoring from Fork](#content-recommendation-6-skill-authoring-from-fork)

---

### 1.6 Future — Non-Website Agents

**Scenario**: Some skills are not tied to website building and can power other agents.

| Agent Type | Relevant Skills Today | Future Expansion |
|------------|------------------------|------------------|
| **Image / Video** | — | New skills: image generation prompts, video script/storyboard, asset specs |
| **Marketing (Influencer)** | `influencer-marketing`, `creator-program`, `twitter-x-posts`, `tiktok-captions`, `linkedin-posts` | Campaign briefs, creator discovery criteria, UGC guidelines |
| **Marketing (Ads)** | `paid-ads-strategy` | Ad copy, landing page alignment, ROAS optimization, creative specs |
| **Analytics** | `analytics-tracking`, `google-search-console`, `ai-traffic-tracking`, `traffic-analysis` | Dashboard design, report templates, attribution models |
| **Content** | `keyword-research`, `content-strategy`, `content-optimization` | Editorial workflows, content repurposing, distribution |

**Content creation**: [§ Non-Website Agent Roadmap](#content-recommendation-5-non-website-agent-roadmap)

---

## 2. Content Creation Recommendations

Based on analysis of existing skills and market trends (agentic SEO, AI website builders, influencer/ads automation), here are concrete content ideas.

### Content Recommendation 1: Personal Site Quick Start

**Format**: Single-page guide or skill bundle.

**Content**:
- Minimal skill subset for personal sites (10–15 skills)
- One-command install: `npx skills add kostja94/marketing-skills --skill robots-txt title-tag meta-description homepage-generator about-page-generator ...`
- Order of operations: technical → on-page → pages
- Optional: `product-marketing-context.md` template for personal branding

**Placement**: `docs/quick-start-personal-site.md` or linked from README.

---

### Content Recommendation 2: Product Website SEO Playbook

**Format**: Doc or series.

**Content**:
- Frontend vs ops ownership model
- How to use rewrite rules for marketing pages (e.g. Vercel, Netlify, Cloudflare)
- Page priority: Must Have / Great to Have / Optional
- Integration with `website-structure` and `seo-strategy` skills
- Case study: ops ships landing page without engineering

**Placement**: `docs/product-website-seo-playbook.md`.

---

### Content Recommendation 3: Vibe Coding SEO Learning Path

**Format**: Learning path doc.

**Content**:
- Week 1: What is SEO, technical foundation (robots, sitemap, canonical)
- Week 2: On-page (title, meta, schema, headings)
- Week 3: Pages and content (homepage, blog, landing)
- Week 4: Channels and analytics
- Each step: which skill to use, example prompts, paste-to-chat workflow for non-Cursor users

**Placement**: `docs/learning-path-seo.md`.

---

### Content Recommendation 4: Vibe Coding Integration Guide

**Format**: Technical integration doc + partnership page.

**Content**:
- How to bundle skills in a vibe coding product
- AGENTS.md / CLAUDE.md integration patterns
- Default skill subset for new projects
- Contact for partnership: zyjstc@gmail.com

**Placement**: `docs/vibe-coding-integration.md` + README partnership CTA.

---

### Content Recommendation 5: Non-Website Agent Roadmap

**Format**: Roadmap doc + future skill proposals.

**Content**:
- Skills that already support non-website use: influencer, paid-ads, analytics, content
- Proposed new skills: `image-generation-prompts`, `video-script-specs`, `influencer-campaign-brief`, `ad-copy-optimization`
- How to structure skills for multi-agent reuse (e.g. shared content-strategy, agent-specific output formats)

**Placement**: `docs/roadmap-non-website-agents.md`.

---

### Content Recommendation 6: Skill Authoring from Fork

**Format**: Short guide or README section.

**Content**:
- Why fork: complete reference, proven structure, 100+ examples
- Step-by-step: fork → pick template skill → copy & rename → edit SKILL.md → test locally → publish
- Links to SKILLS_GUIDE, naming-rules, description-rules
- How to publish: GitHub repo + `npx skills add owner/repo`

**Placement**: `docs/skill-authoring-from-fork.md` or section in CONTRIBUTING.md.

---

## 3. Market Context (from research)

- **Agentic SEO** (2026): Tools that combine Search Console API, site crawling, and autonomous decision loops are emerging; skills can feed into such workflows.
- **AI website builders**: WebbsAI, 10Web, Bloxby, AIWebsiteBuilder — many focus on SEO as a differentiator; skills can complement or be embedded.
- **Influencer/ads automation**: AI agents for creator discovery, campaign management, and performance feedback are scaling; `influencer-marketing` and `paid-ads-strategy` skills are directly relevant.
- **Skills marketplaces**: SkillsMP, MCP Market Skills — 30k+ skills; SEO/marketing is a distinct category with room for curated, high-quality collections.

---

## 4. Partnership

If you are building:
- A **vibe coding product** and want SEO-friendly defaults
- An **AI marketing agent** (influencer, ads, content)
- A **learning platform** for SEO or website building

Reach out: **zyjstc@gmail.com**
