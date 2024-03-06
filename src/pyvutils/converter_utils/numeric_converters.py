
# Built-in Modules
from decimal import Decimal


def convert_decimal_to_numeric(value: Decimal) -> int | float:
    if value % 1 == 0:
        return int(value)
    return float(value)


def convert_numeric_string_to_numeric(value: str) -> int | float:
    try:
        return int(value)
    except ValueError:
        return float(value)


def normalize_numeric_value(value: int | float | str | Decimal) -> int | float:
    if isinstance(value, str):
        return convert_numeric_string_to_numeric(value=value)
    if isinstance(value, Decimal):
        return convert_decimal_to_numeric(value)
    if not isinstance(value, (int, float)):
        raise ValueError(f"Invalid Numeric Value >> {value}")
    return value
