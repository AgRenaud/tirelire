import abc

from app.service_layer.unit_of_work.default_factory import (
    DEFAULT_SESSION_FACTORY,
    DEFAULT_AUTH_SERVICE_FACTORY,
)
from app.service_layer.auth_service import AuthService
from app.adapters.repository import AbstractUserRepository, UserRepository


class UnitOfWork(abc.ABC):
    users: AbstractUserRepository
    auth_service: AuthService

    def __enter__(self) -> "UnitOfWork":
        return self

    def __exit__(self, exn_type, exn_value, traceback):
        if exn_type is None:
            self.commit()
        else:
            self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for user in self.users.seen:
            while user.events:
                yield user.events.pop(0)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
