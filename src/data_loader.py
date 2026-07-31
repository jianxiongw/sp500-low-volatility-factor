import pandas as pd
import yfinance as yf

def load_prices(tickers, start_date, end_date):
    """
    Load daily adjusted close prices for given tickers between start_date and end_date.
    """
    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        auto_adjust=False,
        progress=False,
    )
    prices = data["Adj Close"]
    prices = prices.dropna(how="all")
    return prices