import uuid
import logging

from fastapi import APIRouter, HTTPException

from app.entrypoints.api import schema
from app.domain import commands, model
from app.service_layer import handlers
from app.adapters.redis_event_publisher import publish
from app.bootstrap import bootstrap


logger = logging.getLogger(__name__)

uow = bootstrap()

router = APIRouter()


def create_id() -> str:
    return str(uuid.uuid4())


@router.post("/create_user")
def create_user(new_user: schema.CreateUser):
    cmd = commands.CreateUser(
        id=new_user.user_id,
        password=new_user.password
    )
    try:
        return handlers.create_user(cmd, uow, publish)
    except model.EmailAlreadyExists as e:
        logger.error(f"The following error occurs : {e}")
        raise HTTPException(status_code=400, detail="Email already exists")
    except Exception as e:
        logger.error(f"The following error occurs : {e}")
        raise HTTPException(status_code=500, detail="Unexpected error")


@router.post("/authenticate")
def authenticate(form: schema.Authentication):
    cmd = commands.Authenticate(
        user_id=form.user_id,
        password=form.password,
    )
    return handlers.get_token(cmd, uow)


@router.post("/verify_token")
def verify_token(form: schema.TokenVerification):
    cmd = commands.VerifyToken(
        token=form.token,
    )
    return handlers.verify_token(cmd, uow)
