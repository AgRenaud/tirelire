from unittest import TestCase, mock
from parameterized import parameterized

from app.domain import Value, Transaction, Currency


class TestValue(TestCase):
    
    @parameterized.expand([
        ((12.5, Currency.EUR), (2000.56, Currency.EUR), (2013.06, Currency.EUR)),
        ((12.5, Currency.USD), (2000.56, Currency.USD), (2013.06, Currency.USD)),
        ((4567.33, Currency.USD), (234.65, Currency.USD), (4801.98, Currency.USD))
    ])
    def test_add_must_return_value(self, value_parameters_1, value_parameters_2, result_addition):
        v1 = Value(*value_parameters_1)
        v2 = Value(*value_parameters_2)
        v3 = Value(*result_addition)
        self.assertEqual(v1 + v2, v3)

    @parameterized.expand([
        ((12.5, Currency.USD), (2000.56, Currency.EUR)),
        ((12.5, Currency.EUR), (2000.56, Currency.USD)),
        ((4567.33, Currency.USD), (234.65, Currency.EUR))
    ])
    def test_add_must_raise_exception(self, value_parameters_1, value_parameters_2):
        v1 = Value(*value_parameters_1)
        v2 = Value(*value_parameters_2)
        with self.assertRaises(ValueError):
            v3 = v1 + v2



class TestTransaction(TestCase):
    
    @parameterized.expand([
        (Currency.EUR, ),
        (Currency.USD, ),
    ])
    def test_currency_property_must_return_value(self, curr: Currency):
        value = mock.patch("app.domain.Value")
        value.currency = curr

        t = Transaction("uuid", "My transaction", value)
        self.assertEqual(t.currency, curr)