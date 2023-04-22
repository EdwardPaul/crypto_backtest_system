from abc import ABCMeta
from abc import abstractmethod

import pandas as pd


class BaseStrategy(metaclass=ABCMeta):
    @abstractmethod
    def get_positions(self) -> pd.Series:
        pass