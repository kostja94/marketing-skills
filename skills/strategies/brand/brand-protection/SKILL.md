---
name: brand-protection
description: When the user faces brand impersonation, fake websites, phishing sites, or trademark infringement. Also use when the user mentions "fake site," "impersonation," "phishing site," "trademark infringement," "domain squatting," or "brand abuse." For monitoring, use brand-monitoring.
metadata:
  version: 1.0.1
---

# Strategy: Brand Protection

Guides discovery, reporting, and prevention of brand impersonation—fake websites, phishing sites, trademark infringement, and domain squatting. See **domain-selection** for defensive domain registration; **trust-badges** for official site verification signals; **about-page** for identity declaration.

**When invoking**: On **first use**, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for project context first:** If `.claude/project-context.md` or `.cursor/project-context.md` exists, read it for brand name, official domain, and key assets.

Identify:
1. **Impersonation type**: Fake website, phishing, trademark misuse, domain squatting
2. **Evidence available**: Screenshots, URLs, WHOIS, hosting info
3. **Legal assets**: Registered trademark, copyright ownership
4. **Impact**: Traffic interception (fake site ranks for brand queries)? Payment fraud (users pay on fake site, then contact official support)?

## Evidence Collection Checklist

| Item | Action |
|------|--------|
| **Full URLs** | Document all key pages of the fake site |
| **Screenshots** | Homepage, product pages, logo, layout; include date/time |
| **Comparison** | Side-by-side: official vs fake (layout, logo, copy similarity) |
| **WHOIS** | Use [ICANN Lookup](https://lookup.icann.org/) for registrar, creation date, registrant |
| **Hosting** | IP lookup to identify hosting provider |

## Reporting Channels (Priority Order)

| Channel | Entry | Use Case |
|---------|-------|----------|
| **Domain registrar** | Abuse / Report Misuse on registrar site | Brand impersonation, trademark, fraud |
| **Hosting provider** | Same; submit abuse form | Hosting infringing content |
| **Google Safe Browsing** | [Report Phishing](https://safebrowsing.google.com/safebrowsing/report_phish/) | Phishing / impersonation risk |
| **Google Trademark** | [Trademark Complaint](https://services.google.com/inquiry/aw_tmcomplaint) or trademark@google.com | Trademark infringement in search; requires registered trademark |
| **Bing Content Removal** | [Content Moderation Platform](https://www.bing.com/webmaster/contentremovalform/showanonymouspage) | Copyright/trademark; content removal from Bing |
| **Payment processors** | PayPal Resolution Center, Stripe support | If fake site accepts payments; report fraud |
| **Social platforms** | X, Facebook, Instagram abuse forms | If fake site is promoted or linked there |
| **Google Ads / Microsoft Ads** | Platform trademark complaint forms | If impersonator runs brand ads |
| **DMCA** | To hosting provider | Copyright infringement; images, copy, design copied |
| **ICANN** | [DNS Abuse complaint](https://www.icann.org/en/system/files/files/submitting-dns-abuse-complaints-icann-guide-17nov25-en.pdf) | If registrar does not respond within reasonable time |

**Report content**: Include full URL, clear description of fraudulent activity, and all evidence (screenshots, logs).

## Reporting Best Practices

**Registrar vs hosting**: Use [ICANN Lookup](https://lookup.icann.org/) for registrar. For hosting, use IP lookup (HostingCheckerOnline, HostingDetector, ipinfo.io) to find origin server—registrar may be Cloudflare while origin host is elsewhere; report to both.

**Cloudflare as registrar**: Use [abuse.cloudflare.com](https://abuse.cloudflare.com/) or [abuse form](https://abuse.cloudflare.com/phishing); select "Phishing & Malware" for impersonation. Email complaints are generally not processed; use the online form. Provide specific URLs of infringing pages.

**Hosting detection**: Sites behind Cloudflare CDN hide origin IP. Use reverse IP lookup or hosting detection tools to identify underlying host; submit abuse to that provider as well.

**Parallel reporting**: Submit to registrar, host, and Google Safe Browsing simultaneously; do not wait for one before others. Google trademark review takes 1–8 weeks.

## Legal Options

| Option | When | Notes |
|--------|------|-------|
| **Cease and desist** | Trademark infringement | Lawyer-drafted; often first step |
| **DMCA takedown** | Copyrighted material copied | Images, copy, design; hosting providers typically comply |
| **Consumer protection** | Scam / fraud | FTC ReportFraud.ftc.gov (US) |
| **Law enforcement** | Financial loss, identity theft | IC3 (FBI) for cybercrime |

## Prevention Measures

### Defensive Registration

- Register brand+ai, brand+app, brand+official, etc. See **domain-selection** for defensive registration.
- Redirect variants to main domain; do not deploy separate sites.

### Official Site Verification

Place "Official website: [domain]" prominently:
- **Homepage** (above fold or hero)
- **Sign-in / Sign-up pages**
- **Pricing / Payment pages**: "Only pay at [official-domain]. Do not enter payment on other domains."
- **Footer**: "© [Brand]. Official site: [domain]"
- **FAQ**: "How do I verify I'm on the official site?" → "The only official URL is [domain]. Any other domain is not affiliated."

Use **trust-badges** for verification signals. See **about-page** for identity declaration.

### Customer Support (Payment Fraud)

When users report "can't use after payment" but no record exists—likely paid on fake site:

1. **Verify source**: Ask which URL they used (request screenshot or URL).
2. **Response template**: Explain that the only official site is [official-domain]; if they paid elsewhere, that site is not affiliated. Recommend: (a) dispute charge with payment provider, (b) use only [official-domain] going forward.
3. **Roll out** template to support team; ensure consistent messaging.

### User Education

- Social media pinned post / announcement: "Only use [official-domain]"
- Email signatures, support replies: link to official domain only

## Traffic Recovery (When Impersonation Intercepts Search)

| Tactic | Purpose |
|--------|---------|
| **Brand search ads** | Run Google Ads and Microsoft Ads on brand terms; ensure official site appears first for brand queries |
| **SEO** | Strengthen official site for branded queries; Organization schema, clear H1, meta tags. See **schema-markup**, **title-tag** |
| **Social** | Pinned post: "Only use [official-domain]. Beware of impersonation." |

## Monitoring (Ongoing)

- Periodic search: brand name + common variants (e.g., brand+ai, brand+app)
- See **brand-monitoring** for monitoring setup, tool selection, and cadence

## Timeline (Typical)

| Phase | Focus |
|-------|-------|
| **Immediate (Days 1–3)** | Support template; site declaration; evidence collection |
| **Short-term (Week 1–2)** | Abuse reports; Google Safe Browsing; DMCA if applicable |
| **Traffic (Week 2+)** | Brand ads; SEO; social announcement |
| **Ongoing** | Monitoring; defensive registration if feasible |

## Implementation Checklist

**Short-term (1–2 weeks)**: Evidence collection; abuse reports to registrar and host; Google Safe Browsing report; DMCA if applicable; add "Official website" on site.

**Medium-term**: Add impersonation guidance to domain-selection; official verification to trust-badges, about-page.

**Long-term**: Periodic search (brand + variants); brand monitoring (BrandShield, Doppel); defensive registration of variants.

## Output Format

- **Evidence package** (checklist, evidence list)
- **Report templates** (registrar, hosting, Google)
- **Timeline** (immediate vs medium vs long-term actions)
- **Prevention** (defensive registration, site verification, user education)

## References

- [How to Report and Take Down a Fake Website - LegalClarity](https://legalclarity.org/how-to-report-and-take-down-a-fake-website/)
- [Website Spoofing: Detection and Take Down - BrandShield](https://www.brandshield.com/blog/website-spoofing-detection-take-down/)
- [ICANN DNS Abuse Complaints Guide](https://www.icann.org/en/system/files/files/submitting-dns-abuse-complaints-icann-guide-17nov25-en.pdf)
- [Google Safe Browsing - Report Phishing](https://safebrowsing.google.com/safebrowsing/report_phish/)
- [Cloudflare Abuse Reporting](https://www.cloudflare.com/trust-safety/reporting-abuse/) — use online form; select Phishing & Malware
- [Google Trademark Complaint](https://services.google.com/inquiry/aw_tmcomplaint)
- [Bing Content Removal](https://www.bing.com/webmaster/contentremovalform/showanonymouspage)

## Related Skills

- **domain-selection**: Defensive domain registration; brand variants
- **rebranding-strategy**: When rebranding, sync brand protection checks
- **brand-monitoring**: Proactive monitoring setup; tool selection; this skill = reactive takedown
- **branding**: Brand asset protection; consistency
- **trust-badges**: Official site verification signals
- **about-page**: Official identity and domain declaration
- **homepage-generator**: "Official website" placement
- **google-ads**, **paid-ads-strategy**: Brand search ads for traffic recovery
- **schema-markup**, **title-tag**: SEO for branded queries
