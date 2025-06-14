# src/main.py

from data_loader import AlphaVantageDataLoader
from strategy import *
from utils import *

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key


def main():
    API_KEY = "BQCIW7GXBTH91G57"

    #AAPL_loader = AlphaVantageDataLoader(api_key=API_KEY, symbol="AAPL", outputsize="full")
    #AAPL_df = AAPL_loader.fetch_data()
    #print(AAPL_df)
    #AAPL_loader.save_to_csv(AAPL_df)
    AAPL_df = read_data("AAPL_daily_data")

    #AAPL_indicator = SMAIndicator(window=80)
    #AAPL_SMA = AAPL_indicator.SMACalculator(AAPL_df)
    #print(AAPL_SMA)

    AAPL_reversion = MeanReversionStrategy(10, 20, 2.0)
    print(AAPL_reversion.bollinger_band_signals(AAPL_df))

    

if __name__ == "__main__":
    main()
