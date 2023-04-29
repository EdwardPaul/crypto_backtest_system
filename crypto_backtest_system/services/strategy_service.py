import pandas as pd

from crypto_backtest_system.api.strategy.strategy import Strategy
from crypto_backtest_system.strategy.strategies_list import strategies_list
from crypto_backtest_system.api.services.strategy_service import StrategyService
from crypto_backtest_system.api.repositories.strategy_config_repository import StrategyConfigRepository
from crypto_backtest_system.models.rule_type import RuleType
from crypto_backtest_system.models.strategy_config import StrategyConfig


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
            strategy = self.get_strategy_by_name(strategy_name)
            strategies.append(strategy)
        return strategies

    def list_strategies(self) -> list[str]:
        strategy_names = self._strategy_configs["Strategy Name"].unique()
        return strategy_names

    def get_strategy_by_name(self, strategy_name: str) -> Strategy:
        Strategy = strategies_list[strategy_name]
        strategy_configs = self._strategy_configs[
            self._strategy_configs["Strategy Name"] == strategy_name
        ]
        coin_extractor_configs = self._filter_configs_by_rule_type(
            strategy_configs,
            strategy_name,
            RuleType.COIN_EXTRACTOR
        )
        trading_rule_configs = self._filter_configs_by_rule_type(
            strategy_configs,
            strategy_name,
            RuleType.TRADING_RULE
        )
        stoploss_configs = self._filter_configs_by_rule_type(
            strategy_configs,
            strategy_name,
            RuleType.STOPLOSS
        )
        coin_extractor = CoinExtractor(
            configs=coin_extractor_configs
        )
        trading_rule = TradingRule(
            configs=trading_rule_configs
        )
        stoploss = Stoploss(
            configs=stoploss_configs
        )
        result_strategy = Strategy(
            name = strategy_name,
            coin_extractor=coin_extractor,
            trading_rule=trading_rule,
            stoploss=stoploss
        )
        return result_strategy

    def _filter_configs_by_rule_type(
        self,
        strategy_configs: list[StrategyConfig],
        strategy_name: str,
        rule_type: RuleType
    ) -> list[StrategyConfig]:
        result = list(filter(
            lambda x: x.strategy_name == strategy_name and x.rule_type == rule_type,
            self._strategy_configs
        ))
        return result

