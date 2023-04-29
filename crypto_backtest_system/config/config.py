from configparser import ConfigParser
import pandas as pd


class Config:
    def __init__(self):
        config = ConfigParser()
        config.read("config.ini")
        # self.API_KEY = config['user']['API_KEY']
        # self.API_SECRET = config['user']['API_SECRET']
        self._path_to_result_files = config['DEFAULT']['path_to_result_files']
        self._start_times = config['HISTORICAL_DATA']['start_times'].split('\n')
        self._end_times = config['HISTORICAL_DATA']['end_times'].split('\n')
        self._frequencies = config['HISTORICAL_DATA']['frequencies'].split('\n')
        # self.coin_universe = config['trading']['coin_universe'].split('\n')
        # self.start_date = pd.to_datetime(
        #     config['trading']['start_date'],
        #     dayfirst=True
        # )
        # self.end_date = pd.to_datetime(
        #     config['trading']['end_date'],
        #     dayfirst=True
        # )
        # self.freq = config['trading']['freq']

    @property
    def path_to_result_files(self) -> str:
        return self._path_to_result_files

    @property
    def start_times(self) -> list[str]:
        return self._start_times

    @property
    def end_times(self) -> list[str]:
        return self._end_times

    @property
    def frequencies(self) -> list[str]:
        return self._frequencies
