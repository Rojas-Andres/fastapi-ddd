from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.models.base_model import BaseModel


class LocationORM(BaseModel):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = relationship("LocationCategoryReviewORM", back_populates="location")
