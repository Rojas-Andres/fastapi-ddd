from sqlalchemy.orm import Session

from app.modules.user.domain.repository import AbstractUserRepository
from app.infrastructure.database.models import UserOrm
from app.infrastructure.api.schemas.auth_schema import UserSchema


class UserSqlAlchemyRepository(AbstractUserRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def get_by_id(self, user_id: str) -> UserSchema:
        user = self.session.query(UserOrm).filter(UserOrm.id == user_id).first()
        if not user:
            return None
        return UserSchema(
            id=user.id,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
        )

    def change_password(self, user_id: int, new_password: str) -> UserSchema:
        user = self.session.query(UserOrm).filter(UserOrm.id == user_id).first()
        user.password = new_password
        self.session.flush()
        return UserSchema(
            id=user.id,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
        )
