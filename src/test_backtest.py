from src.data_loader import load_prices
from src.factor import compute_vol_factor
from src.backtest import run_low_high_vol_backtest

def main():
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]
    prices = load_prices(tickers, "2021-01-01", "2026-01-01")
    vol = compute_vol_factor(prices, window=60)

    portfolio_returns = run_low_high_vol_backtest(prices, vol, quantile=0.2)

    print("Portfolio returns shape:", portfolio_returns.shape)
    print(portfolio_returns.head())
    print(portfolio_returns.describe())

if __name__ == "__main__":
    main()