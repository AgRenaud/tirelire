import datetime

from sqlalchemy import (
    Table,
    Column,
    DateTime,
    Date,
    Text,
    create_engine,
)
from sqlalchemy.orm import registry

from app.domain.model import User


mapper_registry = registry()


users = Table(
    "users",
    mapper_registry.metadata,
    Column("id", Text, primary_key=True),
    Column("password", Text),
    Column("first_name", Text),
    Column("last_name", Text),
    Column("birthdate", Date),
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
    user_mapper = mapper_registry.map_imperatively(User, users)


def set_up_db(uri: str) -> None:
    engine = create_engine(uri)
    mapper_registry.metadata.create_all(engine)
