---
name: components-popup
description: When the user wants to add, optimize, or audit popups or modals for lead capture or offers. Also use when the user mentions "popup," "modal," "lightbox," "overlay," or "exit-intent."
metadata:
  version: 1.0.0
---

# Components: Popup / Modal

Guides popup and modal design for conversion. Well-designed popups can achieve up to 25% conversion; poorly timed or intrusive ones hurt UX and SEO. Google penalizes intrusive mobile popups.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## Initial Assessment

**Check for product marketing context first:** If `.claude/product-marketing-context.md` or `.cursor/product-marketing-context.md` exists, read it for offers and audience.

Identify:
1. **Goal**: Newsletter, discount, lead magnet, demo
2. **Trigger**: Time delay, scroll %, exit intent, click
3. **Mobile**: Critical; smaller screens = easier to interrupt

## Best Practices

### Timing and Context

- **Avoid**: Popup on page load; users hate it
- **Prefer**: After engagement (scroll 25-50%, time on page, exit intent)
- **Personalize**: Returning visitors, cart abandoners, discount users
- **Value-first**: Offer genuine value; act as "helpful teammate" not spam

### Design

- **Short copy**: Clear headline, one benefit, single CTA
- **Visual hierarchy**: Guide attention to CTA; don't distract
- **Easy exit**: Clear X, visible "No Thanks"; friction-free exit increases trust and conversion
- **Brand consistency**: Build instant comfort

### Mobile

- **Size**: Fit screen; thumb-friendly close
- **Lightweight**: Avoid heavy assets; affects LCP
- **SEO**: Google penalizes intrusive interstitials; avoid full-page takeover on mobile

### Avoid

- Dark patterns (fake close, hidden options)
- Too early or too frequent
- Multiple popups in one session
- Blocking content without clear value

## Triggers

| Trigger | Use |
|---------|-----|
| **Time delay** | 5-15s typical; after some engagement |
| **Scroll %** | 25-50% read; user invested |
| **Exit intent** | Mouse leaving viewport; last chance |
| **Click** | User-initiated; least intrusive |

## Output Format

- **Offer** and copy
- **Trigger** (timing, scroll, exit intent)
- **Design** (size, CTA, exit)
- **Mobile** checklist

## Related Skills

- **components-newsletter-signup**: Popup often contains signup form
- **components-cta**: Popup CTA design
- **components-top-banner**: Alternative to popup; less intrusive for announcements
- **components-sidebar**: Alternative for CTAs; in-content often converts better
- **components-brand-visual**: Popup styling
