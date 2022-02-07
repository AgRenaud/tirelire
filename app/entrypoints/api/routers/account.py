from fastapi import APIRouter

from app.entrypoints.api.schemas import input
from app.service_layer import services
from app.service_layer.unit_of_work import AccountUnitOfWorkImplem
from app import views


router = APIRouter(
    prefix="/accounts",
    tags=["accounts"]
)

@router.post('/')
def create_account(input: input.AddAccount):
    new_account = services.add_account(input.currency, AccountUnitOfWorkImplem())
    return {"account_id": str(new_account.id)}

@router.get('/{account_id}')
def get_account_from_id(account_id: str):
    return views.account.get_account_by_id(account_id, AccountUnitOfWorkImplem())

@router.post('/{account_id}/operations')
def add_account_operations(account_id: str, operations: input.AddOperations, infer_category: bool = False):
    services.add_operations(account_id, operations.operations, AccountUnitOfWorkImplem())
    return {}

@router.get('/{account_id}/operations')
def get_account_operations(account_id: str, category: input.Category = None):
    if category:
        return views.account.get_account_category_operations(account_id, category, AccountUnitOfWorkImplem())    
    return views.account.get_account_operations(account_id, AccountUnitOfWorkImplem())
