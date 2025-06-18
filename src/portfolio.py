import pandas as pd
import numpy as np

class Portfolio:
    def __init__(self, start_date: str, portfolio_size = 100000):
        self.start_date = start_date
        self.portfolio_size = portfolio_size

    def backtest_portfolio(self, signals: pd.DataFrame) -> pd.DataFrame:
        df = signals.copy()
        #df['position'] = df['signal'].replace(0, np.nan).ffill().shift(1)
        df['position'] = df['signal'].shift(1)
        df['returns'] = df['close'].pct_change()
        df['strategy_returns'] = df['returns'] * df['position']

        df.dropna(subset=['returns', 'position'], inplace=True)

        df['cum_returns'] = (1 + df['returns']).cumprod()
        df['cum_strategy_returns'] = (1 + df['strategy_returns']).cumprod()

        return df.dropna()