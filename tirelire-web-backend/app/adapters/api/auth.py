import requests

from typing import Protocol


class AuthGateway(Protocol):
    url: str

    def register(self, user_id: str, password: str) -> None : ...

    def authenticate(self) -> dict: ...


class UserAlreadyRegistered(Exception):

    def __init__(self, uid: str):
        self.uid = uid

    def __str__(self):
        return f"The following user is already registered {self.uid}"


class AuthTirelire:

    url: str
    
    def __init__(self, url: str):
        self.url = url

    def register( self, user_id: str, password: str) -> None:
        url = f"{self.url}/api/v1/create_user"
        payload = {
            "user_id": user_id,
            "password": password
        }
        req = requests.post(url, json=payload)

        status_code = req.status_code
            
        match status_code:
            case 200:
                pass
            case 400:
                self._register_exceptions()
            case _:
                raise Exception('Unexpected status code')


    def _register_exceptions(self, user_id: str, req: requests.Request):
        detail = req.json()["detail"]

        match detail:
            case "Email already exists":
                raise UserAlreadyRegistered(user_id)
            case _:
                raise Exception('Unexpected error message')

    
    def authenticate(
        self,
        user_id: str, password: str
    ) -> dict:
        url = f"{self.url}/api/v1/authenticate"
        payload = {
            "user_id": user_id,
            "password": password
        }
        req = requests.post(url, json=payload)

        if not req.ok:
            raise ValueError(f'Unable to authenticate. Response code: {req.status_code} ; content: {req.content}')
        
        res: dict = req.json()

        return res
