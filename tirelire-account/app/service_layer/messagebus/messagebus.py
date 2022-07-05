import logging
from re import M

from typing import Callable, Dict, List, Type, TYPE_CHECKING

from app.domain import commands, events
from app.service_layer import unit_of_work


logger = logging.getLogger(__name__)

Message = commands.Command | events.Event


class MessageBus:

    queue: List[Message]

    def __init__(
        self,
        uow: unit_of_work.AbstractUnitOfWork,
        event_handlers: Dict[Type[events.Event], List[Callable]],
        command_handlers: Dict[Type[commands.Command], Callable],
    ):
        self.uow = uow
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers

    def handle(self, message: Message):
        self.queue = [message]
        self._handle()

    def _handle(self):
        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, events.Event):
                self._handle_event(message)
            elif isinstance(message, commands.Command):
                self._handle_command(message)
            else:
                raise Exception(f"{message} was not an Event or Command")

    def _handle_event(self, event: events.Event):
        for handler in self.event_handlers[type(event)]:
            try:
                logger.debug("handling event %s with handler %s", event, handler)
                handler(event)
                self.queue.extend([msg for msg in self.uow.collect_new_events()])
            except Exception:
                logger.exception("Exception handling event %s", event)
                continue

    def _handle_command(self, command: commands.Command):
        logger.debug("handling command %s", command)
        try:
            handler = self.command_handlers[type(command)]
            handler(command)
            self.queue.extend([msg for msg in self.uow.collect_new_events()])
        except Exception:
            logger.exception("Exception handling command %s", command)
            raise
