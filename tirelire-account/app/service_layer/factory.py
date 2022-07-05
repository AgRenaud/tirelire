from functools import partial

from redis import Redis

from app import config
from app.service_layer.unit_of_work import SQLAlchemyUnitOfWork
from app.service_layer.session_factory import DEFAULT_SESSION_FACTORY

SQL_ALCHEMY_UOW_FACTORY = partial(SQLAlchemyUnitOfWork, DEFAULT_SESSION_FACTORY)

REDIS_FACTORY = partial(Redis, decode_responses=True, **config.get_redis_config())

REDIS_LISTENER_FACTORY = partial(Redis, decode_responses=True, **config.get_redis_config())