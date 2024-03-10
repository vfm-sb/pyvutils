"""
Input Splitter Functions
"""


def split_by_char(string: str, char: str) -> list:
    return [part.strip() for part in string.split(char)]


def split_by_comma(string: str) -> list:
    return split_by_char(string, char=",")


def split_by_colon(string: str) -> list:
    return split_by_char(string, char=":")


def split_by_semicolon(string: str) -> list:
    return split_by_char(string, char=";")
