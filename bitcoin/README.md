# Bitcoin Price Forecasting

This directory contains a simple script to forecast future Bitcoin closing prices using an ARIMA time series model. Historical price data is downloaded from Yahoo Finance with [`yfinance`](https://pypi.org/project/yfinance/).

## Requirements

The script depends on:

- `pandas`
- `numpy`
- `yfinance`
- `statsmodels`
- `matplotlib` (optional for plotting)

Install these packages with pip:

```bash
pip install pandas numpy yfinance statsmodels matplotlib
```

## Usage

Run the script from the repository root:

```bash
python bitcoin/bitcoin_forecast.py --start 2020-01-01 --steps 30 --plot
```

Arguments:

- `--start`: Start date (YYYY-MM-DD) for downloading historical data. Defaults to `2020-01-01`.
- `--steps`: Number of days to forecast ahead. Defaults to `30`.
- `--plot`: Display a plot of historical and forecast data.

The forecasted prices are printed to stdout and optionally plotted.
