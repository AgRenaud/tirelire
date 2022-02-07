from fastapi import APIRouter
from uuid import uuid4

from app.domain import commands
from app.entrypoints.api.schemas import input
from app.service_layer.unit_of_work import HolderUnitOfWorkImplem
from app import views, bootstrap


bus = bootstrap.bootstrap()


router = APIRouter(
    prefix="/holders",
    tags=["holders"]
)


def create_id():
    return str(uuid4())


@router.post('/')
def add_holder():
    new_id = create_id()
    cmd = commands.CreateHolder(new_id)
    bus.handle(cmd)
    return {'holder_id': new_id}

@router.get('/{holder_id}')
def get_holder_by_id(holder_id: str):
    return views.holder.get_holder_by_id(
        holder_id, HolderUnitOfWorkImplem()
    )

@router.post('/{holder_id}/accounts')
def add_account_to_holder(holder_id: str, input: input.AddAccount):
    new_id = create_id()
    cmd = commands.CreateAccount(holder_id, new_id, input.currency)
    bus.handle(cmd)
    return {'holder_id': holder_id, 'account_id': new_id, 'currency': input.currency}

@router.get('/{holder_id}/accounts')
def get_all_accounts_of_holder(holder_id: str):
    return views.holder.get_accounts_of_holder(
        holder_id, HolderUnitOfWorkImplem()
    )

@router.get('/{holder_id}/accounts/{account_id}')
def get_account_by_id(holder_id: str, account_id: str):
    return views.holder.get_account_by_id(
        holder_id, account_id, HolderUnitOfWorkImplem()
    )

@router.delete('/{holder_id}/accounts/{account_id}')
def delete_an_account(holder_id: str, account_account_id: str):
    return {}

@router.post('/{holder_id}/accounts/{account_id}/operations')
def add_operations_to_an_account(holder_id: str, account_id: str, input: input.AddOperations):
    cmds = []
    for operation in input.operations:
        new_cmd = commands.AddOperation(
            operation.name, operation.date, operation.value, operation.currency, operation.category
        )
        cmds.append(new_cmd)
    cmd = commands.AddOperations(holder_id, account_id, cmds)
    bus.handle(cmd)
    return {'holder_id': holder_id, 'account_id': account_id, 'operations_added': len(cmds)}

@router.get('/{holder_id}/accounts/{account_id}/operations/{operation_id}')
def get_operation_by_id(holder_id: str, account_id: str, operation_id: str):
    return {}

@router.put('/{holder_id}/accounts/{account_id}/operations/{operation_id}')
def modify_operation_of_an_account(holder_id: str, account_id: str, operation_id: str):
    return {}

@router.delete('/{holder_id}/accounts/{account_id}/operations/{operation_id}')
def delete_operation_of_an_account(holder_id: str, account_id: str, operation_id: str):
    return {}

@router.get('/{holder_id}/accounts/{account_id}/operations')
def get_all_operations_of_an_account(holder_id: str, account_id: str):
    return {}
