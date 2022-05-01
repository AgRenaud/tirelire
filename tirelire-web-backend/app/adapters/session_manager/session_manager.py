from typing import Protocol

from requests import delete


class SessionManager(Protocol):

    def create_session(self, uid: str, token: str, expire_time_in_seconds: int) -> None:
        raise NotImplementedError

    def get_session(self, uid: str) -> dict:
        raise NotImplementedError

    def delete_session(self, uid: str) -> None:
        raise NotImplementedError