import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, close_all_sessions, registry

from app.domain.model import Holder
from app.adapters.repository import HolderRepositoryImplem
from app.adapters.orm import start_mappers



class TestAccountRepository:

        def test_added_holder_must_be_queryable(self, Session):
            repo = HolderRepositoryImplem(Session())
            holder: Holder = Holder('XXX', [])
            repo.add(holder)
            assert repo.get('XXX') == holder
            assert repo.list() == [holder]
