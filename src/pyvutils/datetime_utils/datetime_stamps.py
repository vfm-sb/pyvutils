
# Built-in Modules
from datetime import datetime


def current_year_timestamp() -> str:
    current_time = datetime.now()
    return current_time.strftime("%Y")


def current_month_timestamp() -> str:
    current_time = datetime.now()
    return current_time.strftime("%Y/%m")


def current_date_timestamp() -> str:
    current_time = datetime.now()
    return current_time.strftime("%Y/%m/%d")
