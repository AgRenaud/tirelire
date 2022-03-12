from typing import Callable

from app.domain.model import User, commands, events
from app.service_layer.unit_of_work import UnitOfWork
from app.adapters.redis_event_publisher import publish


def create_user(
    command: commands.CreateUser, uow: UnitOfWork, publish: Callable
) -> None:
    with uow:
        new_user = User(
            command.id,
            command.username,
            uow.auth_service.encrypt_password(command.password),
            command.first_name,
            command.last_name,
            command.email,
        )
        uow.users.add(new_user)
    publish("add_user", events.UserAdded(new_user.id))


def add_app_auth_to_user(
    command: commands.AddAuthorizationToUser, uow: UnitOfWork
) -> None:
    with uow:
        user = uow.users.get(command.user_id)
        user.add_app_auth(command.auth)


def get_token(command: commands.Authenticate, uow: UnitOfWork) -> dict:
    with uow:
        user = uow.users.get_by_email(command.email)
        token = uow.auth_service.generate_token(command.password, user)
    return token


def verify_token(command: commands.VerifyToken, uow: UnitOfWork):
    with uow:
        is_signed = uow.auth_service.verify_token(command.token)
    return is_signed
