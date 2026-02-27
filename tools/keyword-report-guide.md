# Keyword Report Guide

Generate keyword research reports from uploaded Excel/CSV and web enrichment.

## Data Sources

- **Ahrefs** — Keywords Explorer, Site Explorer
- **SEMrush** — Keyword Overview, Organic Research
- **GSC** — Search queries, impressions, clicks
- **GA** — Traffic by landing page
- **PostHog** — Feature/search usage

## Workflow

1. **Parse** — Read Excel/CSV, infer keyword, volume, KD, intent, etc. from headers
2. **Enrich** — Web search, visit competitor/product pages; read `product-marketing-context.md` if present
3. **Build** — Use format from `tools/data/keyword-data.example.json`
4. **Generate** — Fill `templates/keyword-report.md` or run `python tools/generate-report.py --type keyword --data data.json --output report.md`
