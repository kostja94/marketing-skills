---
name: open-source-strategy
description: When the user wants open source strategy, OSS commercialization, or open source growth. Also use when the user mentions "open source strategy," "OSS strategy," "open source commercialization," "open source to paid," "open core," "COSS," "commercial open source," "GitHub stars strategy," "DevHunt," "open source marketing," "open source growth," "Llama," "Dify," "Cursor," "open source business model," or "developer tools directory." For GitHub tactics, use github.
metadata:
  version: 1.0.1
---

# Strategies: Open Source

Guides open source as a commercialization path: build community and trust first, monetize later. Many products use open source for early growth (Cursor from VSCode, Llama, Qwen, Dify) and later commercialize via managed services or open core. For GitHub (SEO, GEO, README, Awesome lists), see **github**. For directory submission (DevHunt, Awesome lists), see **directory-submission**.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Definition & Why

**Open source strategy** = Use open source for distribution, trust, and community; monetize through enterprise features, managed services, or support. 95% of enterprises use open source; 33% increasing usage. Community becomes your marketing force—users self-host, contribute, and recommend.

| Path | Example |
|------|---------|
| **Open source → Commercial product** | Cursor (VSCode fork); Llama, Qwen (enterprise/cloud) |
| **Open core → Managed service** | Dify (self-host free + cloud paid); MongoDB Atlas; Confluent |

**Core insight**: Brand is the moat when code is commoditized. Developers won't pay directly; they become your marketing army through word-of-mouth, content, and recommendations.

## Business Models

| Model | Description | Examples |
|-------|-------------|----------|
| **Open Core** | Core free; enterprise features (SSO, audit, multi-tenancy) paid | GitLab, Elastic, Grafana |
| **Managed Services (SaaS)** | Self-host free; cloud/hosted paid | MongoDB Atlas, Confluent, Dify |
| **Support-First** | Free software; enterprise support subscriptions | Red Hat |
| **Free + Paid Convenience** | 70–80% revenue from cloud; self-host free | Most COSS companies |

**Monetization layer**: Enterprise users buy risk mitigation—SLAs, indemnification, security patches, support—not just code.

## Developer-First Distribution

### GitHub (Primary)

GitHub is the main hub for open source discovery. Optimize for visibility and conversion.

| Element | Purpose | Skill |
|---------|---------|-------|
| **README** | Landing page; answer-first GEO; installation, usage | **github** |
| **About, Topics** | Discovery, keywords; 6–20 topics; 350-char About | **github** |
| **Stars** | Trending status; credibility; search visibility | GitHub + coordinated launch |
| **Awesome lists** | Curated lists; backlinks; discovery | **github**, **directory-submission** |

**Stars strategy**: Stars without strategy are vanity metrics. Coordinate multi-channel launch (HN, Reddit, Dev.to); Tuesday–Wednesday US Pacific morning often outperforms. Quality README and clear value proposition matter more than channel volume.

### DevHunt (Developer Tools Directory)

**DevHunt** is an open-source platform for developer tools—alternative to Product Hunt, built for developers. Naturally aligned with open source projects.

| Aspect | Detail |
|--------|--------|
| **Audience** | Developers, indie makers, open source maintainers |
| **Content** | Dev tools, APIs, libraries, open source projects |
| **Features** | GitHub-verified submissions; 50+ categories; free to submit |
| **Use when** | Open source or developer tool; want dev-focused discovery |

**Submission**: Prepare product info (name, tagline, description, category, GitHub URL). See **directory-submission** for submission workflow and asset preparation.

### GitHub Marketplace

For extensions, actions, integrations. See **distribution-channels** for marketplace listing strategy.

## Community & Trust

| Practice | Guideline |
|----------|-----------|
| **Build in Public** | Share progress, metrics, failures; attracts early adopters | **indie-hacker-strategy** |
| **Contributing** | CONTRIBUTING.md; clear contribution path |
| **Transparency** | Roadmap, changelog; community involvement in planning |
| **Commercialization** | Preserve goodwill; communicate early; keep investing in OSS |

**Community benefits**: Organic word-of-mouth; user-generated content (SEO); free QA via bug reports; contribution activity signals project health.

## Licensing (Brief)

| License | Use | Trade-off |
|---------|-----|-----------|
| **MIT, Apache 2.0** | Permissive; max adoption | Cloud giants can fork without contributing |
| **AGPL** | Prevent cloud fork without contribution | May reduce adoption |
| **BSL/SSPL** | Source-available; commercial restrictions | Elastic, HashiCorp, Redis Labs shifted to this |

## Related Skills

- **github**: GitHub README, About, Topics, Awesome lists; SEO, GEO, parasite SEO
- **directory-submission**: DevHunt, Awesome lists; submission workflow per platform
- **parasite-seo**: GitHub as high-authority platform
- **generative-engine-optimization**: GEO; AI citation for technical content
- **indie-hacker-strategy**: Build in Public; bootstrapped founder path
- **distribution-channels**: GitHub Marketplace, plugin stores
- **link-building**: Backlinks from repos, Awesome lists
- **community-forum**: Forums, Discord, community tactics
