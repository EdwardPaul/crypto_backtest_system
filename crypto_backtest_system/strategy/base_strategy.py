import pandas as pd

from crypto_backtest_system.api.strategy.strategy import Strategy
from crypto_backtest_system.api.rules.trading_rule import TradingRule
from crypto_backtest_system.api.rules.coin_extractor import CoinExtractor
from crypto_backtest_system.api.rules.stoploss import Stoploss


class Strategy(Strategy):
    def __init__(
            self,
            name: str,
            coin_extractor: CoinExtractor,
            stoploss: Stoploss,
            trading_rule: TradingRule,
    ):
        self._name = name
        self._coin_extractor = coin_extractor
        self._stoploss_rule = stoploss
        self._trading_rule = trading_rule

    def get_positions(self, price_data: pd.DataFrame) -> pd.DataFrame:
        positions_df = price_data.copy()
        coins = self._coin_extractor.get_coins(positions_df)
        positions_df = self._trading_rule.get_positions(positions_df, coins)
        positions_df = self._stoploss_rule.adjust_positions(positions_df)
        return positions_df
