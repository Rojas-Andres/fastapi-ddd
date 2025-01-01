from app.modules.reviews.adapters.sqlalchemy_repository import (
    CategorySqlAlchemyRepository,
    LocationSqlAlchemyRepository,
    ReviewsSqlAlchemyRepository,
)
from app.modules.reviews.domain.repository import AbstractReviewsUnitOfWork


class ReviewsUnitOfWork(AbstractReviewsUnitOfWork):
    """
    A unit of work implementation for the Reviews module using SQLAlchemy.

    This class manages the lifecycle of a database session and provides a repository
    for performing operations on the Reviews entity.

    Methods:
        __enter__: Initializes the unit of work and sets up the Reviews repository.
    """

    def __enter__(self):
        super().__enter__()
        self.category = CategorySqlAlchemyRepository(self.session)
        self.locations = LocationSqlAlchemyRepository(self.session)
        self.reviews = ReviewsSqlAlchemyRepository(self.session)
