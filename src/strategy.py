import pandas as pd


class SMAIndicator:
    def __init__(self, window: int):
        self.window = window

    def SMACalculator(self, data: pd.DataFrame):
        return data['close'].rolling(self.window).mean() #pd.series returned
    
class MeanReversionStrategy:
    def __init__(self, short_window=5, long_window=20, num_std = 2):
        self.short_sma = SMAIndicator(short_window)
        self.long_sma = SMAIndicator(long_window)
        self.num_std = num_std
        self.long_window = long_window

    def bollinger_band_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        return
    
    def zscore_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        df = data.copy()
        df['mean'] = self.long_sma.SMACalculator(df)
        df['std'] = data['close'].rolling(self.long_window).std()
        df['zscore'] = (df['close']-df['mean'])/df['std']
        df['signal'] = 0
        df.loc[df['zscore'] < -self.num_std, 'signal'] = 1 #buy signal
        df.loc[df['zscore'] > self.num_std, 'signal'] = -1 #sell signal
        print("Z-score range:", df['zscore'].min(), df['zscore'].max())
        print(df['signal'].value_counts())
        return df.dropna()
    
    def rolling_mean_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        df = data.copy()
        df['sma_short'] = self.short_sma.SMACalculator(df)
        df['sma_long'] = self.long_sma.SMACalculator(df)
        df['signal'] = 0
        df.loc[df['sma_short'] < df['sma_long'], 'signal'] = 1 #buy signal
        df.loc[df['sma_short'] > df['sma_long'], 'signal'] = -1 #sell signal
        
        return df.dropna()