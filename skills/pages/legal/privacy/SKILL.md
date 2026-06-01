---
name: privacy-page-generator
description: When the user wants to create, optimize, or structure Privacy Policy page. Also use when the user mentions "privacy policy," "privacy page," "data protection," "GDPR compliance," "privacy notice," "data privacy," "CCPA," "cookie policy," or "personal data." For legal overview page, use legal-page-generator.
metadata:
  version: 1.1.0
---

# Pages: Privacy Policy

Guides Privacy Policy page content, structure, compliance, and AI-specific disclosures.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

Identify:
1. **Product category**: Free anonymous, free with account, freemium, subscription SaaS, enterprise/B2B, API/developer, marketplace, e-commerce, content/media, mobile app, AI agent/MCP — see legal-page-generator §Product Categories
2. **Data actually collected**: URLs, prompts, uploads, analytics, cookies, account data, payment data — be exhaustive
3. **AI involvement**: Whether AI models process user data and whether data is used for training (see §AI Disclosures)
4. **Jurisdiction needs**: Which privacy regulations apply — see legal-page-generator §Jurisdiction Decision Framework
5. **Indexing**: Typically index (see legal-page-generator §Indexing Strategy)

---

## Required Sections (14-Section Framework)

### 1. Who We Are

- Operator name (or "the operator of [Product]" for anonymous operations)
- Tool purpose in one plain-language sentence
- Contact email

### 2. What [Product] Does

- One paragraph explaining the core function
- Mention that no account or payment is required (if applicable)
- Set expectations: this is a [free/paid] [tool type] that does [X]

### 3. Information We Collect

Structure with clear sub-sections:

**What We Do NOT Collect** (trust signal — include for all products):
- No accounts, no passwords, no user profiles
- No payment information (if free)
- No contact lists or address books
- No precise location data
- Adapt this list to what's actually true for the product

**Data You Submit** (URLs, prompts, uploads, form inputs):
- What happens to it: processed for [purpose], sent to [AI providers if applicable]
- Whether it's stored: "processed in-memory and discarded after the request" or retention period
- Whether it's used for training: "not used to train AI models" (if true — state explicitly)

**Generated Content** (AI output, images, text):
- Returned to user's browser/account
- Whether retained on servers
- Whether used for training

**Analytics Data**:
- Which analytics tool (GA4, Plausible, etc.)
- What's collected (page views, device/browser, referrer, country-level location, session duration)
- Whether it identifies individuals

**Account Data** (if applicable):
- Email, username, profile information
- How it's used and stored

**Payment Data** (if applicable):
- Note that payment is processed by [processor], not stored directly

### 4. How We Use Information

- Purposes: service provision, improvement, security, analytics, legal compliance
- **AI Model Training Disclosure**: State explicitly whether user data is used to train, improve, or fine-tune AI models. If using API-based AI (OpenAI API, Google Cloud), note that these providers do not train on API data. If using consumer AI tools, disclose that training may occur.
- Marketing communications (with consent where required)

### 5. Cookies

Table format with opt-out instructions:

| Cookie | Purpose | Duration | How to Opt Out |
|--------|---------|----------|----------------|
| `_ga`, `_ga_*` | Google Analytics — aggregate usage measurement | Up to 2 years | [GA opt-out browser add-on](https://tools.google.com/dlpage/gaoptout) or block third-party cookies |
| `[session_cookie]` | Session management / fair-use enforcement | 24 hours / session | Clear browser data |

Also state:
- Whether advertising cookies are used
- Whether cross-site tracking occurs
- Whether the site responds to Do Not Track signals

### 6. Third-Party Processors

Table format with privacy policy URLs:

| Provider | Purpose | Privacy Policy |
|----------|---------|----------------|
| [Cloud provider] | Hosting / backend | [URL] |
| [CDN provider] | Content delivery / routing | [URL] |
| [AI model provider 1] | AI generation / processing | [URL] |
| [AI model provider 2] | AI generation / processing | [URL] |
| [Analytics provider] | Usage analytics | [URL] |

### 7. Data Retention

Specify per category — avoid vague "as long as needed" language:

- **Submitted data** (URLs, prompts, uploads): processed in-memory, discarded after response — not stored
- **Generated content**: delivered to browser, not retained on servers
- **Analytics aggregates**: retained for [X] months (GA4 default: 14 months)
- **Server access logs**: retained for 30 days for security/debugging
- **Account data** (if applicable): retained until account deletion; then deleted within [X] days

### 8. Your Rights

Structure by jurisdiction:

**GDPR (EEA/UK)**:
- Rights: access, rectification, erasure, restriction, portability, objection
- Legal basis for processing (Art. 6)
- Right to lodge complaint with supervisory authority
- Response timeframe: 30 days

**CCPA (California)**:
- Rights: know, delete, correct, opt-out of sale/sharing
- Statement: "[Product] does not sell personal information"
- How to exercise rights

**How to Exercise**:
- Email contact
- Identity verification if needed (note: for anonymous tools, minimal data exists)

### 9. International Transfers

- Where data is processed (country/region)
- Safeguards: Standard Contractual Clauses, adequacy decisions, or other mechanisms
- Note that data may transit through other regions as part of standard internet routing

### 10. Children

- Age threshold: under 13 (US/COPPA) or under 16 (EEA/GDPR)
- Statement: "not directed to children" / "do not knowingly collect"
- What to do if a child has submitted data: contact for deletion

### 11. Security

- TLS/HTTPS in transit
- Encryption at rest (provider-managed or self-managed)
- **No-credentials advantage** (if no accounts): "no passwords or credentials to leak"
- No payment data stored (if applicable)
- Breach notification commitment

### 12. Changes

- Material changes posted with new "Last updated" date
- Encouragement to review periodically
- If significant, additional notification (email, banner)

### 13. Contact

- Email address
- Response timeframe (e.g., "within 30 days")
- DPO or representative contact (if required by jurisdiction)

### 14. Regional Supplements

Follow the model of leading AI platforms: append jurisdiction-specific modules. At minimum:

**EEA/UK Supplement**:
- Legal bases for processing (Art. 6: consent, contract, legitimate interest)
- Full data subject rights (Art. 15–22)
- DPO or Art. 27 Representative contact
- Right to complain to supervisory authority
- Standard Contractual Clauses for international transfers

**California Supplement**:
- 11-category data collection and disclosure table
- Right to know, delete, correct
- "Do Not Sell or Share My Personal Information" statement
- Authorized agent provisions

Other supplements (China PIPL, Brazil LGPD, India DPDP) when the product has significant users in those jurisdictions.

---

## AI-Specific Disclosures

These are **mandatory** for any product that uses AI models:

### Must Disclose
1. **Which AI models process user data**: Name them specifically (Google Gemini, OpenAI GPT-4, etc.)
2. **Training data use**: Explicitly state whether submitted data is used for model training. If using API-based services that don't train on API data, state "not used for AI model training" — this is a significant trust signal.
3. **Probabilistic nature**: Generated output may contain inaccuracies, artifacts, or mis-rendered content.
4. **Image authenticity**: AI-generated images are not photographs of real individuals or places.

### 2025–2026 Regulatory Developments to Flag

- **EU AI Act**: Training data disclosure template required for GPAI providers (Aug 2025); full enforcement Aug 2026
- **Connecticut CTDPA**: LLM training data use must be disclosed in privacy notices (effective Jul 2026)
- **China GB/T 45654-2025**: Users must have ≤4-click opt-out from training data collection (effective Nov 2025)
- **California SAM §4986.10**: AI-generated content must carry disclosure labels

---

## Content Principles

- **Plain language**: Explain data practices in terms a non-lawyer can understand
- **Be specific**: "Discarded after the request completes" > "we process your data"
- **Trust signals**: "What we DON'T collect" section; "not used for training"; cookie opt-out instructions
- **Structure**: Numbered sections, tables for cookies and processors, scannable headings
- **"Last updated" date**: Prominently at the top of the page
- **Legal review**: Recommend lawyer review for jurisdiction-specific compliance

## Placement

- **Footer**: Link on every page
- **Forms**: Link near signup, contact, checkout — anywhere data is submitted
- **Cookie banner**: Link to Privacy and Cookie Policy

---

## Output Format

- **Complete section outline**: All applicable sections from the 14-section framework
- **Key points per section**: What each section must cover; sample language for critical clauses
- **Product-category adjustments**: Which sections to add or remove based on product category
- **AI disclosure block**: Specific language for AI model and training data disclosure
- **Cookie table**: Structured for the product's actual cookies
- **Processor table**: All third-party processors with privacy policy URLs
- **Regional supplement flags**: Which jurisdictions need supplements
- **Disclaimer**: Recommend legal review

---

## Related Skills

- **legal-page-generator**: Privacy is a legal page type; product categories, jurisdiction framework, platform dependencies
- **terms-page-generator**: Often linked together; AI disclaimer and output ownership live in Terms
- **cookie-policy-page-generator**: Detailed cookie table and consent mechanism
- **contact-page-generator**: Privacy link near forms
- **indexing**: Index strategy for legal pages
