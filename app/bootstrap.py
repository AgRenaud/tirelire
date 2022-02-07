import inspect
from typing import Callable
from app.adapters import orm
from app.service_layer import handlers, messagebus, unit_of_work


def bootstrap(
    start_orm: bool = True,
    uow: unit_of_work.AbstractAccountHolderUnitOfWork = unit_of_work.AccountHolderUnitOfWorkImplem(),
) -> messagebus.MessageBus:
    """
    TODO: 
        - Add (publish: Callable = redis_eventpublisher.publish)
        - dependencies ("publish": publish)
    """

    if start_orm:
        orm.start_mappers()

    dependencies = {"uow": uow}
    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies)
            for handler in event_handlers
        ]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return messagebus.MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency
        for name, dependency in dependencies.items()
        if name in params
    }
    return lambda message: handler(message, **deps)