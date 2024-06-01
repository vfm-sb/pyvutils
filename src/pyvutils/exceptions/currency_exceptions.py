"""Custom Currency Exceptions"""


class InvalidCurrencyCodeError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
