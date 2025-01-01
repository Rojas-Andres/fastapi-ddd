from sqlalchemy.orm import Session

from app.modules.auth.domain.repository import AbstractUserRepository
from app.infrastructure.database.models import UserOrm
from app.modules.auth.domain.models import User
from app.infrastructure.api.schemas.user_schema import UserSchema


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

    def get_by_email(self, email: str):
        user = self.session.query(UserOrm).filter(UserOrm.email == email).first()
        if not user:
            return None
        return user

    def create(self, user: User) -> UserSchema:
        user = UserOrm(
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
        )
        self.session.add(user)
        self.session.flush()
        return UserSchema(
            id=user.id,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
        )
