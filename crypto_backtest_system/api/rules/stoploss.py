from abc import ABCMeta
from abc import abstractmethod

import pandas as pd


class Stoploss(metaclass=ABCMeta):
    @abstractmethod
    def adjust_positions(self, positions_df: pd.DataFrame) -> pd.DataFrame:
        pass
