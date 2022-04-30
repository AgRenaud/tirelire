from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app import config
from app.model import commands
from app.entrypoints.api.routers.v1 import schemas
from app.adapters.api.auth import AuthTirelire
from app.service_layer.authentication_service import AuthenticationService

_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@_router.post('/register')
def register(register_form: schemas.Register):
    # Parse command
    cmd = commands.Register(
        register_form.first_name,
        register_form.last_name,
        register_form.email,
        register_form.password
    )

    # Init necessary service
    auth_service = AuthenticationService(
        AuthTirelire(config.get_auth_uri())
    )

    # Process command
    res = auth_service.register(cmd)
    
    if not res:
        return JSONResponse(status_code=503)
    return JSONResponse(status_code=201)

@_router.post('/login')
def register(register_form: schemas.Login):
    # Parse command
    cmd = commands.Login(
        register_form.email,
        register_form.password
    )

    # Init necessary service
    auth_service = AuthenticationService(
        AuthTirelire(config.get_auth_uri())
    )

    # Process command
    res = auth_service.login(cmd)
    
    return res


@_router.post('/token')
def register(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data}