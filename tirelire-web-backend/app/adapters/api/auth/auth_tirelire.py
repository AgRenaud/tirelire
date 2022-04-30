import requests


class AuthTirelire:
    
    def __init__(self, url: str):
        self.url = url

    def register( self, first_name: str, last_name: str, email: str, password: str) -> bool:
        url = f"{self.url}/api/v1/create_user"
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }
        req = requests.post(url, json=payload)

        if req.status_code != 200:
            return False
        return True

    def authenticate(
        self,
        email: str, password: str
    ) -> dict:
        url = f"{self.url}/api/v1/authenticate"
        payload = {
            "email": email,
            "password": password
        }
        req = requests.post(url, json=payload)
        if not req.ok:
            raise ValueError(f'Unable to authenticate. Response code: {req.status_code} ; content: {req.content}')
        
        return req.json()
