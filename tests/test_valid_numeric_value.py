from decimal import Decimal
from pyvutils import valid_numeric_value


class TestValidNumericValue:
    def test_valid_numeric_value_with_valid_input(self):
        assert valid_numeric_value(10) is True
        assert valid_numeric_value(10.5) is True
        assert valid_numeric_value(Decimal('10.5')) is True

    def test_valid_numeric_value_with_invalid_input(self):
        assert valid_numeric_value("not a number") is False
        assert valid_numeric_value(None) is False
        assert valid_numeric_value([]) is False

    def test_valid_numeric_value_with_numeric_string(self):
        assert valid_numeric_value("10") is True
        assert valid_numeric_value("10.5") is True
