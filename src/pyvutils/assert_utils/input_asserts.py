"""
Input Assertions
"""


def assert_input(input_string: str) -> None:
    if not input_string:
        raise ValueError("Missing Input Error") # TODO Use MissingInputError Exception
