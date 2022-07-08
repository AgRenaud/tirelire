import uuid
import logging

from app import config
from app.model import commands
from app.adapters.api import auth
from app.adapters.api import user
from app.service_layer.unit_of_work import UnitOfWork
from app.adapters.session_manager import SessionManager


logger = logging.getLogger(__name__)


def create_uid() -> str:
    return str(uuid.uuid4())


class AuthenticationService:
    
    def __init__(self, auth: auth.AuthGateway, user: user.UserGateway, session_manager: SessionManager=None):
        self.auth_service = auth
        self.user_service = user
        self.session_manager = session_manager
        self.uow = UnitOfWork()

    def register(self, cmd: commands.Register):
        with self.uow:
            user_id = create_uid()

            try:
                self.user_service.register(
                    user_id,
                    cmd.first_name,
                    cmd.last_name,
                    cmd.birthdate.isoformat(),
                    cmd.email,
                )
            except RuntimeError:
                # TODO: Create an event DeleteAuthUser( uid=uid ) to ensure atomicity
                logger.fatal(f'Unable to register the client : {user_id} on user_service')

            try: 
                self.auth_service.register(
                    user_id,
                    cmd.password
                )
            except RuntimeError:
                # TODO: Create an event DeleteAuthUser( uid=uid ) to ensure atomicity
                logger.fatal(f"Unable to register the client : {user_id} on auth service")
        
        if not self.uow:
            raise RuntimeError(f'Unable to register the client with {user_id}')

    def login(self, cmd: commands.Login):
        with self.uow:
            auth = self.auth_service.authenticate(cmd.email, cmd.password)
            token = auth.get('access_token')
            session_id = create_uid()

            self.session_manager.create_session(session_id, token, config.get_session_expires_time())
        
        if not self.uow:
            raise RuntimeError(f'User {cmd.email} is unable to log in')

    def logout(self, cmd: commands.Logout):
        self.session_manager.delete_session(cmd.session_id)