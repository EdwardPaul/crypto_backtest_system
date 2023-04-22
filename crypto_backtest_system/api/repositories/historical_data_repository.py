import datetime
from abc import ABCMeta
from abc import abstractmethod
from typing import Optional

import pandas as pd


class HistoricalDataRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_data_for_coins(
            self,
            coins: list[str],
            start_date: Optional[datetime.datetime] = None,
            end_date: Optional[datetime.datetime] = None,
            frequency: Frequency = Frequency.ONE_DAY
    ) -> pd.DataFrame:
        pass
