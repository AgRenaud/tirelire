from unittest import TestCase

from typing import List

from app import bootstrap
from app.domain import commands, model
from app.service_layer import handlers
from app.service_layer.unit_of_work import UnitOfWork
from app.service_layer.auth_service import AuthService


class FakeRepository:

    def __init__(self, users: List[model.User]):
        self._users = set(users)
        self.seen = set()

    def add(self, user: model.User):
        self._users.add(user)

    def get(self, id: str):
        return next((h for h in self._users if h.id == id), None)

    def list(self):
        return self._users

class FakeAuthService:

    def verify_password(self, password: str, user: model.User) -> bool:
        return hash(password) == hash(user.password)

    def encrypt_password(self, password: str) -> str:
        return hash(password)

    def generate_token(self, password: str, user: model.User) -> dict:
        return NotImplemented

    def verify_token(self, token: str) -> bool:
        return NotImplemented


class FakeUnitOfWork(UnitOfWork):
    def __init__(self):
        self.users: AbstractUserRepository = FakeRepository([])
        self.auth_service = FakeAuthService()
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass

def bootstrap_test_app():
    return bootstrap.bootstrap(
        start_orm=False,
        uow=FakeUnitOfWork(),
    )

class TestHandlers(TestCase):

    def test_create_user_must_create_user(self):
        uow = bootstrap_test_app()
        command = commands.CreateUser(
            "id1234", 
            "jdoe", 
            "secure_password", 
            "john", 
            "doe", 
            "john.doe@mail.com"
        )
        handlers.create_user(command, uow)
        self.assertIsNotNone(uow.users.get('id1234'))

    def add_app_auth_to_user_must_return(self):
        pass

    def get_token_must_return(self):
        pass

    def verify_token_must_return(self):
        pass
