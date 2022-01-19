from typing import Protocol, Optional

from app.domain.transaction.transaction import Transaction


class TransactionRepository(Protocol):
    """AccountRepository defines a repository interface for Account entity."""

    def create(self, transaction: Transaction) -> Optional[Transaction]:
        raise NotImplementedError

    def find_by_id(self, id: str) -> Optional[Transaction]:
        raise NotImplementedError

    def update(self, transaction: Transaction) -> Optional[Transaction]:
        raise NotImplementedError

    def delete_by_id(self, id: str):
        raise NotImplementedError
