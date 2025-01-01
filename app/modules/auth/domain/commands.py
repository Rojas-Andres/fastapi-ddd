from dataclasses import dataclass
from typing import Optional

from app.domain.base_domain.domain.message import Command


@dataclass
class CreateUser(Command):
    email: str
    password: str
