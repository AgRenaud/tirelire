import abc

from itertools import chain

from app.service_layer.session_factory import DEFAULT_SESSION_FACTORY
from app.adapters.repository import HolderRepository, HolderRepositoryImplem


class AbstractUnitOfWork(abc.ABC):
    holders: HolderRepository

    def __enter__(self) -> "AbstractUnitOfWork":
        return self

    def __exit__(self, exn_type, exn_value, traceback):
        if exn_type is None:
            self.commit()
        else:
            self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for holder in self.holders.seen:
            while holder.events:
                yield holder.events.pop(0)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class SQLAlchemyUnitOfWorkImplem(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.holders = HolderRepositoryImplem(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
