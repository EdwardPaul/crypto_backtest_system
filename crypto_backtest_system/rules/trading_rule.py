import pandas as pd

from crypto_backtest_system.api.rules.trading_rule import TradingRule
from crypto_backtest_system.models.strategy_config import StrategyConfig


class TradingRule(TradingRule):
    def __init__(self, configs: list[StrategyConfig]):
        self._configs = configs

    def get_positions(self, positions_df: pd.DataFrame, coins: list[str]) -> pd.DataFrame:
        raise NotImplementedError
