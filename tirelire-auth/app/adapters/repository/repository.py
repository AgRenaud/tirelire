from typing import Protocol, List, Set

from app.domain.model import User


class AbstractUserRepository(Protocol):
    seen: Set[User]

    def add(self, account: User) -> None:
        raise NotImplementedError

    def get(self, id: str) -> User:
        raise NotImplementedError

    def get_by_email(self, email: str) -> User:
        raise NotImplementedError

    def list(self) -> List[User]:
        raise NotImplementedError
