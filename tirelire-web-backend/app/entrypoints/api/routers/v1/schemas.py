from datetime import date
from pydantic import BaseModel


class Register(BaseModel):
    first_name: str
    last_name: str
    birthdate: date
    email: str
    password: str


class Login(BaseModel):
    email: str
    password: str

    