import requests

from datetime import date
from typing import Protocol


class AuthGateway(Protocol):
    url: str

    def register(self, user_id: str, password: str):
        raise NotImplementedError

    def authenticate(self):
        raise NotImplementedError


class AuthTirelire:

    url: str
    
    def __init__(self, url: str):
        self.url = url

    def register( self, user_id: str, password: str) -> bool:
        url = f"{self.url}/api/v1/create_user"
        payload = {
            "user_id": user_id,
            "password": password
        }
        req = requests.post(url, json=payload)

        if not req.ok:
            raise RuntimeError('Unable to create User')


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
        
        return req.json()
