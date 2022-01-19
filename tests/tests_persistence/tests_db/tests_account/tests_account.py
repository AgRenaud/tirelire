from unittest import TestCase
from parameterized import parameterized
from datetime import datetime

from app.infrastructure.persistence.db.account.account_orm import AccountORM
from app.domain import Account, Currency


class TestAccountORM(TestCase):

    @parameterized.expand([
        ("f0d97e6c-4ea9-41b3-ae5a-619d83c579e2", Currency.EUR, datetime(2022, 5, 6, 14, 29), datetime(2022, 5, 6, 14, 29)),
        ("276c2b5e-33d1-48e2-96f5-eb92637cf175", Currency.USD, datetime(2022, 5, 6, 14, 29), datetime(2022, 5, 6, 14, 29)),
    ])
    def test_to_entity_must_return_entity(self, id, curr, updated_at, created_at):
        my_persisted_account = AccountORM()
        my_persisted_account.id = id
        my_persisted_account.currency = curr
        my_persisted_account.updated_at = updated_at
        my_persisted_account.created_at = created_at

        my_account = Account(
            id, curr, []
        )
        
        self.assertEqual(my_persisted_account.to_entity(), my_account)