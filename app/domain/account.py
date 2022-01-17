from dataclasses import dataclass
from typing import List

from app.domain.transaction import Transaction, Value
from app.domain.currency import Currency


@dataclass
class Account:
    id: str
    currency: Currency
    transactions: List[Transaction]

    def add_transaction(self, new_transaction: Transaction) -> None:
        if not new_transaction.currency == self.currency:
            raise ValueError(
                f"Wrong currency ! Need {self.currency} get {new_transaction.currency}")
        self.transactions.append(new_transaction)

    def compute_balance(self) -> Value:
        balance = Value(0.0, self.currency)
        for transaction in self.transactions:
            balance += transaction.value
        return balance
