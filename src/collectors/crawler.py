#!/usr/bin/env python
"""Radar-alerts crawler.

Ingests publicly available data and writes JSON snapshots that the static
GitHub Pages site renders. No backend is deployed — collection runs as a
scheduled GitHub Actions job (`collect.yml`) and commits the snapshots.

Snapshot layout (mirrors the static site's data dir):

    <out_dir>/markets/movements.json
    <out_dir>/news/brazil.json
    <out_dir>/news/tech.json
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

CATEGORIES = {
    "markets": "markets/movements.json",
    "news-brazil": "news/brazil.json",
    "news-tech": "news/tech.json",
}


def collect(category: str) -> list[dict]:
    """Return the raw collected items for a category.

    The actual per-site scraping is follow-up work; this returns an empty
    collection so the snapshot pipeline is real and the site degrades
    gracefully before collectors land.
    """
    return []


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="src/data/snapshots", help="snapshot output dir")
    args = parser.parse_args()

    out_dir = Path(args.out)
    for category, rel_path in CATEGORIES.items():
        snapshot = {
            "category": category,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "items": collect(category),
        }
        target = out_dir / rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(snapshot, indent=2) + "\n")
        print(f"wrote {target}")


if __name__ == "__main__":
    main()
