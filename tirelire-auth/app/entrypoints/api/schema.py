from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str


class Authentication(BaseModel):
    email: str
    password: str


class TokenVerification(BaseModel):
    token: str
