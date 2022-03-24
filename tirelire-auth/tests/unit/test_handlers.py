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
        return next((u for u in self._users if u.id == id), None)

    def get_by_email(self, email: str):
        return next((u for u in self._users if u.email == email), None)

    def list(self):
        return self._users

class FakeAuthService:

    def verify_password(self, password: str, user: model.User) -> bool:
        return hash(password) == hash(user.password)

    def encrypt_password(self, password: str) -> str:
        return hash(password)

    def generate_token(self, password: str, user: model.User) -> dict:
        return password

    def verify_token(self, token: str) -> bool:
        return token


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
            "secure_password", 
            "john", 
            "doe", 
            "john.doe@mail.com"
        )
        handlers.create_user(command, uow, lambda *args: None)
        self.assertIsNotNone(uow.users.get('id1234'))

    def test_add_app_auth_to_user_must_return(self):
        uow = bootstrap_test_app()
        command = commands.CreateUser(
            "id1234",
            "secure_password", 
            "john", 
            "doe", 
            "john.doe@mail.com"
        )
        handlers.create_user(command, uow, lambda *args: None)
        app_auth_1 = model.AppAuthorization(model.App.TIRELIRE_APP)
        command = commands.AddAuthorizationToUser("id1234", app_auth_1)
        handlers.add_app_auth_to_user(command, uow)
        app_auth_2 = model.AppAuthorization(model.App.TIRELIRE_WEB)
        command = commands.AddAuthorizationToUser("id1234", app_auth_2)
        handlers.add_app_auth_to_user(command, uow)

        user = uow.users.get('id1234')

        self.assertSetEqual(user._applications_auth, {app_auth_1, app_auth_2})

    def test_get_token_must_return_token(self):
        uow = bootstrap_test_app()
        command = commands.CreateUser(
            "id1234",
            "secure_password", 
            "john", 
            "doe", 
            "john.doe@mail.com"
        )
        handlers.create_user(command, uow, lambda *args: None)
        cmd = commands.Authenticate("john.doe@mail.com", "secure_password")
        token = handlers.get_token(cmd, uow)
        # TODO: Fake token generation

    def verify_token_must_return(self):
        pass
