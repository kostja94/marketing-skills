# Report Generation Tools

Generate keyword and competitor reports from uploaded Excel/CSV, enriched by web search and site visits.

**Templates** (output format): `templates/keyword-report.md`, `templates/competitor-report.md`  
**Guides** (how to generate): [keyword-report-guide.md](keyword-report-guide.md), [competitor-report-guide.md](competitor-report-guide.md)

## Workflow

1. **User uploads Excel** — Ahrefs, SimilarWeb, SEMrush, GA, GSC, PostHog, etc.
2. **Agent parses** — Reads sheets/columns, infers structure
3. **Agent enriches** — Web search, visit competitor sites
4. **Agent generates** — Fills template, writes output

## Data Sources by Report Type

| Keyword Report | Competitor Report |
|----------------|-------------------|
| Ahrefs, SEMrush, GSC, GA, PostHog | SimilarWeb, Ahrefs, SEMrush, GA, PostHog |

## Optional: generate-report.py

```bash
python tools/generate-report.py --type keyword --data data.json --output report.md
python tools/generate-report.py --type competitor --data data.json --output report.md
```

JSON format: `tools/data/*.example.json`
