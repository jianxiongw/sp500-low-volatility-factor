from src.data_loader import load_prices
from src.factor import compute_vol_factor

def main():
    tickers = ["AAPL", "MSFT", "GOOGL"]
    prices = load_prices(tickers, "2021-01-01", "2026-01-01")

    vol = compute_vol_factor(prices, window=60)

    print("Prices shape:", prices.shape)
    print("Vol shape:", vol.shape)
    print(vol.tail())

if __name__ == "__main__":
    main()