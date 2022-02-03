from dataclasses import dataclass
from datetime import date


class Command:
    pass


@dataclass
class CreateAccount(Command):
    id: str
    currency: str


@dataclass
class AddOperation(Command):
    name: str
    date: date
    value: float
    currency: str
    category: str
