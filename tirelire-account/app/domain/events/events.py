from dataclasses import dataclass
from datetime import date


class Event:
    pass


@dataclass
class HolderCreated(Event):
    id: str


@dataclass
class AccountCreated(Event):
    id: str
    currency: str

    holder_id: str


@dataclass
class OperationAdded(Event):
    name: str
    date: date
    value: float
    currency: str
    category: str

    account_id: str
