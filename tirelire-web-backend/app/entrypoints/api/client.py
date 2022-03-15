import logging

from fastapi import FastAPI

from app import config

logger = logging.getLogger(__name__)


def create_app():

    config.set_up_loggers()

    app = FastAPI()

    logger.info("Add router")

    return app
