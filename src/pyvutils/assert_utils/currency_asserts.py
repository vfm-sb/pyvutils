"""
Currency Assertions
"""

# Local Imports
from pyvutils.validator_utils.currency_validators import (
    valid_currency_code, valid_alphabetic_currency_code, valid_numeric_currency_code
)

# Custom Exceptions
from pyvutils.exceptions.currency_exceptions import InvalidCurrencyCodeError


def assert_currency_code(code: str | int) -> None:
    if not valid_currency_code(code):
        raise InvalidCurrencyCodeError("Invalid Currency Code")


def assert_alphabetic_currency_code(code: str) -> None:
    if not valid_alphabetic_currency_code(code):
        raise InvalidCurrencyCodeError("Invalid Alphabetic Currency Code")


def assert_numeric_currency_code(code: int | str) -> None:
    if not valid_numeric_currency_code(code):
        raise InvalidCurrencyCodeError("Invalid Numeric Currency Code")
