import uuid
import logging

from app import config
from app.model import commands
from app.adapters.api import auth
from app.adapters.api import user
from app.adapters.session_manager import SessionManager


logger = logging.getLogger(__name__)


def create_uid() -> str:
    return str(uuid.uuid4())


class AuthenticationService:
    
    def __init__(self, auth: auth.AuthGateway, user: user.UserGateway, session_manager: SessionManager=None):
        self.auth_service = auth
        self.user_service = user
        self.session_manager = session_manager

    def register(self, cmd: commands.Register):
        uid = create_uid()

        self.user_service.register(
            uid,
            cmd.first_name,
            cmd.last_name,
            cmd.birthdate.isoformat(),
            cmd.email,
        )

        self.auth_service.register(
            uid,
            cmd.password
        )

    def login(self, cmd: commands.Login):
        auth = self.auth_service.authenticate(cmd.email, cmd.password)
        token = auth.get('access_token')
        uid = create_uid()

        self.session_manager.create_session(uid, token, config.get_session_expires_time())

        return uid

    def logout(self, cmd: commands.Logout):
        self.session_manager.delete_session(cmd.session_id)