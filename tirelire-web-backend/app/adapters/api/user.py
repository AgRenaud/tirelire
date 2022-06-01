import requests

from datetime import date
from typing import Protocol


class UserGateway(Protocol):
    url: str

    def register(self, uid: str, first_name: str, last_name: str, birthdate: date, email: str):
        raise NotImplementedError

    def get_current_user(self):
        raise NotImplementedError


class UserTirelire:

    url: str
    
    def __init__(self, url: str):
        self.url = url

    def register(self, uid: str, first_name: str, last_name: str, birthdate: date, email: str) -> None:
        url = f"{self.url}/api/v1/users/"
        
        payload = {
            "id": uid,
            "first_name": first_name,
            "last_name": last_name,
            "birthdate": birthdate,
            "email": email
        }

        req = requests.post(url, json=payload)

        if not req.ok:
            raise RuntimeError('Unable to create User')

    def get_current_user(self):
        url = f"{self.url}/api/v1/users/me"

        req = requests.get(url)

        if not req.ok:
            raise RuntimeError('Unable to get User')
