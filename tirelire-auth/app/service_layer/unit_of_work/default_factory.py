from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import config
from app.service_layer.auth_service import AuthServiceImpl
from app.service_layer.auth_service import (
    PasswordEncryptionService,
    TokenEncryptionService,
)


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    ),
    expire_on_commit=False,
)

DEFAULT_AUTH_SERVICE_FACTORY = AuthServiceImpl(
    PasswordEncryptionService(config.get_secret_key()),
    TokenEncryptionService(
        config.get_certs_private_key(), config.get_certs_public_key()
    ),
)
