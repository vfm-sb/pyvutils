"""
Input Assertions
"""


def assert_input(user_input: str) -> None:
    if not user_input:
        raise ValueError("Missing Input Error") # TODO Use MissingInputError Exception
