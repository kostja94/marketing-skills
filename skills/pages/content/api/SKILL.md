---
name: pages-api
description: When the user wants to create, optimize, or audit the API introduction/overview page. Also use when the user mentions "API page," "API landing page," or "/api page." Note: API documentation (endpoint reference, developer docs) is a separate page type.
metadata:
  version: 1.0.0
---

# Pages: API Introduction

Guides the API introduction page ??typically at `/api` ??that overviews the API, use cases, and links to documentation. API documentation (endpoint reference, code examples) lives on separate pages.

**When invoking**: On **first use**, if helpful, open with 1?2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product and developer use cases.

Identify:
1. **API type**: REST, GraphQL, etc.
2. **Audience**: Developers (integration) vs. decision makers (evaluation)
3. **Docs location**: Where API documentation lives (e.g. `/docs`, `/api/reference`, external)

## Page Role

- **API page** (`/api`): Introduction, overview, value prop, CTA to docs or signup
- **API documentation**: Separate pages ??endpoint reference, auth, examples, tutorials

## Best Practices

### Overview and Structure

- **What the API does**: Clear value proposition, key capabilities
- **Use cases**: Who uses it, common scenarios
- **Getting started**: Quick path to first call or docs
- **Link to docs**: Prominent CTA to API documentation

### Content

- **Key concepts**: High-level, not endpoint-level detail
- **Auth overview**: How auth works; link to docs for details
- **Pricing/limits**: If relevant for evaluation
- **SDKs and tools**: If available; link to docs

### SEO and Discovery

- **Developer search**: Target "API" + product/category terms
- **Metadata**: Title, description for developer intent
- **Internal links**: From homepage, features, resources

## Output Format

- **Structure** outline (sections)
- **Value proposition** and key messages
- **CTA** to documentation or signup
- **SEO** metadata for developer search

## Related Skills

- **pages-home**: Link to API page for developers
- **seo-on-page-schema**: WebPage or SoftwareApplication schema
- **seo-on-page-metadata**: API page metadata
