import json
import logging
import redis

from uuid import uuid4

from app import bootstrap, config
from app.adapters.redis_event_publisher import RedisConnector

logger = logging.getLogger(__name__)


redis_pool = redis.ConnectionPool(**config.get_redis_config(), decode_responses=True)
r = redis.Redis(connection_pool=redis_pool, decode_responses=True, charset="utf-8")
redis_conn = RedisConnector(r)

GROUP_NAME = "auth_service"
STREAMS = {"add_application": ">"}


def main():
    logger.info("Start redis listener")
    bus = bootstrap.bootstrap()
    
    try:
        r.xgroup_create("add_user", GROUP_NAME, "$", True)
    except redis.exceptions.ResponseError as e:
        logger.warning("Redis XGroup already exists.")

    try:
        r.xgroup_create("add_application", GROUP_NAME, "$", True)
    except redis.exceptions.ResponseError as e:
        logger.warning("Redis XGroup already exists.")


    while True:
        events_batch = redis_conn.get_events_batche(GROUP_NAME, STREAMS)

        if len(events_batch) == 0:
            logger.info("No events")

        for event in events_batch:
            handle_events(event, bus)


def handle_events(event, bus):
    stream, message = event
    print(str(stream))
    print(message)


if __name__ == "__main__":
    main()
