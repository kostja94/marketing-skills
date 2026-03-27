---
name: robots-txt
description: When the user wants to configure, audit, or optimize robots.txt. Also use when the user mentions "robots.txt," "crawler rules," "block crawlers," "AI crawlers," "GPTBot," "allow/disallow," "disallow path," "crawl directives," "user-agent," "block Googlebot," "fix robots.txt," "robots.txt blocking," or "search engine crawling." For indexing, use indexing.
metadata:
  version: 1.1.1
---

# SEO Technical: robots.txt

Guides configuration and auditing of robots.txt for search engine and AI crawler control.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope (Technical SEO)

- **Robots.txt**: Configure Disallow/Allow, Sitemap, Clean-param; audit for accidental blocks
- **Crawler access**: Path-level crawl control; AI crawler allow/block strategy
- **Differentiation**: robots.txt = crawl control (who accesses what paths); noindex = index control (what gets indexed). See **indexing** for page-level exclusions.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for site URL and indexing goals.

Identify:
1. **Site URL**: Base domain (e.g., `https://example.com`)
2. **Indexing scope**: Full site, partial, or specific paths to exclude
3. **AI crawler strategy**: Allow search/indexing vs. block training data crawlers

## Best Practices

### Purpose and Limitations

| Point | Note |
|-------|------|
| **Purpose** | Controls crawler access; does NOT prevent indexing (disallowed URLs may still appear in search without snippet) |
| **Advisory** | Rules are advisory; malicious crawlers may ignore |
| **Public** | robots.txt is publicly readable; use noindex or auth for sensitive content. See **indexing** |

### Crawl vs Index vs Link Equity (Quick Reference)

| Tool | Controls | Prevents indexing? |
|------|----------|-------------------|
| **robots.txt** | Crawl (path-level) | No—blocked URLs may still appear in SERP |
| **noindex** (meta / X-Robots-Tag) | Index (page-level) | Yes. See **indexing** |
| **nofollow** | Link equity only | No—does not control indexing |

### When to Use robots.txt vs noindex

| Use | Tool | Example |
|-----|------|---------|
| **Path-level** (whole directory) | robots.txt | `Disallow: /admin/`, `Disallow: /api/`, `Disallow: /staging/` |
| **Page-level** (specific pages) | noindex meta / X-Robots-Tag | Login, signup, thank-you, 404, legal. See **indexing** for full list |
| **Critical** | Do NOT block in robots.txt | Pages that use noindex—crawlers must access the page to read the directive |

**Paths to block in robots.txt**: /admin/, /api/, /staging/, temp files. **Paths to use noindex** (allow crawl): /login/, /signup/, /thank-you/, etc.—see **indexing**.

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

### Critical: Do Not Block

| Do not block | Reason |
|--------------|--------|
| CSS, JS, images | Google needs them to render pages; blocking breaks indexing |
| `/_next/` (Next.js) | Breaks CSS/JS loading; static assets in GSC "Crawled - not indexed" is expected. See **indexing** |
| Pages that use noindex | Crawlers must access the page to read the noindex directive; blocking in robots.txt prevents that |

**Only block**: paths that don't need crawling: /admin/, /api/, /staging/, temp files.

### AI Crawler Strategy

robots.txt is effective for all measured AI crawlers ([Vercel/MERJ study](https://vercel.com/blog/the-rise-of-the-ai-crawler), 2024). Set rules per user-agent; check each vendor's docs for current tokens.

| User-agent | Purpose | Typical |
|------------|---------|---------|
| **OAI-SearchBot** | ChatGPT search | Allow |
| **GPTBot** | OpenAI training | Disallow |
| **Claude-SearchBot** | Claude search | Allow |
| **ClaudeBot** | Anthropic training | Disallow |
| **PerplexityBot** | Perplexity search | Allow |
| **Google-Extended** | Gemini training | Disallow |
| **CCBot** | Common Crawl (LLM training) | Disallow |
| **Bytespider** | ByteDance | Disallow |
| **Meta-ExternalAgent** | Meta | Disallow |
| **AppleBot** | Apple (Siri, Spotlight); renders JS | Allow for indexing |

**Allow vs Disallow**: Allow search/indexing bots (OAI-SearchBot, Claude-SearchBot, PerplexityBot); Disallow training-only bots (GPTBot, ClaudeBot, CCBot) if you don't want content used for model training. See **site-crawlability** for AI crawler optimization (SSR, URL management).

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

- **indexing**: Full noindex page-type list; when to use noindex vs robots.txt; GSC indexing diagnosis
- **page-metadata**: Meta robots (noindex, nofollow) implementation
- **xml-sitemap**: Sitemap URL to reference in robots.txt
- **site-crawlability**: Broader crawl and structure guidance; AI crawler optimization
- **rendering-strategies**: SSR, SSG, CSR; content in initial HTML for crawlers
