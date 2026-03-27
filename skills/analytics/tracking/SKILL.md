---
name: analytics-tracking
description: When the user wants to set up, audit, or optimize analytics tracking (GA4, events, conversions). Also use when the user mentions "Google Analytics," "GA4," "event tracking," "conversions," "attribution model," "gtag," "data layer," "GA4 setup," "conversion tracking," "event setup," "User ID tracking," or "CTA attribution." For traffic insights, use traffic-analysis.
metadata:
  version: 1.3.1
---

# Analytics: Tracking

Guides analytics implementation: GA4 setup, event tracking, conversions, and data quality. Applies to web and app tracking across marketing channels.

**When invoking**: On **first use**, if helpful, open with 1-2 sentences on what this skill covers and why it matters, then provide the main output. On **subsequent use** or when the user asks to skip, go directly to the main output.

## User ID

- **Purpose**: Cross-device, cross-session user identification
- **Implementation**: Set `user_id` when user is identified (e.g., login); send to GA4
- **Benefit**: Accurate attribution across sessions; better audience building

## CTA Attribution (Article ROI)

Track CTA clicks on key articles to measure content ROI:

| Action | Purpose |
|--------|---------|
| **Event per CTA** | e.g., `cta_click` with `content_url`, `content_type` |
| **Conversion** | Mark as conversion in GA4 for attribution |
| **Use** | Compare high vs low performers; optimize CTA placement and copy |

See **seo-monitoring** for article database and benchmark context.

## Infrastructure Requirements

| Component | Purpose |
|-----------|---------|
| **Data warehouse** | Centralized data; BI reporting |
| **Event tracking** | User behavior; funnel mapping |
| **Attribution** | Ad pixels; attribution model; impression-to-sale tracking |

**Optimization flow**: Clean UTM + conversion events → attribution reports → optimize channel mix.

## Scope

- **GA4**: Web data stream, gtag.js, configuration
- **User ID**: Cross-device, cross-session identification
- **CTA attribution**: Per-article conversion tracking for content ROI
- **Events**: Recommended and custom events
- **Conversions**: Key events, parameters
- **Quality**: Naming, testing, validation

## GA4 Setup

### Prerequisites

- Google Analytics property and web data stream
- Google tag (gtag.js) on all pages
- Measurement ID (e.g., `G-XXXXXXXXXX`)

### Enhanced Measurement

Enable in Admin > Data Streams > Enhanced Measurement for automatic tracking of:

- Page views, scrolls, outbound clicks
- Site search, file downloads
- Video engagement (YouTube)

## Event Tracking

### Event Types

| Type | Description |
|------|-------------|
| **Automatically collected** | page_view, first_visit, session_start |
| **Enhanced measurement** | scroll, click, file_download, etc. |
| **Recommended** | purchase, sign_up, search, etc. |
| **Custom** | Business-specific actions |

### Naming Conventions

- **Length**: <=40 characters (GA4 hard limit; longer names are not logged)
- **Format**: `snake_case`, lowercase
- **Verb first**: `download_pdf`, `submit_form`, `video_play`
- **Context**: `pricing_page_scroll` vs generic `scroll`

### gtag.js Syntax

```javascript
gtag('event', '<event_name>', {
  <parameter_name>: <value>,
  // e.g. value: 99.99, currency: 'USD'
});
```

Place below the Google tag snippet. Events fire on page load or user action (e.g., button click).

### Recommended Events

| Event | Use | Key Parameters |
|-------|-----|----------------|
| `purchase` | E-commerce | value, currency, items |
| `sign_up` | Registration | method |
| `login` | Login | method |
| `search` | Site search | search_term |
| `view_item` | Product view | items |
| `add_to_cart` | Add to cart | items |

### Custom Events

- Focus on 15-25 meaningful events aligned with KPIs
- Add parameters for context (e.g., `content_type`, `item_id`)
- Avoid tracking everything; prioritize quality over quantity

## Conversions (Key Events)

- Mark important events as conversions in GA4 Admin
- Use for attribution, audiences, and reporting
- Typical: purchase, sign_up, lead, contact

## Attribution & Conversion Optimization

Attribution models determine how conversion credit is assigned across touchpoints. Use attribution data to optimize ads and growth channels.

| Model | Use |
|-------|-----|
| **Data-driven** (GA4 default) | ML assigns credit by actual contribution; best for multi-touch journeys |
| **Last-click** | 100% to final touchpoint; simple but undervalues awareness/consideration |

**Optimization flow**: Clean UTM (source, medium, campaign) + conversion events → GA4 attribution reports → compare channels by attributed conversions → reallocate budget to ads/channels that drive results. Inconsistent UTM fragments data; multi-touch attribution requires reliable touchpoint data.

**Reference**: [UTM.io – UTMs for Marketing Attribution](https://web.utm.io/blog/utms-for-marketing-attribution/), [GA4 – Get started with attribution](https://support.google.com/analytics/answer/10596866)

## Testing & Validation

| Tool | Use |
|------|-----|
| **Realtime** | See events as they fire |
| **DebugView** | Detailed event/parameter inspection; requires debug mode |
| **GA4 Debug mode** | `gtag('config', 'G-XXX', { 'debug_mode': true });` or GTM preview |

- Test before launch; verify parameters and naming
- Check for duplicate events, missing values

## Output Format

- **Event list** (name, trigger, parameters)
- **Implementation** notes (gtag or GTM)
- **Conversion** mapping
- **Testing** checklist

## Related Skills

- **traffic-analysis**: UTM, source attribution; attribution for channel optimization
- **ai-traffic-tracking**: AI traffic in GA4
- **google-search-console**: GSC analysis (correlate with GA4)
- **seo-monitoring**: Article database, benchmark, full SEO monitoring framework
