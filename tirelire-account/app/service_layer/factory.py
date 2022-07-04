from functools import partial

from app.service_layer.messagebus import MessageBus
from app.service_layer.unit_of_work import SQLAlchemyUnitOfWork
from app.service_layer.session_factory import DEFAULT_SESSION_FACTORY
from app.service_layer.handlers.handlers import EVENT_HANDLERS, COMMAND_HANDLERS

SQL_ALCHEMY_UOW_FACTORY = partial(SQLAlchemyUnitOfWork, DEFAULT_SESSION_FACTORY)

MESSAGE_BUS_FACTORY = partial(
    MessageBus,
    event_handlers=EVENT_HANDLERS,
    command_handlers=COMMAND_HANDLERS,
)
