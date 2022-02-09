import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, close_all_sessions
from unittest import TestCase

from app.domain.model import Holder, Currency, Account, Operation, Category
from app.service_layer.unit_of_work import SQLAlchemyUnitOfWorkImplem
from app.adapters.orm import start_mappers, mapper_registry


def get_holder(session, holder_id: str) -> str:
    [res] = session.execute(
        "SELECT * FROM holders"
        " WHERE id=:id",
        dict(id=holder_id))
    return res

def get_account(session, account_id: str) -> str:
    [res] = session.execute(
        "SELECT * FROM accounts"
        " WHERE id=:id",
        dict(id=account_id))
    return res


class TestAccountUoW(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine("sqlite://")
        mapper_registry.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(cls.engine)

    @classmethod
    def tearDownClass(cls):
        close_all_sessions()
        cls.engine.dispose()

    def test_add_holder_and_retrieve_it(self):
        uow = SQLAlchemyUnitOfWorkImplem(self.Session)

        with uow:
            holder = Holder('f6325ab0-d5dd-4c51-a356-75b660ca36fc', [])
            uow.holders.add(holder)
            uow.commit()

        self.assertEqual('f6325ab0-d5dd-4c51-a356-75b660ca36fc', get_holder(self.Session(), 'f6325ab0-d5dd-4c51-a356-75b660ca36fc')[0])

    def test_add_accounts_to_holder_and_retrieve_them(self):
        uow = SQLAlchemyUnitOfWorkImplem(self.Session)

        with uow:
            holder: Holder = Holder('f1366cf5-558b-4508-b4df-2d57dd6ad336', [])
            acc_1: Account = Account('83fa14d1-d8c7-4685-8ec8-1dd9530d74e6', Currency.EUR, [])
            acc_2: Account = Account('ca845b8f-a6ec-4be2-a80e-24c3f9e2b88e', Currency.EUR, [])
            holder.create_account(acc_1)
            holder.create_account(acc_2)
            uow.holders.add(holder)
            uow.commit()

        self.assertEqual('ca845b8f-a6ec-4be2-a80e-24c3f9e2b88e', get_account(self.Session(), 'ca845b8f-a6ec-4be2-a80e-24c3f9e2b88e')[0])
        self.assertEqual('83fa14d1-d8c7-4685-8ec8-1dd9530d74e6', get_account(self.Session(), '83fa14d1-d8c7-4685-8ec8-1dd9530d74e6')[0])
