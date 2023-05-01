from crypto_backtest_system.api.repositories.historical_data_repository import HistoricalDataRepository
from crypto_backtest_system.models.frequency import Frequency
from crypto_backtest_system.utils.const import FREQUENCY_TABLES

from typing import Optional
import pandas as pd
import datetime


class HistoricalDataCsvRepository(HistoricalDataRepository):
    def __init__(self, historical_data_path):
        self._historical_data_path = historical_data_path

    def get_historical_data_for_frequency(self, frequency: Frequency) -> pd.DataFrame:
        file_name = f"{FREQUENCY_TABLES[frequency.value]}.csv"
        historical_data_df = self._read_csv(file_name)
        return historical_data_df

    def get_data_for_coins(
            self,
            coins: list[str],
            start_date: Optional[datetime.datetime] = None,
            end_date: Optional[datetime.datetime] = None,
            frequency: Frequency = Frequency.ONE_DAY
    ) -> pd.DataFrame:
        historical_data_df = self.get_historical_data_for_frequency(frequency)
        coin_filter_condition = historical_data_df["symbol"] in coins
        date_condition = (
            (start_date <= datetime.datetime.strptime(historical_data_df["date"], "%Y-%m-%d %H:%M:%S"))
             & (datetime.datetime.strptime(historical_data_df["date"], "%Y-%m-%d %H:%M:%S") >= end_date)
        )
        filter_condition = coin_filter_condition & date_condition
        result = historical_data_df[filter_condition]
        return result

    def _read_csv(self, file_name):
        df = pd.read_csv(f"{self._historical_data_path}/{file_name}", index_col=None)
        return df
