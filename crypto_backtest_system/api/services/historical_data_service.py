import datetime
from abc import ABCMeta
from abc import abstractmethod
from typing import Optional
import pandas as pd

from crypto_backtest_system.models.frequency import Frequency


class HistoricalDataService(metaclass=ABCMeta):
    @abstractmethod
    def get_data_for_coins(
            self,
            coins: list[str],
            start_date: Optional[datetime.datetime] = None,
            end_date: Optional[datetime.datetime] = None,
            frequency: Frequency = Frequency.ONE_DAY
    ) -> pd.DataFrame:
        pass
