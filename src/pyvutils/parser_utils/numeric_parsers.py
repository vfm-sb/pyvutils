"""
Numeric Parser Utils
"""

# Custom Exceptions
from pyvutils.exceptions.input_exceptions import InvalidNumericInputError


def parse_numeric_value(input_string: str) -> int | float:
    try:
        return int(input_string)
    except ValueError:
        try:
            return float(input_string)
        except ValueError as exc:
            raise InvalidNumericInputError("Invalid Numeric Value") from exc


def parse_integer_value(input_string: str) -> int:
    try:
        return int(input_string)
    except ValueError as exc:
        raise InvalidNumericInputError("Invalid Integer Value") from exc


def parse_float_value(input_string: str) -> float:
    try:
        return float(input_string)
    except ValueError as exc:
        raise InvalidNumericInputError("Invalid Float Value") from exc
