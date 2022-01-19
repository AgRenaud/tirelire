import datetime

from sqlalchemy import Column, Integer, DateTime, Enum
from sqlalchemy.orm import relationship
from typing import List

from app.infrastructure.persistence.db.engine.database import Base
from app.domain import Account, Currency, Transaction


class AccountORM(Base):

    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    currency = Column(Enum(Currency))
    updated_at = Column(DateTime, default=datetime.datetime.now)
    created_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    transactions = relationship('TransactionORM', uselist=True)

    def to_entity(self) -> Account:
        return Account(
            id=self.id,
            currency=self.currency,
            transactions=self._get_transactions_entity())

    def _get_transactions_entity(self) -> List[Transaction]:
        return [
            transaction.to_entity() for transaction in self.transactions
        ]
