---
name: product-launch
description: When the user wants to plan a product launch, execute launch channels, or create a launch checklist. Also use when the user mentions "product launch," "launch strategy," "product announcement," "launch channels," or "market launch." For GTM motion and positioning, use gtm-strategy. For cold start and first users, use cold-start-strategy. For Product Hunt day-of, use product-hunt-launch.
metadata:
  version: 1.2.0
---

# Strategies: Product Launch

Guides product launch execution—channels, timeline, checklist, and cross-functional coordination. Use this skill when planning the launch of a new product or major feature. For GTM strategy (PLG/SLG/MLG, 90-day framework, ICP, new market entry, repositioning), see **gtm-strategy**. For cold start (first users, no product yet), see **cold-start-strategy**.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read full file.

Identify:
1. **Launch type**: New product, major feature, market expansion
2. **GTM mode**: Sales-led, product-led, marketing-led, hybrid (from **gtm-strategy**)
3. **Channels**: PR, paid, organic, email, events

## Launch Checklist

- [ ] GTM strategy defined (see **gtm-strategy**)
- [ ] PMF validated (see **pmf-strategy**)
- [ ] Target market and ICP clear
- [ ] Messaging consistent across teams
- [ ] Channel mix chosen (PR, paid, organic, email)
- [ ] Timeline and milestones set
- [ ] Cross-functional owners assigned (RACI)

## Channel Mix

| Channel | Use | Skills |
|---------|-----|--------|
| **PR** | Press release, media relations | public-relations |
| **Paid ads** | Scale acquisition post-PMF | paid-ads-strategy |
| **Organic** | SEO, content, community | seo-strategy, content-marketing |
| **Email** | Announcement to existing users | email-marketing |
| **Product Hunt / Directories** | Launch-day buzz; early adopters | cold-start-strategy, directory-submission |

## Critical Success Factors

| Factor | Guideline |
|--------|-----------|
| **PMF first** | Validate product-market fit before scaling; see **pmf-strategy** |
| **GTM alignment** | One clear story; all teams use same messaging; see **gtm-strategy** |
| **Avoid rush** | Most failures = scale before PMF |

## Output Format

- **Launch plan** (timeline, channels, owners)
- **Channel** actions (PR, paid, organic, email)
- **Checklist** (pre-launch, launch, post-launch)
- **Cross-ref** to gtm-strategy for framework

## Related Skills

- **gtm-strategy**: GTM framework; modes, 90-day, ICP, new market, repositioning; product launch implements GTM for new product
- **pmf-strategy**: Validate PMF before scaling
- **cold-start-strategy**: First users; Product Hunt; differs from full GTM launch
- **indie-hacker-strategy**: Indie hacker launch; Build in Public; first 100 users
- **public-relations**: Press release; media relations for launch
- **paid-ads-strategy**: Paid channel for launch
- **website-structure**: Pages needed for launch
