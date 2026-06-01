---
name: refund-page-generator
description: When the user wants to create or optimize a refund or return policy page. Also use when the user mentions "refund policy," "return policy," "money-back guarantee," "returns and refunds," "refund page," "return process," "refund terms," "satisfaction guarantee," "cancellation policy," or "withdrawal right." For legal overview, use legal-page-generator.
metadata:
  version: 1.1.0
---

# Pages: Refund / Return Policy

Guides refund and return policy page content for SaaS, digital products, e-commerce, and services. Covers jurisdiction-specific requirements including EU withdrawal rights.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

Identify:
1. **Product category**: See §Product Categories — refund logic is fundamentally different for SaaS vs digital downloads vs physical goods vs services
2. **Jurisdiction**: EU (14-day withdrawal right + mandatory withdrawal button), UK (DMCCA subscription rules), US (FTC clear-and-conspicuous), Australia (consumer guarantees), China (2026 platform rules)
3. **Refund model**: Full refund, partial/pro-rata, store credit only, no refund, or conditional
4. **Payment flow**: One-time, subscription/recurring, or tiered pricing

---

## Product Categories

Refund policies differ radically by product type. Identify the category first:

| Category | Default Refund Stance | Key Considerations |
|---|---|---|
| **SaaS / Subscription** | Pro-rata or conditional | EU withdrawal button required by Jun 2026; trial periods; auto-renewal cancellation; Sky Austria case may reclassify subscriptions as "digital services" with full-period withdrawal rights |
| **Digital Downloads** | Typically non-refundable | "Once downloaded, all sales final"; exceptions for technical failure or duplicate purchase; must obtain explicit consent to waive EU withdrawal right before download |
| **Physical Goods** | 30-day return window (standard) | Return shipping costs; restocking fees; original packaging; final-sale categories |
| **Courses / Coaching** | Conditional | Pre-recorded: non-refundable once accessed; Live: partial refund before start, none after; rescheduling preferred over refunds |
| **API / Usage-Based** | Prorated or non-refundable | Pay-as-you-go typically non-refundable; subscription components may be prorated |
| **Marketplace** | Per-vendor or uniform | Who processes refunds; vendor return rates (>8% review, >15% suspend); uniform policy builds trust |
| **Free Tools** | N/A | No payment = no refund policy needed; state "free, no purchase required" if asked |

---

## Jurisdiction Requirements

### EU — Consumer Rights Directive + 2026 Withdrawal Button

**14-Day Cooling-Off Period**:
- EU consumers have an unconditional 14-day right to withdraw from any distance contract (online purchase)
- Applies to goods, services, AND digital products/SaaS
- You must inform consumers of this right BEFORE purchase — failure extends the period by up to 12 months
- For goods: withdrawal period starts on delivery
- For services/digital: starts on contract conclusion

**Mandatory Withdrawal Button — Deadline June 19, 2026** (Directive EU 2023/2673):

This is the most urgent 2026 compliance item. Requirements:

- A clearly labeled digital withdrawal function (e.g., "Withdraw from contract" button) on your website/app
- **Two-step process**: (1) Withdrawal button → confirmation page → (2) "Confirm withdrawal" button
- Automated confirmation sent to consumer on a **durable medium** (email) with timestamp
- Button must be **permanently available** during the withdrawal period, prominently placed, not hidden behind logins or menus
- Applies to **any business targeting EU consumers**, regardless of where the business is registered
- Penalties: fines up to 4% of annual turnover in some member states; extended withdrawal periods until compliant

**Digital Content vs Digital Services — Sky Austria Case (CJEU, pending 2026)**:

This pending case may significantly change how SaaS refunds work:
- Advocate General opined that streaming subscriptions (and by extension, SaaS) are **"digital services"** — not "digital content"
- **Why it matters**: Digital content can waive withdrawal rights immediately upon access. Digital services only lose withdrawal rights once the service is **fully performed** — not when access begins
- **Practical impact**: If the CJEU follows this opinion, SaaS providers may not be able to extinguish withdrawal rights at first login; the right would persist for the full subscription term
- **Monitor this case** and be prepared to update refund terms

**Exceptions** (Article 16 CRD — withdrawal right does NOT apply to):
- Digital content where performance has begun AND consumer gave prior express consent AND acknowledged loss of withdrawal right (but note Sky Austria risk)
- Fully performed services with consent and acknowledgment
- Customized/personalized products
- Services for specific dates (events, hotel bookings)

**2-Year Conformity Guarantee**: Under Digital Content Directive (2019/770), consumers have a minimum 2-year guarantee for defective digital products and services.

### UK — DMCCA Subscription Rules (Spring 2027)

- Pre-contract disclosure of key subscription terms (trial price, renewal date, cancellation method)
- Two 14-day cooling-off periods (one at sign-up, one after auto-renewal of long-term contracts)
- Mandatory renewal reminders with prescribed information
- Cancellation must be "straightforward" — no unnecessary steps

### US — FTC Requirements

- No federal right of withdrawal for online purchases
- FTC requires refund policies to be "clear and conspicuous"
- Some states have specific rules: California requires posting the refund policy if not offering full refund within 7 days
- State AGs increasingly enforce against "dark patterns" that make cancellation difficult

### Australia — Consumer Guarantees (ACL)

- Consumer guarantees **cannot be excluded** by store policy
- Defective items entitled to refund, repair, or replacement regardless of what the policy says
- No fixed return window — "reasonable time" applies

### China — 2026 Platform Rules (Effective February 1, 2026)

- Platforms **cannot force merchants** to accept "refund without return" (仅退款)
- Rules must be transparent
- Historical versions must be archived for 3+ years

---

## SaaS Refund Patterns

### Trial-to-Paid Conversion
- Free trials are for evaluation; clearly state when the trial ends and when billing begins
- Offer a limited post-conversion refund window (7–30 days) to catch accidental conversions
- Send pre-billing reminders 3–7 days before trial ends

### Pro-Rata Refunds (Mid-Cycle Cancellation)
- Standard for annual subscriptions: refund unused months minus processing fee
- Monthly subscriptions: typically no pro-rata; access continues until period end
- Clearly state whether prepaid fees are forfeited or prorated on termination

### Cancel-Before-Renewal
- State the deadline for cancelling before auto-renewal (e.g., "at least 24 hours before renewal date")
- Send renewal reminders 7–30 days in advance
- Include a "Cancel subscription" link in account settings and renewal emails

### Anti-Abuse
- Consider: maximum refunds per customer per year; manual review for high-value refunds; fraud detection on refund patterns

---

## Digital Products Refund Patterns

**Default**: "Due to the digital nature of this product, all sales are final and non-refundable."

**Recommended Exceptions**:
- **Accidental duplicate purchase**: Refund as goodwill
- **Technical failure preventing access/download**: Refund or re-deliver
- **Product not as described**: Refund if materially different from listing

**EU Compliance for Digital Products**:
- To waive the 14-day withdrawal right for digital content: (1) obtain consumer's prior express consent to immediate performance, AND (2) consumer must acknowledge they will lose the withdrawal right once download/access begins
- Make this a checkbox at checkout — not buried in terms
- After June 2026, the withdrawal button must be available even if the right has been waived (it may still apply if the waiver was invalid)

**Content License Clause**: Make clear the buyer owns a license to use, not the content itself. "You are purchasing a non-exclusive, non-transferable license to use [product], not ownership of the underlying content."

---

## Physical Goods Return Patterns

### Return Window
- **30 days from delivery** is the dominant standard (58.5% of DTC brands)
- Distribution: <14 days (4.7%), 14–29 days (21.4%), exactly 30 (58.5%), 31–60 (9.2%), 60+ (6.1%)
- Shorter windows for food, supplements, personal care; longer for furniture, sleep products

### Return Costs
- **Defective/wrong item**: Vendor pays return shipping
- **Change of mind**: Customer pays return shipping
- **Restocking fees**: $5–15 flat or 5–15% — increasingly common, but **must be prominently displayed** (not buried in fine print)

### Conditions
- Original packaging required: 50.1% of brands require it — clearly state upfront
- Final-sale categories: intimates, cosmetics, food (hygiene); custom/personalized orders (functional). Keep the list logical — don't stack with discount tiers.
- Store-credit-only refunds: only 3.3% of brands; not recommended as the ONLY option

### Refund Method & Timeline
- Original payment method preferred
- Specify timeline: "within 10–14 business days of receiving the returned item"
- EU: must refund within 14 days of receiving the return

---

## Essential Policy Elements

Every refund/return policy should cover:

| Element | What to Include |
|---------|----------------|
| **Eligibility** | What can be returned/refunded; time limits; condition requirements |
| **Non-refundable items** | Final-sale categories; digital products with access/waiver |
| **Refund amount** | Full, pro-rata, minus fees, store credit only |
| **Refund method** | Original payment, store credit, check |
| **Refund timeline** | When the customer will receive the refund |
| **Process** | Step-by-step instructions; withdrawal button location; contact |
| **Exceptions** | Defective items, duplicate purchases, technical failures |
| **Trial terms** (SaaS) | Trial duration, conversion date, billing after trial |
| **Cancellation** (SaaS) | How to cancel; what happens to data; pro-rata refund details |
| **Jurisdiction rights** | EU 14-day withdrawal; Australia consumer guarantees; other statutory rights |

---

## Placement

Place the refund policy where customers need it **before** making a purchase decision:

1. **Checkout page** — Brief summary with link to full policy; visible before purchase completion (FTC requirement)
2. **Website footer** — Persistent link on every page
3. **Product pages** — Returns/refund summary tab or section
4. **Order confirmation email** — Include return/exchange instructions
5. **Account dashboard** — "Request Refund" or "Cancel Subscription" button accessible on eligible orders
6. **Terms of Service** — Cross-link for legal completeness

For SaaS: the cancellation flow should be accessible from account settings, billing page, and support contact — **never** require calling support as the only cancellation method.

---

## Content Principles

- **Be specific about timing**: "Within 30 days of delivery" > "within a reasonable time"
- **Distinguish by product type**: Digital vs physical vs subscription — don't use one blanket policy
- **Prominent fee disclosure**: Restocking fees and return shipping costs must be visible, not buried
- **EU withdrawal button**: Plan for the June 2026 deadline now; describe the mechanism in the policy
- **Plain language**: "If you change your mind, you can return it within 30 days" > legalese
- **Anti-dark-pattern**: Cancellation must be as easy as sign-up; don't hide the withdrawal button
- **Update regularly**: Review when pricing, product types, or regulations change

---

## Industry Benchmarks (2025–2026)

| Metric | Benchmark |
|--------|-----------|
| Median physical-goods return window | 30 days from delivery |
| Brands offering free returns (stated on policy page) | 18.4% |
| Brands with restocking fees | 19.2% |
| Brands requiring original packaging | 50.1% |
| Brands with final-sale clauses | 39.9% |
| Brands using store-credit-only refunds | 3.3% |
| SaaS pro-rata refund standard | Unused months minus processing fee or no refund after window |

---

## Output Format

- **Product-category determination**: Which refund model applies
- **Complete policy outline**: All applicable sections with key clauses
- **EU compliance block**: Withdrawal right explanation + withdrawal button mechanism (if targeting EU)
- **SaaS-specific block** (if applicable): Trial terms, pro-rata details, cancellation flow
- **Refund process description**: Step-by-step in plain language
- **Jurisdiction flags**: Which statutory rights apply and how they interact with the policy
- **Placement recommendations**: Where to surface the policy
- **Disclaimer**: Recommend legal review, especially for EU withdrawal button compliance

---

## Related Skills

- **legal-page-generator**: Refund is a legal page type; product categories, jurisdiction framework
- **terms-page-generator**: Refund terms often embedded in Terms; cancellation and termination clauses
- **shipping-page-generator**: Often paired in footer and checkout for e-commerce
- **faq-page-generator**: FAQ may link to refund policy for common questions
