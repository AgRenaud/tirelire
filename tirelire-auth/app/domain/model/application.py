from dataclasses import dataclass
from enum import Enum


class App(Enum):
    TIRELIRE_WEB = "tirelire_web"
    TIRELIRE_APP = "tirelire_app"


@dataclass
class AppAuthorization:
    name: App

    def __hash__(self):
        return hash(self.name)
