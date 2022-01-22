from pydantic import BaseModel
from datetime import date

from app.domain import Transaction, Currency, Category


class TransactionReadModel(BaseModel):
    id: str
    name: str
    date: date
    amount: float
    currency: Currency
    category: Category
 
    def from_entity(self, transaction: Transaction) -> "TransactionReadModel":
        return TransactionReadModel(
            id=transaction.id, 
            name=transaction.name, 
            date=transaction.date, 
            amount=transaction.amount, 
            currency=transaction.currency,
            category=transaction.category
        )