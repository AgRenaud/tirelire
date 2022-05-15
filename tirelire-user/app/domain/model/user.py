from dataclasses import dataclass, field
from typing import Optional
from datetime import date


@dataclass
class User:
    id: str
    first_name: str
    last_name: str
    email: str
    birthdate: date

    def __hash__(self):
        return hash(self.id)
