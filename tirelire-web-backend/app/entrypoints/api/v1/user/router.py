from fastapi import APIRouter, Depends, Response, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from app import config
from app.model import commands
from app.entrypoints.api.v1.user import schemas
from app.adapters.api.auth import AuthTirelire
from app.service_layer.authentication_service import AuthenticationService
from app.adapters.session_manager import RedisSessionManager

from app import factory


user_router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@user_router.post('/register')
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
    print(res) 
    if not res:
        return JSONResponse(status_code=503)
    return JSONResponse(status_code=201)


@user_router.post('/login')
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
        factory.AUTH_SERVICE_FACTORY(),
        factory.SESSION_MANAGER_FACTORY()
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