---
name: shipping-page-generator
description: When the user wants to create or optimize a shipping or delivery information page. Also use when the user mentions "shipping," "delivery," "shipping policy," "delivery times," "shipping page," "free shipping," "shipping rates," "delivery options," "shipping info," "cross-border shipping," "international delivery," or "order tracking." For legal overview, use legal-page-generator.
metadata:
  version: 1.1.0
---

# Pages: Shipping / Delivery

Guides shipping and delivery information page content for e-commerce, covering domestic and cross-border logistics, regulatory compliance, and AI-era discoverability.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

Identify:
1. **Shipping scope**: Domestic only, cross-border, or global — see §Shipping Scope
2. **Product type**: Physical goods (standard), digital/physical bundles, print-on-demand, dropshipping
3. **Carriers & methods**: Standard, express, overnight; carrier names; real-time vs flat-rate
4. **Regulatory exposure**: EU (2026 customs changes, AI Act), cross-border compliance
5. **AI discoverability**: Can delivery terms be parsed by AI shopping agents? — see §AI-Era Readiness

---

## Shipping Scope

| Scope | Key Considerations |
|---|---|
| **Domestic Only** | Simplest; focus on carrier options, timelines, cutoffs, free-shipping thresholds |
| **Regional** (e.g., EU-wide) | Harmonized customs within single market; local carrier partnerships; OOH networks |
| **Cross-Border / Global** | DDP vs DDU; customs duties transparency; multi-carrier tracking normalization; per-market configurability |

---

## AI-Era Readiness — Critical for 2026

The most significant shift in 2025–2026: **58% of consumers have replaced traditional search engines with GenAI tools** for product research and price comparison (Capgemini 2026). AI shopping agents compare delivery dates, costs, return terms, and total landed costs **before** the shopper ever visits your site.

**What this means for shipping policies**:
- Delivery terms must be **machine-readable and structured** — an AI agent scraping your site must be able to extract delivery promises, costs, cut-off times, and geographic availability
- If your delivery terms are buried in unstructured paragraphs, AI agents may **exclude your brand** from consideration entirely
- Standardize delivery options in consistent formats: option name | cost | timeline | cutoff | regions

**Practical recommendations**:
- Use structured data (schema.org `OfferShippingDetails`) on product and checkout pages
- State delivery promises as clearly as shipping-rate tables — avoid prose-only descriptions
- Keep policy page content synchronized with structured data (mismatches erode AI trust)

---

## EU Regulatory Deadlines (2026)

Two major compliance deadlines converge in summer 2026:

### EU Customs — July 1, 2026

A fixed **€3 customs duty** applies to all consignments valued under €150 entering the EU. This covers **93% of e-commerce imports** into the EU.

**Shipping policy impact**:
- **Landed-cost transparency at checkout is mandatory** — customers must see the total price including duties, taxes, and fees before completing purchase
- If using DDU (duties collected at delivery), explicitly warn: "Additional customs fees of approximately €X may be collected on delivery"
- **DDP (Delivered Duty Paid) is strongly recommended** — surprise duties at the door are the #1 cause of refused parcels and lost repeat purchases

### EU AI Act — August 2026

Online marketplaces and e-commerce platforms using AI for shipping decisions (carrier selection, delivery predictions, automated refund/reroute decisions) must comply with transparency obligations:

- Automated decisions affecting delivery, refunds, or reroutes must be **auditable** — show what rule fired, what evidence supports the outcome
- Customers must be informed when interacting with AI-driven delivery systems
- Governance trails for automated logistics decisions are required

---

## DDP vs DDU Decision Framework

This is now a commercial decision, not just a shipping detail:

| Model | Pros | Cons | Best For |
|---|---|---|---|
| **DDP** (Delivered Duty Paid) | No doorstep surprises; higher conversion; better AI agent compatibility | Higher upfront logistics complexity; need duty calculation infrastructure | Cross-border brands prioritizing customer experience |
| **DDU** (Delivered Duty Unpaid) | Simpler for merchant; lower displayed price at checkout | Doorstep shock; high refused-parcel rates; damages repeat purchase | Low-frequency exporters; items where duties are unpredictable |

**Policy language for DDP**: "All duties, taxes, and customs fees are included in the price shown at checkout. You will not be charged additional fees on delivery."

**Policy language for DDU**: "International orders may be subject to customs duties and import taxes. These charges are your responsibility and are collected by the carrier upon delivery. Estimated fees: [range or calculator link]."

---

## Cross-Border Shipping Essentials

### Tracking Normalization
Cross-border shipments pass through multiple carriers (origin carrier → customs broker → destination carrier → last-mile). Customers need **one coherent tracking story**, not fragmented statuses from each handoff.

Policy should state:
- How tracking is provided (single tracking page/number even across carriers)
- When tracking becomes available (typically 24–48 hours after shipment)
- What to do if tracking shows no movement for [X] days

### Route Volatility (2025–2026 Reality)
- 2,500+ trade restrictions imposed globally in the first 10 months of 2025 alone (World Bank)
- Policy should include: "Delivery times are estimates and may be affected by customs processing, weather, or other factors outside our control"
- Build per-market configurability: delivery windows, fees, and service mixes should be adjustable by region without operational chaos

### Prohibited & Restricted Items
- List categories that cannot be shipped internationally (batteries, aerosols, certain food items, etc.)
- Link to carrier-specific restriction lists
- Note that customs may reject items even if the carrier accepts them

---

## Out-of-Home (OOH) Delivery — Now Mainstream

OOH delivery via lockers and parcel shops is no longer a niche option:

- **35% of European shoppers** use lockers or parcel shops for delivery (DHL 2025)
- **79% prefer to return via locker or parcel shop**
- Missing OOH options at checkout increases cart abandonment

**Policy must include**:
- Which OOH networks are available (InPost, DHL Packstation, Amazon Locker, etc.)
- How to select OOH at checkout
- Pickup windows (typically 3–7 days before return to sender)
- Whether OOH is available for both delivery and returns

---

## Essential Policy Elements

| Element | What to Include |
|---------|----------------|
| **Regions served** | Countries/regions you ship to; any restrictions or exclusions |
| **Carriers & methods** | Standard, express, overnight; carrier names; real-time vs flat-rate; OOH options |
| **Costs** | Flat rate, weight-based, carrier-calculated, free-shipping threshold; DDP/DDU designation |
| **Processing time** | Time between order and handoff to carrier (e.g., "1–3 business days") |
| **Transit time** | Estimated delivery window per method and region; note that international estimates include customs |
| **Cutoff times** | Order-by time for same-day/next-day processing |
| **Tracking** | When and how tracking is provided; multi-carrier normalization approach |
| **Customs & duties** | DDP or DDU; estimated fees; who is responsible; landed-cost transparency |
| **Restrictions** | Items that cannot be shipped; countries excluded |
| **Lost / damaged / delayed** | Process for reporting issues; resolution timeline; carrier claim process |
| **Address accuracy** | Customer responsibility for correct address; redirection/rerouting fees |
| **Returns logistics** | How to return; who pays return shipping; OOH return options |
| **Force majeure** | Delivery delays outside your control (weather, customs, carrier issues) |

---

## Delivery Speed Benchmarks

| Method | Processing | Domestic Transit | International Transit |
|--------|-----------|-----------------|----------------------|
| Standard | 1–3 business days | 3–7 business days | 7–21 business days |
| Express | 1 business day (with cutoff) | 1–3 business days | 3–7 business days |
| Overnight | Same day (with cutoff) | Next business day | N/A |

---

## Post-Purchase as Commercial Inventory

Customers spend significant time on order-tracking pages and delivery-status messages. This real estate is underutilized:

- Tracking pages are now considered **branded commercial inventory**, not just operational notifications
- Cross-sell and upsell embedded in tracking flows show higher conversion rates than standalone campaigns
- IAB Europe forecasts retail media spend reaching **€31 billion by 2028**, with post-purchase touchpoints as a key channel

**Policy doesn't need to address this directly**, but the delivery experience described in the policy should align with the actual post-purchase UX.

---

## SaaS Tools for Delivery Management (2026 Baseline)

Modern delivery management platforms now include these capabilities as table stakes. When recommending tooling to e-commerce clients:

| Capability | Why It Matters |
|------------|----------------|
| AI carrier rate shopping | Automatically select best carrier/service per shipment; pilots show 10–20% cost reduction |
| Normalized multi-carrier tracking | Map disparate carrier statuses into one coherent customer story |
| Predictive delivery risk detection | Flag delays before shipment leaves warehouse |
| Auditable decision governance | Required under EU AI Act — show what rule fired and why |
| Returns management with proof of drop-off | Reduce fraud; track return status end-to-end |
| Per-market policy configurability | Adjust delivery options, fees, windows by region |

---

## Content Principles

- **Be precise about costs**: "Free shipping on orders over $50; $5.99 flat rate below $50" — no ambiguity
- **Be honest about timelines**: "Typically 5–7 business days" not "fast shipping"; under-promise and over-deliver
- **Landed-cost transparency**: Show total price including duties before checkout completion
- **AI-readable structure**: Use consistent, structured formats that both humans and AI agents can parse
- **Cutoff clarity**: "Orders placed before 2 PM ET ship same day" with timezone specified
- **Per-region specificity**: Don't use one blanket statement for all international — specify per market
- **"Last updated" date**: Shipping costs and carriers change; update and date the policy

---

## Placement

Surface shipping information at every decision point:

1. **Product pages** — Estimated delivery date or shipping-cost summary
2. **Cart** — Shipping calculator before checkout
3. **Checkout** — Full shipping options with costs and estimated dates; landed-cost total for international
4. **Order confirmation** — Selected method, estimated delivery date, tracking instructions
5. **Footer** — Link to full shipping policy
6. **FAQ** — Common shipping questions linked to policy

---

## Output Format

- **Shipping-scope determination**: Domestic, regional, or global
- **Carrier/method table**: Option name | cost | processing time | transit time | cutoff | regions
- **Customs & duties block**: DDP or DDU; estimated fees; responsibility statement
- **Tracking & issue-resolution section**: How tracking works; what to do about lost/delayed/damaged items
- **OOH options**: If applicable, which networks and how to select them
- **EU compliance flags**: 2026 customs duty disclosure; AI Act automation transparency
- **AI-readiness note**: Whether the policy is structured for machine parsing
- **Placement recommendations**: Where to surface shipping info throughout the purchase flow
- **Disclaimer**: Recommend legal review for cross-border compliance

---

## Related Skills

- **legal-page-generator**: Shipping is a legal page type; jurisdiction framework, platform requirements
- **refund-page-generator**: Often paired in footer and checkout; returns logistics overlap
- **faq-page-generator**: Shipping questions are the most common FAQ category
- **terms-page-generator**: Customs liability and force majeure often appear in Terms
