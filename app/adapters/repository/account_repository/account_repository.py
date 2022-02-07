from typing import Protocol, List
from app.domain.model import Account


class AccountRepository(Protocol):

    def add(self, account: Account) -> None:
        raise NotImplementedError

    def get(self, id: str) -> Account:
        raise NotImplementedError

    def list(self) -> List[Account]:
        raise NotImplementedError
