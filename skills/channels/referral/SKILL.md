---
name: channels-referral
description: When the user wants to plan, implement, or optimize referral program strategy. Also use when the user mentions "referral program," "referral marketing," "user referral," "refer-a-friend," or "word-of-mouth growth."
metadata:
  version: 1.0.0
---

# Channels: Referral

Guides referral program strategy for AI/SaaS products. Leverage existing users to drive growth; 3%-5% conversion vs 1%-2% for ads; CAC 50%-70% lower; referred users LTV 30%-50% higher, retention 20%-30% higher. Referral is necessity in overseas markets, not alternative.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for product, audience, and value proposition.

Identify:
1. **Product type**: SaaS, AI tool, subscription
2. **User base**: Size, engagement, retention
3. **Goal**: Signups, purchases, or both

## Referral vs. Affiliate vs. Influencer

| Dimension | Referral | Affiliate | Influencer |
|-----------|----------|-----------|------------|
| **Who** | Existing users | Professional promoters | KOLs |
| **Incentive** | Discounts, credits | Commission | Fees, product |
| **Barrier** | Low (all users) | Medium | High |
| **Conversion** | 3%-5% | Varies | Varies |

**Referral vs affiliate**: Referral needs no landing page or application; integrated in dashboard. Affiliate requires landing page and approval.

## Reward Models

| Model | Use |
|-------|-----|
| **Two-way** | Both referrer and referee get rewards; highest participation |
| **One-way** | Only referrer rewarded; cost control |
| **Tiered** | Rewards increase with referral count (e.g. $10 for 1-5, $15 for 6-10, $20 for 11+); incentivizes volume |

**Benchmark**: Rewards typically 10%-30% of product price; ~11% off or ~$21 value; weak incentives = low participation. Triggers: signup, purchase, activation, or sustained use.

## Mechanism Types

| Type | Use |
|------|-----|
| **Link-based** | Unique referral link; easy to implement; accurate tracking; share via email, social, SMS; works for web and app |
| **Code-based** | Referral code (e.g. FRIEND20); memorable; offline events; mobile-friendly input |
| **Social referral** | Share buttons (Facebook, X, LinkedIn); viral spread; friend trust; young users |

## Tracking & Attribution

| Method | Use |
|-------|-----|
| **Cookie** | Web apps; 30-90 day window |
| **URL params** | All platforms; persistent in link |
| **Referral code** | Mobile, offline; manual entry |
| **Account association** | Long-term tracking; subscription products |

**Attribution window**: 30-90 days typical; 180 days for subscription. First-touch attribution to avoid double-counting.

## Fraud Prevention

| Risk | Action |
|------|--------|
| **Self-referral** | Detect same device, payment, IP |
| **Fake accounts** | Validate email, payment; monitor patterns |
| **Bulk/automation** | Rate limits; anomaly detection |
| **Per-user cap** | e.g. Max 10 referrals per user |

Use tool anti-fraud features; audit referrals regularly.

## Design Framework

1. **Reward structure**: Type (cash, discount, credits, free service); amount (10%-30% of price); trigger; cap
2. **Tracking**: Choose method; set attribution window; first-touch rule
3. **UX**: One-click share; clear rules; dashboard with referral data; notify on success
4. **Fraud prevention**: See above
5. **Monitor & optimize**: Referral rate, conversion, CAC, LTV; A/B test rewards and flow

## Best Practices

- **Run multiple programs**: Target different audiences, stages, goals
- **Tiered rewards**: Motivate top performers; progressive incentives
- **Friction-free sharing**: Mobile-friendly; one-click share
- **Time-boxed incentives**: "Refer this week for $15 off" creates urgency
- **Placement**: Web, email, app, in-product touchpoints; dashboard integration primary

## Implementation

| Approach | Use |
|----------|-----|
| **Self-build** | Full control; low cost; URL params or cookie + reward logic + fraud checks; open-source (e.g. RefRef) for faster start |
| **Third-party** | Fast launch; Cello, Viral Loops, ReferralCandy (e-commerce), Impact (enterprise); monthly fee |

**Placement**: Most programs integrate in product dashboard; no landing page or application needed. Optional landing page for value prop, rewards, and case studies.

**Startup cost**: Typically hundreds for tools + dev.

## Tools

| Tool | Use |
|------|-----|
| **Cello** | SaaS; AI-driven automation |
| **Viral Loops** | Referral + waitlist + contests |
| **ReferralCandy** | Shopify, e-commerce |
| **Impact** | Enterprise; unified platform |
| **RefRef** | Open-source; self-hosted |

## KPIs

Referral rate, conversion, CAC, LTV of referred users, referred-user retention.

## Output Format

- **Reward model** and mechanism type (link/code/social)
- **Tracking** approach and attribution window
- **Placement** (dashboard vs landing page)
- **Fraud prevention** measures
- **Tool** selection (self-build vs third-party)
- **KPI** framework

## Related Skills

- **channels-affiliate**: Different audience; can run both
- **channels-influencer**: Brand building vs. user-driven growth
- **channels-directories**: Directory submission for discovery; referral for user-driven growth
- **analytics-tracking**: Referral link tracking, UTM
