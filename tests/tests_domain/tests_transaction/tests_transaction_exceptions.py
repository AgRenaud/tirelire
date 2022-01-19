from unittest import TestCase

from app.domain.transaction import TransactionNotFoundError, TransactionsNotFoundError


class TestAccountExceptions(TestCase):

    def test_exception_message_must_be_correct(self):
        self.assertEqual(TransactionNotFoundError().__str__(), "The transaction you spcecified does not exist.")
        self.assertEqual(TransactionsNotFoundError().__str__(), "No transactions were found.")
