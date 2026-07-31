# SP500-low-volatility-factor
S&amp;P 500 low volatility factor backtest

## Overview

This project implements and analyzes a simple low-volatility factor on S&P 500 stocks.

- Universe: selected S&P 500 names (test set: AAPL, MSFT, GOOGL, AMZN, META).
- Factor: 60-day rolling annualized realized volatility.
- Strategy: each month, rank stocks by volatility; build equal-weight portfolios of the 20% least volatile ("low vol") and 20% most volatile ("high vol") names.
- Backtest: monthly rebalanced, long-only low-vol and high-vol portfolios.

The code is structured into:
- `src/data_loader.py` for data ingestion,
- `src/factor.py` for volatility computation,
- `src/returns.py` and `src/backtest.py` for monthly returns and portfolio backtesting,
- `notebooks/01_explore_volatility.ipynb` for exploratory analysis and plots.
