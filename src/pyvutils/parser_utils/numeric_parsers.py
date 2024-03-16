"""
Numeric Parser Utils
"""

# Custom Exceptions
from pyvutils.exceptions import InvalidNumericValueError


def parse_numeric_value(input_string: str) -> int | float:
    try:
        return int(input_string)
    except ValueError:
        try:
            return float(input_string)
        except ValueError as exc:
            raise InvalidNumericValueError("Invalid Numeric Value") from exc


def parse_integer_value(input_string: str) -> int:
    try:
        return int(input_string)
    except ValueError as exc:
        raise InvalidNumericValueError("Invalid Integer Value") from exc


def parse_float_value(input_string: str) -> float:
    try:
        return float(input_string)
    except ValueError as exc:
        raise InvalidNumericValueError("Invalid Float Value") from exc
