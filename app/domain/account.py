from dataclasses import dataclass
from datetime import date
from typing import List

from app.domain.transaction import Transaction
from app.domain.currency import Currency
from app.domain.category import Category


@dataclass
class Account:
    id: str
    currency: Currency
    transactions: List[Transaction]

    def __hash__(self):
        return hash(self.id)

    def add_transaction(self, name: str, date: date, value: float, currency: str, category: str) -> None:
        new_transaction = Transaction(name, date, value, Currency[currency], Category[category])
        if not new_transaction.currency == self.currency:
            raise ValueError(
                f"Wrong currency ! Need {self.currency} get {new_transaction.currency}")
        self.transactions.append(new_transaction)

    def compute_balance(self) -> float:
        balance = 0.0
        for transaction in self.transactions:
            balance += transaction.value
        return balance

    def compute_category_balance(self, category: Category) -> float:
        balance = 0.0
        category_transactions = [
            transaction for transaction in self.transactions 
            if transaction.category == category
        ] 
        for transaction in category_transactions:
            balance += transaction.value
        return balance
