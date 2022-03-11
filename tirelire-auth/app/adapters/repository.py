from sqlalchemy.orm import Session
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


class UserRepository:
    def __init__(self, session):
        self.session: Session = session
        self.seen = set()

    def add(self, user: User) -> None:
        self.session.add(user)

    def get(self, id: str) -> User:
        user = self.session.query(User).filter_by(id=id).one()
        if user:
            self.seen.add(user)
        return user

    def get_by_email(self, email: str) -> User:
        user = self.session.query(User).filter_by(email=email).one()
        if user:
            self.seen.add(user)
        return user

    def list(self) -> List[User]:
        return self.session.query(User).all()
