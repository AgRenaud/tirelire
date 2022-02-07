from dataclasses import dataclass, field
from typing import List

from app.domain.model.account import Account
from app.domain.model.operation import Operation


@dataclass
class AccountHolder:
    id: str
    accounts: List[Account] = field(default_factory=list)

    def create_account(self, account: Account):
        self.accounts.append(account)

    def get_account_by_id(self, id: str):
        return next((a for a in self.accounts if a.id == id), None)
