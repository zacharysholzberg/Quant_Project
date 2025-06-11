import pandas as pd


class SMAIndicator:
    def __init__(self, window: int):
        self.window = window

    def SMACalculator(self, data: pd.DataFrame):
        return data['close'].rolling(self.window).mean()