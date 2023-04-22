from api.services.historical_data_service import HistoricalDataService
from api.repositories.historical_data_repository import HistoricalDataRepository

from typing import Optional
import datetime
import pandas as pd


class HistoricalDataService(HistoricalDataService):
    def __init__(self, historical_data_repository: HistoricalDataRepository):
        self._historical_data_repository = historical_data_repository

    def get_data_for_coins(
            self,
            coins: list[str],
            start_date: Optional[datetime.datetime] = None,
            end_date: Optional[datetime.datetime] = None,
            frequency: Frequency = Frequency.ONE_DAY
    ) -> pd.DataFrame:
        result = self._historical_data_repository.get_data_for_coins(
            coins, start_date, end_date, frequency
        )
        return result
