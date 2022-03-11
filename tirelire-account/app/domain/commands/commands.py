from dataclasses import dataclass
from datetime import date
from typing import Optional, List


class Command:
    pass


@dataclass
class CreateHolder(Command):
    holder_id: str


@dataclass
class CreateAccount(Command):
    holder_id: str
    account_id: str
    currency: str


@dataclass
class AddOperation(Command):
    name: str
    date: date
    value: float
    currency: str
    category: Optional[str] = None


@dataclass
class AddOperations(Command):
    holder_id: str
    account_id: str
    operations: List[AddOperation]
