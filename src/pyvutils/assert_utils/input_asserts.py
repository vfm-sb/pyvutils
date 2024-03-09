"""
Input Assertions
"""

# Custom Exceptions
from pyvutils.exceptions.input_exceptions import MissingInputError


def assert_input(input_string: str) -> None:
    if not input_string:
        raise MissingInputError("Missing Input Error")
