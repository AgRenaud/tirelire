from sqlalchemy.orm import Session
from typing import List

from app.domain.model import Account


class AccountRepositoryImplem:
    def __init__(self, session):
        self.session: Session = session
        self.seen = set()

    def add(self, holder: Account) -> None:
        self.session.add(holder)

    def get(self, id: str) -> Account:
        account = self.session.query(Account).filter_by(id=id).one()
        self.seen.add(account)
        return account

    def list(self) -> List[Account]:
        return self.session.query(Account).all()
