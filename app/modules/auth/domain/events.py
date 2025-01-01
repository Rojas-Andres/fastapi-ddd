# Standard Library
from dataclasses import dataclass
from uuid import UUID

# Libraries
from app.domain.base_domain.domain.message import Event


@dataclass
class UserCreated(Event):
    user_id: int


@dataclass
class NewUserNotification(Event):
    user_id: int
