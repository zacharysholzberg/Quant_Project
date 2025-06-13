#src/data_loader.py

import pandas as pd
import requests
import os

class AlphaVantageDataLoader:
    def __init__(self, api_key: str, symbol: str, outputsize: str = "full"):
        self.api_key = api_key
        self.symbol = symbol
        self.outputsize = outputsize

    def _build_url(self) -> str:
        return (
            f"https://www.alphavantage.co/query?"
            f"function=TIME_SERIES_DAILY"
            f"&symbol={self.symbol}"
            f"&outputsize={self.outputsize}"
            f"&apikey={self.api_key}"
        )

    def fetch_data(self) -> pd.DataFrame:
        url = self._build_url()
        response = requests.get(url)
        data = response.json()

        if "Time Series (Daily)" not in data:
            raise ValueError(f"Unexpected response: {data}")

        ts_data = data["Time Series (Daily)"]
        df = pd.DataFrame.from_dict(ts_data, orient="index")
        df.columns = [col.split(". ")[1] for col in df.columns]  # clean columns
        df.index = pd.to_datetime(df.index)
        df = df.sort_index().astype(float)
        return df

    def save_to_csv(self, df: pd.DataFrame, filename: str = None):
        #if filename is None:
        #    filename = f"{self.symbol}_daily_data.csv"
        #df.to_csv(filename)
        #print(f"✅ Saved {self.symbol} daily stock data to: {filename}")

        if filename is None:
            filename = f"{self.symbol}_daily_data.csv"

        # Get the path to the parent directory of 'src'
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, "data")

        # Create 'data' directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)

        # Full path to save the CSV
        file_path = os.path.join(data_dir, filename)

        df.to_csv(file_path)
        print(f"✅ Saved {self.symbol} daily stock data to: {file_path}")