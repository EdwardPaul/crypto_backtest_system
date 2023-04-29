from crypto_backtest_system.api.rules.coin_extractor import CoinExtractor
from crypto_backtest_system.models.strategy_config import StrategyConfig


class CoinExtractor(CoinExtractor):
    def __init__(self, configs: list[StrategyConfig]):
        self._configs = configs

    def get_coins(self, position_df) -> list[str]:
        raise NotImplementedError
