import jwt

from ecdsa import SigningKey, VerifyingKey


class TokenEncryptionService:
    def __init__(self, private_key: str, public_key: str) -> None:
        self.private_key = private_key
        self.public_key = public_key

    def encrypt_token(self, payload: dict) -> str:
        sk = SigningKey.from_pem(self.private_key)
        token: str = jwt.encode(payload, sk.to_pem(), algorithm="ES256")
        return token

    def verify_token(self, token: str) -> bool:
        vk = VerifyingKey.from_pem(self.public_key)
        try:
            return jwt.decode(
                token,
                vk.to_pem(),
                algorithms=["ES256"],
                options={"verify_signature": True},
            )
        except jwt.exceptions.InvalidSignatureError as e:
            raise ValueError(f"Invalid signature for {token}")
        except:
            raise Exception(f"Undefined token exception: {token}")
