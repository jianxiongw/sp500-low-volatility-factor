import numpy as np
import pandas as pd

def compute_vol_factor(prices: pd.DataFrame, window: int = 60) -> pd.DataFrame:
    """
    Compute annualized realized volatility over a rolling window of daily log returns.

    Parameters
    ----------
    prices : pd.DataFrame
        DataFrame of adjusted close prices with dates as index and tickers as columns.
    window : int
        Rolling window length in trading days (default 60).

    Returns
    -------
    vol : pd.DataFrame
        DataFrame of annualized realized volatility with same shape as prices.
    """
    # 1. Compute daily log returns
    log_prices = np.log(prices)
    log_returns = log_prices.diff()

    # 2. Rolling standard deviation over 'window' days
    rolling_std = log_returns.rolling(window=window, min_periods=window).std()

    # 3. Annualize: multiply by sqrt(252)
    vol = rolling_std * np.sqrt(252)

    return vol