import logging
import redis

from uuid import uuid4

from app import bootstrap, config
from app.service_layer import messagebus
from app.adapters.event_publisher import RedisConnector

logger = logging.getLogger(__name__)


GROUP_NAME = "auth_service"

STREAMS = {"add_user": ">"}


def main():
    logger.info("Start redis listener")

    redis_pool = redis.ConnectionPool(
        **config.get_redis_config(), decode_responses=True
    )
    r = redis.Redis(connection_pool=redis_pool, decode_responses=True, charset="utf-8")
    redis_conn = RedisConnector(r)

    bus = bootstrap.bootstrap(start_orm=False)

    try:
        r.xgroup_create("add_user", GROUP_NAME, "$", True)
    except redis.exceptions.ResponseError as e:
        logger.warning("Redis XGroup already exists.")

    while True:
        events_batch = redis_conn.get_events_batche(GROUP_NAME, STREAMS)

        if len(events_batch) == 0:
            logger.info("No events")

        for event in events_batch:
            handle_events(event, bus)


def handle_events(event, bus: messagebus.MessageBus):
    stream, messages = event
    for message in messages:
        bus.handle(message)


if __name__ == "__main__":
    main()
