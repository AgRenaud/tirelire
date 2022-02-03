import abc

from app.service_layer.unit_of_work.session_factory import DEFAULT_SESSION_FACTORY
from app.adapters.repository import AccountHolderRepository, AccountHolderRepositoryImplem


class AbstractAccountHolderUnitOfWork(abc.ABC):
    account_holders: AccountHolderRepository

    def __enter__(self) -> "AbstractAccountHolderUnitOfWork":
        return self

    def __exit__(self, exn_type, exn_value, traceback):
        if exn_type is None:
            self.commit()
        else:
            self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class AccountHolderUnitOfWorkImplem(AbstractAccountHolderUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.account_holders = AccountHolderRepositoryImplem(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
