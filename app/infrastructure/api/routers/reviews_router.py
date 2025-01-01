from fastapi import APIRouter

from app.infrastructure.api.schemas.reviews_schema import (
    ReviewCreateReturn,
    ReviewRecommendationReturn,
)
from app.modules.reviews.adapters.unit_of_work import ReviewsUnitOfWork
from app.modules.reviews.domain.models import ReviewCreate
from app.modules.reviews.service_layer import services

router = APIRouter()


@router.post("/", response_model=ReviewCreateReturn)
def api_create_review(review_create: ReviewCreate):
    review_create = services.CreateReview(uow=ReviewsUnitOfWork()).create(
        **review_create.dict()
    )
    return ReviewCreateReturn(data=review_create)


@router.get("/recommendation", response_model=ReviewRecommendationReturn)
def api_recomendation_review():
    reviews_recommendation = services.GetRecomendationReview(
        uow=ReviewsUnitOfWork()
    ).get()
    return ReviewRecommendationReturn(data=reviews_recommendation)
