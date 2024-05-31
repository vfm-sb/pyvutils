
# Built-in Modules
from datetime import datetime


def current_year() -> str:
    current_time = datetime.now()
    return current_time.strftime("%Y")


def current_month() -> str:
    current_time = datetime.now()
    return current_time.strftime("%Y/%m")


def current_date() -> str:
    current_time = datetime.now()
    return current_time.strftime("%Y/%m/%d")
