import datetime

from sqlalchemy.orm import Session
from sqlalchemy.sql import func, literal

from app.infrastructure.api.schemas.reviews_schema import (
    ReviewCreate,
    ReviewRecommendation,
)
from app.infrastructure.database.models import (
    CategoryORM,
    LocationCategoryReviewORM,
    LocationORM,
)
from app.modules.reviews.domain.repository import (
    AbstractCategoryRepository,
    AbstractLocationRepository,
    AbstractReviewsRepository,
)


class ReviewsSqlAlchemyRepository(AbstractReviewsRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def create_review(self, location_id: int, category_id: int) -> ReviewCreate:
        review = LocationCategoryReviewORM(
            location_id=location_id, category_id=category_id
        )
        self.session.add(review)
        self.session.flush()
        return ReviewCreate(
            location_id=review.location_id,
            category_id=review.category_id,
            id=review.id,
        )

    def get_recomendation_review(self) -> list[ReviewRecommendation]:
        fecha_limite = datetime.datetime.now() - datetime.timedelta(days=30)

        never_reviewed = (
            self.session.query(
                LocationORM.id.label("location_id"),
                LocationORM.name.label("location_name"),
                CategoryORM.id.label("category_id"),
                CategoryORM.name.label("category_name"),
                literal(0).label("review_priority"),
            )
            .select_from(LocationORM)
            .join(CategoryORM, literal(True))
            .outerjoin(
                LocationCategoryReviewORM,
                (LocationORM.id == LocationCategoryReviewORM.location_id)
                & (CategoryORM.id == LocationCategoryReviewORM.category_id),
            )
            .filter(LocationCategoryReviewORM.id.is_(None))
        )

        recently_reviewed = (
            self.session.query(
                LocationCategoryReviewORM.location_id.label("location_id"),
                LocationORM.name.label("location_name"),
                CategoryORM.id.label("category_id"),
                CategoryORM.name.label("category_name"),
                func.count(LocationCategoryReviewORM.id).label("review_priority"),
            )
            .select_from(LocationCategoryReviewORM)
            .join(LocationORM, LocationORM.id == LocationCategoryReviewORM.location_id)
            .join(CategoryORM, CategoryORM.id == LocationCategoryReviewORM.category_id)
            .filter(LocationCategoryReviewORM.reviewed_at < fecha_limite)
            .group_by(
                LocationCategoryReviewORM.location_id,
                LocationORM.name,
                CategoryORM.id,
                CategoryORM.name,
            )
        )

        union_query = never_reviewed.union_all(recently_reviewed).subquery()

        final_query = (
            self.session.query(
                union_query.c.location_id,
                union_query.c.location_name,
                union_query.c.category_id,
                union_query.c.category_name,
                union_query.c.review_priority,
            )
            .order_by(union_query.c.review_priority)
            .limit(10)
        )
        results = final_query.all()
        return [
            ReviewRecommendation(
                location_id=row.location_id,
                location_name=row.location_name,
                category_id=row.category_id,
                category_name=row.category_name,
                review_priority=row.review_priority,
            )
            for row in results
        ]


class CategorySqlAlchemyRepository(AbstractCategoryRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def get_category_by_id(self, category_id: int) -> int:
        category = self.session.query(CategoryORM).filter_by(id=category_id).first()
        if not category:
            return None
        return category.id


class LocationSqlAlchemyRepository(AbstractLocationRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def get_location_by_id(self, location_id: int) -> int:
        location = self.session.query(LocationORM).filter_by(id=location_id).first()
        if not location:
            return None
        return location.id
