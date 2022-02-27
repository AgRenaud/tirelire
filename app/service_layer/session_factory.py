from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import config


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    ),
    expire_on_commit=False,
)
