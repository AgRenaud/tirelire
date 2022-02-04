import abc

from itertools import chain

from app.service_layer.unit_of_work.session_factory import DEFAULT_SESSION_FACTORY
from app.adapters.repository import HolderRepository, HolderRepositoryImplem
from app.adapters.repository import AccountRepository, AccountRepositoryImplem


class AbstractHolderUnitOfWork(abc.ABC):
    holders: HolderRepository
    accounts: AccountRepository

    def __enter__(self) -> "AbstractHolderUnitOfWork":
        return self

    def __exit__(self, exn_type, exn_value, traceback):
        if exn_type is None:
            self.commit()
        else:
            self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        return chain(self._collect_accounts_events(), self._collect_holders_events())
    
    def _collect_holders_events(self):
        for holder in self.holders.seen:
            while holder.events:
                yield holder.events.pop(0)

    def _collect_accounts_events(self):
        for account in self.accounts.seen:
            while account.events:
                yield account.events.pop(0)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class HolderUnitOfWorkImplem(AbstractHolderUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.holders = HolderRepositoryImplem(self.session)
        self.accounts = AccountRepositoryImplem(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
