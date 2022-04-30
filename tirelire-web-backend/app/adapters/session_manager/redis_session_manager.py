import logging
import redis



class RedisSessionManager:

    def __init__(self, client: redis.Redis):
        self.client = client

    def create_session(self, uid: str, token: str, expire_time_in_seconds: int) -> None:
        self.client.set(key=uid, value=token, ex=expire_time_in_seconds)

    def check_session(self, uid: str):
        self.client.get(name=uid)
