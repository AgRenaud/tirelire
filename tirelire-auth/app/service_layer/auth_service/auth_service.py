from typing import Protocol

from app.service_layer.auth_service.password_encryption import PasswordEncryptionService
from app.service_layer.auth_service.token_encryption import TokenEncryptionService
from app.domain.model import User


class AuthService(Protocol):

    password_encryption: PasswordEncryptionService
    token_encryption: TokenEncryptionService

    def verify_password(self, password: str, user: User) -> bool:
        raise NotImplementedError

    def encrypt_password(self, password: str) -> str:
        raise NotImplementedError

    def generate_token(self, password: str, user: User) -> dict:
        raise NotImplementedError

    def verify_token(self, token: str) -> bool:
        raise NotImplementedError


class AuthServiceImpl:
    def __init__(
        self,
        password_encryption: PasswordEncryptionService,
        token_encryption: TokenEncryptionService,
    ) -> None:
        self.password_encryption = password_encryption
        self.token_encryption = token_encryption

    def verify_password(self, password: str, user: User) -> bool:
        return self.password_encryption.verify_password(password, user.password)

    def encrypt_password(self, password: str) -> str:
        return self.password_encryption.encrypt_password(password)

    def generate_token(self, password: str, user: User) -> dict:

        if not self.verify_password(password, user):
            raise ValueError("Wrong password")

        payload = dict(client_id=user.id, aud=" ".join(list(user._applications_auth)))

        return dict(
            token_type="bearer",
            access_token=self.token_encryption.encrypt_token(payload),
        )

    def verify_token(self, token: str) -> bool:
        return True
