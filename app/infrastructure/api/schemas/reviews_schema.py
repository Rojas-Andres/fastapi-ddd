from typing import Generic, List, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    """
    Modelo genérico para las respuestas de la API.
    """

    data: T


class ReviewRecommendation(BaseModel):
    """
    ReviewRecommendation schema for review recommendations.
    """

    location_id: int
    category_id: int
    review_priority: int
    category_name: str
    location_name: str


class ReviewCreate(BaseModel):
    """
    ReviewRecommendation schema for review recommendations.
    """

    id: int
    location_id: int
    category_id: int


class ReviewRecommendationReturn(ResponseModel[List[ReviewRecommendation]]):
    pass


class ReviewCreateReturn(ResponseModel[ReviewCreate]):
    pass
