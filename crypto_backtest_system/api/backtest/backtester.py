from abc import ABCMeta
from abc import abstractmethod
import pandas as pd


class Backtester(metaclass=ABCMeta):
    @abstractmethod
    def run(self, price_data: pd.DataFrame) -> dict[str, pd.DataFrame]:
        pass
