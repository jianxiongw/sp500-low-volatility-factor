import numpy as np
import pandas as pd

from src.returns import compute_monthly_returns

def run_low_high_vol_backtest(
    prices: pd.DataFrame,
    vol: pd.DataFrame,
    quantile: float = 0.2
) -> pd.DataFrame:
    """
    Run a long-only low-vol and high-vol backtest with monthly rebalancing.

    Parameters
    ----------
    prices : pd.DataFrame
        Daily adjusted close prices.
    vol : pd.DataFrame
        Daily annualized volatility (same index/columns as prices).
    quantile : float
        Quantile for low/high portfolios (e.g., 0.2 -> 20%).

    Returns
    -------
    portfolio_returns : pd.DataFrame
        Monthly returns of low-vol and high-vol portfolios with columns ['low_vol', 'high_vol'].
    """
    # 1. Monthly returns from daily prices (month-end)
    month_end_prices = prices.resample("ME").last()
    monthly_returns = month_end_prices.pct_change()

    # 2. Align volatility to month-end (rebalance dates)
    month_end_vol = vol.resample("ME").last()

    portfolio_dates = []
    low_vol_rets = []
    high_vol_rets = []

    for date in month_end_vol.index:
        vols_t = month_end_vol.loc[date]

        # Only keep tickers that have both vol and next-month return
        if date not in monthly_returns.index:
            continue

        rets_next = monthly_returns.loc[date]

        # Drop NaNs
        combined = pd.concat([vols_t, rets_next], axis=1, keys=["vol", "ret"]).dropna()
        if combined.empty:
            continue

        vols_clean = combined["vol"]
        rets_clean = combined["ret"]

        # Determine quantile cutoffs
        low_cut = vols_clean.quantile(quantile)
        high_cut = vols_clean.quantile(1 - quantile)

        low_names = vols_clean[vols_clean <= low_cut].index
        high_names = vols_clean[vols_clean >= high_cut].index

        if len(low_names) > 0:
            low_ret = rets_clean.loc[low_names].mean()
        else:
            low_ret = np.nan

        if len(high_names) > 0:
            high_ret = rets_clean.loc[high_names].mean()
        else:
            high_ret = np.nan

        portfolio_dates.append(date)
        low_vol_rets.append(low_ret)
        high_vol_rets.append(high_ret)

    portfolio_returns = pd.DataFrame(
        {
            "low_vol": low_vol_rets,
            "high_vol": high_vol_rets,
        },
        index=portfolio_dates,
    )

    return portfolio_returns