import inspect
from typing import Callable
from app.adapters import orm, redis_event_publisher
from app.service_layer import unit_of_work


def bootstrap(
    start_orm: bool = True,
    uow: unit_of_work.UnitOfWork = unit_of_work.SQLAlchemyUnitOfWork(),
) -> unit_of_work.UnitOfWork:

    if start_orm:
        orm.start_mappers()

    return uow
