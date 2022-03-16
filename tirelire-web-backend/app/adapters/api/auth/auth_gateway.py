from typing import Protocol


class AuthGateway(Protocol):
    url: str

    def create_user( self, first_name: str, last_name: str, email: str, password: str):
        raise NotImplementedError

    def authenticate(self):
        raise NotImplementedError
