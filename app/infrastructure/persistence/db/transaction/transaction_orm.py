import datetime

from sqlalchemy import Column, Float, Integer, DateTime, Enum, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.infrastructure.persistence.db.engine.database import Base
from app.domain import Transaction, Currency, Category, Value


class TransactionORM(Base):

    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)
    amount = Column(Float)
    currency = Column(Enum(Currency))
    category = Column(Enum(Category))
    updated_at = Column(DateTime, default=datetime.datetime.now)
    created_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    account_id = Column(Integer, ForeignKey('account.id'))

    account = relationship(
        'AccountORM', 
        back_populates="transactions", 
        uselist=False)

    def to_entity(self) -> Transaction:
        return Transaction(
            id=self.id,
            name=self.name,
            date=self.date,
            value=Value(self.amount, self.currency), 
            category=self.category)