from app.adapters.api import auth
from app.model import commands


class AuthenticationService:
    
    def __init__(self, auth: auth.AuthGateway):
        self.auth_service = auth

    def register(self, cmd: commands.Register):
        return self.auth_service.register(
            cmd.first_name,
            cmd.last_name,
            cmd.email,
            cmd.password
        )
