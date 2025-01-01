from app.core.exceptions import ObjectNotFoundException
from app.infrastructure.api.schemas.reviews_schema import (
    ReviewCreate,
    ReviewRecommendation,
)
from app.modules.reviews.domain.repository import AbstractReviewsUnitOfWork


class CreateReview:
    def __init__(self, uow: AbstractReviewsUnitOfWork):
        self.uow = uow

    def create(self, location_id: int, category_id: int) -> ReviewCreate:
        with self.uow:
            if not self.uow.locations.get_location_by_id(location_id):
                raise ObjectNotFoundException("Location not found")
            if not self.uow.category.get_category_by_id(category_id):
                raise ObjectNotFoundException("Category not found")
            review = self.uow.reviews.create_review(location_id, category_id)
            self.uow.commit()
            return review


class GetRecomendationReview:
    def __init__(self, uow: AbstractReviewsUnitOfWork):
        self.uow = uow

    def get(self) -> list[ReviewRecommendation]:
        with self.uow:
            reviews = self.uow.reviews.get_recomendation_review()
            return reviews
