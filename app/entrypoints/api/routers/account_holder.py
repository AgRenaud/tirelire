from fastapi import APIRouter

from app.entrypoints.api.schemas import input
from app.service_layer.services import AccountHolderService
from app.service_layer.unit_of_work import AccountHolderUnitOfWorkImplem
from app import views


router = APIRouter(
    prefix="/account_holders",
    tags=["account_holders"]
)

@router.post('/')
def add_account_holder():
    service = AccountHolderService(AccountHolderUnitOfWorkImplem())
    return service.add_account_holder()

@router.get('/{account_holder_id}')
def get_account_holder_by_id(account_holder_id: str):
    return views.account_holder.get_account_holder_by_id(
        account_holder_id, AccountHolderUnitOfWorkImplem()
    )

@router.post('/{account_holder_id}/accounts')
def add_account_to_account_holder(account_holder_id: str, input: input.AddAccount):
    service = AccountHolderService(AccountHolderUnitOfWorkImplem())
    return service.add_account(account_holder_id, input.currency)

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
    service = AccountHolderService(AccountHolderUnitOfWorkImplem())
    return service.add_operations(account_holder_id, account_id, input.operations)

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
