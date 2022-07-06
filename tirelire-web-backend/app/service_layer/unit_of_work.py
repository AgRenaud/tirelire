import abc


class AbstractUnitOfWork(abc.ABC):
    is_commited: bool

    def __enter__(self) -> "AbstractUnitOfWork":
        self.is_commited = False
        return self

    def __exit__(self, exn_type, exn_value, traceback):
        if exn_type is None:
            self.commit()
        else:
            self.rollback()
            

    def commit(self):
        self._commit()
        self.is_commited = True

    def rollback(self):
        self._rollback()
        self.is_commited = False

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _rollback(self):
        raise NotImplementedError


class UnitOfWork(AbstractUnitOfWork):
    def _commit(self):
        pass

    def _rollback(self):
        pass