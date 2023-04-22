from crypto_backtest_system.api.services.strategy_service import StrategyService
from crypto_backtest_system.api.strategy.strategy import Strategy
from crypto_backtest_system.api.repositories.strategy_config_repository import StrategyConfigRepository
from crypto_backtest_system.strategy.strategies_list import strategies_list

class StrategyService(StrategyService):
    def __init__(
            self,
            strategy_config_repository: StrategyConfigRepository,
    ):
        self._strategy_config_repository = strategy_config_repository
        self._strategy_configs = self._strategy_config_repository.get_strategy_configs()

    def get_strategies(self) -> list[Strategy]:
        strategies = []
        strategy_names = self._extract_strategy_names()
        for strategy_name in strategy_names:
            strategy = self._get_strategy(strategy_name)
            strategies.append(strategy)
        return strategies

    def _extract_strategy_names(self) -> list[str]:
        raise NotImplementedError

    def _get_strategy(self, strategy_name: str) -> Strategy:
        return strategies_list[strategy_name]