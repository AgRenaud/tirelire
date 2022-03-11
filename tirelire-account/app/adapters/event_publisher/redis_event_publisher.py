import json
import logging
from dataclasses import asdict
import redis

from app import config
from app.domain import events


logger = logging.getLogger(__name__)

r = redis.Redis(decode_responses=True, **config.get_redis_config())


def publish(channel: str, event: events.Event):
    logger.info("publishing: channel=%s, event=%s", channel, event)
    res = r.xadd(channel, asdict(event))
