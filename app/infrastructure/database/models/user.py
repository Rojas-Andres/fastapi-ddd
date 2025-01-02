from sqlalchemy import Column, Integer, String

from app.infrastructure.database.models.base_model import BaseModel


class UserOrm(BaseModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
