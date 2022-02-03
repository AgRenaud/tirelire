import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, close_all_sessions
from unittest import TestCase
from datetime import date

from app.domain.model import Account, Currency, Account, Operation, Category
from app.adapters.repository import AccountRepository, AccountRepositoryImplem
from app.adapters.orm import start_mappers, mapper_registry


class TestAccountRepository(TestCase):

        @classmethod
        def setUpClass(cls):
            cls.engine = create_engine("sqlite://")
            mapper_registry.metadata.create_all(cls.engine)
            cls.Session = sessionmaker(cls.engine)
            cls.repo: AccountRepository = AccountRepositoryImplem(cls.Session())

        @classmethod
        def tearDownClass(cls):
            close_all_sessions()
            cls.engine.dispose()

        def test_added_accounts_must_be_queryable(self):
            operations = [
                Operation("my operation", date(2022,1,26), -12345.90, Currency.USD, Category.HOUSING),
                Operation("my operation", date(2022,1,26), -14.99, Currency.USD, Category.HOBBIES_SPORT),
                Operation("my operation", date(2021,12,28), 2349.77, Currency.USD, Category.SALARY)
            ]
            accountX = Account('XXX', Currency.USD, operations)
            self.repo.add(accountX)
            self.assertEqual(self.repo.get('XXX'), accountX)
            self.assertEqual(self.repo.list(), [accountX])
