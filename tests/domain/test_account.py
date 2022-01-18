from unittest import TestCase
from unittest.mock import patch
from datetime import date

from app.domain import (
    Currency, 
    Category, 
    Account, 
    Value, 
    Transaction
)


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
        t1 = Transaction(
            "uuid_1", 
            "My transaction one", 
            date.today(), 
            Value(12.36, Currency.EUR)
        )

        t2 = Transaction(
            "uuid_2", 
            "My transaction two", 
            date.today(), 
            Value(29.78, Currency.EUR)
        )
        my_account = Account("uuid", Currency.EUR, [t1, t2])
        self.assertEqual(my_account.compute_balance(), t1.value + t2.value)

    def test_compute_balance_category_must_return_value(self):
        t1 = Transaction(
            "uuid_1", 
            "My transaction one", 
            date.today(), 
            Value(1290.36, Currency.EUR),
            Category.SALARY
        )

        t2 = Transaction(
            "uuid_2", 
            "My transaction two", 
            date.today(), 
            Value(29.78, Currency.EUR),
            Category.HOBBIES_SPORT
        )

        t3 = Transaction(
            "uuid_3", 
            "My transaction three", 
            date.today(), 
            Value(4.99, Currency.EUR),
            Category.HOBBIES_SPORT
        )

        my_account = Account("uuid", Currency.EUR, [t1, t2, t3])
        self.assertEqual(my_account.compute_category_balance(Category.SALARY), t1.value)
        self.assertEqual(my_account.compute_category_balance(Category.HOBBIES_SPORT), t2.value + t3.value)
        self.assertEqual(my_account.compute_category_balance(Category.HOUSING), Value(0.0, Currency.EUR))
