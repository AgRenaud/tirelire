from fastapi import APIRouter

from app.api.schemas import input
from app.service import services
from app.service.unit_of_work import AccountUnitOfWorkImplem
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

@router.get('/{account_id}/compute_balance')
def compute_balance(account_id: str, category: input.Category = None):
    if category:
        return services.compute_category_balance(account_id, category, AccountUnitOfWorkImplem())
    return services.compute_balance(account_id, AccountUnitOfWorkImplem())

@router.post('/{account_id}/transactions')
def add_account_transactions(account_id: str, transactions: input.AddTransactions, infer_category: bool = False):
    services.add_transactions(account_id, transactions.transactions, AccountUnitOfWorkImplem())
    return {}

@router.get('/{account_id}/transactions')
def get_account_transactions(account_id: str, category: input.Category = None):
    if category:
        return views.account.get_account_category_transactions(account_id, category, AccountUnitOfWorkImplem())    
    return views.account.get_account_transactions(account_id, AccountUnitOfWorkImplem())
