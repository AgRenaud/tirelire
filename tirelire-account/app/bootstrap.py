import inspect

from typing import Callable
from sqlalchemy.orm import registry
from sqlalchemy.exc import ArgumentError

from app import config
from app.adapters import orm
from app.service_layer import handlers
from app.service_layer.messagebus import MessageBus 
from app.service_layer.unit_of_work import AbstractUnitOfWork


def bootstrap(
    uow: AbstractUnitOfWork,
    publish: Callable,
    start_orm: bool = True,
) -> MessageBus:

    if start_orm:
        mapper_registry = registry()
        try:
            orm.start_mappers(mapper_registry)
        except ArgumentError:
            print("Mapper already exists")
        orm.set_up_db(config.get_postgres_uri(), mapper_registry)

    dependencies = {"uow": uow, "publish": publish}
    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies) for handler in event_handlers
        ]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters  # Inspect handler arguments
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }  # Match handler arguments by name
    return lambda message: handler(message, **deps)  # Inject argument as kwargs
