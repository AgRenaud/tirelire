from dataclasses import dataclass


@dataclass
class Event:
    pass


@dataclass
class UserAdded:
    user_id: str
