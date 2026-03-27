---
name: rebranding-strategy
description: When the user wants to plan or execute a rebrand—domain change, 301 redirects, migration, or announcement. Also use when the user mentions "rebranding," "rebrand," "domain change," "domain migration," "301 redirect," "change domain name," "rebrand announcement," "social media rebrand," "brand launch," or "domain redirect." For domain choice, use domain-selection.
metadata:
  version: 1.0.1
---

# Strategy: Rebranding

Guides rebranding execution: domain change, 301 redirects, migration checklist, and communication (social media, internal). Plan for months, not days or weeks. See **domain-selection** for initial domain choice; **domain-architecture** for domain structure decisions; **multi-domain-brand-seo** when multiple domains coexist.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for brand and product info.

Identify:
1. **Scope**: Full rebrand (name, domain, identity) vs partial (logo, messaging only)
2. **Domain change**: Yes or no; old → new mapping
3. **Timeline**: Target launch date; typical 4–12 weeks
4. **Channels**: Website, social, product UI, directories, email

## Rebranding Timeline (Typical)

| Phase | Duration | Focus |
|-------|----------|-------|
| **Audit & plan** | Weeks 1–2 | Brand audit; inventory touchpoints; migration plan |
| **Prepare** | Weeks 2–6 | New assets; redirect mapping; staging; backup |
| **Pre-launch** | Week 6–8 | Internal announcement; social handle check; teasers |
| **Launch** | Week 8+ | Go live; 301 redirects; multi-channel announcement |
| **Post-launch** | 2–4 weeks | Monitor search, traffic; fix 404s; iterate |

**Principle**: Plan for months. Avoid changing domain and major structure in one migration—split into smaller migrations when possible.

## 301 Redirect Best Practices

| Practice | Purpose |
|----------|---------|
| **1:1 mapping** | Each old URL → most relevant new URL; never redirect all to homepage |
| **301 (permanent)** | Use 301, not 302; 302 does not fully transfer SEO equity |
| **No chains/loops** | Old URL → final destination directly; avoid A→B→C |
| **Redirect mapping sheet** | Document every old→new mapping; prevents ~80% of migration failures |
| **Don't block in robots.txt** | Redirected URLs should not be disallowed |

### Common Mistakes

- Redirect chains (multiple hops)
- Redirect loops
- Redirecting everything to homepage
- Using 302 for permanent moves
- Blocking redirected URLs in robots.txt

## Domain Migration Checklist

### Pre-Migration

- [ ] Create SEO migration plan
- [ ] Collect benchmarks (GA4, GSC, rankings)
- [ ] Run site crawler; inventory all pages
- [ ] Create redirect mapping sheet (old URL → new URL)
- [ ] Purchase new domain; configure DNS
- [ ] Technical SEO audit
- [ ] Staging environment; backup
- [ ] Check for manual penalties on both domains

### Launch

- [ ] Implement 301 redirects
- [ ] Update Google Search Console (change of address)
- [ ] Update sitemaps, robots.txt
- [ ] Verify new site works; test redirects (curl, Screaming Frog)
- [ ] Add GA4 annotation for migration date

### Post-Migration

- [ ] Monitor GSC coverage; fix "Page with Redirect" issues
- [ ] Fix 404s immediately
- [ ] Expect temporary ranking fluctuation (2–4 weeks)
- [ ] Do not delete old site as fallback

## Social Media Announcement

### Three Phases

| Phase | Actions |
|-------|---------|
| **Pre-Launch** | Finalize new identity; audit social presence; secure handles across platforms; internal alignment |
| **Build Anticipation** | Tease with sneak peeks; cryptic visuals; influencer/ambassador previews; avoid announcing too soon |
| **Execute** | All platforms updated together; new bios, handles, visuals; compelling rebrand story (why, not what) |

### What to Avoid

- Don't list steps or technical details—focus on story and benefit
- Don't announce before all pieces are in place (mixed messaging)
- Don't rely on one channel—multi-channel rollout
- Don't bombard with "why we rebranded" unless it resonates

### Rebrand Story

- **Anchor**: Emotionally resonating narrative; why now; how it benefits customers
- **Avoid**: "We changed our logo" / "We updated our website" without context

## Internal Communication

- Brief all employees before public launch
- Explain strategic reasons; equip them to answer customer questions
- Update email signatures, Slack, internal docs
- Internal FAQ for common rebrand questions

## Output Format

- **Timeline** (phases, milestones)
- **Redirect mapping** approach (template, tools)
- **Migration checklist** (customized)
- **Social announcement plan** (phases, channels, content angles)
- **Internal communication** (briefing, FAQ)

## Related Skills

- **domain-selection**: Domain choice (Brand/PMD/EMD, TLD); informs new domain choice when rebranding
- **domain-architecture**: Domain structure before/after rebrand
- **website-structure**: New site structure after migration
- **schema-markup**: Update Organization schema on new domain
- **multi-domain-brand-seo**: When old and new domains coexist during transition
- **branding**: Brand strategy, identity; rebranding implements the change
- **brand-protection**: Sync impersonation checks when rebranding; update official domain declaration
- **gtm-strategy**: Repositioning GTM; when repositioning includes rebrand
