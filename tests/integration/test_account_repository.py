import sqlite3

from sqlalchemy.orm import sessionmaker
from unittest import TestCase
from datetime import date

from app.domain import Account, Currency, Account, Transaction, Category
from app.repositories import AccountRepository, AccountRepositoryImplem
from app.infrastructure.orm import start_mappers, get_engine

start_mappers()
engine = get_engine("sqlite://")
Session = sessionmaker(engine)


class TestAccountRepository(TestCase):


        fake_repo: AccountRepository = AccountRepositoryImplem(Session())

        def test_added_accounts_must_be_queryable(self):
            transactions = [
                Transaction("my transaction", date(2022,1,26), -12345.90, Currency.USD, Category.HOUSING),
                Transaction("my transaction", date(2022,1,26), -14.99, Currency.USD, Category.HOBBIES_SPORT),
                Transaction("my transaction", date(2021,12,28), 2349.77, Currency.USD, Category.SALARY)
            ]
            accountX = Account('XXX', Currency.USD, transactions)
            self.fake_repo.add(accountX)
            self.assertEqual(self.fake_repo.get('XXX'), accountX)
            self.assertEqual(self.fake_repo.list(), [accountX])
