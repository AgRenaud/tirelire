from dataclasses import dataclass
from datetime import date


class Event:
    pass


@dataclass
class AccountCreated(Event):
    id: str
    currency: str


@dataclass
class OperationAdded(Event):
    name: str
    date: date
    value: float
    currency: str
    category: str
