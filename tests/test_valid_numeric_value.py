from decimal import Decimal
from pyvutils import valid_numeric


class TestValidNumericValue:
    def test_valid_numeric_value_with_valid_input(self):
        assert valid_numeric(10) is True
        assert valid_numeric(10.5) is True
        assert valid_numeric(Decimal('10.5')) is True

    def test_valid_numeric_with_invalid_input(self):
        assert valid_numeric("not a number") is False
        assert valid_numeric(None) is False
        assert valid_numeric([]) is False

    def test_valid_numeric_with_numeric_string(self):
        assert valid_numeric("10") is True
        assert valid_numeric("10.5") is True
