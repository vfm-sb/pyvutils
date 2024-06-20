"""
File Asserts
"""

import pathvalidate


def assert_filename(filename: str) -> None:
    pathvalidate.validate_filename(filename)
