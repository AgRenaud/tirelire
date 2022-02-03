from dataclasses import dataclass
from datetime import date


class Event:
    pass

@dataclass
class AccountHolderCreated(Event):
    id: str

@dataclass
class AccountCreated(Event):
    account_holder_id: str
    account_id: str
    currency: str

@dataclass
class OperationAdded(Event):
    account_id: str
    name: str
    date: date
    value: float
    currency: str
    category: str
