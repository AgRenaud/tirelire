import uuid
import logging

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer

from app.entrypoints.api import schema
from app.domain import commands, model
from app.service_layer import handlers
from app.adapters.redis_event_publisher import publish
from app.bootstrap import bootstrap


logger = logging.getLogger(__name__)

uow = bootstrap()

bearer_token = HTTPBearer()

router = APIRouter()


def create_id() -> str:
    return str(uuid.uuid4())


@router.post("/users/")
def register(new_user: schema.User):
    cmd = commands.CreateUser(
        id=new_user.id,
        first_name=new_user.first_name,
        last_name=new_user.last_name,
        birthdate=new_user.birthdate,
        email=new_user.email,
        
    )
    try:
        return handlers.create_user(cmd, uow, publish)
    except model.EmailAlreadyExists as e:
        logger.error(f"The following error occurs : {e}")
        raise HTTPException(status_code=400, detail="Email already exists")
    except Exception as e:
        logger.error(f"The following error occurs : {e}")
        raise HTTPException(status_code=500, detail="Unexpected error")


@router.get("/users/me")
def get_currnet_user(bearer: str = Depends(bearer_token)):
    return {
        "first_name": "John",
        "last_name": "Doe"
    }
