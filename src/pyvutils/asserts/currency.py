"""
Currency Assertions
"""

# Local Imports
from pyvutils.validators.currency import (
    valid_currency_code,
    valid_alphabetic_currency_code,
    valid_numeric_currency_code
)

# Custom Exceptions
from pyvutils.exceptions.currency_exceptions import InvalidCurrencyCodeError


def assert_currency_code(code: str | int) -> None:
    if not valid_currency_code(code):
        raise InvalidCurrencyCodeError(f"Invalid Currency Code: {code}")


def assert_alphabetic_currency_code(code: str) -> None:
    if not valid_alphabetic_currency_code(code):
        raise InvalidCurrencyCodeError(f"Invalid Alphabetic Currency Code: {code}")


def assert_numeric_currency_code(code: int | str) -> None:
    if not valid_numeric_currency_code(code):
        raise InvalidCurrencyCodeError(f"Invalid Numeric Currency Code: {code}")
