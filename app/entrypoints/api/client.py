import logging

from fastapi import FastAPI

from app import config
from app.entrypoints.api.routers import router_holder
from app.adapters import orm

logger = logging.getLogger(__name__)


def create_app():

    config.set_up_loggers()

    orm.set_up_db(config.get_postgres_uri())
    app = FastAPI()

    logger.info("Add router")
    app.include_router(router_holder, prefix="/v1")

    return app
