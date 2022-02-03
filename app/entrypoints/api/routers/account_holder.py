from fastapi import APIRouter
from uuid import uuid4

from app.domain import commands
from app.entrypoints.api.schemas import input
from app.service_layer.unit_of_work import AccountHolderUnitOfWorkImplem
from app import views, bootstrap


bus = bootstrap.bootstrap()


router = APIRouter(
    prefix="/account_holders",
    tags=["account_holders"]
)


def create_id():
    return str(uuid4())


@router.post('/')
def add_account_holder():
    new_id = create_id()
    cmd = commands.CreateAccountHolder(new_id)
    bus.handle(cmd)
    return {'account_holder_id': new_id}

@router.get('/{account_holder_id}')
def get_account_holder_by_id(account_holder_id: str):
    return views.account_holder.get_account_holder_by_id(
        account_holder_id, AccountHolderUnitOfWorkImplem()
    )

@router.post('/{account_holder_id}/accounts')
def add_account_to_account_holder(account_holder_id: str, input: input.AddAccount):
    new_id = create_id()
    cmd = commands.CreateAccount(account_holder_id, new_id, input.currency)
    bus.handle(cmd)
    return {'account_holder_id': account_holder_id, 'account_id': new_id, 'currency': input.currency}

@router.get('/{account_holder_id}/accounts')
def get_all_accounts_of_account_holder(account_holder_id: str):
    return views.account_holder.get_accounts_of_account_holder(
        account_holder_id, AccountHolderUnitOfWorkImplem()
    )

@router.get('/{account_holder_id}/accounts/{account_id}')
def get_account_by_id(account_holder_id: str, account_id: str):
    return views.account_holder.get_account_by_id(
        account_holder_id, account_id, AccountHolderUnitOfWorkImplem()
    )

@router.delete('/{account_holder_id}/accounts/{account_id}')
def delete_an_account(account_holder_id: str, account_account_id: str):
    return {}

@router.post('/{account_holder_id}/accounts/{account_id}/operations')
def add_operations_to_an_account(account_holder_id: str, account_id: str, input: input.AddOperations):
    cmds = []
    for operation in input.operations:
        new_cmd = commands.AddOperation(
            operation.name, operation.date, operation.value, operation.currency, operation.category
        )
        print(new_cmd)
        cmds.append(new_cmd)
    cmd = commands.AddOperations(account_holder_id, account_id, cmds)
    bus.handle(cmd)
    return {'account_holder_id': account_holder_id, 'account_id': account_id, 'operations_added': len(cmds)}

@router.get('/{account_holder_id}/accounts/{account_id}/operations/{operation_id}')
def get_operation_by_id(account_holder_id: str, account_id: str, operation_id: str):
    return {}

@router.put('/{account_holder_id}/accounts/{account_id}/operations/{operation_id}')
def modify_operation_of_an_account(account_holder_id: str, account_id: str, operation_id: str):
    return {}

@router.delete('/{account_holder_id}/accounts/{account_id}/operations/{operation_id}')
def delete_operation_of_an_account(account_holder_id: str, account_id: str, operation_id: str):
    return {}

@router.get('/{account_holder_id}/accounts/{account_id}/operations')
def get_all_operations_of_an_account(account_holder_id: str, account_id: str):
    return {}
