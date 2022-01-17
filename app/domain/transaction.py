from dataclasses import dataclass

from app.domain.currency import Currency
from app.domain.category import Category


@dataclass
class Value:
    amount: float
    currency: Currency = Currency.EUR
    category: Category = Category.UNKNOWN

    def __add__(self, other):
        if not other.currency == self.currency:
            raise ValueError(
                f"Wrong currency ! Need {self.currency} get {other.currency}")
        return Value(self.amount + other.amount, self.currency)

@dataclass
class Transaction:
    id: str
    name: str
    value: Value
