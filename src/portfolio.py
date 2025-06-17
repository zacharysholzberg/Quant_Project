import pandas as pd

class Portfolio:
    def __init__(self, start_date, portfolio_size):
        self.start_date = start_date
        self.portfolio_size = portfolio_size

    def backtest_portfolio(signals: pd.DataFrame) -> pd.DataFrame:
        df = signals.copy()

        return df.dropna()