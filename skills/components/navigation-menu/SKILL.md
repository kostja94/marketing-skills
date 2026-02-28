---
name: navigation-menu-generator
description: When the user wants to design, optimize, or audit site navigation menus. Also use when the user mentions "navigation," "nav menu," "header menu," "site structure," "menu design," "navbar," "main menu," "mega menu," "dropdown menu," "mobile menu," or "hamburger menu." For breadcrumbs, use breadcrumb-generator.
metadata:
  version: 1.0.0
---

# Components: Navigation Menu

Guides navigation menu design for SEO, UX, and accessibility. Navigation helps users find content and signals site structure to search engines.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for key pages and audience.

Identify:
1. **Site structure**: Main sections, hierarchy
2. **Primary goals**: Conversion paths, key pages
3. **Platform**: Web, mobile, both

## Structure & Organization

### Menu Size

- **Primary nav**: 7-9 items; avoid overwhelming users
- **Sub-navigation**: Up to 2 levels; deeper topics in sub-menus
- **Pattern**: Horizontal top nav or vertical side nav; avoid novel patterns

### Hierarchy

- Reflect sitemap structure; need not match exactly
- Prioritize what visitors need most
- Logical grouping by topic or task

## SEO Best Practices

| Practice | Purpose |
|----------|---------|
| **Semantic HTML** | `<nav>`, `<ul>`, `<li>`; proper landmark roles |
| **Descriptive anchor text** | Target keywords; avoid "Click here" |
| **Text links** | Prefer text over images; crawlers need readable links |
| **Initial render** | All nav HTML in first paint; no JS-only menus for critical links |
| **Visible links** | Prefer visible over hidden; helps crawlers understand structure |

### Crawlability

- Sub-menus: Ensure HTML is in DOM (e.g., CSS-hidden, not JS-injected)
- Footer nav: Include secondary links
- Breadcrumbs: See breadcrumb-generator for implementation

## UX Guidelines

### Visibility & Location

- **Desktop**: Visible nav; avoid hiding behind hamburger when space allows
- **Expected placement**: Primary nav in header; footer nav at bottom
- **Current location**: Indicate active page/section in menu

### Accessibility

| Requirement | Practice |
|-------------|----------|
| **Labels** | Clear, intuitive wording |
| **Contrast** | 4.5:1 for link text |
| **Touch targets** | >=44x44px; adequate spacing |
| **Keyboard** | Full keyboard navigation; focus visible |
| **Screen readers** | Proper ARIA; skip links for long menus |

### Design

- Simple, clear; avoid covering entire screen with open menus on desktop
- Consistent across pages
- Mobile: Hamburger acceptable; ensure menu is usable when open

## Output Format

- **Structure** (primary items, sub-items)
- **Anchor text** suggestions
- **HTML/ARIA** notes
- **SEO** checklist
- **Accessibility** checklist

## Related Skills

- **xml-sitemap**: Nav should reflect discoverable pages
- **internal-links**: Nav is primary internal linking
- **site-crawlability**: Nav affects crawl paths
- **category-page-generator**: Category hierarchy in nav
- **footer-generator**: Footer nav complements header nav
- **logo-generator**: Logo typically sits in header with nav
- **breadcrumb-generator**: Breadcrumb navigation; BreadcrumbList schema
