---
name: analytics-ai-traffic
description: When the user wants to track AI search traffic in GA4 or GSC. Also use when the user mentions "AI traffic," "ChatGPT referral," "Perplexity traffic," "AI Overviews," "GA4 AI sources," or "AI search analytics."
metadata:
  version: 1.0.0
---

# Analytics: AI Traffic

Guides tracking of AI-driven search traffic in Google Analytics 4 and Google Search Console.

**When invoking**: On **first use**, if helpful, open with 1?2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Scope

- **AI search traffic**: Track in GA4 and GSC; separate AI sources from organic referral
- **Google AI Overviews**: AI summary box in Google search (formerly SGE)
- **AI-driven search**: Traffic from ChatGPT, Perplexity, Gemini, Claude, Copilot, etc.

## Why Track Separately

- AI traffic is growing but GA4 often groups it as Referral, Organic, or Direct
- AI visitors may have stronger intent and higher conversion
- Separating AI Overviews from organic helps assess AI impact

## GA4: AI-Driven Search

### Option 1: Exploration Report (Recommended)

1. **Explore** ??**Free form**
2. **Dimensions**: `Session source` (or `Session source / medium`)
3. **Metrics**: Sessions, Engagement rate, Event count, etc.
4. **Filters**: Add filter ??`Session source` **Matches regex** ??use regex below
5. Configure table, save report

**Regex (common AI sources):**

```
chatgpt\.com|openai\.com|openai|perplexity\.ai|perplexity|doubao\.com|chat\.qwen\.ai|copilot\.microsoft\.com|copilot\.com|(business\.)?gemini\.google|chat\.deepseek\.com|deepseek\.com|poe\.com|anthropic\.com|claude\.ai|bard\.google\.com|edgeservices\.bing\.com
```

### Option 2: Custom Channel Group

1. **Admin** ??**Data Display** ??**Channel Groups**
2. Copy default group, name e.g. "Default and AI Chatbots"
3. Add channel "AI Chatbots": `Source` **Matches regex** (same regex)
4. **Important**: Place "AI Chatbots" above "Referral" so it matches first
5. Save and use in Traffic Acquisition

### Option 3: Custom Report

1. **Reports** ??**Library** ??Create Detail Report
2. Use Traffic Acquisition template
3. Add filter: `Session source` **Matches regex** (same regex)
4. Save and add to menu

## Common AI Source Domains

| Platform | GA4 Source examples |
|----------|---------------------|
| ChatGPT | chatgpt.com, openai |
| Perplexity | perplexity.ai, perplexity |
| Copilot | copilot.com, copilot.microsoft.com |
| Gemini | business.gemini.google, gemini.google |
| Claude | claude.ai, anthropic.com |
| Bing Chat | edgeservices.bing.com |

## Google AI Overviews

- **GA4 + URL fragment**: Some AI Overview clicks add URL fragments; can use GTM (partial coverage)
- **GSC**: For AI Overviews analysis in GSC (filter, limitations), see analytics-google-search-console

## Checklist

- [ ] AI sources identified in GA4 (Session Source)
- [ ] AI traffic Exploration report created
- [ ] Channel group updated with AI above Referral (if used)
- [ ] Custom report added to Library (optional)
- [ ] GTM + URL fragment for AI Overviews (optional)
- [ ] GSC AI-oriented query filter (optional; see analytics-google-search-console)

## Output Format

- **GA4 setup**: Exploration, channel group, or custom report
- **Regex**: Adapted to user's observed sources

## Related Skills

- **analytics-traffic**: Traffic sources, attribution, UTM
- **analytics-tracking**: GA4 events and conversions
- **analytics-google-search-console**: GSC AI traffic analysis
- **seo-technical-robots**: AI crawler allow/block strategy
