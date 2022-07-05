import abc

from app.service_layer.unit_of_work.default_factory import (
    DEFAULT_SESSION_FACTORY,
)
from app.adapters.repository import AbstractUserRepository, UserRepository


class UnitOfWork(abc.ABC):
    users: AbstractUserRepository

    def __enter__(self) -> "UnitOfWork":
        return self

    def __exit__(self, exn_type, exn_value, traceback):
        if exn_type is None:
            self.commit()
        else:
            self.rollback()
            raise traceback

    def commit(self):
        self._commit()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
