#!/usr/bin/env python3
"""
Generate keyword or competitor reports from JSON data and Markdown templates.

Usage:
  python generate-report.py --type keyword --data keyword-data.json --output report.md
  python generate-report.py --type competitor --data competitor-data.json --output report.md

Data format: See tools/data/*.example.json
"""

import argparse
import json
from datetime import datetime
from pathlib import Path


def load_template(template_dir: Path, report_type: str) -> str:
    """Load report template from templates/ directory."""
    template_path = template_dir / f"{report_type}-report.md"
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    return template_path.read_text(encoding="utf-8")


def load_data(data_path: Path) -> dict:
    """Load JSON data file."""
    with open(data_path, encoding="utf-8") as f:
        return json.load(f)


def format_table_rows(rows, columns):
    """Convert list of dicts to Markdown table rows."""
    if not rows:
        return "| (none) |"
    lines = []
    for row in rows:
        cells = [str(row.get(col, "")) for col in columns]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def render_keyword_report(template, data):
    """Fill keyword report template with data."""
    replacements = {
        "{{date}}": data.get("date", datetime.now().strftime("%Y-%m-%d")),
        "{{project_name}}": data.get("project_name", "Project"),
        "{{scope}}": data.get("scope", "SEO keywords"),
        "{{executive_summary}}": data.get("executive_summary", ""),
        "{{priority_1}}": data.get("priorities", [""] * 3)[0],
        "{{priority_2}}": data.get("priorities", [""] * 3)[1],
        "{{priority_3}}": data.get("priorities", [""] * 3)[2],
        "{{total_keywords}}": str(data.get("total_keywords", 0)),
        "{{primary_intent}}": data.get("primary_intent", "Informational"),
        "{{avg_difficulty}}": str(data.get("avg_difficulty", "")),
        "{{content_gaps_count}}": str(data.get("content_gaps_count", 0)),
    }

    keywords = data.get("keywords", [])
    replacements["{{keyword_rows}}"] = format_table_rows(
        keywords,
        ["keyword", "volume", "kd", "intent", "priority", "target_page"],
    )

    mapping = data.get("keyword_mapping", [])
    replacements["{{mapping_rows}}"] = format_table_rows(
        mapping,
        ["page", "keywords", "status"],
    )

    gaps = data.get("content_gaps", [])
    replacements["{{gap_rows}}"] = format_table_rows(
        gaps,
        ["keyword", "volume", "competitor", "opportunity"],
    )

    actions = data.get("action_plan", [])
    replacements["{{action_rows}}"] = format_table_rows(
        actions,
        ["priority", "action", "impact", "effort"],
    )

    result = template
    for k, v in replacements.items():
        result = result.replace(k, v)
    return result


def render_competitor_report(template, data):
    """Fill competitor report template with data."""
    competitors = data.get("competitors", [])
    comp_names = [c.get("name", "") for c in competitors[:2]]

    replacements = {
        "{{date}}": data.get("date", datetime.now().strftime("%Y-%m-%d")),
        "{{project_name}}": data.get("project_name", "Project"),
        "{{competitor_count}}": str(len(competitors)),
        "{{executive_summary}}": data.get("executive_summary", ""),
        "{{finding_1}}": data.get("findings", [""] * 3)[0],
        "{{finding_2}}": data.get("findings", [""] * 3)[1],
        "{{finding_3}}": data.get("findings", [""] * 3)[2],
        "{{recommendation_1}}": data.get("recommendations", [""] * 3)[0],
        "{{recommendation_2}}": data.get("recommendations", [""] * 3)[1],
        "{{recommendation_3}}": data.get("recommendations", [""] * 3)[2],
        "{{competitor_1}}": comp_names[0] if len(comp_names) > 0 else "Competitor A",
        "{{competitor_2}}": comp_names[1] if len(comp_names) > 1 else "Competitor B",
        "{{our_strengths}}": data.get("our_strengths", ""),
        "{{our_weaknesses}}": data.get("our_weaknesses", ""),
        "{{our_opportunities}}": data.get("our_opportunities", ""),
        "{{our_threats}}": data.get("our_threats", ""),
    }

    replacements["{{competitor_overview_rows}}"] = format_table_rows(
        data.get("competitor_overview", []),
        ["name", "category", "position", "strength"],
    )

    replacements["{{comparison_rows}}"] = format_table_rows(
        data.get("product_comparison", []),
        ["feature", "us", "competitor_1", "competitor_2"],
    )

    replacements["{{marketing_rows}}"] = format_table_rows(
        data.get("marketing", []),
        ["competitor", "value_prop", "audience", "channels"],
    )

    replacements["{{gap_rows}}"] = format_table_rows(
        data.get("gaps", []),
        ["gap", "opportunity", "priority"],
    )

    replacements["{{recommendation_rows}}"] = format_table_rows(
        data.get("recommendation_list", []),
        ["num", "recommendation", "impact", "effort", "owner"],
    )

    replacements["{{competitor_swot_section}}"] = data.get(
        "competitor_swot_section",
        "*(Add competitor SWOT details)*",
    )

    result = template
    for k, v in replacements.items():
        result = result.replace(k, str(v))
    return result


def main():
    parser = argparse.ArgumentParser(description="Generate marketing reports from JSON data")
    parser.add_argument("--type", choices=["keyword", "competitor"], required=True)
    parser.add_argument("--data", type=Path, required=True, help="Path to JSON data file")
    parser.add_argument("--output", type=Path, required=True, help="Output report path")
    parser.add_argument(
        "--templates",
        type=Path,
        default=Path(__file__).parent.parent / "templates",
        help="Path to templates directory",
    )
    args = parser.parse_args()

    template = load_template(args.templates, args.type)
    data = load_data(args.data)

    if args.type == "keyword":
        report = render_keyword_report(template, data)
    else:
        report = render_competitor_report(template, data)

    args.output.write_text(report, encoding="utf-8")
    print(f"Report written to {args.output}")


if __name__ == "__main__":
    main()
