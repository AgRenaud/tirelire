from app.domain import commands, events
from app.service_layer.handlers.commands import add_holder, add_account, add_operations 
from app.service_layer.handlers.events import publish_added_operation


EVENT_HANDLERS = {
    events.OperationAdded: [publish_added_operation]
}

COMMAND_HANDLERS = {
    commands.CreateHolder: add_holder,
    commands.CreateAccount: add_account,
    commands.AddOperations: add_operations,
}
