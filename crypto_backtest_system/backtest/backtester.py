import pandas as pd

from api.backtest.backtester import Backtester
from api.strategy.strategy import Strategy


class Backtester(Backtester):
    def __init__(self):
        pass

    def run(self, price_data: pd.DataFrame, strategy: Strategy) -> None:
        positions = strategy.get_positions(price_data)


