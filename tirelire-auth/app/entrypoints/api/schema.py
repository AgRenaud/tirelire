from pydantic import BaseModel


class CreateUser(BaseModel):
    user_id: str
    password: str


class Authentication(BaseModel):
    user_id: str
    password: str


class TokenVerification(BaseModel):
    token: str
