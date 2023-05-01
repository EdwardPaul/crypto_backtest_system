from abc import ABCMeta
from abc import abstractmethod

import pandas as pd


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def get_positions(
            self,
            price_data: pd.DataFrame
    ) -> pd.DataFrame:
        pass
