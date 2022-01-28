import datetime

from sqlalchemy import ForeignKey, Table, Column, Integer, DateTime, Enum, Text, Float, create_engine
from sqlalchemy.orm import relationship, registry

from app.domain import Transaction, Account

from app.domain import Category, Currency

mapper_registry = registry()

transactions = Table(
    'transactions',
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text, nullable=False),
    Column("date", DateTime, nullable=False),
    Column("value", Float),
    Column("currency", Enum(Currency)),
    Column("category", Enum(Category)),
    Column("account_id", ForeignKey("accounts.id")), 
    Column("updated_at", DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now),
    Column("created_at", DateTime, default=datetime.datetime.now),
)

accounts = Table(
    'accounts',
    mapper_registry.metadata,
     Column("id", Text, primary_key=True),
     Column("currency", Enum(Currency)),
     Column("updated_at", DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now),
     Column("created_at", DateTime, default=datetime.datetime.now),
)

def start_mappers():
    transaction_mapper = mapper_registry.map_imperatively(
        Transaction, transactions)
    account_mapper = mapper_registry.map_imperatively(
        Account, accounts,
        properties={
            "transactions": relationship(transaction_mapper)
        },
    )
    

def set_up_db(uri: str) -> None:
    engine = create_engine(uri)
    mapper_registry.metadata.create_all(engine)
