---
name: terms-page-generator
description: When the user wants to create, optimize, or structure Terms of Service page. Also use when the user mentions "terms of service," "terms and conditions," "terms of use," "user agreement," "ToS," "legal terms," "service agreement," or "terms page." For legal overview page, use legal-page-generator.
metadata:
  version: 1.1.0
---

# Pages: Terms of Service

Guides Terms of Service page content, structure, compliance, and AI-specific clauses.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

Identify:
1. **Product category**: Free anonymous, free with account, freemium, subscription SaaS, enterprise/B2B, API/developer, marketplace, e-commerce, content/media, mobile app, AI agent/MCP — see legal-page-generator §Product Categories
2. **Jurisdiction**: Governing law, dispute resolution, whether dual-jurisdiction fallback is needed — see legal-page-generator §Jurisdiction Decision Framework
3. **AI involvement**: Whether AI models generate output, and whether third-party model terms apply — see §AI Clauses
4. **User types**: B2B, B2C, or both
5. **Indexing**: Typically index (see legal-page-generator §Indexing Strategy)

---

## Required Sections (18-Section Framework)

### 1. Agreement

- "By accessing or using [domain], you agree to be bound by these Terms"
- "If you do not agree, please do not use the service"
- Reference to other incorporated documents (Privacy Policy, AUP, Community Guidelines)

### 2. The Service

- What the product does in one paragraph
- **Fair-use limits**: If applicable, state daily/monthly quotas with rationale ("to keep the service fair and available for all users")
- Whether the service is free or paid

### 3. Eligibility

- Minimum age: 13 (US/COPPA) or 16 (EEA/GDPR)
- Statement: "By using [Product], you confirm that you meet this age requirement"
- Additional restrictions if applicable (e.g., not available in certain countries)

### 4. No Accounts (If Applicable)

For products without user accounts:
- "No account or sign-up is required"
- User is solely responsible for: content submitted, output generated, compliance with these Terms each session
- User bears the risk of browser/local data loss

For products with accounts:
- Account security: user responsible for credentials, notify of unauthorized access
- Accurate information: provide truthful registration data

### 5. Acceptable Use

List specific prohibited content and behaviors:

**Prohibited Content**:
- Illegal content under applicable law
- Child sexual abuse material (CSAM) or content exploiting minors
- Content that infringes intellectual property, privacy, or publicity rights
- Content that promotes violence, harassment, or hate

**Prohibited Behaviors**:
- Scraping, crawling, or automating access beyond normal browser use
- Attempting to bypass quotas, rate limits, or security measures
- Reverse engineering, decompiling, or jailbreaking the service
- Submitting URLs or content the user does not have the legal right to access or reproduce
- Using the service for high-risk automated decisions affecting individuals

**Enforcement**: Right to investigate, block IPs/sessions, and take legal action.

### 6. Your Content

- User retains ownership of submitted content (URLs, prompts, uploads)
- User grants a **limited, non-exclusive, request-scoped license** to process content solely to provide the service
- Statement: "We do not store Your Content after the request completes" (if true)
- Statement: "We do not use Your Content to train AI models" (if true — significant trust signal)
- User warrants they have the right to submit the content and doing so doesn't violate third-party rights

### 7. Generated Output

- **Ownership**: User owns the output and may use it for any lawful purpose, including commercial use
- **AI caveat**: Because output is AI-generated, user is responsible for:
  - Verifying accuracy, artifacts, mis-rendered text
  - Ensuring output doesn't infringe third-party trademarks, copyrighted imagery, or likenesses
  - Complying with terms of any website whose URL was submitted
- **Copyright note**: AI-generated content may not qualify for copyright protection in all jurisdictions
- **Image disclaimer**: AI-generated images are not photographs of real individuals; resemblance is coincidental

### 8. AI Disclaimer (Standalone Section)

- "Output is produced by probabilistic AI models"
- "May contain artifacts, inaccuracies, hallucinated text, or unexpected visual results"
- "Verify all content before publishing"
- "[Product] is a creative tool, not a source of factual representation"
- Not liable for decisions made based on AI output

### 9. Third-Party Services

- List AI model providers used (Google Gemini, OpenAI, etc.)
- **Their terms also apply**: Users' data submitted for generation is subject to those providers' terms and policies
- Link to each provider's Terms of Service and Privacy Policy
- For API/enterprise products: note sub-processor commitments and DPA availability

### 10. Free Service / No SLA (If Applicable)

For free products:
- "Provided free of charge on a best-effort basis"
- No guarantee of: uninterrupted operation, feature availability, response time, output quality
- "We may rate-limit, suspend, or discontinue features at our discretion without prior notice"
- Not liable for unavailability or discontinuation

For paid products:
- Uptime commitment (e.g., 99.9% SLA)
- Service credits for downtime
- Scheduled maintenance windows

### 11. Intellectual Property

- Operator owns: name, logo, website design, source code, UI, templates, curated content
- User-owned items explicitly excluded: user-submitted content and user-generated output
- No license to copy, modify, or redistribute operator IP without permission

### 12. Termination

- Operator may block IPs/sessions that violate §5 (Acceptable Use)
- Termination does not affect provisions that by nature survive (disclaimers, liability, indemnity, governing law)
- For account-based products: user may terminate by deleting account; operator may terminate for ToS violations

### 13. Disclaimer of Warranties

Standard US-style all-caps paragraph:

"THE SERVICE IS PROVIDED ON AN 'AS IS' AND 'AS AVAILABLE' BASIS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT. [PRODUCT] DOES NOT WARRANT THAT THE SERVICE WILL BE UNINTERRUPTED, ERROR-FREE, OR SECURE, OR THAT AI-GENERATED OUTPUT WILL BE ACCURATE, APPROPRIATE, OR FREE OF INFRINGING CONTENT."

### 14. Limitation of Liability

- To maximum extent permitted by law, operator not liable for indirect, incidental, special, consequential, or punitive damages
- Total liability capped at a specific amount (e.g., USD $100 for free tools; amount paid in last 6–12 months for paid tools)
- **Jurisdictional carve-out** (mandatory): "Some jurisdictions do not allow the exclusion or limitation of certain warranties or liabilities. In those jurisdictions, the operator's liability is limited to the maximum extent permitted by law, and the above limitations may not apply to you."

### 15. Indemnity

- User indemnifies operator against claims, damages, liabilities, and expenses (including reasonable legal fees) arising from:
  - User's submitted content
  - User's use of generated output
  - User's violation of these Terms
  - User's violation of third-party rights or applicable law

### 16. Governing Law & Venue

Three patterns to choose from:

**Single Jurisdiction**:
"These Terms are governed by the laws of [State/Country], without regard to conflict-of-law principles. Disputes will be brought exclusively in [courts of County/City]."

**Dual Jurisdiction (Fallback)**:
"These Terms are governed by the laws of [Primary Jurisdiction]. Disputes will be brought exclusively in [Primary Courts]. Where a party is unable to bring a claim in [Primary Jurisdiction] (for example, due to jurisdictional limitations), the parties consent to [Alternate Courts] as the alternate forum."

**Arbitration**:
"Disputes will be resolved through binding arbitration administered by [JAMS/AAA/SIAC] under its [applicable rules]. Users may opt out of arbitration within 30 days of first using the service."

### 17. Changes

- "We may update these Terms from time to time"
- "Material changes will be posted with a new 'Last updated' date"
- **Critical clause**: "Your continued use of [Product] after changes are posted constitutes acceptance of the revised Terms"
- For significant changes: consider email notification, in-app banner, or re-acceptance flow

### 18. Contact

- Email address for Terms-related questions
- **DMCA/Copyright complaint channel** (for US-hosted sites): designated email or form for takedown requests
- For account-based products: support channel for account issues
- Response timeframe expectation

---

## AI Clauses — Minimum Requirements

For any product using AI models, these clauses are mandatory:

### In §6 (Your Content)
- Limited license: "solely to process Your Content during your request — to generate output and return the result"
- "We do not store Your Content after the request completes" (if true)
- "We do not use Your Content to train AI models" (if true)

### In §7 (Generated Output)
- User owns output; may use commercially
- User responsible for verifying output before publishing
- Copyright ambiguity note: AI-generated content may not be copyrightable

### In §8 (AI Disclaimer)
- Probabilistic; may contain artifacts
- Verify before use
- Not a source of factual truth

### In §9 (Third-Party Services)
- Name the AI model providers
- Their terms also apply to the user
- Link to provider terms

### 2025–2026 Regulatory References to Flag
- **EU AI Act** (full enforcement Aug 2026): GPAI providers must disclose training data; AI systems must inform users of AI interaction
- **Connecticut CTDPA** (Jul 2026): LLM training use must be disclosed
- **California SAM §4986.10**: AI-generated content must be labeled
- **India DPDP Act** (phased 2025–2027): under-18 parental consent; significant data fiduciary obligations

---

## Product-Category Adjustments

| Category | Add | Remove |
|---|---|---|
| **Free Anonymous** | §4 No Accounts (full), §10 Free/No SLA | §5 Account security sub-section, payment references |
| **Free with Account** | §4 Account security, §12 Account termination | Payment references |
| **Freemium / Subscription** | Payment terms, auto-renewal, cancellation, refund policy link | §10 Free/No SLA (replace with paid SLA) |
| **Enterprise / B2B** | DPA reference, sub-processor list, security certifications, custom retention | §2 Fair-use limits, §10 Free/No SLA |
| **API / Developer** | Rate limits, API key security, data processor role, uptime SLA | §4 No Accounts (replace with API key management) |
| **Marketplace** | Content moderation, takedown process, submitter licenses, third-party disclaimer | — |
| **E-commerce** | Refund policy link, shipping policy link, consumer rights | §7 Generated output (unless AI features exist) |

---

## Content Principles

- **Plain language**: Explain legal obligations in terms a user can understand
- **Be specific about AI**: Don't bury AI caveats in a generic "disclaimer" — give them standalone sections
- **Jurisdictional carve-out**: Always include the "some jurisdictions do not allow" safety valve in §14
- **"Continued use = acceptance"**: Always include in §17
- **DMCA contact**: Always include for US-hosted sites
- **Structure**: Numbered sections, scannable headings — users (and courts) should find clauses quickly
- **"Last updated" date**: Prominently at the top
- **Legal review**: Recommend lawyer review for jurisdiction-specific enforceability

---

## Placement

- **Footer**: Link on every page
- **Signup flow**: Require checkbox acceptance before account creation
- **Checkout**: Link before purchase confirmation
- **API onboarding**: Acceptance required before key issuance

---

## Output Format

- **Complete section outline**: All applicable sections from the 18-section framework
- **Key points per section**: What each clause must cover; sample language for critical clauses
- **Product-category adjustments**: Which sections to add or skip
- **AI clause block**: Full language for §6, §7, §8, §9 when AI is involved
- **Governing law recommendation**: Based on operator and user locations
- **Disclaimer**: Recommend legal review

---

## Related Skills

- **legal-page-generator**: Terms is a legal page type; product categories, jurisdiction framework, platform dependencies
- **privacy-page-generator**: Often linked together; AI disclosures in Privacy complement AI clauses in Terms
- **contact-page-generator**: Contact for Terms questions
- **indexing**: Index strategy for legal pages
