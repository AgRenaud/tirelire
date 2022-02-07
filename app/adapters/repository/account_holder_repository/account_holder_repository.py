from typing import Protocol, List
from app.domain.model import AccountHolder


class AccountHolderRepository(Protocol):

    def add(self, account: AccountHolder) -> None:
        raise NotImplementedError

    def get(self, id: str) -> AccountHolder:
        raise NotImplementedError

    def list(self) -> List[AccountHolder]:
        raise NotImplementedError
