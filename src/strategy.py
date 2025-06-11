import pandas as pd


class SMAIndicator:
    def __init__(self, window: int):
        self.window = window

    def SMACalculator(self, data: pd.DataFrame):
        print(type(data['close'].rolling(self.window).mean()))
        return data['close'].rolling(self.window).mean()
    
class MeanReversionStrategy:
    def __init__(self, short_window=5, long_window=20, num_std = 2):
        self.short_sma = SMAIndicator(short_window) #type is pd series
        self.long_sma = SMAIndicator(long_window) #type is pd series
        self.num_std = num_std
        self.long_window = long_window

    def bollinger_band_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        return
    
    def zscore_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        return
    
    def rolling_mean_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        df = data.copy()
        df['sma_short'] = self.short_sma.calculate(df)
        df['sma_long'] = self.long_sma.calculate(df)
        df['signal'] = 0
        df.loc[df['sma_short'] < df['sma_long'], 'signal'] = 1
        df.loc[df['sma_short'] > df['sma_long'], 'signal'] = -1
        
        return 