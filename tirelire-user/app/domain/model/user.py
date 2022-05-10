from dataclasses import dataclass, field
from typing import Set
from datetime import date


@dataclass
class User:
    id: str
    first_name: str
    last_name: str
    birthdate: date
    email: str


    def __hash__(self):
        return hash(self.id)
