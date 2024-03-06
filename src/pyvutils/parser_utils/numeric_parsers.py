"""
Numeric Parser Utils
"""


def parse_numeric_value(input_string: str) -> int | float:
    try:
        return int(input_string)
    except ValueError:
        try:
            return float(input_string)
        except ValueError as exc:
            raise ValueError("Invalid Numeric Value") from exc # TODO Use InvalidNumericInputError


def parse_integer_value(input_string: str) -> int:
    try:
        return int(input_string)
    except ValueError as exc:
        raise ValueError("Invalid Integer Value") from exc # TODO Use InvalidNumericInputError


def parse_float_value(input_string: str) -> float:
    try:
        return float(input_string)
    except ValueError as exc:
        raise ValueError("Invalid Float Value") from exc # TODO Use InvalidNumericInputError
