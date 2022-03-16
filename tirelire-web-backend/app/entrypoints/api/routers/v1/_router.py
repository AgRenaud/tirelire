from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.entrypoints.api.routers.v1 import schemas

_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@_router.post('/register')
def register(register_form: schemas.RegisterForm):
    print(register_form)
    return 200


@_router.post('/token')
def register(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data}