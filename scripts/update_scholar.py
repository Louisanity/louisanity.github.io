#!/usr/bin/env python3
"""Update _data/scholar.yml from SerpAPI's Google Scholar Author endpoint.

Required environment variable:
  SERPAPI_KEY

The website remains static; GitHub Actions refreshes _data/scholar.yml.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

AUTHOR_ID = "KoUPm0MAAAAJ"
PROFILE_URL = f"https://scholar.google.com/citations?user={AUTHOR_ID}&hl=en"
OUT = Path("_data/scholar.yml")


def _require_key() -> str:
    key = os.environ.get("SERPAPI_KEY", "").strip()
    if not key:
        print("SERPAPI_KEY is not set; skipping Scholar update.")
        sys.exit(0)
    return key


def _fetch(api_key: str) -> dict:
    params = {
        "engine": "google_scholar_author",
        "author_id": AUTHOR_ID,
        "hl": "en",
        "api_key": api_key,
        "output": "json",
        "num": "100",
    }
    url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def _first_metric(table: list[dict], candidates: tuple[str, ...]) -> dict:
    for row in table:
        for key in candidates:
            if key in row:
                return row[key]
    return {"all": 0}


def _second_key(metric: dict) -> str:
    keys = [k for k in metric.keys() if k != "all"]
    return keys[0] if keys else "since_2021"


def _as_int(value) -> int:
    try:
        return int(str(value).replace(",", ""))
    except Exception:
        return 0


def _write_yaml(data: dict) -> None:
    cited_by = data.get("cited_by", {})
    table = cited_by.get("table", [])
    graph = cited_by.get("graph", [])

    citations = _first_metric(table, ("citations",))
    h_index = _first_metric(table, ("h_index", "indice_h", "h-index"))
    i10_index = _first_metric(table, ("i10_index", "indice_i10", "i10-index"))

    citations_since_key = _second_key(citations)
    h_since_key = _second_key(h_index)
    i10_since_key = _second_key(i10_index)

    current_year = _dt.date.today().year
    years = [str(year) for year in range(current_year - 4, current_year + 1)]
    yearly_citations = {year: 0 for year in years}

    for item in graph:
        year = str(_as_int(item.get("year")))
        cites = _as_int(item.get("citations"))
        if year in yearly_citations:
            yearly_citations[year] = cites

    chart_max = max(list(yearly_citations.values()) + [1])
    chart_max = int(((chart_max + 49) // 50) * 50)

    today = _dt.date.today().isoformat()
    lines = [
        "# Auto-generated Google Scholar metrics. Edit manually only if the updater is disabled.",
        f'profile_url: "{PROFILE_URL}"',
        f'author_id: "{AUTHOR_ID}"',
        f'last_updated: "{today}"',
        "metrics:",
        "  citations:",
        f"    all: {_as_int(citations.get('all'))}",
        f"    since_2021: {_as_int(citations.get(citations_since_key))}",
        "  h_index:",
        f"    all: {_as_int(h_index.get('all'))}",
        f"    since_2021: {_as_int(h_index.get(h_since_key))}",
        "  i10_index:",
        f"    all: {_as_int(i10_index.get('all'))}",
        f"    since_2021: {_as_int(i10_index.get(i10_since_key))}",
        f"chart_max: {chart_max}",
        "yearly_citations:",
    ]

    for year in years:
        lines.append(f'  "{year}": {yearly_citations[year]}')

    lines.append("yearly:")
    for year in years:
        lines.extend([f"  - year: {year}", f"    citations: {yearly_citations[year]}"])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    key = _require_key()
    data = _fetch(key)
    if data.get("error"):
        raise RuntimeError(data["error"])
    _write_yaml(data)
    print(f"Updated {OUT}")


if __name__ == "__main__":
    main()
