from abc import ABCMeta
from abc import abstractmethod

from api.strategy.strategy import Strategy


class StrategyService(metaclass=ABCMeta):
    @abstractmethod
    def get_strategies(self) -> list[Strategy]:
        pass
