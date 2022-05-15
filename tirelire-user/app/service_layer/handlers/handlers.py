from typing import Callable
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from app.domain import model, commands, events
from app.service_layer.unit_of_work import UnitOfWork


def create_user(
    command: commands.CreateUser, uow: UnitOfWork, publish: Callable
) -> None:
    try:
        with uow:
            new_user = model.User(
                id=command.id,
                first_name=command.first_name,
                last_name=command.last_name,
                birthdate=command.birthdate,
                email=command.email,
            )
            uow.users.add(new_user)
        publish("add_user", events.UserAdded(new_user.id))
        return {"message": "User has been created"}
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            raise model.EmailAlreadyExists
        else:
            raise Exception("Unknown exception")
