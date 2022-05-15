from fastapi import APIRouter, Depends, Response, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from app import config
from app.model import commands
from app.entrypoints.api.routers.v1 import schemas
from app.service_layer.authentication_service import AuthenticationService
from app.adapters.session_manager import RedisSessionManager

from app import factory


v1_router = APIRouter( prefix='/v1')


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@v1_router.post('/register')
def register(register_form: schemas.Register):
    # Parse command
    cmd = commands.Register(
        register_form.first_name,
        register_form.last_name,
        register_form.birthdate,
        register_form.email,
        register_form.password
    )

    auth_service = AuthenticationService(
        factory.AUTH_SERVICE_FACTORY(),
        factory.USER_SERVICE_FACTORY()
    )

    res = auth_service.register(cmd)
    
    if not res:
        return JSONResponse(status_code=503)
    return JSONResponse(status_code=201)


@v1_router.post('/login')
def login(register_form: schemas.Login, response: Response):
    cmd = commands.Login(
        register_form.email,
        register_form.password
    )

    auth_service = AuthenticationService(
        factory.AUTH_SERVICE_FACTORY(),
        factory.SESSION_MANAGER_FACTORY()
    )

    session_id = auth_service.login(cmd)
    
    response.set_cookie(key="tirelire-session", value=session_id)

    return True

@v1_router.post('/logout')
def logout(request: Request, oauth2_scheme: str = Depends(oauth2_scheme)):
    
    # Parse command
    cmd = commands.Logout(
        session_id=request.cookies.get('tirelire-session')
    )

    # Init necessary service
    auth_service = AuthenticationService(
        factory.AUTH_SERVICE_FACTORY(),
        factory.SESSION_MANAGER_FACTORY()
    )

    auth_service.logout(cmd)

    return True
