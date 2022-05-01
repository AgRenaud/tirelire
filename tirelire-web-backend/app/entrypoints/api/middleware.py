from fastapi import Request
from fastapi.responses import JSONResponse
from requests import session

from app import config
from app.adapters.session_manager import RedisSessionManager


class AuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        assert scope["type"] == "http"
        headers = dict(scope["headers"])
        cookies = parse_cookies(headers.get(b'cookie', None))
        cookie_session = cookies.get('tirelire-session')
        if cookie_session:
            session_manager = RedisSessionManager(*config.get_redis_session_manager_conf())
            token = session_manager.get_session(cookie_session)
            if token: 
                token = token.get('cookie')
                headers[b"authorization"] = f'Bearer {token}'.encode('utf-8')
        scope["headers"] = [(k, v) for k, v in headers.items()]
        await self.app(scope, receive, send)

def parse_cookies(cookies: str) -> dict:
    if not cookies:
        return {}
    cookies = cookies.decode("utf-8")
    cookies = [elt.split('=', 1) for elt in cookies.split(';')]
    return {k.strip(): v for k, v in cookies}
     