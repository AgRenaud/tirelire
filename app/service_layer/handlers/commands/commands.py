from typing import List, Callable
from uuid import uuid4

from app.domain import commands
from app.domain.model import Holder, Account, Operation, Currency, Category
from app.service_layer.unit_of_work import AbstractUnitOfWork



def add_holder(cmd: commands.CreateHolder, uow: AbstractUnitOfWork) -> None:
    with uow:
        holder = Holder(cmd.holder_id, [])
        uow.holders.add(holder)
        uow.commit()


def add_account(cmd: commands.CreateAccount, uow: AbstractUnitOfWork) -> None:
    with uow:
        account = Account(cmd.account_id, Currency[cmd.currency], [])
        holder: Holder = uow.holders.get(cmd.holder_id)
        holder.create_account(account)
        uow.commit()


def add_operations(cmd: commands.AddOperations, uow: AbstractUnitOfWork) -> Account:
    with uow:
        holder: Holder = uow.holders.get(cmd.holder_id)
        account: Holder = holder.get_account_by_id(cmd.account_id)
        if account is None:
            raise ValueError
        for operation in cmd.operations: 
            new_operation = Operation(
                operation.name,
                operation.date,
                operation.value,
                Currency[operation.currency],
                Category[operation.category] if operation.category else None
                )
            holder.add_operation_to_account(cmd.account_id, new_operation)
        uow.commit()
