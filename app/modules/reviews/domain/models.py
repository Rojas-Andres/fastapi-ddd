from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    location_id: int = Field(..., example=2)
    category_id: int = Field(..., example=1)
