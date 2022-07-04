import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, close_all_sessions, registry

from app.domain.model import Holder, Currency, Account
from app.service_layer.unit_of_work import SQLAlchemyUnitOfWork
from app.adapters.orm import start_mappers


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


class TestAccountUoW:


    def test_add_holder_and_retrieve_it(self, Session):
        uow = SQLAlchemyUnitOfWork(Session)

        with uow:
            holder = Holder('f6325ab0-d5dd-4c51-a356-75b660ca36fc', [])
            uow.holders.add(holder)
            uow.commit()

        assert get_holder(Session(), 'f6325ab0-d5dd-4c51-a356-75b660ca36fc')[0] == 'f6325ab0-d5dd-4c51-a356-75b660ca36fc'

    def test_add_accounts_to_holder_and_retrieve_them(self, Session):
        uow = SQLAlchemyUnitOfWork(Session)

        with uow:
            holder: Holder = Holder('f1366cf5-558b-4508-b4df-2d57dd6ad336', [])
            acc_1: Account = Account('83fa14d1-d8c7-4685-8ec8-1dd9530d74e6', Currency.EUR, [])
            acc_2: Account = Account('ca845b8f-a6ec-4be2-a80e-24c3f9e2b88e', Currency.EUR, [])
            holder.create_account(acc_1)
            holder.create_account(acc_2)
            uow.holders.add(holder)
            uow.commit()

        assert get_account(Session(), 'ca845b8f-a6ec-4be2-a80e-24c3f9e2b88e')[0] == 'ca845b8f-a6ec-4be2-a80e-24c3f9e2b88e' 
        assert get_account(Session(), '83fa14d1-d8c7-4685-8ec8-1dd9530d74e6')[0] == '83fa14d1-d8c7-4685-8ec8-1dd9530d74e6' 
