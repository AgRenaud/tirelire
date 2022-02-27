from dataclasses import dataclass
from datetime import date
from typing import List

from app.domain.model.operation import Operation
from app.domain.model.currency import Currency
from app.domain.model.category import Category
from app.domain.events import events


@dataclass
class Account:
    id: str
    currency: Currency
    operations: List[Operation]

    def __hash__(self):
        return hash(self.id)

    def add_operation(self, new_operation: Operation) -> None:
        if not new_operation.currency == self.currency:
            raise ValueError(
                f"Wrong currency ! Need {self.currency} get {new_operation.currency}"
            )
        self.operations.append(new_operation)

    def compute_balance(self) -> float:
        balance = 0.0
        for operation in self.operations:
            balance += operation.value
        return balance

    def compute_category_balance(self, category: Category) -> float:
        balance = 0.0
        category_operations = [
            operation for operation in self.operations if operation.category == category
        ]
        for operation in category_operations:
            balance += operation.value
        return balance
