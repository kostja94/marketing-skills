---
name: legal-page-generator
description: When the user wants to create, optimize, or structure legal pages (Privacy, Terms, etc.). Also use when the user mentions "privacy policy," "terms of service," "legal pages," "cookie policy," "terms and conditions," "legal footer," "legal section," "compliance pages," or "legal requirements." For Privacy Policy content, use privacy-page-generator. For Terms of Service, use terms-page-generator. For Cookie Policy, use cookie-policy-page-generator.
metadata:
  version: 1.2.0
---

# Pages: Legal

Guides legal page content, structure, compliance, and platform readiness for AI/SaaS products.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

Identify:
1. **Product category**: Free anonymous, free with account, freemium, subscription SaaS, enterprise/B2B, API/developer, marketplace/platform, e-commerce, content/media, mobile app, AI agent/MCP — see §Product Categories
2. **Page type**: Privacy Policy, Terms of Service, Cookie Policy, etc.
3. **Jurisdiction needs**: Which countries' laws apply — see §Jurisdiction Decision Framework
4. **Indexing strategy**: Index or noindex — see §Indexing Strategy
5. **Platform dependencies**: Which external platforms require these pages — see §Platform Dependencies

---

## Product Categories

The legal page structure depends heavily on the product category. Identify which one applies before drafting:

| Category | Key Legal Characteristics | Sections to INCLUDE | Sections to SKIP |
|---|---|---|---|
| **Free Anonymous** | No accounts, no payment, no persistent storage, GA4 analytics | What we DON'T collect, no-training statement, fair-use limits, free/no-SLA | Payment, account responsibilities, refund, data portability |
| **Free with Account** | Login required, user data stored, may have social features | Account security, data access/portability, user responsibilities | Payment, billing, refund |
| **Freemium** | Free + paid tiers, payment data, auto-renewal | Payment terms, billing, tier differences, data handling per tier | — |
| **Subscription SaaS** | Recurring billing, auto-renewal, cancellation | Payment, billing cycles, auto-renewal disclosure, cancellation process | — |
| **Enterprise / B2B** | DPA, SOC 2, zero-training guarantees, SCCs | DPA reference, sub-processor list, security certifications, data processing roles, custom retention | Fair-use limits (usually N/A) |
| **API / Developer** | Data processor role, rate limits, API keys | Rate limits, API key security, data processor terms, uptime/SLA | End-user account sections |
| **Marketplace / Platform** | Multi-party, UGC responsibility, submission licensing | Content moderation, takedown process, submitter licenses, third-party content disclaimer | — |
| **E-commerce** | Physical/digital goods, refunds, shipping | Refund policy, shipping policy, consumer rights, payment security | — |
| **Content / Media** | Copyright, DMCA, content licensing | DMCA contact, content ownership, republication terms | Payment (unless paid content) |
| **Mobile App** | App store review, privacy nutrition labels, permissions | App store compliance notes, permission justifications, data collection summary | — |
| **AI Agent / MCP** | Automated decisions, tool invocation, sub-processor chains | AI decision transparency, sub-processor chain disclosure, autonomous action limits | — |

---

## Platform Dependencies

Many external platforms **require** posted Privacy Policy and/or Terms of Service before the product can be listed, advertised, or operate in compliance. These should be flagged to the user during generation.

### Submission & Directory Platforms

Most AI tool directories, MCP/Skills marketplaces, and software directories require both Privacy Policy and Terms of Service to be publicly accessible before a listing can be approved. Common requirements across these platforms:

- Publicly linked Privacy Policy and Terms of Service
- No illegal, deceptive, or IP-infringing content
- Accurate, non-misleading product descriptions
- Submitter warrants ownership or authority to list
- Platform reserves right to reject or remove listings at discretion
- Often require a DMCA/copyright complaint contact

### Advertising & Distribution Platforms

| Platform | Requires | Consequence if Missing |
|----------|----------|----------------------|
| Google Ads | Privacy Policy link during account setup | Cannot launch campaigns |
| Meta Ads (Facebook/Instagram) | Privacy Policy for ad account verification | Ad account suspended |
| TikTok Ads | Privacy Policy for account review | Cannot launch |
| Apple App Store | Privacy Policy URL + privacy nutrition labels | App rejected |
| Google Play Console | Privacy Policy URL for all apps | App rejected |
| LinkedIn Ads | Privacy Policy for business page verification | Restricted access |

### Infrastructure & Compliance

| Requirement | What's Needed |
|-------------|---------------|
| Google Analytics ToS §7 | Posted privacy policy that discloses GA usage |
| Stripe / payment processors | Privacy Policy URL during onboarding |
| OAuth providers (Google, GitHub) | Privacy Policy URL for app verification |
| SOC 2 / ISO 27001 | Both pages are standard vendor-assessment prerequisites |
| Enterprise procurement | Both pages are due-diligence checklist items |
| Accelerators (YC, Techstars, etc.) | Legal pages are standard application requirements |

---

## Jurisdiction Decision Framework

Use a three-layer approach to determine which laws apply:

**Layer 1 — Operator location** → determines primary governing law and venue in Terms.

**Layer 2 — User locations** → determines which privacy regulations apply and whether regional supplements are needed. If the product is accessible globally, assume GDPR (EU), CCPA (California), and the operator's home jurisdiction at minimum.

**Layer 3 — Data storage location** → determines data localization obligations. China (PIPL) and India (DPDP) may require local storage.

### Major Privacy Regulations (2025–2026)

| Jurisdiction | Law | Consent Model | Max Penalty | Notable |
|---|---|---|---|---|
| EU/EEA | GDPR | Opt-in | €20M / 4% global revenue | 72h breach notification; DPO required for certain entities |
| UK | UK GDPR + DPA 2018 | Opt-in | £17.5M / 4% | Post-Brexit independent; UK Representative required |
| California | CCPA/CPRA | Opt-out | $7,988/violation (no cap) | 19 US states now enforce; ADMT rules effective Jan 2026 |
| China | PIPL | Opt-in + separate consent for sensitive data | ¥50M / 5% revenue | **Data localization mandatory**; cross-border transfer requires security assessment |
| Brazil | LGPD | Opt-in | R$50M (~$10M USD) | DPO required for larger orgs |
| India | DPDP Act 2023 | Consent-centric | ₹250Cr (~$30M USD) | **Under-18 requires parental consent**; phased enforcement 2025–2027 |
| Canada | PIPEDA + Quebec Law 25 | Opt-in | CAD $10M+ | Quebec has independent requirements |
| South Korea | PIPA | Opt-in | 3% of revenue | Criminal penalties possible; among the strictest globally |
| Japan | APPI | Opt-in for transfers | Criminal penalties | "Pseudonymized" data concept |
| Australia | Privacy Act 1988 + 2025 amendments | Opt-in | AUD $50M+ | New "fair and reasonable" test; children's privacy code |

### Regional Supplements Pattern

Follow the model used by leading AI platforms: one main policy covering universal practices, plus **regional supplement sections** for jurisdictions with unique requirements. At minimum, provide:

- **EEA/UK Supplement**: GDPR legal bases (Art. 6), data subject rights (Art. 15–22), SCCs for transfers, DPO/representative contacts, complaint to supervisory authority
- **California Supplement**: 11-category data collection table, right to know/delete/correct, "Do Not Sell or Share" statement, opt-out mechanisms

Other regional supplements (China, Brazil, India, etc.) should be added when the product has significant users in those jurisdictions.

### Governing Law Patterns for Terms

| Pattern | Use Case | Venue Clause |
|---|---|---|
| **Single jurisdiction** | Operator and users in same country | Governing law of [State], venue in [County] |
| **Dual jurisdiction (fallback)** | Operator has ties to two countries | Primary: [Jurisdiction A]; Alternate: [Jurisdiction B] only where A is unavailable |
| **EU-first** | Primarily EU users | Ireland or Estonia (English-language EU courts) |
| **Arbitration** | Crypto/Web3 or international | Binding arbitration (JAMS, SIAC, HKIAC); opt-out window for users |

---

## Best Practices

### Content Principles

- **Clear language**: Avoid legalese where possible; explain what data is collected and why in plain terms
- **Structure**: Headings, sections, table of contents; use tables for cookies and processors
- **Updates**: "Last updated" date prominently at the top; version number if needed
- **Legal review**: Recommend that a qualified lawyer review for jurisdiction-specific compliance

### AI-Specific Content Requirements

These are **mandatory disclosures** for any product using AI models (generation, processing, or analysis):

**In Privacy Policy:**
1. Name the specific AI models used (e.g., Google Gemini, OpenAI GPT-4)
2. State whether submitted data is used for model training — if NOT, state this prominently as a trust signal
3. Disclose that generated output is probabilistic and may contain inaccuracies
4. Disclose that images are AI-generated, not photographs of real people/places

**In Terms of Service:**
1. Ownership of generated output (typically: user owns it, but AI-generated content may not qualify for copyright)
2. AI disclaimer: artifacts, mis-rendered text, hallucinated content; verify before publishing
3. User responsibility for verifying output before use
4. Third-party model providers' terms also apply to the user
5. Copyright ambiguity: generated content may inadvertently reproduce training data elements

### Trust-Building Patterns (Recommended)

- **"What we DON'T collect" section**: For no-login tools, list what's NOT collected (accounts, passwords, payment, contacts) — this builds immediate trust
- **"No training on your data"**: If using API-based AI (not consumer chat), state that data is not used for training — users assume the worst otherwise
- **Retention by category**: Be specific about what's deleted when, rather than vague "we keep data as needed"
- **Cookie opt-out instructions**: Don't just list cookies — tell users how to opt out of each one

### Common Pitfalls

| Pitfall | Why It Matters | Fix |
|---|---|---|
| **Over-promising data deletion** | Saying "we delete everything immediately" while keeping server logs for 30 days creates a false statement | Specify retention per category: submitted data (immediate), analytics (14 months), logs (30 days) |
| **Missing GA4 cookie disclosure** | Google Analytics sets `_ga` and `_ga_*` cookies — must be in the cookie table | Always include GA4 cookies when using Google Analytics |
| **Skipping "no training" statement** | Users assume AI tools train on their data by default; silence = assumed training | Explicitly state "not used for AI model training" if true |
| **Jurisdiction mismatch** | Operator in one country but Terms only list another — users may challenge forum convenience | Use dual-jurisdiction fallback pattern when operator has cross-border ties |
| **No DMCA/copyright complaint channel** | US-hosted sites need a takedown contact; even free tools get requests | Include copyright complaint email in Terms §Contact |
| **Liability cap without jurisdictional carve-out** | EU, AU, NZ don't allow blanket disclaimers or very low caps | Add: "Some jurisdictions do not allow these limitations, so they may not apply to you" |
| **Confusing cookie notice with cookie consent** | Notice = "we use cookies, here they are" (sufficient for analytics only). Consent = "click accept/reject" (required for ads/tracking) | Classify cookies by type and recommend the right mechanism |
| **Updating Terms without "continued use = acceptance"** | Without this clause, existing users can argue they never agreed to new terms | Always include: "Your continued use after changes are posted constitutes acceptance" |

---

## Indexing Strategy

Legal page indexing is **not one-size-fits-all**. The decision depends on the product's goals:

| Scenario | Strategy | Reason |
|---|---|---|
| **Submission/directory listing required** | **Index** | Many AI tool directories and submission platforms crawl the site to verify legal pages exist; noindex blocks this verification |
| **General SaaS / content site** | **Noindex** | Legal pages are low-value for organic search; noindex keeps them out of search results while remaining accessible |
| **Multiple language versions** | **Canonical** | Point all language variants to the primary (usually English) version |
| **Regional variants** | **Index + canonical** | If legally required to have jurisdiction-specific versions, index each and self-canonical |

**Default recommendation**: Index both pages unless the product has a specific reason not to. The SEO cost of indexing two utility pages is negligible, and the platform-verification benefit of indexable legal pages is significant.

---

## Placement

- **Footer**: Links to all legal pages on every route
- **Consent flows**: Cookie banner links to Privacy and Cookie Policy
- **Sign-up / checkout**: Link to Terms before commitment
- **Contact forms**: Link to Privacy near data submission points

---

## Structure

Quick-reference section frameworks by page type:

### Privacy Policy (14 sections for full coverage)

1. Who we are + contact
2. What the product does (one sentence)
3. Information we collect (with "What we DON'T collect" sub-section)
4. How we use information (with AI model training disclosure)
5. Cookies (table format: name | purpose | duration | how to opt out)
6. Third-party processors (each with privacy policy URL)
7. Data retention (per category)
8. Your rights (GDPR + CCPA + regional supplements)
9. International transfers
10. Children (COPPA/GDPR-K age thresholds)
11. Security
12. Changes
13. Contact (with response timeframe)
14. Regional supplements (EEA/UK, California, others as needed)

### Terms of Service (18 sections for full coverage)

1. Agreement (using = accepting)
2. The service (what + fair-use limits if applicable)
3. Eligibility (age requirement)
4. No accounts (if applicable — anonymous use + user responsibility)
5. Acceptable use (prohibited content + prohibited behaviors)
6. Your content (ownership retained, limited license to process)
7. Generated output (ownership, commercial use, AI caveats)
8. AI disclaimer (probabilistic, verify before publishing)
9. Third-party services (model providers, their terms apply)
10. Free service / No SLA (if applicable — best-effort, can change)
11. Intellectual property (what the operator owns)
12. Termination
13. Disclaimer of warranties (AS-IS, all-caps)
14. Limitation of liability ($ cap + jurisdictional carve-out)
15. Indemnity
16. Governing law & venue (+ alternate forum if applicable)
17. Changes (continued use = acceptance)
18. Contact (+ DMCA/copyright complaint channel if US-hosted)

### Cookie Policy

- What cookies are (brief explanation)
- Cookie table: name | type | purpose | duration | how to opt out
- Third-party cookies (GA4, etc.)
- How to manage/disable cookies in browser settings
- Notice vs consent: classify whether the site needs a notice or a consent banner

---

## Output Format

For each legal page type, provide:
- **Sections**: Complete outline with all applicable sections
- **Key points**: What each section must cover, with specific language for critical clauses
- **Product-category adjustments**: Which sections to add or remove based on the product category
- **Jurisdiction flags**: Which sections need regional variants
- **Platform readiness**: Confirm the pages meet submission/advertising platform requirements
- **Disclaimer**: Recommend legal review before publishing

---

## Related Skills

- **privacy-page-generator**: Privacy Policy page
- **terms-page-generator**: Terms of Service page
- **cookie-policy-page-generator**: Cookie Policy page
- **indexing**: Index/noindex strategy for legal pages
- **title-tag, meta-description, page-metadata**: Legal page metadata
- **homepage-generator**: Footer links to legal
