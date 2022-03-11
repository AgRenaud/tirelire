import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, close_all_sessions
from unittest import TestCase
from datetime import date

from app.domain.model import Holder
from app.adapters.repository import HolderRepository, HolderRepositoryImplem
from app.adapters.orm import start_mappers, mapper_registry


class TestAccountRepository(TestCase):

        @classmethod
        def setUpClass(cls):
            cls.engine = create_engine("sqlite://")
            mapper_registry.metadata.create_all(cls.engine)
            cls.Session = sessionmaker(cls.engine)
            cls.repo: HolderRepository = HolderRepositoryImplem(cls.Session())

        @classmethod
        def tearDownClass(cls):
            close_all_sessions()
            cls.engine.dispose()

        def test_added_holder_must_be_queryable(self):
            holder: Holder = Holder('XXX', [])
            self.repo.add(holder)
            self.assertEqual(self.repo.get('XXX'), holder)
            self.assertEqual(self.repo.list(), [holder])
