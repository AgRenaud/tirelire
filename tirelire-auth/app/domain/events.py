from dataclasses import dataclass

from app.domain.model import App


@dataclass
class Event:
    pass

@dataclass
class UserAdded:
    user_id: str

@dataclass
class UserSubscribedToApp(Event):
    user_id: str
    app_name: str
