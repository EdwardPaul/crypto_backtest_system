import pandas as pd

from crypto_backtest_system.api.strategy.strategy import Strategy
from crypto_backtest_system.strategy.strategies_list import strategies_list
from crypto_backtest_system.api.services.strategy_service import StrategyService
from crypto_backtest_system.api.repositories.strategy_config_repository import StrategyConfigRepository

class StrategyService(StrategyService):
    def __init__(
            self,
            strategy_config_repository: StrategyConfigRepository,
    ):
        self._strategy_config_repository = strategy_config_repository
        self._strategy_configs = self._strategy_config_repository.get_strategy_configs()
        self._strategy_names = self._strategy_configs["Strategy Name"].unique()

    def get_strategies(self) -> list[Strategy]:
        strategies = []
        for strategy_name in self._strategy_names:
            strategy = self._get_strategy(strategy_name)
            strategies.append(strategy)
        return strategies

    def list_strategies(self) -> list[str]:
        strategy_names = self._strategy_configs["Strategy Name"].unique()
        return strategy_names

    def _get_strategy(self, strategy_name: str) -> Strategy:
        Strategy = strategies_list[strategy_name]
        strategy_configs = self._strategy_configs[
            self._strategy_configs["Strategy Name"] == strategy_name
        ]
        result_strategy = Strategy(
            name = strategy_name,
            parameters = strategy_configs
        )
        return result_strategy
