# data-science

Collect public data → analyze it → static dashboard. Async collection only, no backend deployed. Collectors run on a schedule in GitHub Actions and commit JSON snapshots; the vanilla JS static site on GitHub Pages renders them as reports. Public, no auth, little interaction.

Three focus pillars:

- **Stock market** — B3 quotes: returns, moving averages, volatility, and threshold events (below/above 3% today, 5% week, 10% two weeks).
- **Lottery** — Brazilian Caixa draws (Mega-Sena, Dupla Sena, +Milionária, …): frequency, gaps, sums, pairs, prize/accumulation cycles. Descriptive statistics only — draws are independent.
- **News** — Brazil + tech headlines: volume, keyword trends, optional sentiment.

## Structure

```text
src/
  collectors/  Python collectors — ingest public data, write JSON snapshots
  analysis/    Python analysis — statistics/trends over the snapshots
  data/        curated rules + watchlists (seed) and snapshots/ (collector output)
  ui/          vanilla JS static pages → GitHub Pages
docs/
```

## Data sources

| Pillar | Source |
| --- | --- |
| Stock market | [`brapi.dev`](https://brapi.dev) (B3 quotes); Yahoo Finance (`*.SA`) as fallback |
| Lottery | [`loteriascaixa-api`](https://loteriascaixa-api.herokuapp.com/api) (full history) + official `servicebus2.caixa.gov.br` (increments) |
| News | RSS feeds |

## How it works

Scheduled GitHub Actions run the collectors → write `src/data/snapshots/` → the analysis pass derives stats → `pages.yml` rebuilds the static site from `src/ui/` + the data. No API, no database, no long-running services — everything is batch and static.

## Quick start

```bash
python src/collectors/crawler.py --out src/data/snapshots   # collect
python -m http.server -d src/ui                             # preview UI
```

See the issue backlog for the roadmap.
