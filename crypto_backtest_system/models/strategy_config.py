from dataclasses import dataclass
from decimal import Decimal

from crypto_backtest_system.models.rule_type import RuleType


@dataclass(frozen=True, order=True, eq=True)
class StrategyConfig:
    strategy_name: str
    rule_type: RuleType
    parameter_name: str
    value: Decimal
