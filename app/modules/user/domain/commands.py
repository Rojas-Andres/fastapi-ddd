from dataclasses import dataclass

from app.domain.base_domain.domain.message import Command


@dataclass
class ChangePasswordUser(Command):
    current_password: str
    new_password: str
    user_id: int
