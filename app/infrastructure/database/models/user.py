from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.models.base_model import BaseModel


class UserOrm(BaseModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True, nullable=False)
    last_name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
