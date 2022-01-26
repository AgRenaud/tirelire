import datetime

from sqlalchemy import ForeignKey, MetaData, Table, Column, Integer, DateTime, Enum, Text, Float,create_engine
from sqlalchemy.orm import mapper, relationship

from app.domain import Transaction, Account

from app.domain import Category, Currency

metadata = MetaData()

transactions = Table(
    'transactions',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text, nullable=False),
    Column("date", DateTime, nullable=False),
    Column("value", Float),
    Column("currency", Enum(Currency)),
    Column("category", Enum(Category)),
    Column("account_id", ForeignKey("accounts.id")), 
    Column("updated_at", DateTime, default=datetime.datetime.now),
    Column("created_at", DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now),
)

accounts = Table(
    'accounts',
    metadata,
     Column("id", Text, primary_key=True),
     Column("currency", Enum(Currency)),
     Column("updated_at", DateTime, default=datetime.datetime.now),
     Column("created_at", DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
)

def start_mappers():
    transaction_mapper = mapper(Transaction, transactions)
    account_mapper = mapper(Account, accounts,
        properties={
            "transactions": relationship(transaction_mapper)
        },
    )
    

def get_engine(uri):
    engine = create_engine(uri)
    metadata.create_all(engine, checkfirst=True)
    return engine
