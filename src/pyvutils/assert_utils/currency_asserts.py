"""
Currency Assertions
"""

# Local Imports
from pyvutils.validator_utils.currency_validators import (
    valid_currency_code, valid_iso_alphabetic_code, valid_iso_numeric_code
)


def assert_currency_code(code: str | int) -> None:
    if not valid_currency_code(code):
        raise ValueError("Invalid Currency Code") # TODO Use InvalidCurrencyCodeError


def assert_iso_alphabetic_code(code: str) -> None:
    if not valid_iso_alphabetic_code(code):
        raise ValueError("Invalid Alphabetic Currency Code") # TODO Use InvalidCurrencyCodeError


def assert_iso_numeric_code(code: int | str) -> None:
    if not valid_iso_numeric_code(code):
        raise ValueError("Invalid Numeric Currency Code") # TODO Use InvalidCurrencyCodeError
