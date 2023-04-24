from abc import ABCMeta
from abc import abstractmethod
import pandas as pd

from crypto_backtest_system.api.strategy.strategy import Strategy


class Strategy(Strategy):
    def __init__(
            self,
            name: str,
            coin_extractor: CoinExtractor,
            stoploss: StoplossRule,
            trading_rule: TradingRule,
    ):
        self._name = name
        self._coin_extractor = coin_extractor
        self._stoploss_rule = stoploss_rule
        self._trading_rule = trading_rule
        self._parameter_space = self._get_parameter_space()

    @abstractmethod
    def get_positions(self, price_data: pd.DataFrame) -> pd.Series:
        positions_df = price_data.copy()
        for parameters in self._parameter_space:
            coin_parameter = self._get_coin_extractor_parameters(parameters)
            trading_rule_parameter = self._get_trading_rule_parameters(parameters)
            stoploss_rule_parameter = self._get_stoploss_rule_parameters(parameters)
            coins = self._coin_extractor.get_coins(positions_df, coin_parameter)
            positions_df = self._trading_rule.get_positions(positions_df, coins, trading_rule_parameter)
            positions_df = self._stoploss_rule.adjust_positions(positions_df, stoploss_rule_parameter)
        return positions_df
