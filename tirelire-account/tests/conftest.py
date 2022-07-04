import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker, close_all_sessions
from sqlalchemy.exc import ArgumentError

from app.adapters.orm import start_mappers


@pytest.fixture(scope="class")
def engine():
    engine = create_engine(f"sqlite://")
    yield engine
    engine.dispose()


@pytest.fixture(scope="class")
def Session(engine):
    mapper_registry = registry()
    try:
        start_mappers(mapper_registry)
    except ArgumentError:
        print("Mappers already exists")
    mapper_registry.metadata.create_all(engine)
    sess = sessionmaker(engine)
    yield sess
    close_all_sessions()