from abc import ABCMeta
from abc import abstractmethod

import pandas as pd


class StrategyConfigRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_strategy_configs(self) -> pd.DataFrame:
        pass
