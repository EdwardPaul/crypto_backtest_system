import pandas as pd

from crypto_backtest_system.api.rules.stoploss import Stoploss
from crypto_backtest_system.models.strategy_config import StrategyConfig


class Stoploss(Stoploss):
    def __init__(self, configs: StrategyConfig):
        self._configs = configs

    def adjust_positions(self, positions_df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError
