from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

from app.entrypoints.api.routers.v1._router import _router


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
v1_router = APIRouter()

v1_router.include_router(_router, prefix='/v1')
