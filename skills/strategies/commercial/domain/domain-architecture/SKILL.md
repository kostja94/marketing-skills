---
name: domain-architecture
description: When the user wants to decide domain structure for multiple products or brands—subfolder vs subdomain vs independent domain. Also use when the user mentions "subfolder vs subdomain," "subdirectory vs subdomain," "multiple products domain," "multiple websites," "brand architecture," "branded house," "house of brands," "where to host product," "domain structure," or "hub-spoke domain." For brand SERP, use multi-domain-brand-seo.
metadata:
  version: 1.0.1
---

# Strategy: Domain Architecture

Guides domain structure decisions for multiple products or brands: subfolder (subdirectory), subdomain, or independent domain. Covers brand architecture (Branded House vs House of Brands) and Hub-Spoke principles when multiple domains coexist. See **domain-selection** for initial domain choice (Brand/PMD/EMD, TLD); **website-structure** for single-domain page planning; **rebranding-strategy** for domain change and migration; **multi-domain-brand-seo** for brand search optimization.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for product portfolio and growth goals.

Identify:
1. **Product count**: Single product vs multiple products/brands
2. **Brand strategy**: Unified brand vs distinct brands
3. **Current state**: Planning from scratch vs consolidating existing domains
4. **Constraints**: Tech stack, team, budget

## Domain Structure Options

| Structure | Example | SEO Authority | Brand Independence | Typical Use |
|-----------|---------|---------------|-------------------|-------------|
| **Subfolder** | company.com/product-a | Shared with main domain | Low | Products under one brand; SMB; content consolidation |
| **Subdomain** | product.company.com | Treated separately by Google | Medium | Separate product experience; tech isolation; support/docs |
| **Independent domain** | product.ai | None shared | High | Acquired brands; different markets; distinct brand identity |

### When to Use Each

| Choose | When |
|--------|------|
| **Subfolder** | Products share value proposition; want to strengthen main domain; SMB; blog, tools, features under one brand |
| **Subdomain** | Need separate tech stack (e.g., app vs marketing); support portal; docs; distinct UX but same brand |
| **Independent domain** | House of Brands; acquired company; different audience; different TLD (e.g., .ai for AI product) |

**SEO consensus**: Subfolders typically outperform subdomains for most cases—authority flows to the main domain. Subdomains require separate SEO effort.

## Brand Architecture

| Model | Description | Domain Tendency | Examples |
|-------|-------------|-----------------|----------|
| **Branded House** | One master brand; products use functional descriptors | Subfolder or subdomain | Google (google.com/search, google.com/maps), FedEx |
| **House of Brands** | Each brand independent; parent hidden | Independent domains | Unilever (dove.com, axe.com) |
| **Sub-brands / Endorsed** | Sub-brands with parent endorsement | Subdomain or independent | FedEx Express, Marriott Bonvoy |

**Decision factors**: Business strategy, market positioning, product overlap, resource availability.

## Hub-Spoke (Multiple Domains Coexist)

When company main site (company.com) and product site (product.ai) both exist:

| Role | Domain | Focus |
|------|--------|-------|
| **Hub** | company.com | Brand, About, Research, product matrix; brand queries |
| **Spoke** | product.ai | Product features, pricing, signup; product queries |

**Principles**:
- Hub links to Spoke (Products section); Spoke links back (About, Footer, "A [Company] product")
- Spoke avoids competing for brand queries in Title; Hub avoids competing for product keywords
- See **multi-domain-brand-seo** for brand search optimization.

## Output Format

- **Recommendation** (subfolder / subdomain / independent) with rationale
- **Brand architecture** fit (Branded House / House of Brands / Sub-brands)
- **Domain mapping** (e.g., product A → company.com/product-a)
- **Hub-Spoke** guidance (if multiple domains)
- **Related** next steps (website-structure, rebranding-strategy)

## Related Skills

- **domain-selection**: Initial domain choice (Brand/PMD/EMD, TLD); single-site use case
- **website-structure**: Plan pages within a domain; single-domain structure
- **rebranding-strategy**: Domain change, 301 redirects, migration
- **multi-domain-brand-seo**: Brand search control when Hub and Spoke coexist
- **branding**: Brand strategy, positioning; domain architecture implements brand structure
