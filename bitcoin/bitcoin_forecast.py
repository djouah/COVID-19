import argparse
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


def download_close_prices(start_date: str = "2020-01-01") -> pd.Series:
    """Download daily closing prices for Bitcoin from Yahoo Finance."""
    data = yf.download("BTC-USD", start=start_date)
    if "Close" not in data:
        raise ValueError("Unexpected data format: 'Close' column missing")
    return data["Close"]


def forecast_prices(series: pd.Series, steps: int = 30) -> pd.Series:
    """Fit an ARIMA model and forecast future prices."""
    model = ARIMA(series, order=(5, 1, 0))
    fitted = model.fit()
    forecast = fitted.forecast(steps=steps)
    # Align forecast index to continue from series end
    forecast.index = pd.date_range(series.index[-1] + pd.Timedelta(days=1),
                                   periods=steps, freq="D")
    return forecast


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Forecast Bitcoin closing prices using an ARIMA model"
    )
    parser.add_argument("--start", default="2020-01-01",
                        help="Historical data start date (YYYY-MM-DD)")
    parser.add_argument("--steps", type=int, default=30,
                        help="Number of days to forecast")
    parser.add_argument("--plot", action="store_true",
                        help="Plot historical and forecast data")
    args = parser.parse_args()

    prices = download_close_prices(args.start)
    forecast = forecast_prices(prices, args.steps)
    print(forecast)

    if args.plot:
        plt.figure(figsize=(10, 5))
        prices.plot(label="Historical")
        forecast.plot(label="Forecast")
        plt.legend()
        plt.title("Bitcoin Price Forecast")
        plt.ylabel("USD")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
