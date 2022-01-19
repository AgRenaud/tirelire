from unittest import TestCase

from app.domain.account import AccountNotFoundError, AccountsNotFoundError


class TestAccountExceptions(TestCase):

    def test_exception_message_must_be_correct(self):
        self.assertEqual(AccountNotFoundError().__str__(), "The account you spcecified does not exist.")
        self.assertEqual(AccountsNotFoundError().__str__(), "No accounts were found.")
