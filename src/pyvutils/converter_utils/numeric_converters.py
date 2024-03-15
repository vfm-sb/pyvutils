
# Built-in Modules
from decimal import Decimal

# Custom Exceptions
from pyvutils.exceptions import InvalidNumericValueError
from pyvutils.exceptions import InvalidDecimalValueError
from pyvutils.exceptions import InvalidStringValueError


def convert_decimal_to_numeric(value: Decimal) -> int | float:
    if not isinstance(value, Decimal):
        raise InvalidDecimalValueError(value=value)
    if value % 1 == 0:
        return int(value)
    return float(value)


def convert_numeric_string_to_numeric(value: str) -> int | float:
    if not isinstance(value, str):
        raise InvalidStringValueError(value=value)
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError as exc:
            raise InvalidNumericValueError(f"Invalid Numeric String: {value}") from exc


def normalize_numeric_value(value: int | float | str | Decimal) -> int | float:
    if isinstance(value, str):
        return convert_numeric_string_to_numeric(value=value)
    if isinstance(value, Decimal):
        return convert_decimal_to_numeric(value)
    if not isinstance(value, (int, float)):
        raise InvalidNumericValueError(value=value)
    return value
