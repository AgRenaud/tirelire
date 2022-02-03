from dataclasses import dataclass
from datetime import date

from app.domain.model.category import Category
from app.domain.model.currency import Currency


@dataclass
class Operation:
    name: str
    date: date
    value: float
    currency: Currency
    category: Category = Category.UNKNOWN
