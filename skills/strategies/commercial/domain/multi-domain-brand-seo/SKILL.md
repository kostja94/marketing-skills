---
name: multi-domain-brand-seo
description: When the user wants to optimize brand search for a company with multiple domains (e.g. parent company.com vs product.ai). Ensure the parent/company domain ranks first for brand queries. Also use when the user mentions "brand search," "multi-domain SEO," "company domain first," "parent vs product domain," "hub-spoke domain," "brand SERP control," or "differentiate company and product domains." For domain structure, use domain-architecture.
metadata:
  version: 1.0.1
---

# SEO: Multi-Domain Brand Search

When a company has multiple domains (e.g., company.com and product.ai), ensure the **company/main site** ranks first for brand queries. Product sites focus on product keywords and do not compete for brand position. See **domain-architecture** for structure decisions; **rebranding-strategy** for domain change and migration.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Typical Scenarios

| Scenario | Description |
|----------|-------------|
| **Multiple domains** | Company main site (company.com), product site (product.ai / product.io) |
| **Brand query competition** | Product site or third-party (Crunchbase, LinkedIn, reviews) may outrank main site for brand |
| **Entity confusion** | Legacy brands, sub-brands, directories dilute brand perception |
| **Goal** | Brand queries → company.com first; product.ai → product keywords only |

## Hub-Spoke Model

| Role | Domain | Responsibility |
|------|--------|----------------|
| **Hub** | company.com | Brand #1; About, Research, ecosystem, product matrix |
| **Spoke** | product.ai | Product keywords, features, pricing; visible "by [Company]" and link back to company.com |

## Differentiation

| Dimension | Hub (company.com) | Spoke (product.ai) |
|-----------|--------------------|---------------------|
| **Audience** | Investors, partners, media, developers | Product users, prospects |
| **Keywords** | Brand name, company name, industry | Product features, use cases |
| **Content** | Mission, About, Research, Events, product matrix | Features, Use Cases, Pricing, Sign up |
| **Conversion** | Contact, Waitlist, Early Access | Sign up, Try free, Pricing |

## Avoid Cannibalization

- Hub does not target Spoke product keywords (e.g., "virtual staging," "AI design tool")
- Spoke does not target Hub brand keywords (Title avoids brand-only; add product description)
- Internal links: Hub → Spoke (Products); Spoke → Hub (About, Footer)

## Optimization Checklist

### Hub (company.com) On-Page

| Item | Recommendation |
|------|----------------|
| **Title** | Company full name + positioning, e.g. `[Company] — [Slogan] \| AI Research & Products` |
| **Meta Description** | Company name, core business, partners; 150–160 chars |
| **H1** | Company name or main slogan |
| **URL** | Canonicalize www vs non-www (301) |

### Hub Content & Structure

| Item | Recommendation |
|------|----------------|
| **About** | Company intro, founders, founding date, positioning; link to product sites |
| **Products** | Product matrix; each product links to its site |
| **Research / News** | Papers, events, partnerships; increase brand mentions |
| **FAQ** | "What is [Company]?" "What is [Product]?"; FAQ schema |

### Spoke (product.ai) Differentiation

| Item | Recommendation |
|------|----------------|
| **Title** | Product name + product description, e.g. `[Product] — [Core function]` or `[Product keyword] \| [Product]`; avoid brand-only |
| **About** | "A product of [Company](https://company.com)" |
| **Footer** | "© [Company]" or "A [Company] Product" + link to company.com |
| **Schema** | SoftwareApplication with `author` or `publisher` pointing to Company |

### Schema (Hub)

Use Organization schema with `subOrganization` to define product relationships:

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Company Name]",
  "url": "https://www.company.com",
  "description": "[Company description]",
  "sameAs": ["https://linkedin.com/company/...", "https://github.com/..."],
  "subOrganization": [
    {
      "@type": "SoftwareApplication",
      "name": "[Product Name]",
      "url": "https://product.ai",
      "applicationCategory": "[Category]"
    }
  ]
}
```

## Entity & Knowledge Panel

See **entity-seo** for full entity optimization. Key for multi-domain:
- **Consistency**: Same brand name, description, logo across Hub and Spoke
- **Entity Home**: Authoritative About page on Hub as primary reference
- **Knowledge Panel**: Claim via Google; suggest updates when available

## Output Format

- **Hub vs Spoke** mapping (domains, roles)
- **On-page checklist** (Hub and Spoke)
- **Schema** (Organization with subOrganization)
- **Internal linking** plan
- **Cannibalization** check

## Related Skills

- **domain-architecture**: Hub-Spoke structure; when to use multiple domains
- **schema-markup**: Organization, SoftwareApplication; subOrganization
- **serp-features**: Knowledge Panel, Sitelinks; brand SERP
- **entity-seo**: Entity & Knowledge Panel; Organization schema; consistency
- **rebranding-strategy**: Domain change; 301 redirects during transition
