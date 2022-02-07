
from app.domain import commands, events, model

from typing import List, Callable

from uuid import uuid4

from typing import List

from app.domain.model import Holder, Account, Operation, Currency, Category
from app.service_layer.unit_of_work import AbstractHolderUnitOfWork



def add_holder(cmd: commands.CreateHolder, uow: AbstractHolderUnitOfWork) -> None:
    with uow:
        holder = Holder(cmd.holder_id, [])
        uow.holders.add(holder)
        uow.commit()


def add_account(cmd: commands.CreateAccount, uow: AbstractHolderUnitOfWork) -> None:
    with uow:
        account = Account(cmd.account_id, Currency[cmd.currency], [])
        holder: Holder = uow.holders.get(cmd.holder_id)
        holder.create_account(account)
        uow.commit()


def add_operations(cmd: commands.AddOperations, uow: AbstractHolderUnitOfWork) -> Account:
    with uow:
        account: Account = uow.accounts.get(cmd.account_id)
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
