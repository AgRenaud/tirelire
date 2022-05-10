from sqlalchemy.orm import Session

from app.service_layer.unit_of_work.unit_of_work import UnitOfWork
from app.service_layer.unit_of_work.default_factory import (
    DEFAULT_SESSION_FACTORY,
)
from app.adapters.repository import UserRepository


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(
        self,
        session_factory=DEFAULT_SESSION_FACTORY,
    ):
        self.session_factory = session_factory

    def __enter__(self):
        self.session: Session = self.session_factory()
        self.users = UserRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
