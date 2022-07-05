import logging

from fastapi import FastAPI
from sqlalchemy.orm import registry

from app import config
from app.entrypoints.api.routers import router_holder

logger = logging.getLogger(__name__)


def create_app():

    config.set_up_loggers()

    app = FastAPI()

    logger.info("Add router")
    app.include_router(router_holder, prefix="/v1")

    return app
