# analysis

Python analysis over the committed snapshots — the "data science" layer.

- **Stock market**: returns, moving averages, volatility, threshold events, correlations.
- **Lottery**: frequency/hot-cold, gaps/overdue, sum/parity/range distributions, pairs, prize & accumulation cycles, expected value. **Descriptive only — draws are independent; nothing here predicts future results.**
- **News**: volume/trends, keyword frequency, optional sentiment.

Reads `src/data/snapshots/`, writes derived series (e.g. `src/data/derived/`) for the UI.
