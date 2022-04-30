from typing import Protocol


class SessionManager(Protocol):

    def create_session(self, uid: str, token: str, expire_time_in_seconds: int) -> None:
        raise NotImplementedError

    def get_session(self, uid: str) -> str:
        raise NotImplementedError
