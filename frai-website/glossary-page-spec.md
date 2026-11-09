# Final Round AI - Main Glossary Page Specification
## Hybrid Approach: Main Glossary Hub

**Document Version:** 1.1
**Last Updated:** April 13, 2026
**Page URL:** `finalroundai.com/glossary`

---

## Project Overview

Build a comprehensive interview terminology glossary as a single-page hub containing 130+ short-form definitions. This page will serve as the central glossary resource, with select high-value terms linking out to separate deep-dive pages (to be built in Phase 2).

**Purpose:**
- Capture informational search traffic ("what is [term]", "interview glossary", "interview terminology")
- Provide quick reference resource for job seekers
- Create internal linking hub supporting product pages and blog content
- Establish topical authority in interview preparation space

**SEO Strategy:**
- Primary keyword: "interview terminology glossary"
- Secondary keywords: "job interview terms", "interview glossary", "interview vocabulary", "interview definitions"
- Long-tail capture: Each term definition targets "what is [term]" queries via anchor links

---

## Page Structure & Architecture

### URL Structure
```
Primary URL: /glossary
Anchor links: /glossary#[term-slug]

Examples:
- /glossary#star-method
- /glossary#behavioral-interview
- /glossary#panel-interview
```

### Page Hierarchy
```
<h1> Main page title
  <section> Introduction + search
  <section> Alphabet navigation

  <h2> Letter section (A)
    <div class="term-card featured"> Featured term (links to deep page)
      <h3> Term name
    <div class="term-short"> Standard term (definition only)
      <h3 id="term-slug"> Term name

  <h2> Letter section (B)
    [repeat pattern]

  [Continue through Z]
```

---

## Detailed Component Specifications

### 1. Page Header Section

**HTML Structure:**
```html
<header class="glossary-header">
  <h1>Interview Terminology Glossary: 130+ Terms Every Job Seeker Should Know</h1>

  <div class="glossary-intro">
    <p>Master the language of job interviews. From AI interview copilot to behavioral questions, this comprehensive glossary covers every term you'll encounter during your job search. Whether you're preparing for your first interview or landing a senior role, understanding these terms will help you navigate the process with confidence.</p>
  </div>

  <!-- Search/Filter -->
  <div class="glossary-search">
    <input type="text" id="glossary-search" placeholder="Search for a term..." aria-label="Search glossary terms" />
  </div>
</header>
```

**Styling Requirements:**
- H1: Instrument Serif, 48px (site standard)
- Intro paragraph: Roboto, 16px body
- Search box: Required for UX with 130+ terms. Lightweight JS filter (~2kb).
- Mobile responsive: Stack elements vertically on mobile

---

### 2. Alphabet Navigation

**HTML Structure:**
```html
<nav class="alphabet-nav" id="alphabet-nav" aria-label="Glossary alphabetical navigation">
  <div class="alphabet-nav-label">Jump to:</div>
  <div class="alphabet-links">
    <a href="#a">A</a>
    <a href="#b">B</a>
    <a href="#c">C</a>
    <a href="#d">D</a>
    <a href="#e">E</a>
    <a href="#f">F</a>
    <a href="#g">G</a>
    <a href="#h">H</a>
    <a href="#i">I</a>
    <a href="#j">J</a>
    <a href="#k">K</a>
    <a href="#l">L</a>
    <a href="#m">M</a>
    <a href="#n">N</a>
    <a href="#o">O</a>
    <a href="#p">P</a>
    <a href="#q">Q</a>
    <a href="#r">R</a>
    <a href="#s">S</a>
    <a href="#t">T</a>
    <a href="#u">U</a>
    <a href="#v">V</a>
    <a href="#w">W</a>
    <a href="#x">X</a>
    <a href="#y">Y</a>
    <a href="#z">Z</a>
  </div>
  <a href="#top" class="back-to-top">Back to Top</a>
</nav>
```

**Behavior Requirements:**
- Sticky position: Remains visible as user scrolls
- Smooth scroll: Clicking letter smoothly scrolls to that section
- Mobile adaptation: Horizontal scroll on mobile
- Active state: Highlight current section's letter as user scrolls

**CSS:**
```css
.alphabet-nav {
  position: sticky;
  top: 80px; /* Adjust based on header height */
  background: var(--fr-white, #FFFFFF);
  border-bottom: 1px solid #e5e7eb;
  padding: 16px 0;
  z-index: 100;
}

.alphabet-links {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
}

.alphabet-links a {
  font-family: var(--fr-font-body, 'Roboto', system-ui, sans-serif);
  font-weight: 600;
  color: var(--fr-primary, #FF4800);
  text-decoration: none;
  padding: 4px 8px;
  border-radius: var(--fr-radius, 8px);
  transition: background 0.2s;
}

.alphabet-links a:hover {
  background: var(--fr-peach, #FFF8EE);
}

.alphabet-links a.active {
  background: var(--fr-primary, #FF4800);
  color: var(--fr-white, #FFFFFF);
}

@media (max-width: 768px) {
  .alphabet-links {
    overflow-x: auto;
    flex-wrap: nowrap;
    justify-content: flex-start;
  }
}
```

---

### 3. Letter Section Template

**HTML Structure:**
```html
<section class="letter-section" id="a">
  <h2 class="letter-header">A</h2>

  <!-- Featured Term (links to separate page) -->
  <div class="term-card featured">
    <span class="featured-badge">Featured Guide</span>
    <h3>
      <a href="/glossary/ai-interview-copilot">AI Interview Copilot</a>
    </h3>
    <p class="term-preview">A real-time AI assistant that provides instant answers during live interviews without being detected by interviewers. Unlike mock interview tools that help you practice beforehand, an AI interview copilot works alongside you during actual interviews.</p>
    <a href="/glossary/ai-interview-copilot" class="read-more-link">Read full guide</a>
  </div>

  <!-- Standard Term (definition on this page only) -->
  <div class="term-short" id="applicant-tracking-system">
    <h3>Applicant Tracking System (ATS)</h3>
    <p><strong>Definition:</strong> Software used by employers to automatically filter and rank resumes before human review. Over 90% of Fortune 500 companies use ATS systems to screen candidates.</p>
  </div>

  <!-- Another standard term -->
  <div class="term-short" id="assessment-center">
    <h3>Assessment Center</h3>
    <p><strong>Definition:</strong> A structured evaluation process where candidates complete multiple exercises including group tasks, presentations, and role-plays. Common in UK graduate schemes and management roles.</p>
    <p class="related-terms"><strong>Related:</strong> <a href="#competency-based-interview">Competency-Based Interview</a>, <a href="#group-interview">Group Interview</a></p>
  </div>

</section>
```

**Component Breakdown:**

#### 3a. Letter Header
```html
<h2 class="letter-header">A</h2>
```
- Styling: Instrument Serif, 36px, bold, clear visual separator
- ID matches alphabet nav anchor
- Scroll margin to account for sticky nav

#### 3b. Featured Term Card (15-20 terms total)
```html
<div class="term-card featured">
  <span class="featured-badge">Featured Guide</span>
  <h3><a href="/glossary/[term-slug]">Term Name</a></h3>
  <p class="term-preview">[100-150 word preview/excerpt]</p>
  <div class="term-meta">
    <span class="read-time">5 min read</span>
    <a href="/glossary/[term-slug]" class="read-more-link">Read full guide</a>
  </div>
</div>
```

**Which terms are "featured":** See Section 7 (Featured Terms List) below.

**Styling Requirements:**
- Visual distinction: Orange border, peach background
- Clickable: Entire card should be interactive
- Preview text: 100-150 words (excerpt from full page)
- "Read full guide" CTA clearly visible

#### 3c. Standard Term (130+ terms)
```html
<div class="term-short" id="term-slug">
  <h3>Term Name</h3>
  <p><strong>Definition:</strong> [50-100 word definition]</p>
  <p class="term-example"><strong>Example:</strong> [Optional 1 sentence example]</p>
  <p class="related-terms"><strong>Related:</strong> <a href="#term1">Term 1</a>, <a href="#term2">Term 2</a></p>
</div>
```

**Content Requirements:**
- **Definition:** 50-100 words, clear and concise
- **Example (optional):** Real-world usage example in 1 sentence
- **Related terms (optional):** 2-3 internal links to related glossary terms
- **NO CTAs** on standard terms (keeps page clean)

---

### 4. Term Categories & Content Structure

#### Definition Format Standards

**For all definitions, follow this pattern:**

```
<strong>Definition:</strong> [What it is in 1-2 sentences]. [Why it matters or when it's used in 1 sentence].
```

**Example:**
```html
<p><strong>Definition:</strong> A behavioral interview is an interview format where employers ask about past experiences to predict future performance. Questions typically start with "Tell me about a time when..." and require STAR method responses.</p>
```

**Avoid:**
- Starting with "A [term] is when..."
- Overly technical jargon without explanation
- Vague or circular definitions
- Marketing language or hype

**Do:**
- Clear, straightforward language
- Context for when/why term is used
- Mention related terms naturally in definition
- Include geographic specificity when relevant (e.g., "Common in UK graduate schemes")

---

### 5. CTA Strategy (Minimal on Main Page)

**IMPORTANT:** Main glossary page should have **minimal CTAs** to avoid overwhelming users. CTA copy follows brand standards from `brand-visual.md`.

**Where to place CTAs:**

#### Option A: Sticky Bottom Bar (Recommended)
```html
<div class="glossary-cta-bar sticky-bottom">
  <div class="cta-content">
    <span>Ready to ace your next interview?</span>
    <a href="/getting-started" class="cta-button-primary">Get Started Free</a>
    <a href="/download" class="cta-button-secondary">Download Now</a>
  </div>
</div>
```

**Behavior:**
- Appears after user scrolls past alphabet nav
- Sticky to bottom of viewport
- Dismissible with X button
- Mobile responsive (stacks vertically)

#### Option B: End-of-Page CTA
```html
<section class="glossary-footer-cta">
  <h2>Ready to Ace Your Next Interview?</h2>
  <p>Try Final Round AI Free — 100% invisible, real-time answers, 10M+ users.</p>
  <div class="cta-buttons">
    <a href="/getting-started" class="cta-button-primary">Get Started Free</a>
    <a href="/download" class="cta-button-secondary">Download Now</a>
  </div>
</section>
```

**AVOID:**
- CTAs after every term definition
- Popup modals interrupting reading
- Multiple CTAs in alphabet nav
- Auto-playing videos or demos

---

### 6. Schema Markup

**Implement DefinedTermSet schema for SEO:**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "DefinedTermSet",
  "name": "Interview Terminology Glossary",
  "description": "Comprehensive glossary of 130+ interview terms and definitions for job seekers",
  "publisher": {
    "@type": "Organization",
    "name": "Final Round AI",
    "url": "https://finalroundai.com"
  },
  "hasDefinedTerm": [
    {
      "@type": "DefinedTerm",
      "@id": "https://finalroundai.com/glossary#ai-interview-copilot",
      "name": "AI Interview Copilot",
      "description": "A real-time AI assistant that provides instant answers during live interviews without being detected by interviewers.",
      "url": "https://finalroundai.com/glossary/ai-interview-copilot"
    },
    {
      "@type": "DefinedTerm",
      "@id": "https://finalroundai.com/glossary#star-method",
      "name": "STAR Method",
      "description": "A structured approach to answering behavioral interview questions by describing the Situation, Task, Action, and Result.",
      "inDefinedTermSet": "https://finalroundai.com/glossary"
    },
    {
      "@type": "DefinedTerm",
      "@id": "https://finalroundai.com/glossary#behavioral-interview",
      "name": "Behavioral Interview",
      "description": "An interview format where employers ask about past experiences to predict future performance.",
      "inDefinedTermSet": "https://finalroundai.com/glossary"
    }
  ]
}
</script>
```

**Notes:**
- Featured terms (with separate pages): Include "url" property pointing to deep page
- Standard terms (on main page only): Use "inDefinedTermSet" property
- Update schema when adding new terms
- Full schema should include ALL terms at launch

---

### 7. Featured Terms List (15-18 Terms)

**These terms get the "featured" card treatment and link to separate deep-dive pages.**

#### Tier 1: Product-Aligned Terms (6 terms)

These map directly to actual Final Round AI products per `project-context.md`:

| # | Term | Deep Page URL | Maps To Product |
|---|------|--------------|-----------------|
| 1 | Interview Copilot | `/glossary/interview-copilot` | Interview Copilot (core) |
| 2 | AI Interview Assistant | `/glossary/ai-interview-assistant` | Interview Copilot (category term) |
| 3 | AI Mock Interview | `/glossary/ai-mock-interview` | AI Mock Interview |
| 4 | AI Resume Builder | `/glossary/ai-resume-builder` | AI Resume Builder |
| 5 | Mock Interview | `/glossary/mock-interview` | AI Mock Interview (general term) |
| 6 | Real-time Interview Help | `/glossary/real-time-interview-help` | Interview Copilot (feature term) |

#### Tier 2: High-Value Informational Terms (9-12 terms)

High search volume, strong internal linking value:

| # | Term | Deep Page URL |
|---|------|--------------|
| 7 | STAR Method | `/glossary/star-method` |
| 8 | Behavioral Interview | `/glossary/behavioral-interview` |
| 9 | Technical Interview | `/glossary/technical-interview` |
| 10 | Case Interview | `/glossary/case-interview` |
| 11 | Coding Interview | `/glossary/coding-interview` |
| 12 | HireVue Interview | `/glossary/hirevue-interview` |
| 13 | Competency-Based Interview | `/glossary/competency-based-interview` |
| 14 | Panel Interview | `/glossary/panel-interview` |
| 15 | Assessment Center | `/glossary/assessment-center` |
| 16 | Phone Screen | `/glossary/phone-screen` (optional) |
| 17 | System Design Interview | `/glossary/system-design-interview` (optional) |
| 18 | Video Interview | `/glossary/video-interview` (optional) |

**Notes:**
- Tier 1 terms should naturally mention the relevant Final Round AI product in the preview text
- Tier 2 terms are purely informational — no product pitch in the preview
- Deep pages will be built in Phase 2
- Deep page URLs for Tier 1 product terms should NOT duplicate existing product pages (`/interview-copilot`, `/ai-mock-interview`). The glossary deep page explains the *concept*; the product page sells the *tool*. Cross-link between them.

---

### 8. Standard Terms List (130+ Terms)

**These terms get short definitions on the main page only (no separate pages).**

**A:**
- Applicant Tracking System (ATS)
- Asynchronous Interview
- Assessment Day
- Aptitude Test

**B:**
- Background Check
- Blind Hiring
- Body Language
- Brainteaser Questions

**C:**
- CAR Method
- Case Study Interview
- Coffee Interview
- Competency Framework
- Conversational Interview
- Cover Letter
- Culture Fit Interview

**D:**
- Direct Hire
- Diversity Interview

**E:**
- Elevator Pitch
- Exit Interview

**F:**
- Final Round Interview
- Follow-up Interview
- Functional Interview

**G:**
- Group Interview
- Graduate Scheme (UK term)

**H:**
- Headhunter
- HR Interview
- Hypothetical Questions

**I:**
- In-basket Exercise
- Informational Interview
- Initial Screening
- Internal Interview

**J:**
- Job Simulation

**K:**
- Key Performance Indicator (KPI)

**L:**
- Leadership Interview
- Lunch Interview

**M:**
- Motivational Fit Interview

**N:**
- Networking Interview
- Non-Verbal Communication

**O:**
- Onboarding
- One-Way Video Interview
- Onsite Interview
- Open-Ended Questions

**P:**
- Pre-Employment Assessment
- Presentation Interview
- Psychometric Test

**Q:**
- Qualification Interview

**R:**
- Recruitment Agency
- Reference Check
- Rejection Email
- Remote Interview
- Resume Screening
- Role-Play Interview

**S:**
- Salary Negotiation
- Screening Interview
- Second Interview
- Situational Interview
- Skills Assessment
- SOAR Method
- Stress Interview
- Structured Interview

**T:**
- Talent Acquisition
- Technical Assessment
- Telephone Interview
- Thank You Email
- Third-Party Recruiter
- Timeline Questions
- Trial Period

**U:**
- Unstructured Interview

**V:**
- Values-Based Interview
- Virtual Interview
- Virtual Onboarding

**W:**
- Walk-in Interview
- Whiteboard Interview
- Work Sample Test

**X, Y, Z:**
- (Add if relevant terms exist)

**TOTAL: ~120 standard terms** + ~18 featured = ~138 terms

---

### 9. Mobile Responsiveness Requirements

**Breakpoint Specifications:**

#### Desktop (1024px+)
- Single or 2-column layout for terms (if design allows)
- Sticky alphabet nav at top
- Full-width featured cards

#### Tablet (768px - 1023px)
- Single column layout
- Sticky alphabet nav (horizontal scroll)
- Featured cards slightly smaller
- Standard terms full width

#### Mobile (< 768px)
- Single column, full width
- Alphabet nav becomes horizontal scroll
- Featured cards stack vertically
- Increase tap target size for links (min 44px)
- Sticky bottom CTA bar (if used)

**Performance Requirements:**
- Page load time: < 3 seconds on 3G
- Lazy load images (if any)
- Minimize JavaScript (smooth scroll + search filter only)
- Critical CSS inline

---

### 10. SEO Metadata

**Title Tag:**
```
Interview Terminology Glossary: 130+ Terms Job Seekers Should Know | Final Round AI
```
(80 characters)

**Meta Description:**
```
Master interview terminology with our comprehensive glossary. Learn 130+ essential terms from AI interview copilot to STAR method. Free resource for job seekers.
```
(158 characters)

**Open Graph Tags:**
```html
<meta property="og:title" content="Interview Terminology Glossary: 130+ Terms Every Job Seeker Should Know" />
<meta property="og:description" content="Master the language of job interviews with our comprehensive glossary covering 130+ essential terms." />
<meta property="og:url" content="https://finalroundai.com/glossary" />
<meta property="og:type" content="website" />
```

**Canonical Tag:**
```html
<link rel="canonical" href="https://finalroundai.com/glossary" />
```

**Robots Meta:**
```html
<meta name="robots" content="index, follow" />
```

---

### 11. Internal Linking Strategy

**Links FROM glossary page:**

#### To Product Pages:
- Featured term cards (Tier 1) mention products naturally in preview text
- Sticky CTA bar links to `/getting-started`
- End-of-page CTA links to `/getting-started` and `/download`

#### To Blog Posts:
- Contextual mentions in definitions where relevant
- Example: "Learn more about [preparing for behavioral interviews](/blog/behavioral-interview-questions-and-answers)"
- Link to planned pillar articles from `blog-strategy.md` as they publish:
  - STAR Method definition links to `/blog/behavioral-interview-ai`
  - HireVue Interview definition links to `/blog/hirevue-interview-prep-ai`
  - Technical Interview definition links to `/blog/ai-coding-interview-guide`

#### Within Glossary:
- Related terms link to other anchor IDs (`#star-method`)
- "Back to top" link in alphabet nav

**Links TO glossary page (add at launch):**

#### From /explore page (SEO task 2.1):
```html
<a href="/glossary">Interview Terminology Glossary</a>
```

#### From Footer (SEO task 2.2):
Add `/glossary` under "Resources" section in site footer.

#### From Product Pages:
```html
Not sure what a <a href="/glossary#behavioral-interview">behavioral interview</a> is?
```

#### From Blog Posts:
```html
Learn more about the <a href="/glossary#star-method">STAR method</a> in our glossary.
```

---

### 12. Analytics & Tracking

**Events to Track:**

```javascript
// Alphabet nav clicks
gtag('event', 'glossary_nav_click', {
  'letter': 'A' // or B, C, etc.
});

// Featured term clicks
gtag('event', 'glossary_featured_click', {
  'term': 'AI Interview Copilot',
  'destination': '/glossary/ai-interview-copilot'
});

// CTA clicks
gtag('event', 'glossary_cta_click', {
  'cta_type': 'sticky_bar', // or 'end_of_page'
  'destination': '/getting-started'
});

// Search usage
gtag('event', 'glossary_search', {
  'search_term': '[user search query]'
});
```

**Metrics to Monitor:**
- Page views
- Average time on page
- Scroll depth (% of users reaching each letter section)
- Click-through rate on featured terms
- CTA conversion rate
- Bounce rate
- Search usage frequency and top queries

---

### 13. Content Writing Guidelines for Definitions

**Voice & Tone:**
- Conversational but professional (per `brand-visual.md` voice guidelines)
- Accessible to entry-level job seekers
- No jargon without explanation
- US English spelling (except UK-specific terms like "graduate scheme")
- Confident, de-stressing tone — consistent with FRAI brand

**Length Guidelines:**
- Standard definitions: 50-100 words
- Featured term previews: 100-150 words
- Keep it scannable (short sentences, simple structure)

**Structure Template:**
```
1. What it is (1-2 sentences)
2. When/why it's used (1 sentence)
3. Example or key detail (optional, 1 sentence)
```

**Example - Good Definition:**
```
Panel Interview

Definition: An interview format where a candidate is interviewed simultaneously by
multiple people (typically 3-6 interviewers) representing different departments or
levels within the company. Panel interviews are common for senior roles, academic
positions, and government jobs where diverse perspectives inform hiring decisions.

Example: "My final round at Google was a panel interview with the hiring manager,
team lead, and two senior engineers."

Related: Group Interview, Final Round Interview
```

**Example - Bad Definition:**
```
Panel Interview

Definition: A panel interview is when you interview with a panel.
```
(Too vague, circular, no value)

---

### 14. Technical Implementation Notes

**Required:**
- Smooth scroll polyfill (for older browsers)
- Search/filter JavaScript (lightweight, < 5kb)

**Accessibility Requirements:**
- ARIA labels on navigation elements
- Keyboard navigation support (tab through alphabet nav)
- Focus states on all interactive elements
- Sufficient color contrast (WCAG AA minimum)
- Screen reader friendly (semantic HTML)

**HTML Validation:**
- Valid HTML5
- Proper heading hierarchy (no skipped levels)
- Unique IDs for all anchor links
- Alt text on any images (if used)

**Performance Optimization:**
- Minify CSS/JS
- Compress images (if any)
- Enable browser caching
- Consider lazy loading for below-fold content
- Inline critical CSS

---

### 15. Content Approval Workflow

**Phase 1: Main Glossary Page**

**Step 1: Term List Finalization**
- Review and approve final list of 120+ standard terms
- Confirm 15-18 featured terms
- Assign term categories (A-Z)

**Step 2: Definition Writing**
- Write all 120+ definitions (50-100 words each)
- Write 15-18 featured term previews (100-150 words each)
- Internal review for accuracy and consistency

**Step 3: Design & Development**
- Implement page structure and styling per brand guidelines
- Add alphabet navigation and smooth scroll
- Add search/filter functionality
- Integrate schema markup
- Set up analytics tracking

**Step 4: QA Testing**
- Test all anchor links
- Verify mobile responsiveness
- Check page load performance
- Validate HTML/accessibility
- Cross-browser testing

**Step 5: Launch**
- Publish to production
- Add to `/explore` page and footer
- Submit sitemap to Google Search Console
- Add internal links from product/blog pages
- Monitor analytics for first 2 weeks

---

### 16. Success Metrics (3 Months Post-Launch)

**Traffic Goals:**
- 500-1,000 monthly organic visits
- Average time on page: 2+ minutes
- Bounce rate: < 60%

**Engagement Goals:**
- 10-15% click-through on featured terms
- 5-8% CTA conversion rate (sticky bar or end-of-page)
- 20+ featured snippet rankings (Google position 0)

**SEO Goals:**
- Rank top 10 for "interview terminology glossary"
- Rank top 20 for "interview terms dictionary"
- 50+ long-tail keywords ranking (e.g., "what is STAR method")

---

### 17. Future Enhancements (Post-Launch)

**Phase 2 Additions:**
- Build out 15-18 deep-dive term pages
- Add "Recently Updated" section
- Create downloadable PDF version
- Add user-submitted terms (moderated)

**Content Expansion:**
- Add video explanations for top 10 terms
- Industry-specific glossary sections (tech, finance, consulting)
- Geographic variations (US vs UK vs Canada terminology)

---

## Appendix A: Sample Featured Term Card HTML

```html
<div class="term-card featured">
  <span class="featured-badge">Featured Guide</span>
  <h3>
    <a href="/glossary/ai-interview-copilot">AI Interview Copilot</a>
  </h3>
  <p class="term-preview">
    A real-time AI assistant that provides instant answers during live interviews
    without being detected by interviewers. Unlike mock interview tools that help
    you practice beforehand, an AI interview copilot works alongside you during
    actual interviews. It transcribes questions in real-time and generates tailored
    responses based on your resume and job description.
  </p>
  <div class="term-meta">
    <span class="read-time">5 min read</span>
    <a href="/glossary/ai-interview-copilot" class="read-more-link">
      Read full guide
    </a>
  </div>
</div>
```

## Appendix B: Sample Standard Term HTML

```html
<div class="term-short" id="panel-interview">
  <h3>Panel Interview</h3>
  <p><strong>Definition:</strong> An interview format where a candidate is interviewed simultaneously by multiple people (typically 3-6 interviewers) representing different departments or levels within the company. Panel interviews are common for senior roles, academic positions, and government jobs where diverse perspectives inform hiring decisions.</p>
  <p class="term-example"><strong>Example:</strong> "My final round at Google was a panel interview with the hiring manager, team lead, and two senior engineers."</p>
  <p class="related-terms"><strong>Related:</strong> <a href="#group-interview">Group Interview</a>, <a href="#final-round-interview">Final Round Interview</a>, <a href="#behavioral-interview">Behavioral Interview</a></p>
</div>
```

## Appendix C: CSS Styling Reference (FRAI Brand)

Uses CSS variables from `brand-visual.md`. All colors, fonts, and radii reference the FRAI design system.

```css
/* =============================================
   FRAI Glossary Page Styles
   Brand ref: brand-visual.md
   ============================================= */

/* Letter Section */
.letter-section {
  padding: 48px 0;
  border-bottom: 1px solid #e5e7eb;
}

.letter-header {
  font-family: var(--fr-font-heading, 'Instrument Serif', serif);
  font-size: 36px;
  font-weight: 700;
  color: var(--fr-text, #0A0A0A);
  margin-bottom: 32px;
  scroll-margin-top: 120px; /* Account for sticky nav */
}

/* Featured Term Card */
.term-card.featured {
  background: var(--fr-peach, #FFF8EE);
  border: 2px solid var(--fr-primary, #FF4800);
  border-radius: var(--fr-radius-lg, 10px);
  padding: 24px;
  margin-bottom: 24px;
  transition: box-shadow 0.2s;
}

.term-card.featured:hover {
  box-shadow: 0 8px 24px rgba(255, 72, 0, 0.12);
}

.featured-badge {
  display: inline-block;
  background: var(--fr-primary, #FF4800);
  color: var(--fr-white, #FFFFFF);
  font-family: var(--fr-font-body, 'Roboto', system-ui, sans-serif);
  font-size: 12px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 4px;
  margin-bottom: 12px;
}

.term-card h3 {
  font-family: var(--fr-font-heading, 'Instrument Serif', serif);
  font-size: 24px;
  margin-bottom: 12px;
}

.term-card h3 a {
  color: var(--fr-text, #0A0A0A);
  text-decoration: none;
}

.term-card h3 a:hover {
  color: var(--fr-primary, #FF4800);
}

.term-preview {
  font-family: var(--fr-font-body, 'Roboto', system-ui, sans-serif);
  color: var(--fr-gray, #6B7280);
  line-height: 1.6;
  margin-bottom: 16px;
}

.term-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.read-time {
  font-size: 14px;
  color: var(--fr-gray, #6B7280);
}

.read-more-link {
  color: var(--fr-primary, #FF4800);
  font-weight: 600;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 4px;
}

.read-more-link:hover {
  color: var(--fr-warm-orange, #FF7640);
}

/* Standard Term */
.term-short {
  margin-bottom: 32px;
  padding-bottom: 32px;
  border-bottom: 1px solid #f3f4f6;
  scroll-margin-top: 120px;
}

.term-short:last-child {
  border-bottom: none;
}

.term-short h3 {
  font-family: var(--fr-font-body, 'Roboto', system-ui, sans-serif);
  font-size: 20px;
  font-weight: 600;
  color: var(--fr-text, #0A0A0A);
  margin-bottom: 8px;
}

.term-short p {
  font-family: var(--fr-font-body, 'Roboto', system-ui, sans-serif);
  color: var(--fr-gray, #6B7280);
  line-height: 1.6;
  margin-bottom: 8px;
}

.term-example {
  font-style: italic;
  color: var(--fr-gray, #6B7280);
}

.related-terms {
  font-size: 14px;
}

.related-terms a {
  color: var(--fr-primary, #FF4800);
  text-decoration: none;
}

.related-terms a:hover {
  text-decoration: underline;
  color: var(--fr-warm-orange, #FF7640);
}

/* Sticky CTA Bar */
.glossary-cta-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: var(--fr-charcoal, #1C1D20);
  padding: 12px 24px;
  z-index: 200;
  display: flex;
  justify-content: center;
  align-items: center;
}

.glossary-cta-bar .cta-content {
  display: flex;
  align-items: center;
  gap: 16px;
}

.glossary-cta-bar span {
  color: var(--fr-white, #FFFFFF);
  font-family: var(--fr-font-body, 'Roboto', system-ui, sans-serif);
  font-weight: 500;
}

.cta-button-primary {
  background: var(--fr-primary, #FF4800);
  color: var(--fr-white, #FFFFFF);
  padding: 10px 24px;
  border-radius: var(--fr-radius, 8px);
  font-weight: 600;
  text-decoration: none;
  transition: background 0.2s;
}

.cta-button-primary:hover {
  background: var(--fr-warm-orange, #FF7640);
}

.cta-button-secondary {
  color: var(--fr-white, #FFFFFF);
  padding: 10px 24px;
  border: 1px solid var(--fr-white, #FFFFFF);
  border-radius: var(--fr-radius, 8px);
  font-weight: 600;
  text-decoration: none;
  transition: background 0.2s;
}

.cta-button-secondary:hover {
  background: rgba(255, 255, 255, 0.1);
}

/* Search Box */
.glossary-search input {
  font-family: var(--fr-font-body, 'Roboto', system-ui, sans-serif);
  width: 100%;
  max-width: 480px;
  padding: 12px 16px;
  border: 1px solid #e5e7eb;
  border-radius: var(--fr-radius, 8px);
  font-size: 16px;
  color: var(--fr-text, #0A0A0A);
  transition: border-color 0.2s;
}

.glossary-search input:focus {
  outline: none;
  border-color: var(--fr-primary, #FF4800);
  box-shadow: 0 0 0 3px rgba(255, 72, 0, 0.1);
}

/* Footer CTA Section */
.glossary-footer-cta {
  text-align: center;
  padding: 64px 24px;
  background: var(--fr-peach, #FFF8EE);
  border-radius: var(--fr-radius-lg, 10px);
  margin: 48px 0;
}

.glossary-footer-cta h2 {
  font-family: var(--fr-font-heading, 'Instrument Serif', serif);
  font-size: var(--fr-h2, 30px);
  color: var(--fr-text, #0A0A0A);
  margin-bottom: 12px;
}

.glossary-footer-cta p {
  font-family: var(--fr-font-body, 'Roboto', system-ui, sans-serif);
  color: var(--fr-gray, #6B7280);
  margin-bottom: 24px;
}

.glossary-footer-cta .cta-buttons {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}

@media (max-width: 768px) {
  .glossary-cta-bar .cta-content {
    flex-direction: column;
    gap: 8px;
  }

  .glossary-footer-cta .cta-buttons {
    flex-direction: column;
    align-items: center;
  }
}
```

---

## Appendix D: Changes from v1.0

Summary of corrections applied in v1.1:

| Area | v1.0 (Original) | v1.1 (Corrected) |
|------|-----------------|-------------------|
| **Accent colors** | `#6366f1` (indigo) throughout | `#FF4800` (FRAI primary orange) per `brand-visual.md` |
| **Hover backgrounds** | `#e0e7ff` (indigo tint) | `#FFF8EE` (peach) per brand palette |
| **Card shadows** | Indigo-tinted | Orange-tinted `rgba(255, 72, 0, 0.12)` |
| **Typography** | Generic sans-serif | Instrument Serif (headings) + Roboto (body) per brand |
| **CSS approach** | Hardcoded hex values | CSS variables from `brand-visual.md` with fallbacks |
| **CTA copy** | "Try Mock Interview" / "Get Interview Copilot" | "Get Started Free" / "Download Now" per `brand-visual.md` CTA standards |
| **CTA destinations** | `/ai-mock-interview`, `/interview-copilot` | `/getting-started`, `/download` per brand conversion path |
| **Featured terms (Tier 1)** | 10 "product terms" including non-products | 6 product-aligned terms matching actual FRAI products |
| **Featured terms (Tier 2)** | 5-10 informational | 9-12 high-value informational terms |
| **Search/filter** | Optional | Required (130+ terms needs search for UX) |
| **Term count** | H1 said "150+" but listed ~130 | Consistent "130+" throughout |
| **Mock Interview duplicate** | Listed in both featured and standard | Removed from standard list |
| **Internal linking** | No /explore or footer mentions | Added /explore page and footer integration per SEO tasks |
| **Blog cross-links** | Generic mentions | Specific links to planned pillar articles from `blog-strategy.md` |
| **Accessibility** | Basic mentions | ARIA labels added to HTML examples |

---

## End of Specification

**Next Steps:**
1. Review and approve this specification
2. Finalize term list (120+ standard terms with definitions)
3. Write featured term previews (15-18 terms)
4. Design and develop page following FRAI brand guidelines
5. QA testing
6. Launch and integrate with /explore page + footer
