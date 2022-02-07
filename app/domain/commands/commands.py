from dataclasses import dataclass
from datetime import date
from typing import Optional, List


class Command:
    pass


@dataclass
class CreateAccountHolder(Command):
    account_holder_id: str

@dataclass
class CreateAccount(Command):
    account_holder_id: str
    account_id: str
    currency: str

@dataclass
class AddOperation(Command):
    name: str
    date: date
    value: float
    currency: str
    category: Optional[str]


@dataclass
class AddOperations(Command):
    account_holder_id: str
    account_id: str
    operations: List[AddOperation]