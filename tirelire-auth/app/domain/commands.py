from dataclasses import dataclass

from app.domain.model import App


@dataclass
class Command:
    pass


@dataclass
class CreateUser(Command):
    id: str
    username: str
    password: str
    first_name: str
    last_name: str
    email: str


@dataclass
class AddAuthorizationToUser(Command):
    user_id: str
    app: App


@dataclass
class Authenticate(Command):
    email: str
    password: str


@dataclass
class VerifyToken(Command):
    token: str
