# Brand Impersonation Response Plan

Complete response plan for brand impersonation scenarios (example: official-site.com vs impersonation-site.com).

---

## 1. Immediate Actions

### 1.1 Evidence Collection

| Item | Action |
|------|--------|
| **Full URLs** | Document all key pages of the impersonation site |
| **Screenshots** | Homepage, product pages, logo, layout; include date/time |
| **Comparison** | Side-by-side: official vs fake (layout, logo, copy similarity) |
| **WHOIS** | Use [ICANN Lookup](https://lookup.icann.org/) for registrar, creation date, registrant |
| **Hosting** | IP lookup to identify hosting provider |

### 1.2 Reporting Channels (Priority Order)

| Channel | Entry | Use Case |
|---------|-------|----------|
| **Domain registrar** | "Abuse" / "Report Misuse" on registrar site | Brand impersonation, trademark, fraud |
| **Hosting provider** | Same; submit abuse form | Hosting infringing content |
| **Google Safe Browsing** | [Report Phishing](https://safebrowsing.google.com/safebrowsing/report_phish/) | Phishing / impersonation risk |
| **DMCA** | If fake site copies product images, copy, design | Copyright infringement; request takedown |
| **ICANN** | If registrar does not respond | [DNS Abuse complaint](https://www.icann.org/en/system/files/files/submitting-dns-abuse-complaints-icann-guide-17nov25-en.pdf) |

### 1.3 Legal Options

- **Trademark infringement**: Cease and desist letter; consult lawyer
- **Consumer protection**: FTC ReportFraud.ftc.gov (US)
- **Cybercrime**: IC3 (FBI)—if financial fraud or identity theft

### 1.4 User-Side Protection

- Add "Official website" / "Only use [official-domain]" prominently on homepage, footer, About
- Include official domain statement in About, Footer
- Pinned post / announcement on social media: remind users to use official domain only

---

## 2. Brand Protection Skill

### 2.1 Location

- **Path**: `skills/strategies/brand-protection/SKILL.md`
- **Purpose**: Discovery, reporting, and prevention of brand impersonation, phishing, trademark infringement, domain squatting
- **Trigger terms**: brand impersonation, fake website, impersonation, phishing site, trademark infringement, domain squatting, brand abuse

### 2.2 Core Content Structure

1. Evidence collection checklist (URLs, screenshots, WHOIS, hosting)
2. Reporting channel matrix (registrar, hosting, Google, DMCA, ICANN)
3. Legal options (trademark, DMCA, consumer protection)
4. Prevention measures (defensive registration, official site declaration, user education)
5. Output format (evidence package, report templates, timeline)

### 2.3 Related Skills

| Related Skill | Relationship |
|---------------|--------------|
| **domain-selection** | Defensive domain registration (.com, .net, brand+ai variants); brand-protection references its defensive registration section |
| **rebranding-strategy** | Sync impersonation checks when rebranding; update official declaration |
| **branding** | Brand asset (logo, visual, copy) protection and consistency |
| **trust-badges** | Official site trust signals; help users distinguish official from fake |
| **about-page** | Official identity declaration; official domain statement |
| **homepage** | "Official website" placement on homepage |

---

## 3. Skill Dependency Diagram

```
                    ┌─────────────────────────────────────┐
                    │         brand-protection            │
                    │  Discover · Report · Prevent · Educate │
                    └─────────────────────┬───────────────┘
                                          │
         ┌────────────────────────────────┼────────────────────────────────┐
         ▼                                ▼                                ▼
┌──────────────────┐           ┌──────────────────────┐           ┌──────────────────┐
│ domain-selection │           │   trust-badges       │           │  about-page       │
│ Defensive reg.   │           │ Official site signal│           │ Identity decl.    │
│ .com/.net vars   │           │ Official badge       │           │ Official domain   │
└──────────────────┘           └──────────────────────┘           └──────────────────┘
         │                                │                                │
         └────────────────────────────────┼────────────────────────────────┘
                                          │
                              ┌───────────┴───────────┐
                              ▼                       ▼
                    ┌──────────────────┐    ┌──────────────────┐
                    │ rebranding-strategy│    │    branding      │
                    │ Sync on rebrand   │    │ Asset protection │
                    └──────────────────┘    └──────────────────┘
```

---

## 4. Implementation Checklist

### Short-term (1–2 weeks)

- [ ] Complete evidence collection (screenshots, WHOIS, hosting)
- [ ] Submit abuse reports to domain registrar and hosting provider
- [ ] Report to Google Safe Browsing
- [ ] Prepare DMCA notice if copyright material is copied
- [ ] Add "Official website" declaration on site

### Medium-term (1–2 months)

- [ ] Create `brand-protection` skill
- [ ] Add impersonation domain variant guidance to `domain-selection`
- [ ] Add official verification guidance to `trust-badges`, `about-page`
- [ ] Update `skills-relationships.md` with brand-protection node

### Long-term

- [ ] Periodic search: brand name + common variants (e.g., brand+ai, brand+app)
- [ ] Consider brand monitoring services (BrandShield, Doppel)
- [ ] Defensive registration of brand+ai, brand+app variants (if feasible)

---

## References

- [How to Report and Take Down a Fake Website - LegalClarity](https://legalclarity.org/how-to-report-and-take-down-a-fake-website/)
- [Website Spoofing: Detection and Take Down - BrandShield](https://www.brandshield.com/blog/website-spoofing-detection-take-down/)
- [ICANN DNS Abuse Complaints Guide](https://www.icann.org/en/system/files/files/submitting-dns-abuse-complaints-icann-guide-17nov25-en.pdf)
- [Google Safe Browsing - Report Phishing](https://safebrowsing.google.com/safebrowsing/report_phish/)
