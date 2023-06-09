from abc import ABCMeta
from abc import abstractmethod

from crypto_backtest_system.api.strategy.strategy import Strategy


class StrategyService(metaclass=ABCMeta):
    @abstractmethod
    def get_strategies(self) -> list[Strategy]:
        pass

    @abstractmethod
    def list_strategies(self) -> list[str]:
        pass

    @abstractmethod
    def get_strategy_by_name(self, strategy_name: str) -> Strategy:
        pass
