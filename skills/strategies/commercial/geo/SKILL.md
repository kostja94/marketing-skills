---
name: generative-engine-optimization
description: When the user wants to optimize for AI search visibility (ChatGPT, Claude, Perplexity, AI Overviews). Also use when the user mentions "GEO," "AEO," "generative engine optimization," "AI search visibility," "LLM optimization," "GitHub GEO," "Grokipedia," "optimize for ChatGPT," "AI Overviews," "Bing Copilot," "Yandex AI," "Perplexity optimization," "GEO strategy," or "AI search optimization." For third-party publishing strategy (which platforms to use), use parasite-seo. For GitHub repos, README, and Awesome lists, use github. For Medium.com only, use medium-posts. For Grokipedia edits, use grokipedia-recommendations. For traditional Google SERP strategy, use seo-strategy.
metadata:
  version: 1.3.0
---

# Strategies: GEO (Generative Engine Optimization)

Guides GEO/AEO strategy for AI search visibility. GEO optimizes content for ChatGPT, Claude, Perplexity, and AI search summaries (Google AI Overviews, Bing Copilot, Yandex Search with AI)—getting cited in AI-generated answers rather than ranking in traditional SERPs. See **serp-features** for AI search as SERP features; **featured-snippet** for snippet optimization that overlaps with AI Overviews.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **GEO** = Generative Engine Optimization
- **AEO** = Answer Engine Optimization
- **LLMO** = Large Language Model Optimization
- **AIO** = Artificial Intelligence Optimization

All refer to the same goal: visibility in AI assistant responses.

## GEO vs. SEO

| Dimension | SEO | GEO |
|-----------|-----|-----|
| **Goal** | Rankings in search results | Citations in AI answers |
| **User path** | Click → visit → convert | Answer in-place; may not visit |
| **Content** | Full page optimization | Clear, citable paragraphs |
| **Metrics** | Clicks, traffic | Citations, brand mentions |
| **Platforms** | Google, Bing, Yandex (organic) | AI Overviews, Copilot, Yandex AI, ChatGPT, Perplexity |

**Both matter**: Create content that ranks and gets cited. AI search summaries (AI Overviews, Copilot, Yandex AI) are **SERP features**—see **serp-features**. When SERP features cause **zero-click** (user gets answer without clicking), citation becomes the primary value; optimize for being cited, not just ranked.

## AI Search Platforms (SERP Features + Standalone)

| Platform | Type | Source Selection | Optimization Focus |
|----------|------|------------------|---------------------|
| **Google AI Overviews** | SERP feature | Top 10–12 organic; Gemini; favors older domains (49% over 15 yrs) | Traditional SEO; structured data; citable blocks |
| **Bing Copilot Search** | SERP feature | Bing index; GPT-4; 9.81% domain overlap with Google; favors younger domains (18.85%); LinkedIn signals for B2B | Bing optimization; LinkedIn presence; structured content |
| **Yandex Search with AI / Neuro** | SERP feature | Real-time Yandex search; YandexGPT; Russia-focused | Yandex indexing; Russian content; cited sources |
| **Perplexity** | Standalone | 200B+ URL index; independent crawl; favors recency, semantic alignment | Content freshness; semantic markup; mid-tier site opportunity |
| **ChatGPT (web search)** | Standalone | GPTbot; high-authority, frequently updated, LLM-friendly; favors older domains (45.8%) | Backlinks; structured data; authority signals |

**Citation behavior**: AI Overview citations 20–35% higher CTR than equivalent organic. Copilot: shortest responses, fewest links (~3.13/response). Perplexity: prominent URL citations, high trackability. [Geneo](https://geneo.app/blog/chatgpt-vs-perplexity-vs-google-ai-overview-geo-comparison/), [GEO AIO](https://geoaiomarketing.com/how-bing-copilot-selects-sources-compared-to-perplexity/)

## How GEO Works

- **RAG (Retrieval-Augmented Generation)**: AI tools search first, then generate answers. Optimize for search result performance to influence AI responses.
- **Search APIs**: Bing, Brave, etc. feed AI tools. SEO fundamentals still apply.
- **Core model training**: Long, costly; not practical for most strategies. Focus on RAG.

## Technical Crawlability (AI Crawlers)

AI crawlers (GPTBot, ClaudeBot, PerplexityBot) do **not** execute JavaScript—critical content must be in initial HTML. See **rendering-strategies** for SSR, SSG, CSR; **site-crawlability** for AI crawler optimization; **robots-txt** for allow/block. [Vercel/MERJ study](https://vercel.com/blog/the-rise-of-the-ai-crawler) (2024)

## Content Best Practices

| Practice | Purpose |
|----------|---------|
| **Direct-answer format** | Answer specific questions in clear paragraphs |
| **Entity signals** | Clear brand, product, author identity; see **entity-seo** |
| **Citable paragraphs** | Each block understandable on its own |
| **Distribution** | Website, **YouTube** (Google prioritizes YouTube in search; ~78% of social media citations in AI Overviews come from YouTube + Reddit), forums, Reddit—thoughtful comments can outrank blog posts |

### Article-Level GEO

For blog posts and articles, structure content for AI citation. Content with these elements is cited ~35% more frequently.

| Element | Guideline |
|---------|-----------|
| **TL;DR or Key Takeaways** | Choose one: **TL;DR** = 50–100 word bold summary paragraph; **Key Takeaways** = 5–7 bullet points; placed after intro |
| **QAE pattern** | Question (H2) → Answer (2 sentences) → Evidence (data, examples, lists) |
| **Answer-first** | Direct answer in first 40–60 words after each H2 |
| **Answer blocks** | 100–200 words per section; direct answer + context + evidence + nuance |
| **Structured formats** | Lists, tables, numbered steps increase citation rate |

See **article-content** for content creation; **article-page-generator** for page structure.

## Parasite SEO & High-Authority Platforms

**Parasite SEO** = Placing content on high-authority platforms to leverage their domain strength for rankings and AI citation. See **parasite-seo** for full strategy.

**GitHub**: Tier 2 technical authority; very high AI citation. See **github** for repos, README, Pages, gists, awesome lists.

**YouTube**: Google prioritizes YouTube in search; YouTube citations in AI Overviews surged 25.21% (2025). Long-form instructional and visual-demo videos dominate. See **youtube-seo** for channel and video optimization; **video-optimization** for website-embedded video SEO.

**Grokipedia**: xAI's AI encyclopedia; ChatGPT, Perplexity, Copilot cite it. See **grokipedia-recommendations** for adding recommendations or links. Contribute genuinely useful content; avoid manipulative placement (Google Site Reputation Abuse policy).

## Tools

- GEO tracking and optimization tools for measuring AI citation and visibility

## Key Insight

ChatGPT traffic converts ~6x higher than Google search. AI tool users often have clearer intent.

## Output Format

- **Content structure** for AI citation
- **Entity** optimization; see **entity-seo**
- **Distribution** strategy
- **Measurement** approach

## Related Skills

- **site-crawlability**: AI crawler optimization; URL/redirect management
- **rendering-strategies**: SSR, SSG, CSR; content in initial HTML for AI crawlers
- **robots-txt**: AI crawler allow/block (GPTBot, ClaudeBot, PerplexityBot)
- **parasite-seo**: Parasite SEO strategy; high-authority platforms for GEO
- **github**: GitHub for GEO; repos, README; Tier 2 technical authority
- **youtube-seo**: YouTube optimization; GEO distribution; Google prioritizes YouTube
- **serp-features**: **Strongly related**—AI Overviews, Bing Copilot, Yandex AI; platform comparison
- **featured-snippet**: Snippet optimization; overlaps with AI Overviews
- **entity-seo**: Entity signals; Organization, Person schema; GEO citation
- **article-content**: Article body creation; TL;DR, Key Takeaways, QAE pattern
- **article-page-generator**: Article page structure; schema; layout
- **faq-page-generator**: FAQ structure for GEO; citable Q&A blocks; content in initial HTML
- **howto-section-generator**: HowTo step sections; citable ordered procedures; HowTo JSON-LD
