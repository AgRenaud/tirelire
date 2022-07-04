from sqlalchemy.orm import Session

from app.service_layer.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.adapters.repository.holder_repository import HolderRepositoryImplem


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session: Session = self.session_factory()
        self.holders = HolderRepositoryImplem(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
