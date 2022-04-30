from dataclasses import dataclass


@dataclass
class Command:
    pass


@dataclass
class Register(Command):
    first_name: str
    last_name: str
    email: str
    password: str


@dataclass
class Login(Command):
    email: str
    password: str