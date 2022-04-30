import logging
import redis



class RedisSessionManager:

    def __init__(self, host, port, password):
        self.client = redis.Redis(decode_responses=True, host=host, port=port, password=password)

    def create_session(self, uid: str, token: str, expire_time_in_seconds: int) -> None:
        self.client.set(name=uid, value=token, ex=expire_time_in_seconds)

    def check_session(self, uid: str):
        self.client.get(name=uid)
