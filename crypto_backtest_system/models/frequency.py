from enum import Enum


class Frequency(Enum):
    ONE_MINUTE = "1m"
    FIVE_MINUTES = "5m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    ONE_HOUR = "1h"
    TWO_HOURS = "2h"
    FOUR_HOURS = "4h"
    TWELVE_HOURS = "12h"
    ONE_DAY = "1D"
    SEVEN_DAYS = "7D"
    FOURTEEN_DAYS = "14D"
    ONE_MONTH = "1M"
