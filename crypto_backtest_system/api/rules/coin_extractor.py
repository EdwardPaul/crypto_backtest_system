from abc import ABCMeta
from abc import abstractmethod

import pandas as pd


class CoinExtractor(metaclass=ABCMeta):
    @abstractmethod
    def get_coins(self, positions_df: pd.DataFrame) -> list[str]:
        pass
