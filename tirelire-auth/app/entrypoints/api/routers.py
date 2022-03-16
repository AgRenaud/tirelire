import uuid
import logging

from fastapi import APIRouter, HTTPException

from app.entrypoints.api import schema
from app.domain import commands, model
from app.service_layer import handlers
from app.bootstrap import bootstrap


logger = logging.getLogger(__name__)

uow = bootstrap()

router = APIRouter()


def create_id() -> str:
    return str(uuid.uuid4())


@router.post("/create_user")
def create_user(new_user: schema.User):
    cmd = commands.CreateUser(
        id=create_id(),
        password=new_user.password,
        first_name=new_user.first_name,
        last_name=new_user.last_name,
        email=new_user.email,
    )
    try:
        return handlers.create_user(cmd, uow)
    except model.EmailAlreadyExists as e:
        logger.error(f'The following error occurs : {e}')
        raise HTTPException(status_code=400, detail="Email already exists")
    except Exception as e:
        logger.error(f'The following error occurs : {e}')
        raise HTTPException(status_code=500, detail="Unexpected error")


@router.post("/authenticate")
def authenticate(form: schema.Authentication):
    cmd = commands.Authenticate(
        email=form.email,
        password=form.password,
    )
    return handlers.get_token(cmd, uow)


@router.post("/verify_token")
def verify_token(form: schema.TokenVerification):
    cmd = commands.VerifyToken(
        token=form.token,
    )
    return handlers.verify_token(cmd, uow)
