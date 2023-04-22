from abc import ABCMeta
from abc import abstractmethod
import pandas as pd

from crypto_backtest_system.api.strategy.strategy import Strategy


class Strategy(Strategy):
    def __init__(
            self,
            coin_extractor: CoinExtractor,
            stoploss: StoplossRule,
            trading_rule: TradingRule,
    ):
        self._coin_extractor = coin_extractor
        self._stoploss_rule = stoploss_rule
        self._trading_rule = trading_rule

    @abstractmethod
    def get_positions(self, price_data: pd.DataFrame) -> pd.Series:
        positions_df = price_data.copy()
        coins = self._coin_extractor.get_coins(positions_df)
        positions_df = self._trading_rule.get_positions(positions_df, coins)
        positions_df = self._stoploss_rule.adjust_positions(positions_df)
        return positions_df
