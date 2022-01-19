from typing import Protocol, Optional

from app.domain.account.account import Account


class AccountRepository(Protocol):
    """AccountRepository defines a repository interface for Account entity."""

    def create(self, account: Account) -> Optional[Account]:
        raise NotImplementedError

    def find_by_id(self, id: str) -> Optional[Account]:
        raise NotImplementedError

    def update(self, account: Account) -> Optional[Account]:
        raise NotImplementedError

    def delete_by_id(self, id: str):
        raise NotImplementedError
