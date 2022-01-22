from pydantic import BaseModel,  Field
from typing import List

from app.domain import Account, Currency
from app.service.transaction import TransactionReadModel


class AccountReadModel(BaseModel):
    id: str
    currency: Currency
    transactions: List[TransactionReadModel]
    

    def from_entity(self, account: Account) -> "AccountReadModel":
        return AccountReadModel(
            id=account.id,
            currency=account.currency, 
            transactions=[
                TransactionReadModel.from_entity(transaction) 
                for transaction in account.transactions
            ]
        )
