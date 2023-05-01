from itertools import product
import pandas as pd

from crypto_backtest_system.backtest.backtester import Backtester
from crypto_backtest_system.services.strategy_service import StrategyService
from crypto_backtest_system.services.historical_data_service import HistoricalDataService
from crypto_backtest_system.config.config import Config


class BacktestSystem:
    def __init__(self, config: Config):
        self._config = config
        self._init_configs()
        self._price_data_parameters = product(
            self._start_times,
            self._end_times,
            self._frequencies
        )
        self._path_to_result_files = self._config.path_to_result_files

        self._historical_data_service = HistoricalDataService()
        self._strategy_service = StrategyService()
        self._backtester = Backtester(
            self._historical_data_service,
            self._strategy_service
        )
        self._metric_calculator = MetricCalculator()
        self._strategies = self._strategy_service.get_strategies()
        self._strategies_list = self._strategy_service.list_strategies()

    def _init_configs(self) -> None:
        self._start_times = self._config.start_times
        self._end_times = self._config.end_times
        self._frequencies = self._config.frequencies

    def _save_result(self, result: pd.DataFrame, strategy_name: str) -> None:
        result.to_csv(f"{self._path_to_result_files}/{strategy_name}.csv")

    def run(self) -> None:
        for price_data_parameter in self._price_data_parameters:
            historical_data = self._historical_data_service.get_price_data(
                start_time = price_data_parameter[0],
                end_time = price_data_parameter[1],
                frequency = price_data_parameter[2]
            )
            result = self._backtester.run(historical_data)
            result_metrics = self._metric_calculator.get_result_metrics(historical_data, result)
            self._save_result(result_metrics)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config = Config()
    backtest = BacktestSystem(config)
    backtest.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
