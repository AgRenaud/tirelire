from unittest import TestCase
from parameterized import parameterized
from datetime import date, datetime

from app.infrastructure.persistence.db.transaction.transaction_orm import TransactionORM
from app.domain import Transaction, Value, Currency, Category

class TestTransactionORM(TestCase):

    @parameterized.expand([
        ("f0d97e6c-4ea9-41b3-ae5a-619d83c579e2", "Electro Shop", date(2022, 4, 23), -236.59, Currency.EUR, Category.TELEPHONE_TV_INTERNET, datetime(2022, 5, 6, 14, 29), datetime(2022, 5, 6, 14, 29)),
        ("276c2b5e-33d1-48e2-96f5-eb92637cf175", "SLRY COMP", date(2022, 4, 23), 2270.83, Currency.USD, Category.SALARY, datetime(2022, 5, 6, 14, 29), datetime(2022, 5, 6, 14, 29)),
    ])
    def test_to_entity_must_return_entity(self, id, name, tr_date, amount, curr, cat, updated_at, created_at):
        my_persisted_transaction = TransactionORM()
        my_persisted_transaction.id = id
        my_persisted_transaction.name = name
        my_persisted_transaction.date = tr_date
        my_persisted_transaction.amount = amount
        my_persisted_transaction.currency = curr
        my_persisted_transaction.category = cat
        my_persisted_transaction.updated_at = updated_at
        my_persisted_transaction.created_at = created_at

        my_transaction = Transaction(
            id, name, tr_date, Value(amount, curr), cat
        )
        
        self.assertEqual(my_persisted_transaction.to_entity(), my_transaction)