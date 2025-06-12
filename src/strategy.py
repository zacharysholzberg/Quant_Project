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
        df = data.copy()
        df['mean'] = self.long_sma.SMACalculator(df)
        df['std'] = data['close'].rolling(self.long_window).std()
        df['upper'] = df['mean'] + self.num_std * df['std']
        df['lower'] = df['mean'] - self.num_std * df['std']
        df['signal'] = 0
        df.loc[df['close'] <= df['lower'], 'signal'] = 1 #buy signal
        df.loc[df['close'] >= df['upper'], 'signal'] = -1 #sell signal
        print("Z-score range:", df['lower'].min(), df['upper'].max())
        print(df['signal'].value_counts())
        return df.dropna()
    
    def zscore_signals(self, data: pd.DataFrame, num_zScore = 1.5) -> pd.DataFrame:
        df = data.copy()
        df['mean'] = self.long_sma.SMACalculator(df)
        df['std'] = data['close'].rolling(self.long_window).std()
        df['zscore'] = (df['close']-df['mean'])/df['std']
        df['signal'] = 0
        df.loc[df['zscore'] <= -num_zScore, 'signal'] = 1 #buy signal
        df.loc[df['zscore'] >= num_zScore, 'signal'] = -1 #sell signal
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