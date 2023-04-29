import pandas as pd

from crypto_backtest_system.api.repositories.strategy_config_repository import StrategyConfigRepository


class StrategyConfigCsvRepository(StrategyConfigRepository):
    def __init__(self, strategy_config: pd.DataFrame):
        self._strategy_config = strategy_config

    def get_strategy_configs(self) -> pd.DataFrame:
        return self._strategy_config
    