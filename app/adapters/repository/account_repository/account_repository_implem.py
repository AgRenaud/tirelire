from typing import List
from app.domain.model import Account


class AccountRepositoryImplem:
    def __init__(self, session):
        self.session = session

    def add(self, account_holder: Account) -> None:
        self.session.add(account_holder)

    def get(self, id: str) -> Account:
        return self.session.query(Account).filter_by(id=id).one()

    def list(self) -> List[Account]:
        return self.session.query(Account).all()
