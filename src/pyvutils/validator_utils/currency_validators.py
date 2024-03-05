"""
Currency Validators
"""


def valid_currency_code(code: str | int) -> bool:
    return valid_iso_alphabetic_code(code) or valid_iso_numeric_code(code)


def valid_iso_alphabetic_code(code: str) -> bool:
    return isinstance(code, str) and code.isalpha() and len(code) == 3


def valid_iso_numeric_code(code: int | str) -> bool:
    return str(code).isdigit() and len(str(code)) == 3
