import pandas as pd

from crypto_backtest_system.api.backtest.backtester import Backtester
from crypto_backtest_system.api.strategy.strategy import Strategy
from crypto_backtest_system.api.services.strategy_service import StrategyService
from crypto_backtest_system.api.services.historical_data_service import HistoricalDataService


class Backtester(Backtester):
    def __init__(
        self,
        strategy_service: StrategyService,
        historical_data_service: HistoricalDataService
    ):
        self._strategy_service = strategy_service
        self._historical_data_service = historical_data_service
        self._strategies_list = self._strategy_service.list_strategies()

    def run(self, price_data: pd.DataFrame) -> dict[str, pd.DataFrame]:
        positions_dict = dict()
        for strategy_name in self._strategies_list:
            strategy = self._strategy_service.get_strategy_by_name(strategy_name)
            positions = strategy.get_positions(price_data)
            positions_dict[strategy_name] = positions
        return positions_dict


