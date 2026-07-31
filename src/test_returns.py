from src.data_loader import load_prices
from src.returns import compute_monthly_returns

def main():
    tickers = ["AAPL", "MSFT", "GOOGL"]
    prices = load_prices(tickers, "2021-01-01", "2026-01-01")

    monthly_returns = compute_monthly_returns(prices)

    print("Daily prices shape:", prices.shape)
    print("Monthly returns shape:", monthly_returns.shape)
    print(monthly_returns.head())

if __name__ == "__main__":
    main()