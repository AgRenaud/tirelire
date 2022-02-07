from unittest import TestCase
from typing import Dict, List

from app import bootstrap
from app.domain import commands
from app.domain.model import Holder, Account
from app.service_layer import handlers
from app.service_layer.unit_of_work import AbstractHolderUnitOfWork


class FakeHolderRepository:
    def __init__(self, holders):
        super().__init__()
        self._holders = set(holders)

    def _add(self, holder: Holder):
        self._products.add(holder)

    def _get(self, id: str):
        return next((h for h in self._holders if h.id == id), None)


class FakeAccountRepository:
    def __init__(self, products):
        super().__init__()
        self._accounts = set(products)

    def _add(self, account: Account):
        self._accounts.add(account)

    def _get(self, id):
        return next((a for a in self._accounts if a.id == id), None)


class FakeUnitOfWork(AbstractHolderUnitOfWork):
    def __init__(self):
        self.holders = FakeHolderRepository([])
        self.accounts = FakeAccountRepository([])
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass

class TestCommand(TestCase):
    pass