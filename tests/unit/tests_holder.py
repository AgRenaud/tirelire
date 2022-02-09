from unittest import TestCase

from app.domain.model import Holder, Account, Currency


class TestHolder(TestCase):
    
    def test_create_new_holder_and_add_operations(self):
        new_holder = Holder("str_id", [])
        self.assertIsInstance(new_holder, Holder)
        new_account_1 = Account("id_account_1", Currency.EUR, [])
        new_account_2 = Account("id_account_2", Currency.USD, [])
        new_holder.create_account(new_account_1)
        new_holder.create_account(new_account_2)
        self.assertEqual(len(new_holder.accounts), 2)
        self.assertEqual(new_holder.get_account_by_id("id_account_1"), new_account_1)
        self.assertEqual(new_holder.get_account_by_id("id_account_2"), new_account_2)

