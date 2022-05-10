import logging

from fastapi import FastAPI

from app import config
from app.adapters import orm
from app.entrypoints.api.routers import router

logger = logging.getLogger(__name__)


def create_app():

    app = FastAPI()

    orm.set_up_db(config.get_postgres_uri())

    logger.info("Add /api/v1")
    app.include_router(router, prefix="/api/v1")

    return app
