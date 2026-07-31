from src.data_loader import load_prices

def main():
    tickers = ["AAPL", "MSFT", "GOOGL"]
    prices = load_prices(tickers, "2021-01-01", "2026-01-01")
    print(prices.shape)
    print(prices.head())

if __name__ == "__main__":
    main()