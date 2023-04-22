from api.services.strategy_service import StrategyService
from api.strategy.strategy import Strategy


class StrategyService(StrategyService):
    def __init__(
            self,
            strategy_config_repository: StrategyConfigRepository,
    ):
        self._strategy_config_repository = strategy_config_repository
        self._strategy_configs = self._strategy_config_repository.get_strategy_configs()

    def get_strategies(self) -> list[Strategy]:
        strategies = []


    def _get_strategies(self):
        strategies = []
        strategy_names = self._extract_strategy_names()
        



