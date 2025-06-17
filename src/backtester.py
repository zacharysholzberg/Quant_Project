import pandas as pd
from strategy import MeanReversionStrategy
from portfolio import Portfolio

class backtester:
    def __init__(self, start_date, portfolio_size = 100000, short_window=5, long_window=20, num_std=2):
        self.portfolio_size = portfolio_size
        self.start_date = start_date
        self.short_window = short_window
        self.long_window = long_window

    def run_backtest(self, data: pd.DataFrame, strategy_type: str = "zscore_signals") -> pd.DataFrame:
        strategy = MeanReversionStrategy(self.short_window, self.long_window, self.num_std)
        signals = None

        #if self.start_date < less than availabe date
        #    raise ValueError("Start date is earlier than available data") 

        if strategy_type == "zscore":
            signals = strategy.zscore_signals(data)
        elif strategy_type == "bollinger":
            signals = strategy.bollinger_band_signals(data)
        elif strategy_type == "rolling":
            signals = strategy.rolling_mean_signals(data)

        if signals is None:
            print("Please choose: zscore | bollinger | rolling")
            raise ValueError("Unknown strategy type provided.")

        portfolio = Portfolio()
        results = portfolio.backtest_portfolio(signals)

        return results