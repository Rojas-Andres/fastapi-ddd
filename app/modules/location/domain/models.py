from pydantic import BaseModel, Field


class LocationCreate(BaseModel):
    name: str = Field(..., example="Parque Central")
    latitude: float = Field(..., example=40.7128)
    longitude: float = Field(..., example=-74.0060)
