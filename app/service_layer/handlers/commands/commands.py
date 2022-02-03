
from app.domain import commands, events, model

from typing import List, Callable

from app.service_layer.unit_of_work import AbstractUnitOfWork


def add_account(event: events.CreateAccount, uow: AbstractUnitOfWork) -> model.Account:
    with uow:
        account = model.Account(event.id, model.Currency[event.currency], [])
        uow.accounts.add(account)
        uow.commit()
    return account


def add_operations(account_id: str, operations: List, uow: AbstractUnitOfWork) -> float:
    with uow:
        account: model.Account = uow.accounts.get(account_id)
        for operation in operations:
            account.add_operation(**operation)
        uow.commit()

def publish_operation_added_event(event: events.OperationAdded, publish: Callable) -> None:
    publish("operation_added", event)