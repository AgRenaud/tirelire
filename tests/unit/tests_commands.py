from unittest import TestCase
from typing import List
from datetime import date

from app import bootstrap
from app.domain import commands
from app.domain.model import Holder, Account, Currency
from app.adapters.repository import  HolderRepository
from app.service_layer.unit_of_work import AbstractUnitOfWork


class FakeHolderRepository:

    def __init__(self, holders: List[Holder]):
        self._holders = set(holders)
        self.seen = set()

    def add(self, holder: Holder):
        self._holders.add(holder)

    def get(self, id: str):
        return next((h for h in self._holders if h.id == id), None)

    def list(self):
        return self._holders


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.holders: HolderRepository = FakeHolderRepository([])
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass

def bootstrap_test_app():
    return bootstrap.bootstrap(
        start_orm=False,
        uow=FakeUnitOfWork(),
        publish=lambda *args: None,
    )


class TestCommandHandlers(TestCase):
    """Test
    add_holder
    add_account
    add_operations
    """

    def test_add_holder_must_commit(self):
        bus = bootstrap_test_app()
        bus.handle(commands.CreateHolder("id12345"))
        self.assertIsNotNone(bus.uow.holders.get("id12345"))


    def test_add_account_must_commit(self):
        bus = bootstrap_test_app()
        bus.handle(commands.CreateHolder("holder_id1234"))
        bus.handle(commands.CreateAccount("holder_id1234", "account_id1234", "EUR"))
        self.assertEqual(1, len(bus.uow.holders.get("holder_id1234").accounts))

    def test_add_operations_must_commit(self):
        bus = bootstrap_test_app()
        bus.handle(commands.CreateHolder("holder_id1234"))
        bus.handle(commands.CreateAccount("holder_id1234", "account_id1234", "EUR"))
        bus.handle(commands.AddOperations(
            "holder_id1234",
            "account_id1234",
            [
                commands.AddOperation("a123", date(2022, 2, 9), -14.99, "EUR"),
                commands.AddOperation("b123", date(2022, 2, 9), 1234.78, "EUR")
            ]
        ))
        self.assertEqual(2, len(bus.uow.holders.get("holder_id1234").get_account_by_id("account_id1234").operations))
