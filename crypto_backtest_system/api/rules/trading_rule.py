from abc import ABCMeta
from abc import abstractmethod

import pandas as pd


class TradingRule(metaclass=ABCMeta):
    @abstractmethod
    def get_positions(self, positions_df: pd.DataFrame, coins: list[str]) -> pd.DataFrame:
        pass
