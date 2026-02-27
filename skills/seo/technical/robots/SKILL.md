---
name: seo-technical-robots
description: When the user wants to configure, audit, or optimize robots.txt. Also use when the user mentions "robots.txt," "crawler rules," "block crawlers," "AI crawlers," "GPTBot," "allow/disallow," or "search engine crawling."
metadata:
  version: 1.0.0
---

# SEO Technical: robots.txt

Guides configuration and auditing of robots.txt for search engine and AI crawler control.

**When invoking**: On **first use**, if helpful, open with 1â€? sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **Robots.txt**: Review Disallow/Allow; avoid blocking important pages
- **Crawler access**: Ensure crawlers (including AI crawlers) can access key pages
- **Indexing**: Misconfigured robots.txt can block indexing; verify no accidental blocks

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for site URL and indexing goals.

Identify:
1. **Site URL**: Base domain (e.g., `https://example.com`)
2. **Indexing scope**: Full site, partial, or specific paths to exclude
3. **AI crawler strategy**: Allow search/indexing vs. block training data crawlers

## Best Practices

### Purpose and Limitations

| Point | Note |
|-------|------|
| **Purpose** | Controls crawler access; does NOT prevent indexing (disallowed URLs may still appear in search without snippet) |
| **No-index** | Use noindex meta or auth for sensitive content; robots.txt is publicly readable |
| **Indexed vs non-indexed** | Not all content should be indexed. robots.txt and noindex complement each other: robots for path-level crawl control, noindex for page-level indexing. See seo-technical-indexing |
| **Advisory** | Rules are advisory; malicious crawlers may ignore |

### Location and Format

| Item | Requirement |
|------|-------------|
| **Path** | Site root: `https://example.com/robots.txt` |
| **Encoding** | UTF-8 plain text |
| **Standard** | RFC 9309 (Robots Exclusion Protocol) |

### Core Directives

| Directive | Purpose | Example |
|-----------|---------|---------|
| `User-agent:` | Target crawler | `User-agent: Googlebot`, `User-agent: *` |
| `Disallow:` | Block path prefix | `Disallow: /admin/` |
| `Allow:` | Allow path (can override Disallow) | `Allow: /public/` |
| `Sitemap:` | Declare sitemap absolute URL | `Sitemap: https://example.com/sitemap.xml` |
| `Clean-param:` | Strip query params (Yandex) | See below |

### Critical: Do Not Block Rendering Resources

- **Do not** block CSS, JS, images; Google needs them to render pages
- **Only** block paths that don't need crawling: admin, API, temp files

### AI Crawler Strategy

| User-agent | Purpose | Typical |
|------------|---------|---------|
| **OAI-SearchBot** | ChatGPT search | Allow |
| **GPTBot** | OpenAI training | Disallow |
| **Claude-SearchBot** | Claude search | Allow |
| **ClaudeBot** | Anthropic training | Disallow |
| **PerplexityBot** | Perplexity search | Allow |
| **Google-Extended** | Gemini training | Disallow |
| **CCBot** | Common Crawl | Disallow |

### Clean-param (Yandex)

```
Clean-param: utm_source&utm_medium&utm_campaign&utm_term&utm_content&ref&fbclid&gclid
```

## Output Format

- **Current state** (if auditing)
- **Recommended robots.txt** (full file)
- **Compliance checklist**
- **References**: [Google robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt)

## Related Skills

- **seo-technical-sitemap**: Sitemap URL to reference in robots.txt
- **seo-technical-crawlability**: Broader crawl and structure guidance
