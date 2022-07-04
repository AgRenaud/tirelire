import logging
import redis

from uuid import uuid4
from dataclasses import asdict

from app import config
from app.domain import events


logger = logging.getLogger(__name__)

r = redis.Redis(decode_responses=True, **config.get_redis_config())


def publish(channel: str, event: events.Event):
    logger.info("publishing: channel=%s, event=%s", channel, event)
    res = r.xadd(channel, asdict(event))


class RedisConnector:
    def __init__(self, redis_api):
        self.redis_api = redis.Redis(redis_api)
        self.consumer_id = str(uuid4())

    def publish(self, channel: str, event: events.Event):
        logger.info("publishing: channel=%s, event=%s", channel, event)
        res = self.redis_api.xadd(channel, asdict(event))

    def get_events_batche(self, group: str, streams: dict):
        logger.info("Consumer %s subscribe to group=%s", self.consumer_id, group)
        events_batch = r.xreadgroup(group, self.consumer_id, streams, block=10000)
        return events_batch
