# Competitor Report Guide

Generate competitor analysis reports from uploaded Excel/CSV and web enrichment.

## Data Sources

- **SimilarWeb** — Traffic, engagement, traffic sources by domain
- **Ahrefs** — Competitor domains, backlinks, DR
- **SEMrush** — Organic competitors, traffic share
- **GA** — Referral traffic, acquisition by source
- **PostHog** — Competitor feature usage (if tracked)

## Workflow

1. **Parse** — Read Excel/CSV, infer domain, visits, traffic sources, etc. from headers
2. **Enrich** — Web search, visit competitor sites; read `product-marketing-context.md` if present
3. **Build** — Use format from `tools/data/competitor-data.example.json`
4. **Generate** — Fill `templates/competitor-report.md` or run `python tools/generate-report.py --type competitor --data data.json --output report.md`
