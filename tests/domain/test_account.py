from unittest import TestCase
from unittest.mock import patch

from app.domain import Currency, Category, Account


class TestAccount(TestCase):
    
    def test_add_transaction_must_append_to_account(self):
        my_account = Account("uuid", Currency.EUR, [])
        t1 = patch("app.domain.Transaction")
        t1.currency = Currency.EUR
        my_account.add_transaction(t1)
        self.assertEqual(my_account.transactions, [t1])

    def test_add_transaction_must_raise_exception(self):
        my_account = Account("uuid", Currency.USD, [])
        t1 = patch("app.domain.Transaction")
        t1.currency = Currency.EUR
        with self.assertRaises(ValueError):
            my_account.add_transaction(t1)

    def test_compute_balance_must_return_value(self):
        pass

    def test_compute_balance_category_must_return_value(self):
        pass
