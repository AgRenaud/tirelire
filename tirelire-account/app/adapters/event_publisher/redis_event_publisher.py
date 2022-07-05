import logging

from redis import Redis
from uuid import uuid4
from dataclasses import asdict

from app.domain import events


logger = logging.getLogger(__name__)


class RedisConnector:
    def __init__(self, redis_api: Redis):
        self.redis_api = redis_api
        self.consumer_id = str(uuid4())

    def publish(self, channel: str, event: events.Event):
        logger.info("publishing: channel=%s, event=%s", channel, event)
        res = self.redis_api.xadd(channel, asdict(event))

    def get_events_batche(self, group: str, streams: dict):
        logger.info("Consumer %s subscribe to group=%s", self.consumer_id, group)
        events_batch = self.redis_api.xreadgroup(group, self.consumer_id, streams, block=1000)
        return events_batch
