"""
Input Splitter Functions
"""


def split_by_char(input_string: str, char: str) -> list:
    return [part.strip() for part in input_string.split(char)]


def split_by_comma(input_string: str) -> list:
    return split_by_char(input_string, char=",")
