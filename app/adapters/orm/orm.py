import datetime

from sqlalchemy import ForeignKey, Table, Column, Integer, DateTime, Enum, Text, Float, create_engine
from sqlalchemy.orm import relationship, registry

from app.domain.model import Operation, Account, AccountHolder, Category, Currency

mapper_registry = registry()

operations = Table(
    'operations',
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
     Column("account_holder_id", ForeignKey("account_holders.id")), 
     Column("updated_at", DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now),
     Column("created_at", DateTime, default=datetime.datetime.now),
)

account_holders = Table(
    'account_holders',
    mapper_registry.metadata,
     Column("id", Text, primary_key=True),
     Column("updated_at", DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now),
     Column("created_at", DateTime, default=datetime.datetime.now),
)

def start_mappers():
    operation_mapper = mapper_registry.map_imperatively(
        Operation, operations)
    account_mapper = mapper_registry.map_imperatively(
        Account, accounts,
        properties={
            "operations": relationship(operation_mapper)
        },
    )
    account_holder_mapper = mapper_registry.map_imperatively(
        AccountHolder, account_holders,
        properties={
            "accounts": relationship(account_mapper)
        },
    )
    

def set_up_db(uri: str) -> None:
    engine = create_engine(uri)
    mapper_registry.metadata.create_all(engine)
