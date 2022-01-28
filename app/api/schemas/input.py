from typing import List, Optional
from pydantic import BaseModel, validator
from enum import Enum
from datetime import date


class Currency(str, Enum):
    EUR = 'EUR'
    USD = 'USD'


class Category(str, Enum):
    HOUSING = "HOUSING"
    SALARY = "SALARY"
    TRANSFERS = "TRANSFERS"
    FOOD = "FOOD"
    CAFE_RESTAURANT_BAR = "CAFE_RESTAURANT_BAR"
    FOOD_DELIVERY = "FOOD_DELIVERY"
    ONLINE = "ONLINE"
    BOOK = "BOOK"
    HOBBIES_SPORT = "HOBBIES_SPORT"
    INSURANCE = "INSURANCE"
    LOAN = "LOAN"
    ELEC_HEAT_GAS = "ELEC_HEAT_GAS"
    TELEPHONE_TV_INTERNET = "TELEPHONE_TV_INTERNET"
    TRANSPORTATION = "TRANSPORTATION"
    UNKNOWN = "UNKNOWN"


class AddAccount(BaseModel):
    currency: Currency

    @validator('currency')
    def currency_to_string(cls, v):
        return Currency[v].value


class Transaction(BaseModel):
    name: str
    date: date
    value: float
    currency: Currency
    category: Optional[Category]

    @validator('currency')
    def currency_to_string(cls, v):
        return Currency[v].value

    @validator('category')
    def category_to_string(cls, v):
        return Category[v].value

class AddTransactions(BaseModel):
    transactions: List[Transaction]

    @validator('transactions')
    def transaction_to_dict(cls, transactions):
        return [dict(t) for t in transactions]

