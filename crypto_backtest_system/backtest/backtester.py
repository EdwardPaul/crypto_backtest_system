import pandas as pd

from crypto_backtest_system.api.backtest.backtester import Backtester
from crypto_backtest_system.api.strategy.strategy import Strategy


class Backtester(Backtester):
    def __init__(self):
        pass

    def run(self, price_data: pd.DataFrame, strategy: Strategy) -> pd.DataFrame:
        positions = strategy.get_positions(price_data)
        return positions


