from typing import List, Optional, Protocol

from app.service.account.account_service_dto import AccountReadModel


class AccountQueryService(Protocol):
    """AccountQueryService defines a query service inteface related Account entity."""

    def find_by_id(self, id: str) -> Optional[AccountReadModel]:
        raise NotImplementedError

    def find_all(self) -> List[AccountReadModel]:
        raise NotImplementedError
