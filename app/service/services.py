import uuid

from typing import List

from app.domain import Account, Currency, Category
from app.service.unit_of_work import AccountUnitOfWork


def add_account(currency: str, uow: AccountUnitOfWork) -> Account:
    with uow:
        account = Account(uuid.uuid4(), Currency[currency], [])
        uow.accounts.add(account)
        uow.commit()
    return account


def compute_balance(account_id: str, uow: AccountUnitOfWork) -> float:
    with uow:
        account = uow.accounts.get(account_id)
        balance = account.compute_balance()
    return balance


def compute_category_balance(account_id: str, category: str, uow: AccountUnitOfWork) -> float:
    with uow:
        account: Account = uow.accounts.get(account_id)
        balance = account.compute_category_balance(Category[category])
    return balance

def add_transactions(account_id: str, transactions: List, uow: AccountUnitOfWork) -> float:
    with uow:
        account: Account = uow.accounts.get(account_id)
        for transaction in transactions:
            account.add_transaction(**transaction)
        uow.commit()
