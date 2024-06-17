from pathvalidate import is_valid_filename


def valid_filename(filename: str) -> bool:
    return is_valid_filename(filename)
