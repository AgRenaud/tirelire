import sqlite3

from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, close_all_sessions


from app.domain import model
from app.adapters.repository import UserRepository
from app.adapters.orm import start_mappers, mapper_registry


class TestUserRepository(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine("sqlite://")
        mapper_registry.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(cls.engine)
        

    def test_add_user_to_database(self):
        new_user_1 = model.User('123', 'password', 'john', 'doe', 'jdoe@mail.com',)
        new_user_2 = model.User('abc', 'password', 'matthew', 'someone', 'msome1@mail.com',)

        repository: UserRepository = UserRepository(self.Session())

        repository.add(new_user_1)
        repository.add(new_user_2)

        self.assertEqual(repository.get('123'), new_user_1)
        self.assertEqual(repository.get('abc'), new_user_2)
        
        self.assertEqual(repository.get_by_email('jdoe@mail.com'), new_user_1)
        self.assertEqual(repository.get_by_email('msome1@mail.com'), new_user_2)
