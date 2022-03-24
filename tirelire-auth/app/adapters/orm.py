import datetime

from sqlalchemy import (
    ForeignKey,
    Table,
    Column,
    Integer,
    DateTime,
    Enum,
    Text,
    create_engine,
)
from sqlalchemy.orm import relationship, registry

from app.domain.model import User, App, AppAuthorization

mapper_registry = registry()


applications = Table(
    "authorizations",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Enum(App)),
    Column("user_id", ForeignKey("users.id")),
    Column(
        "updated_at",
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    ),
    Column("created_at", DateTime, default=datetime.datetime.now),
)

users = Table(
    "users",
    mapper_registry.metadata,
    Column("id", Text, primary_key=True),
    Column("password", Text),
    Column("first_name", Text),
    Column("last_name", Text),
    Column("email", Text, unique=True),
    Column(
        "updated_at",
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    ),
    Column("created_at", DateTime, default=datetime.datetime.now),
)


def start_mappers():
    operation_mapper = mapper_registry.map_imperatively(AppAuthorization, applications)
    account_mapper = mapper_registry.map_imperatively(
        User,
        users,
        properties={
            "_applications_auth": relationship(operation_mapper, collection_class=set)
        },
    )


def set_up_db(uri: str) -> None:
    engine = create_engine(uri)
    mapper_registry.metadata.create_all(engine)
