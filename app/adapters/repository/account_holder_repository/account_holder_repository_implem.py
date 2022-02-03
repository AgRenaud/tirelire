from typing import List
from app.domain.model import AccountHolder


class AccountHolderRepositoryImplem:
    def __init__(self, session):
        self.session = session

    def add(self, account_holder: AccountHolder) -> None:
        self.session.add(account_holder)

    def get(self, id: str) -> AccountHolder:
        return self.session.query(AccountHolder).filter_by(id=id).one()

    def list(self) -> List[AccountHolder]:
        return self.session.query(AccountHolder).all()
