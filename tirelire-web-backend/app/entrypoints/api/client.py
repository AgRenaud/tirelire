import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from app import config
from app.entrypoints.api.middleware import auth_middleware
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

    app.add_middleware(BaseHTTPMiddleware, dispatch=auth_middleware)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    logger.info("Add router")
    app.include_router(v1_router, prefix="/api")
    

    return app
