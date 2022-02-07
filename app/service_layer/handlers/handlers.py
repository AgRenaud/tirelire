from app.domain import commands
from app.service_layer.handlers.commands import add_account_holder, add_account, add_operations 


EVENT_HANDLERS = {}

COMMAND_HANDLERS = {
    commands.CreateAccountHolder: add_account_holder,
    commands.CreateAccount: add_account,
    commands.AddOperations: add_operations,
}
