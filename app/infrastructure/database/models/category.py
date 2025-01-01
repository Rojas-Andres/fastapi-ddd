from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.models.base_model import BaseModel


class CategoryORM(BaseModel):
    """
    CategoryORM is a SQLAlchemy ORM model representing the 'categories' table.

    Attributes:
        id (Column): An integer primary key for the category.
        name (Column): A unique string representing the name of the category.
    """

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    reviews = relationship("LocationCategoryReviewORM", back_populates="category")
