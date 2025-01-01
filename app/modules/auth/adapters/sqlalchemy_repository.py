from sqlalchemy.orm import Session

from app.infrastructure.database.models import CategoryORM
from app.modules.auth.domain.repository import AbstractAuthRepository


class AuthSqlAlchemyRepository(AbstractAuthRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def get_by_id(self, user_id: str):
        return ""

    def get_by_email(self, email: str):
        return ""

    def create(self, user):
        return ""

    def update(self, user):
        return ""

    def change_password(self, user, password) -> None:
        return ""
