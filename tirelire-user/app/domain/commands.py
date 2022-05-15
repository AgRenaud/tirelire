from dataclasses import dataclass
from datetime import date


@dataclass
class Command:
    pass


@dataclass
class CreateUser(Command):
    id: str
    birthdate: date
    first_name: str
    last_name: str
    email: str
