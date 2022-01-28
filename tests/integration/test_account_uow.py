import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, close_all_sessions
from unittest import TestCase

from app.domain import Account, Currency, Account, Transaction, Category
from app.service.unit_of_work import AccountUnitOfWorkImplem
from app.infrastructure.orm import start_mappers, mapper_registry


# class TestAccountUoW(TestCase):
# 
#     @classmethod
#     def setUpClass(cls):
#         start_mappers()
#         cls.engine = create_engine("sqlite://")
#         mapper_registry.metadata.create_all(cls.engine)
#         cls.Session = sessionmaker(cls.engine)
# 
#     @classmethod
#     def tearDownClass(cls):
#         close_all_sessions()
#         cls.engine.dispose()
# 
#     def test_uow_can_retrieve_a_batch_and_allocate_to_it(self):
#         session = self.Session()
#         pass