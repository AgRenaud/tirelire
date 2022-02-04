from typing import Protocol, List, Set
from app.domain.model import Holder


class HolderRepository(Protocol):
    seen: Set[Holder]

    def add(self, account: Holder) -> None:
        raise NotImplementedError

    def get(self, id: str) -> Holder:
        raise NotImplementedError

    def list(self) -> List[Holder]:
        raise NotImplementedError
