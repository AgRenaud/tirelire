from dataclasses import dataclass
from datetime import date

from app.domain.category import Category
from app.domain.currency import Currency


@dataclass
class Transaction:
    name: str
    date: date
    value: float
    currency: Currency
    category: Category = Category.UNKNOWN
