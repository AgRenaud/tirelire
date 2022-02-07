from typing import Protocol, List, Set
from app.domain.model import Account


class AccountRepository(Protocol):
    seen: Set[Account]

    def add(self, account: Account) -> None:
        raise NotImplementedError

    def get(self, id: str) -> Account:
        raise NotImplementedError

    def list(self) -> List[Account]:
        raise NotImplementedError
