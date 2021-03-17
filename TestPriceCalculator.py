import pytest

from PriceCalculator import PriceCalculator


class TestPriceCalculator:

    def setup_method(self):
        self.calc = PriceCalculator()

    def test_calculating_gross_price_with_default_vat(self):
        result = self.calc.calculate_gross_price(100)
        assert result == 123

    def test_calculating_price_with_different_vat(self):
        # given
        calc = self.calc
        self.calc.change_vat(0.08)

        # when
        result = calc.calculate_gross_price(100)

        # then
        assert result == 108

    def test_changing_vat_with_incorrect_value(self):
        calc = self.calc
        with pytest.raises(ValueError):
            calc.change_vat(-1)
