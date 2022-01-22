from typing import Protocol, List, Optional

from app.service.account.account_query_service import AccountQueryService, AccountReadModel


class AccountQueryUserCase(Protocol):
    """AccountQueryService defines a query usecase inteface related Account entity."""

    def fetch_book_by_id(self, id: str) -> Optional[AccountReadModel]:
        raise NotImplementedError

    def fetch_books(self) -> List[AccountReadModel]:
        raise NotImplementedError


class AccountQueryServiceImpl(AccountQueryUserCase):
    """AccountQueryServiceImpl implements a query usecases related Account entity."""

    def __init__(self, account_query_service: AccountQueryService):
        self.book_query_service: AccountQueryService = account_query_service

    def fetch_book_by_id(self, id: str) -> Optional[AccountReadModel]:
        try:
            book = self.account_query_service.find_by_id(id)
            if book is None:
                raise BookNotFoundError
        except:
            raise

        return book

    def fetch_books(self) -> List[BookReadModel]:
        try:
            books = self.book_query_service.find_all()
        except:
            raise

        return books