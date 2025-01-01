from app.modules.category.adapters.sqlalchemy_repository import (
    CategorySqlAlchemyRepository,
)
from app.modules.category.domain.repository import AbstractCategoryUnitOfWork


class CategoryUnitOfWork(AbstractCategoryUnitOfWork):
    """
    A unit of work implementation for the Category module using SQLAlchemy.

    This class manages the lifecycle of a database session and provides a repository
    for performing operations on the Category entity.

    Methods:
        __enter__: Initializes the unit of work and sets up the category repository.
    """

    def __enter__(self):
        super().__enter__()
        self.category = CategorySqlAlchemyRepository(self.session)
