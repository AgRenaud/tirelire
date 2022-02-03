from unittest import TestCase

from app.service_layer.unit_of_work import AbstractAccountUnitOfWork
from app.adapters.repository import AccountRepository
from app.service_layer import services


class FakeRepository(AccountRepository):
    def __init__(self, accounts):
        super().__init__()
        self.accounts = set(accounts)

    def add(self, account):
        self.accounts.add(account)

    def get(self, id):
        return next((a for a in self.accounts if a.id == id), None)


class FakeAccountUoW(AbstractAccountUnitOfWork):
    def __init__(self):
        self.accounts = FakeRepository([])
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass


class TestServices(TestCase):

    def setUp(self):
        self.uow = FakeAccountUoW()

    def test_add_account(self):
        pass


    def ctest_ompute_balance(self):
        pass

    def test_compute_category_balance(self):
        pass

    def test_add_operations(self):
        pass
