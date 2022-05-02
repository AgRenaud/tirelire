from fastapi import APIRouter, Depends, Response, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from app import config
from app.model import commands
from app.entrypoints.api.v1.user import schemas
from app.adapters.api.auth import AuthTirelire
from app.service_layer.authentication_service import AuthenticationService
from app.adapters.session_manager import RedisSessionManager


user_router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@user_router.post('/register')
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


@user_router.post('/login')
def login(register_form: schemas.Login, response: Response):
    # Parse command
    cmd = commands.Login(
        register_form.email,
        register_form.password
    )

    # Init necessary service
    auth_service = AuthenticationService(
        AuthTirelire(config.get_auth_uri()),
        RedisSessionManager(*config.get_redis_session_manager_conf())
    )

    # Process command
    session_id = auth_service.login(cmd)
    
    response.set_cookie(key="tirelire-session", value=session_id, httponly=True, max_age=config.get_session_expires_time())

    return True

@user_router.post('/logout')
def logout(request: Request, oauth2_scheme: str = Depends(oauth2_scheme)):
    
    # Parse command
    cmd = commands.Logout(
        session_id=request.cookies.get('tirelire-session')
    )

    # Init necessary service
    auth_service = AuthenticationService(
        AuthTirelire(config.get_auth_uri()),
        RedisSessionManager(*config.get_redis_session_manager_conf())
    )

    auth_service.logout(cmd)

    return True

@user_router.get('/me')
def logout(oauth2_scheme: str = Depends(oauth2_scheme)):
    
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@mail.com"
    }