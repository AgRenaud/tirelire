from datetime import date
from pydantic import BaseModel


class User(BaseModel):
    id: str
    first_name: str
    last_name: str
    birthdate: date
    email: str


class Authentication(BaseModel):
    email: str
    password: str
