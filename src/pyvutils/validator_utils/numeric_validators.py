
# Built-in Modules
from decimal import Decimal


def valid_numeric_value(value: int | float | str | Decimal) -> bool:
    try:
        if isinstance(value, (str, Decimal)):
            value = float(value)
        return isinstance(value, (int, float))
    except (TypeError, ValueError):
        return False
