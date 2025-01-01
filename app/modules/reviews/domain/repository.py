from abc import ABC, abstractmethod

from app.modules.shared.domain.repository import SqlAlchemyUnitOfWork


class AbstractCategoryRepository(ABC):
    @abstractmethod
    def get_category_by_id(self, category_id: int):
        raise NotImplementedError


class AbstractLocationRepository(ABC):
    @abstractmethod
    def get_location_by_id(self, location_id: int):
        raise NotImplementedError


class AbstractReviewsRepository(ABC):
    @abstractmethod
    def create_review(self, location_id: int, category_id: int):
        raise NotImplementedError

    @abstractmethod
    def get_recomendation_review(self):
        raise NotImplementedError


class AbstractReviewsUnitOfWork(SqlAlchemyUnitOfWork):
    locations: AbstractLocationRepository
    category: AbstractCategoryRepository
    reviews: AbstractReviewsRepository

    def __enter__(self):
        self.session = self.session_factory()
        return super().__enter__()
