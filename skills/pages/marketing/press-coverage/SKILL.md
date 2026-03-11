---
name: press-coverage-page-generator
description: When the user wants to create a press coverage page, "As Seen In" section, or media mentions aggregation. Also use when the user mentions "press coverage," "media mentions," "as seen in," "as featured in," "in the news," "press mentions," "media coverage page," or "trusted by publications."
metadata:
  version: 1.0.0
---

# Pages: Press Coverage

Guides press coverage and media mentions aggregation—showcasing third-party coverage from authoritative sites to build trust. Optional page; when coverage is sparse, implement as a small "As Seen In" or "As Featured In" section on homepage or elsewhere. Distinct from **media-kit-page-generator** (assets for journalists). For conceptual overview and comparison table, see [reference.md](reference.md).

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read for company story and key messages.

Identify:
1. **Coverage volume**: Few mentions vs substantial
2. **Format**: Full page vs section
3. **Sources**: Publications, podcasts, awards, industry lists

## Full Page vs Section

| Format | When to Use | Placement |
|--------|-------------|-----------|
| **Full page** | Substantial coverage (10+ mentions); journalists visit for expert contacts; "inbound PR" | /press, /news, /in-the-news |
| **Section** | Sparse coverage (1–10); quick credibility; logo strip or quote carousel | Homepage below hero; About page; footer |

**Rule**: Homepage section = logos only, minimal, below main CTA. Full page = headlines, links, dates, contact.

## Full Page Structure

| Element | Guideline |
|---------|-----------|
| **Coverage list** | Chronological or by publication; headline, outlet, date, link |
| **Separation** | Press coverage (third-party) vs press releases (company-authored); coverage carries more credibility |
| **Types** | News, podcasts, video features, awards, "Best X" lists |
| **Contact** | Media inquiries; link to media kit |
| **Dates** | Optional on evergreen content; omit to keep timeless |

## Section Structure ("As Seen In" / "As Featured In")

| Element | Guideline |
|---------|-----------|
| **Logos** | Publication logos; high-contrast, consistent size |
| **Placement** | Below hero/CTA; above fold or just below |
| **Quote** | Optional: one compelling snippet; extract from best coverage |
| **Link** | Optional: "See all coverage" → full page if exists |

**Avoid**: Clutter; too many logos; low-authority outlets that dilute trust.

## Content Types to Aggregate

| Type | Example |
|------|---------|
| **News articles** | Forbes, Bloomberg, TechCrunch, industry trade |
| **Podcasts** | Interview features, guest appearances |
| **Video** | TV segments, YouTube features |
| **Awards** | "Best X 2024," "Top 10 Startups" |
| **Reviews** | Product reviews, roundups |

## Trust Principles

- **Third-party > self-authored**: Media mentions beat press releases for credibility
- **Authority matters**: Forbes, Bloomberg > unknown blogs
- **Recency**: Recent coverage signals active business; update regularly

## Output Format

- **Format** (full page vs section) recommendation
- **Structure** (elements, order)
- **Copy** (headline, intro if full page)
- **Placement** (URL, page location)
- **SEO**: Index for "company name press" / "company name news"; or noindex if thin

## Related Skills

- **media-kit-page-generator**: Press assets for journalists; press coverage page can link to media kit; distinct purposes (coverage = social proof for visitors; media kit = assets for press)
- **homepage-generator**: "As Seen In" section often on homepage
- **about-page-generator**: Press quotes can appear on About
- **customer-stories-page-generator**: Social proof; different from press (customer success vs media coverage)
- **trust-badges-generator**: "Trusted by" logos; similar visual treatment
- **public-relations**: Press release creation; coverage is outcome of PR
