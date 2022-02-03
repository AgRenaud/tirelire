
from app.domain import commands, events, model

from typing import List, Callable

from uuid import uuid4

from typing import List

from app.domain.model import AccountHolder, Account, Operation, Currency, Category
from app.service_layer.unit_of_work import AbstractAccountHolderUnitOfWork



def add_account_holder(cmd: commands.CreateAccountHolder, uow: AbstractAccountHolderUnitOfWork) -> None:
    with uow:
        account_holder = AccountHolder(cmd.account_holder_id, [])
        uow.account_holders.add(account_holder)
        uow.commit()


def add_account(cmd: commands.CreateAccount, uow: AbstractAccountHolderUnitOfWork) -> None:
    with uow:
        account = Account(cmd.account_id, Currency[cmd.currency], [])
        account_holder: AccountHolder = uow.account_holders.get(cmd.account_holder_id)
        account_holder.create_account(account)
        uow.commit()


def add_operations(cmd: commands.AddOperations, uow: AbstractAccountHolderUnitOfWork) -> Account:
    with uow:
        account_holder: AccountHolder = uow.account_holders.get(cmd.account_holder_id)
        account = account_holder.get_account_by_id(cmd.account_id)
        for operation in cmd.operations: 
            new_operation = Operation(
                operation.name,
                operation.date,
                operation.value,
                Currency[operation.currency],
                Category[operation.category] if operation.category else None
                )
            account.add_operation(new_operation)
        uow.commit()
