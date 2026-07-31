import pandas as pd
import numpy as np

import pandas as pd

def compute_monthly_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Compute simple monthly returns from daily prices.
    """
    month_end_prices = prices.resample("ME").last()
    monthly_returns = month_end_prices.pct_change()
    return monthly_returns