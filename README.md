# QUANT_LAB
## Stock Collector — *Planting the Seed*
*A first step into quantitative finance*

---

### Data.

Data is the foundation of every analysis, every decision. It is data that moves the world and the agents within it. The starting point of every decision, every movement, every impulse, lies in data — and in the information we build from it.

Every system — financial, natural, social — feeds on information to operate. In this first phase of the project, we start at the beginning: selection, collection, and storage.

---

### Architecture

The pipeline is composed of four modules operating in sequence, each with a single, well-defined responsibility:
```
api_client.py → transform.py → db_writer.py → PostgreSQL
                     ↑
          collector.py (orchestrator)
```

**`api_client.py`**
Receives a ticker and a valid period, queries Yahoo Finance via `yfinance`, and handles connection errors and timeouts. Returns a DataFrame with Open, High, Low, Close, Adj Close, and Volume.

**`transform.py`**
Prepares the DataFrame for insertion. Drops the `Dividends` and `Stock Splits` columns — redundant, since `Adj Close` already reflects their impact on price. Adds the `ticker` column, normalizes the datetime index by removing timezone info, and renames columns to `snake_case` to match the SQL table schema.

**`db_writer.py`**
Establishes the connection to PostgreSQL and writes data into the `stock_prices` table. Credentials are loaded from a `.env` file whose path is built dynamically. Insertion uses `ON CONFLICT DO NOTHING` to silently handle duplicates via the `UNIQUE (ticker, date)` constraint.

**`collector.py`**
Pipeline orchestrator. Uses `argparse` to receive ticker and period as command-line arguments and runs the three modules in sequence. It is the entry point of the system — the place from which everything flows.

---

### Usage
```bash
python collector.py <TICKER> <PERIOD>
```

Example:
```bash
python collector.py AAPL 1y
```

Valid periods: `1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max`

---

### Installation
```bash
git clone <repo-url>
cd quant_lab
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# fill in .env with your database credentials
```

---

### Security

Database credentials are managed via environment variables. The `.env` file is never committed to the repository — it is listed in `.gitignore`. A `.env.example` template is provided.

---

### Stack

- Python 3.12
- yfinance
- pandas
- psycopg2
- python-dotenv
- PostgreSQL

---

### Roadmap

This project is built with a systems thinking mindset — each version is a layer that builds on the previous one, forming a system that grows in complexity and capability organically.

- **v0.1 — Data pipeline ✅**
- **v0.2 — Feature engineering** — log returns, volatility, rolling stats, drawdown, z-score ✅
- **v0.3 — Quantitative analysis** — correlations, VaR, distributions, statistical tests
- **v0.4 — Visualization** — Matplotlib, Plotly, Power BI
- **v0.5 — Backtesting** — strategies, Sharpe ratio, max drawdown
- **v0.6 — Machine learning** — scikit-learn, time series
- **v0.7 — Simulations** — where systems theory will find its most concrete expression: Monte Carlo, GBM, agent-based models, market dynamics as complex systems

Cross-cutting layers across all versions: data validation, logging, config.yaml, multi-asset support.

**End goal:** a complete quantitative laboratory, comparable in structure to the research environments of investment funds.

---

*v0.1 — QUANT_LAB, 2026*
