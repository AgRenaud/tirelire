from unittest import TestCase
from datetime import date

from app.domain.model import (
    Currency, 
    Category, 
    Account,
    Operation
)


class TestAccount(TestCase):
    
    def test_hashes_must_be_identical(self):
        account = Account("abc", Currency.EUR, [])
        self.assertEqual(hash(account), hash("abc"))

    def test_add_operation_must_append_to_account(self):
        my_account = Account("uuid", Currency.EUR, [])
        t1 = Operation("my operation", date(2022,1,26), -12345.90, Currency.EUR, Category.HOUSING)
        my_account.add_operation(t1)
        self.assertEqual(my_account.operations, [t1])

    def test_add_operation_must_raise_exception(self):
        my_account = Account("uuid", Currency.USD, [])
        with self.assertRaises(ValueError):
            new_op = Operation("my operation", date(2022,1,26), -12345.90, 'EUR', 'HOUSING')
            my_account.add_operation(new_op)

    def test_compute_balance_must_return_value(self):
        t1 = Operation(
            "My operation one", 
            date.today(), 
            12.36, 
            Currency.EUR
        )

        t2 = Operation(
            "My operation two", 
            date.today(), 
            29.78, 
            Currency.EUR
        )
        my_account = Account("uuid", Currency.EUR, [t1, t2])
        self.assertEqual(my_account.compute_balance(), t1.value + t2.value)

    def test_compute_balance_category_must_return_value(self):
        t1 = Operation(
            "My operation one", 
            date.today(), 
            1290.36, 
            Currency.EUR,
            Category.SALARY
        )

        t2 = Operation(
            "My operation two", 
            date.today(), 
            29.78, 
            Currency.EUR,
            Category.HOBBIES_SPORT
        )

        t3 = Operation(
            "My operation three", 
            date.today(), 
            4.99, 
            Currency.EUR,
            Category.HOBBIES_SPORT
        )

        my_account = Account("uuid", Currency.EUR, [t1, t2, t3])
        self.assertEqual(my_account.compute_category_balance(Category.SALARY), t1.value)
        self.assertEqual(my_account.compute_category_balance(Category.HOBBIES_SPORT), t2.value + t3.value)
        self.assertEqual(my_account.compute_category_balance(Category.HOUSING), 0.0, Currency.EUR)
