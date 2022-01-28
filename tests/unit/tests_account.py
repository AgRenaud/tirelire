from unittest import TestCase
from unittest.mock import patch
from datetime import date

from app.domain import (
    Currency, 
    Category, 
    Account,
    Transaction
)


class TestAccount(TestCase):
    
    def test_hashes_must_be_identical(self):
        account = Account("abc", Currency.EUR, [])
        self.assertEqual(hash(account), hash("abc"))

    def test_add_transaction_must_append_to_account(self):
        my_account = Account("uuid", Currency.EUR, [])
        t1 = Transaction("my transaction", date(2022,1,26), -12345.90, Currency.EUR, Category.HOUSING)
        my_account.add_transaction( "my transaction", date(2022,1,26), -12345.90, 'EUR', 'HOUSING')
        self.assertEqual(my_account.transactions, [t1])

    def test_add_transaction_must_raise_exception(self):
        my_account = Account("uuid", Currency.USD, [])
        with self.assertRaises(ValueError):
            my_account.add_transaction( "my transaction", date(2022,1,26), -12345.90, 'EUR', 'HOUSING')

    def test_compute_balance_must_return_value(self):
        t1 = Transaction(
            "My transaction one", 
            date.today(), 
            12.36, 
            Currency.EUR
        )

        t2 = Transaction(
            "My transaction two", 
            date.today(), 
            29.78, 
            Currency.EUR
        )
        my_account = Account("uuid", Currency.EUR, [t1, t2])
        self.assertEqual(my_account.compute_balance(), t1.value + t2.value)

    def test_compute_balance_category_must_return_value(self):
        t1 = Transaction(
            "My transaction one", 
            date.today(), 
            1290.36, 
            Currency.EUR,
            Category.SALARY
        )

        t2 = Transaction(
            "My transaction two", 
            date.today(), 
            29.78, 
            Currency.EUR,
            Category.HOBBIES_SPORT
        )

        t3 = Transaction(
            "My transaction three", 
            date.today(), 
            4.99, 
            Currency.EUR,
            Category.HOBBIES_SPORT
        )

        my_account = Account("uuid", Currency.EUR, [t1, t2, t3])
        self.assertEqual(my_account.compute_category_balance(Category.SALARY), t1.value)
        self.assertEqual(my_account.compute_category_balance(Category.HOBBIES_SPORT), t2.value + t3.value)
        self.assertEqual(my_account.compute_category_balance(Category.HOUSING), 0.0, Currency.EUR)
