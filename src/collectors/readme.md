# collectors

Python collectors — ingest publicly available data (stock market, lottery, news) and write JSON snapshots consumed by the static GitHub Pages site.

- Stock market: B3 quotes, returns, thresholds.
- Lottery: Brazilian Caixa draws (Mega-Sena, Dupla Sena, +Milionária, …).
- News: Brazilian + tech sources.
- Output: `src/data/snapshots/<pillar>/...json` (committed by `collect.yml`).

Run locally:

```bash
python src/collectors/crawler.py --out src/data/snapshots
```
