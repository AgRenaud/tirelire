from unittest import TestCase
from parameterized import parameterized
from datetime import date

from app.domain.model import Operation, Currency


class TestOperation(TestCase):
    
    @parameterized.expand([
        (15035.30, Currency.EUR),
        (120.50, Currency.USD),
    ])
    def test_currency_property_must_return_value(self, value: float, curr: Currency):

        t = Operation("My operation", date.today(), value, curr)
        self.assertEqual(t.currency, curr)
