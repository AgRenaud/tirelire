import logging

from fastapi import FastAPI

from app import config
from app.entrypoints.api.settings import settings
from app.entrypoints.api.routers import v1_router

logger = logging.getLogger(__name__)


def create_app():

    config.set_up_loggers()

    app = FastAPI(
        title=settings.app_name,
        description=settings.description,
        version=settings.version
    )

    logger.info("Add router")
    app.include_router(v1_router, prefix="/api")
    

    return app
