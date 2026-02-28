---
name: blog-page-generator
description: When the user wants to create, optimize, or audit blog page structure and content. Also use when the user mentions "blog page," "blog index," "blog layout," "content hub," "blog homepage," "blog listing," "subdomain vs subdirectory," "blog structure," or "blog SEO."
metadata:
  version: 1.0.0
---

# Pages: Blog

Guides blog page structure, SEO, and content marketing best practices.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for topics, audience, and keywords.

Identify:
1. **Blog purpose**: SEO traffic, thought leadership, product education
2. **Content mix**: Pillar pages, cluster content, news
3. **Audience**: Buyers, existing customers, developers

## Best Practices

### Blog Placement: Subdomain vs Subdirectory

| Option | Example | SEO / Use |
|--------|---------|-----------|
| **Subdirectory** | `example.com/blog` | SEO weight flows to main domain; recommended for product blogs |
| **Subdomain** | `blog.example.com` | Treated as separate entity; consider for distinct brands or technical isolation |

Choose based on SEO weight distribution, brand consistency, and technical architecture. See [Alignify subdomain vs subdirectory guide](https://alignify.co/zh/seo/create-blog) for details.

### Blog Index Page Structure

| Section | Purpose |
|---------|---------|
| **Featured/Recent** | Highlight newest or most important posts |
| **Categories/Topics** | Help users find by theme |
| **Editor's Picks** | Curate best content |
| **Related posts** | Per-article recommendations |
| **Search** | Help users find specific topics |

### Content Strategy

- **Topical authority**: Topic clusters -> pillar page per core topic + 6-12 cluster articles
- **Intent mapping**: Transactional, problem-aware, informational
- **EEAT signals**: Author bios, Organization schema, citations, changelog
- **Refresh > new**: For established sites, updating existing content often outperforms publishing new posts; avoid changing only the date without substantive edits
- **Quality > quantity**: Fewer high-quality posts beat many mediocre ones; consider deleting, merging, or refreshing underperformers
- **Topic focus**: Avoid blindly expanding topics; dilution can hurt authority on core topics
- **Conversion as north star**: SEO KPIs should tie to leads, signups, or sales -> not just traffic

### SEO

- **Title**: 55 chars, power words, primary keyword
- **Meta**: Clear CTA in description
- **Headers**: H1-H3 hierarchy, table of contents
- **Content depth**: 2,500+ words for pillars; Grade 8 readability
- **URL**: Use **url-slug-generator** -> clean slugs, 3-5 words, under 60 chars
- **Schema**: Article, BlogPosting, FAQPage where relevant

### Technical

- **Core Web Vitals**: LCP < 1.0s on mobile
- **Images**: WebP, compressed
- **IndexNow**: For fast indexing of new posts

### Design

- **Scannable**: Preview copy, thumbnails, hero images
- **Social sharing**: Share buttons on article pages -> see **social-share-generator**
- **Quick answers**: Definition boxes, mini-FAQs for AEO
- **TOC**: Table of contents for Featured Snippets; jump links in long articles
- **CTA placement**: Sidebar CTA or in-paragraph CTA at key conversion points
- **Related/Recent posts**: Manual curation or plugin; same topic cluster

## Output Format

- **Structure** for blog index and post template
- **Content** strategy (pillar + clusters)
- **SEO** metadata and schema
- **Internal linking** approach

## Related Skills

- **article-page-generator**: Single article/post page structure, SEO, schema -> use for individual post templates
- **url-slug-generator**: URL slug for blog posts; 3-5 words, primary keyword
- **content-strategy**: Content clusters, editorial calendar
- **keyword-research**: Keywords for blog topics
- **title-tag, meta-description, page-metadata, open-graph, twitter-cards**: Blog metadata and social previews
- **schema-markup**: Article schema
- **resources-page-generator**: Blog may be part of resources hub
