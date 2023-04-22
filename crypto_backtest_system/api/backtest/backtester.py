from abc import ABCMeta
from abc import abstractmethod
import pandas as pd

from api.strategy.strategy import Strategy


class Backtester(metaclass=ABCMeta):
    @abstractmethod
    def run(self, price_data: pd.DataFrame, strategy: Strategy) -> None:
        pass
