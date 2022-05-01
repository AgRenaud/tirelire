import redis


class RedisSessionManager:

    def __init__(self, host, port, password):
        self.client = redis.Redis(decode_responses=True, host=host, port=port, password=password)

    def create_session(self, uid: str, token: str, expire_time_in_seconds: int) -> None:
        self.client.hmset(name=uid, mapping={"token": token})
        self.client.expire(name=uid, time=expire_time_in_seconds)

    def get_session(self, uid: str) -> dict:
        return self.client.hgetall(name=uid)

    def delete_session(self, uid: str) -> None:
        self.client.delete(uid)
