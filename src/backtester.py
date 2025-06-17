import pandas as pd
from strategy import MeanReversionStrategy
from portfolio import Portfolio

class Backtester:
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

        strategy_map = {
        "zscore": strategy.zscore_signals,
        "bollinger": strategy.bollinger_band_signals,
        "rolling": strategy.rolling_mean_signals
        }

        if strategy_type not in strategy_map:
            raise ValueError(f"Unknown strategy type: {strategy_type}")

        signals = strategy_map[strategy_type](data)

        portfolio = Portfolio()

        results = portfolio.backtest_portfolio(signals)

        return results