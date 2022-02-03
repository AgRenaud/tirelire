from uuid import uuid4

from typing import List

from app.domain.model import AccountHolder, Account, Operation, Currency, Category
from app.service_layer.unit_of_work import AbstractAccountHolderUnitOfWork

class AccountHolderService:

    def __init__(self, uow: AbstractAccountHolderUnitOfWork):
        self.uow = uow

    @staticmethod
    def _new_id() -> str:
        return str(uuid4())

    def add_account_holder(self) -> AccountHolder:
        with self.uow as uow:
            account_holder = AccountHolder(self._new_id(), [])
            uow.account_holders.add(account_holder)
            uow.commit()
        return account_holder

    def add_account(self, account_holder_id: str, currency: str) -> Account:
        with self.uow as uow:
            account = Account(self._new_id(), currency, [])
            account_holder: AccountHolder = uow.account_holders.get(account_holder_id)
            account_holder.create_account(account)
            uow.commit()
        return account

    def add_operations(self, account_holder_id: str, account_id: str, operations: List[dict]) -> Account:
        with self.uow as uow:
            account_holder: AccountHolder = uow.account_holders.get(account_holder_id)
            account = account_holder.get_account_by_id(account_id)
            print(account)
            for operation in operations:
                new_operation = Operation(operation['name'], operation['date'], operation['value'], Currency[operation['currency']])
                account.add_operation(new_operation)
            uow.commit()
        return None
