from dataclasses import dataclass

from app.domain.base_domain.domain.message import Command


@dataclass
class CreateUser(Command):
    email: str
    password: str
    first_name: str
    last_name: str
