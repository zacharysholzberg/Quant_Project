# src/main.py

from data_loader import AlphaVantageDataLoader
from strategy import *
#from strategy import sma_crossover_strategy
#from backtester import run_backtest
#from metrics import compute_metrics
#from alpha_vantage.timeseries import TimeSeries 
#import requests
#import pandas as pd

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key


def main():
    API_KEY = "BQCIW7GXBTH91G57"

    AAPL_loader = AlphaVantageDataLoader(api_key=API_KEY, symbol="AAPL", outputsize="full")
    AAPL_df = AAPL_loader.fetch_data()
    #AAPL_loader.save_to_csv(AAPL_df)

    AAPL_indicator = SMAIndicator(window=5)
    print(AAPL_indicator.SMACalculator(data=AAPL_df))



    

if __name__ == "__main__":
    main()
