from abc import ABC, abstractmethod

from app.modules.shared.domain.repository import SqlAlchemyUnitOfWork


class AbstractCategoryRepository(ABC):
    """
    Abstract base class for Category repository.

    This class defines the interface for a Category repository, which includes methods
    for retrieving, creating, and fetching categories by ID. All methods must be
    implemented by any concrete subclass.

    Methods
    -------
    get_categorys() -> list[dict]
        Retrieve a list of all categories.

    create_category(name: str) -> dict
        Create a new category with the given name.

    get_category_by_id(Category_id: int) -> dict
        Retrieve a category by its unique ID.
    """

    @abstractmethod
    def get_categorys(self) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def create_category(self, name: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    def get_category_by_id(self, category_id: int) -> dict:
        raise NotImplementedError


class AbstractCategoryUnitOfWork(SqlAlchemyUnitOfWork):
    """
    A unit of work class for managing category-related transactions using SQLAlchemy.

    Attributes:
        category (AbstractCategoryRepository): An abstract repository for category operations.

    Methods:
        __enter__(): Initializes the session and enters the runtime context.
    """

    category: AbstractCategoryRepository

    def __enter__(self):
        self.session = self.session_factory()  # noqa: W0201
        return super().__enter__()
