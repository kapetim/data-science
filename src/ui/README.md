# ui

Vanilla JS static pages → GitHub Pages (public, no auth). Renders the collected snapshots as reports — little interaction, results only:

- `markets/` — movers (below/above thresholds).
- `news/` — brazil (crimes · politics · health) + tech (ai · hardware).
- `index.html` — home.

Data comes from `src/data/snapshots/` (served alongside the ui by `pages.yml`); no API calls.
