import unittest

import pytest

from PriceCalculator import PriceCalculator


class MyTestCase(unittest.TestCase):

    def test_calculating_gross_price_with_defailt_vat(self):
        calc = PriceCalculator()
        result = calc.calculate_gross_price(100)
        assert result == 123

    def test_calculating_price_with_different_vat(self):
        calc = PriceCalculator()
        calc.change_vat(0.08)
        result = calc.calculate_gross_price(100)
        assert result == 108

    def test_changing_vat_with_incorrect_value(self):
        calc = PriceCalculator()
        with pytest.raises(ValueError):
            calc.change_vat(-1)
            calc.change_vat(0)
            calc.change_vat(1)
            calc.change_vat(8)
