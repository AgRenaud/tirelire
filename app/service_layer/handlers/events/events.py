from app.domain import events
from typing import Callable


def publish_added_operation(event: events.OperationAdded, publish: Callable):
    publish("new_operation", event)