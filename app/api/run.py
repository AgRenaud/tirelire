import logging

from fastapi import FastAPI

from app import config
from app.api.routers import router_account
from app.infrastructure import orm

logger = logging.getLogger(__name__)

def create_app():
    
    orm.start_mappers()
    orm.set_up_db(config.get_postgres_uri())

    app = FastAPI()

    logger.info('Add router')
    app.include_router(router_account)

    return app
