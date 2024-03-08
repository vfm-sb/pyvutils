"""
Currency Validators
"""


def valid_currency_code(code: str | int) -> bool:
    return valid_alphabetic_currency_code(code) or valid_numeric_currency_code(code)


def valid_alphabetic_currency_code(code: str) -> bool:
    return isinstance(code, str) and code.isalpha() and len(code) == 3


def valid_numeric_currency_code(code: int | str) -> bool:
    return str(code).isdigit() and len(str(code)) == 3
