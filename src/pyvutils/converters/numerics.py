
# Built-in Modules
from decimal import Decimal

# Custom Exceptions
from pyvutils.exceptions import InvalidNumericValueError
from pyvutils.exceptions import InvalidDecimalValueError
from pyvutils.exceptions import InvalidStringValueError


def decimal_to_numeric(value: Decimal) -> int | float:
    if not isinstance(value, Decimal):
        raise InvalidDecimalValueError(value=value)
    if value % 1 == 0:
        return int(value)
    return float(value)


def numeric_str_to_numeric(value: str) -> int | float:
    if not isinstance(value, str):
        raise InvalidStringValueError(value=value)
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError as exc:
            raise InvalidNumericValueError(f"Invalid Numeric String: {value}") from exc


def normalize_numeric(value: int | float | str | Decimal) -> int | float:
    if isinstance(value, str):
        return numeric_str_to_numeric(value)
    if isinstance(value, Decimal):
        return decimal_to_numeric(value)
    if not isinstance(value, (int, float)):
        raise InvalidNumericValueError(value=value)
    return value
