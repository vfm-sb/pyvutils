"""
Input Assertions
"""

# Custom Exceptions
from pyvutils.exceptions import MissingInputError


def assert_input(input_string: str) -> None:
    """
    Raises a MissingInputError if the input_string is empty or None.

    Args:
        input_string (str): The input string to be checked.

    Raises:
        MissingInputError: If the input_string is empty or None.
    """
    if input_string is None or input_string.strip() == '':
        raise MissingInputError("Input String Cannot Be Empty")
