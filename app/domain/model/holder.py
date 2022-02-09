from dataclasses import dataclass, field
from typing import List

from app.domain.model.account import Account
from app.domain.model.operation import Operation
from app.domain.events import events


@dataclass
class Holder:
    id: str
    accounts: List[Account] = field(default_factory=list)
    events = []

    def __hash__(self) -> int:
        return hash(self.id)

    def create_account(self, account: Account):
        self.accounts.append(account)

    def get_account_by_id(self, id: str) -> Account:
        return next((a for a in self.accounts if a.id == id), None)

    def add_operation_to_account(self, account_id: str, operation: Operation):
        account: Account = self.get_account_by_id(account_id)
        account.add_operation(operation)
        self.events.append(
            events.OperationAdded(
                operation.name, operation.date.strftime('%Y-%m-%d'), 
                operation.value, operation.currency.name, 
                operation.category.name, self.id
            )
        )
