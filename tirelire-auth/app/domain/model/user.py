from dataclasses import dataclass, field
from typing import Set

from app.domain.model.application import App, AppAuthorization


@dataclass
class User:
    id: str
    password: str

    events = []

    _applications_auth: Set[AppAuthorization] = field(default_factory=set)

    def add_app_auth(self, app_auth: AppAuthorization):
        if app_auth in self._applications_auth:
            raise ValueError("Application Authorization already exists")
        self._applications_auth.add(app_auth)

    def __hash__(self):
        return hash(self.id)
