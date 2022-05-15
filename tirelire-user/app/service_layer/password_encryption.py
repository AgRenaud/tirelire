import bcrypt
import hashlib
import hmac


class PasswordEncryptionService:
    def __init__(self, secret_key: str):
        self.n_rounds = 10
        self.secret_key = secret_key

    def _hash_password(self, password: str) -> str:
        return hmac.new(
            self.secret_key.encode("utf-8"), password.encode("utf-8"), hashlib.sha256
        ).hexdigest()

    def _salt_password(self, password: str, salt: bytes) -> bytes:
        password_bytes = password.encode("utf-8")
        return bcrypt.hashpw(password_bytes, salt)

    def encrypt_password(self, password: str) -> str:
        salt = bcrypt.gensalt(self.n_rounds)
        peppered_password = self._hash_password(password)
        salt_password = self._salt_password(peppered_password, salt)
        return salt_password.decode("utf-8")

    def verify_password(self, input_password: str, crypted_password: str) -> bool:
        return bcrypt.checkpw(
            self._hash_password(input_password).encode("utf-8"),
            crypted_password.encode("utf-8"),
        )
